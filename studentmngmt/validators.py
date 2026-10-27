import re

class ValidationError(Exception):
    # Raised when user input fails validation.
    pass

def validate_student_id(student_id):
    if not student_id or not student_id.isalnum():
        raise ValidationError("Student ID must be alphanumeric.")
    return student_id

def validate_name(name):
    name = name.strip()
    if len(name) < 2:
        raise ValidationError("Name must be at least 2 characters.")
    if not all(c.isalpha() or c.isspace() for c in name):
        raise ValidationError("Name must contain only letters and spaces.")
    return name.title()

def validate_age(age_str):
    try:
        age = int(age_str)
    except ValueError:
        raise ValidationError("Age must be a whole number.")
    if not 15 <= age <= 80:
        raise ValidationError("Age must be between 15 and 80.")
    return age

def validate_email(email):
    email = email.strip().lower()
    pattern = r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}"
    if not re.fullmatch(pattern, email):
        raise ValidationError("Invalid email format.")
    return email

def validate_score(score_str):
    try:
        score = float(score_str)
    except ValueError:
        raise ValidationError("Score must be a number.")
    if not 0 <= score <= 100:
        raise ValidationError("Score must be between 0 and 100.")
    return score
