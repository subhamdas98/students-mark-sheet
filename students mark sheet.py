n = int(input("enter number of students:"))
for i in range(n):
    print("\n--- Enter details for Student", i+1, "---")
    
    name = input("Enter student name: ")
    
    marks = []
    total = 0
    pass_status = True
    
    for j in range(5):
        m = int(input(f"Enter marks for Subject {j+1}: "))
        marks.append(m)
        total += m
        
        if m < 33:
            pass_status = False

    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    result = "Pass" if pass_status else "Fail"

    
    print("\n----- MARK SHEET -----")
    print("Name:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
    print("Result:", result)

