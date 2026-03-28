attendance = float(input("Enter Attendance (0-100): "))
assignment = float(input("Enter Assignment Marks (0-100): "))
test = float(input("Enter Test Marks (0-100): "))

if attendance < 40:
    performance = "Poor"
elif attendance >= 40 and attendance < 70:
    if test < 50:
        performance = "Average"
    else:
        performance = "Good"
else:
    if assignment > 60 and test > 60:
        performance = "Good"
    else:
        performance = "Average"

print("Predicted Performance:", performance)