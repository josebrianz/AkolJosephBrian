score = int(input("Enter the students score: "))

if score >= 90:
    grade = "A"
    message = "Excellent work!"

elif score >= 80:
    grade = "B"
    message = "Good work!"
elif score >= 70:
    grade = "C"
    message = "Satisfactory work!"
elif score >= 60:
    grade = "D"
    message = "You need to improve."
else:
    grade = "F"
    message = "You Failed."