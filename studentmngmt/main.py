from manager import StudentManager
from validators import (ValidationError, validate_name, validate_age,
                        validate_email, validate_score)

def print_menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print(" 1. Add Student        5. Add Score")
    print(" 2. View All Students  6. Statistics")
    print(" 3. Search Students    7. Export to CSV")
    print(" 4. Update Student     8. Delete Student")
    print(" 0. Exit")

def add_student_flow(mgr):
    try:
        name = validate_name(input(" Name : "))
        age = validate_age(input(" Age : "))
        email = validate_email(input(" Email : "))
        course = input(" Course : ").strip().title()
        student = mgr.add_student(name, age, email, course)
        print(f" Added {student.name} with ID {student.student_id}")
    except ValidationError as e:
        print(f" Input error: {e}")

def view_all_flow(mgr):
    students = mgr.all_students()
    if not students:
        print(" No students registered yet.")
        return
    print("\n " + "-" * 70)
    for s in students:
        print(f" {s}")  # uses Student.__str__
    print(" " + "-" * 70)
    print(f" Total: {len(students)} student(s)")

def search_flow(mgr):
    query = input(" Search (name/ID/course): ").strip()
    results = mgr.search(query)
    if not results:
        print(" No matching students found.")
        return
    for s in results:
        print(f" {s}")

def update_flow(mgr):
    sid = input(" Student ID to update: ").strip().upper()
    student = mgr.get_student(sid)
    if not student:
        print(" Student not found.")
        return
    print(" Leave blank to keep current value.")
    try:
        name = input(f" Name ({student.name}): ").strip()
        if name: name = validate_name(name)
        
        age_str = input(f" Age ({student.age}): ").strip()
        age = validate_age(age_str) if age_str else None
        
        email = input(f" Email ({student.email}): ").strip()
        if email: email = validate_email(email)
        
        course = input(f" Course ({student.course}): ").strip().title()
        
        updates = {}
        if name: updates["name"] = name
        if age: updates["age"] = age
        if email: updates["email"] = email
        if course: updates["course"] = course
        
        if updates:
            mgr.update_student(sid, **updates)
            print(" Student updated.")
        else:
            print(" No changes made.")
    except ValidationError as e:
        print(f" Input error: {e}")

def add_score_flow(mgr):
    sid = input(" Student ID: ").strip().upper()
    if not mgr.get_student(sid):
        print(" Student not found.")
        return
    try:
        subject = input(" Subject: ").strip().title()
        score = validate_score(input(" Score (0-100): "))
        mgr.add_score(sid, subject, score)
        print(f" Added {subject}: {score}")
    except ValidationError as e:
        print(f" Input error: {e}")

def delete_flow(mgr):
    sid = input(" Student ID to delete: ").strip().upper()
    student = mgr.get_student(sid)
    if not student:
        print(" Student not found.")
        return
    confirm = input(f" Delete {student.name}? (yes/no): ").strip().lower()
    if confirm == "yes":
        mgr.delete_student(sid)
        print(" Student deleted.")
    else:
        print(" Cancelled.")

def stats_flow(mgr):
    stats = mgr.statistics()
    if not stats:
        print(" No data for statistics.")
        return
    print(f"\n Total students : {stats['total']}")
    print(f" Class average : {stats['class_avg']}")
    if stats["top_student"]:
        top = stats["top_student"]
        print(f" Top student : {top.name} ({top.average})")
    print(f" Grade distribution: {stats['grade_dist']}")

def main():
    mgr = StudentManager()
    actions = {
        "1": add_student_flow,
        "2": view_all_flow,
        "3": search_flow,
        "4": update_flow,
        "5": add_score_flow,
        "6": stats_flow,
        "7": lambda m: m.export_csv(),
        "8": delete_flow,
    }
    
    while True:
        print_menu()
        choice = input(" Choose an option: ").strip()
        if choice == "0":
            print(" Goodbye!")
            break
        
        action = actions.get(choice)
        if action:
            action(mgr)
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
