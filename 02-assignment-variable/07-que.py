academic_score = 78.88
attendence_percentage = 85.88
extracurricular_participation = "yes"

if(academic_score >= 60 and 
    attendence_percentage >=75 and

    extracurricular_participation.lower() == "yes"):

    print("eligible for interview")
else:
    print("not eligible for interview")
