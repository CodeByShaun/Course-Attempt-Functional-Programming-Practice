from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def sum_of_all_credits(attempts: list[CourseAttempt]) -> int:
    return reduce(lambda sum, attempt: sum + attempt.credits, attempts, 0)

def sum_of_passed_credits(attempts: list[CourseAttempt]) -> int:
    return reduce(lambda sum, attempt: sum + attempt.credits, filter(lambda attempt: attempt.grade > 0, attempts), 0)

def average(attempts: list[CourseAttempt]) -> float:
    filtered_attempts = list(filter(lambda attempt: attempt.grade > 0, attempts))
    len_of_filtered_attempts = len(filtered_attempts)
    if len_of_filtered_attempts > 0:
        reduced =  reduce(lambda total, attempt: total + attempt.grade, filtered_attempts, 0)
    else:
        return "Average grade isn't able to be calculated!"
    return reduced / len_of_filtered_attempts

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)
    print()
    cr = sum_of_all_credits([s1,s2,s3])
    print(cr)
    print()
    pcr = sum_of_passed_credits([s1,s2,s3])
    print(pcr)
