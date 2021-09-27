import heroes
import random

names = heroes.genarr(7)
# print(names)
student_scores = {student:random.randint(0,100) for student in names}
# print(student_scores)
# print(student_scores.items())
passed_students = {key:value for (key, value) in student_scores.items() if value > 50}
# print(passed_students)