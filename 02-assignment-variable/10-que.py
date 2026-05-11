marks = int(input("enter the students 's marks:"))
if 90 <= marks <=100:
    print("grade: a")

elif 80 <= marks <=89:
    print("grade: b")

elif 70 <= marks <=79:
    print("grade: c") 

elif 60  <= marks <=69:
    print("grade: d") 

elif 50  <= marks <=59:
    print("grade: e") 

elif 0  <= marks <=49:
    print("grade: f")

else:
    print("invalid marks")
