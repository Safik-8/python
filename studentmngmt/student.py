class Student:
    def __init__(self, student_id, name, age, email, course, scores=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.course = course
        # Each student gets their own dict (never a shared mutable default!)
        self.scores = scores if scores is not None else {}

    @property
    def average(self):
        # Computed on demand — always reflects current scores
        if not self.scores:
            return 0.0
        return round(sum(self.scores.values()) / len(self.scores), 2)

    @property
    def grade(self):
        avg = self.average
        if avg >= 90: return "A"
        elif avg >= 75: return "B"
        elif avg >= 60: return "C"
        elif avg >= 40: return "D"
        return "F"

    def add_score(self, subject, score):
        self.scores[subject] = score

    def to_dict(self):
        # Convert to a JSON-serialisable dictionary
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "course": self.course,
            "scores": self.scores,
        }

    @classmethod
    def from_dict(cls, data):
        # Alternative constructor: build a Student from a saved dict
        return cls(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            email=data["email"],
            course=data["course"],
            scores=data.get("scores", {}),
        )

    def __str__(self):
        return (f"{self.student_id} | {self.name:<18} | Age {self.age} | "
                f"{self.course:<12} | Avg {self.average:>5} ({self.grade})")

    def __repr__(self):
        return f"Student({self.student_id!r}, {self.name!r}, {self.course!r})"
