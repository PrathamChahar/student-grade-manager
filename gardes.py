print("===== Student Grade Manager =====")

student_name = input("Enter student name: ")
math = float(input("Enter Math marks (out of 100): "))
science = float(input("Enter Science marks (out of 100): "))
english = float(input("Enter English marks (out of 100): "))
computer = float(input("Enter Computer marks (out of 100): "))

average = (math + science + english + computer) / 4

print("\n--- Result Card ---")
print("Student:", student_name)
print("Math:", math)
print("Science:", science)
print("English:", english)
print("Computer:", computer)
print("Average:", round(average, 2))

if average >= 90:
    print("Grade: A+ | Outstanding!")
elif average >= 75:
    print("Grade: A | Excellent!")
elif average >= 60:
    print("Grade: B | Good!")
elif average >= 40:
    print("Grade: C | Needs Improvement")
else:
    print("Grade: F | Failed")