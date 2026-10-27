import json
import csv
import os
from pathlib import Path
from student import Student

class StudentManager:
    def __init__(self, data_file="students.json"):
        self.data_file = Path(data_file)
        self.students = {}  # student_id -> Student object
        self.load()  # load existing data on startup

    def load(self):
        # Load students from the JSON file into memory.
        if not self.data_file.exists():
            self.students = {}
            return
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                # Rebu
                # ild Student objects from the saved dicts
                self.students = {
                    sid: Student.from_dict(record)
                    for sid, record in data.items()
                }
            print(f"Loaded {len(self.students)} student(s).")
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Warning: could not read data file ({e}). Starting fresh.")
            self.students = {}

    def save(self):
        # Persist all students to the JSON file.
        try:
            data = {sid: s.to_dict() for sid, s in self.students.items()}
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except OSError as e:
            print(f"Error: could not save data ({e}).")

    def export_csv(self, filename="students_export.csv"):
        # Export the roster to a CSV file for spreadsheets.
        if not self.students:
            print("No students to export.")
            return
        try:
            with open(filename, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Name", "Age", "Email",
                                 "Course", "Average", "Grade"])
                for s in self.students.values():
                    writer.writerow([s.student_id, s.name, s.age, s.email,
                                     s.course, s.average, s.grade])
            print(f"Exported {len(self.students)} student(s) to {filename}")
        except OSError as e:
            print(f"Error: could not export CSV ({e}).")

    # ── CREATE ──────────────────────────────────────────────
    def add_student(self, name, age, email, course):
        # Generate the next sequential ID like S001, S002...
        next_num = len(self.students) + 1
        while f"S{next_num:03d}" in self.students:
            next_num += 1
        student_id = f"S{next_num:03d}"
        student = Student(student_id, name, age, email, course)
        self.students[student_id] = student
        self.save()  # persist immediately
        return student

    # ── READ ────────────────────────────────────────────────
    def get_student(self, student_id):
        return self.students.get(student_id)

    def search(self, query):
        # Search by name, ID, or course (case-insensitive, partial).
        query = query.lower()
        return [
            s for s in self.students.values()
            if query in s.name.lower()
            or query in s.student_id.lower()
            or query in s.course.lower()
        ]

    def all_students(self):
        # Return students sorted by ID.
        return sorted(self.students.values(), key=lambda s: s.student_id)

    # ── UPDATE ──────────────────────────────────────────────
    def update_student(self, student_id, **fields):
        student = self.students.get(student_id)
        if not student:
            return False
        for key, value in fields.items():
            if hasattr(student, key):
                setattr(student, key, value)
        self.save()
        return True

    def add_score(self, student_id, subject, score):
        student = self.students.get(student_id)
        if not student:
            return False
        student.add_score(subject, score)
        self.save()
        return True

    # ── DELETE ──────────────────────────────────────────────
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            self.save()
            return True
        return False

    # ── STATISTICS ──────────────────────────────────────────
    def statistics(self):
        if not self.students:
            return None
        averages = [s.average for s in self.students.values() if s.scores]
        grades = {}
        for s in self.students.values():
            grades[s.grade] = grades.get(s.grade, 0) + 1
        return {
            "total": len(self.students),
            "class_avg": round(sum(averages) / len(averages), 2) if averages else 0,
            "top_student": max(self.students.values(),
                               key=lambda s: s.average, default=None),
            "grade_dist": grades,
        }
