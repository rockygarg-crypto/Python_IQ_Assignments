age = int(input("Enter your age : "))
graduate_status = input("Graduation status : ")
nationality = input("Enter your Nationality : ")

if age >= 21 and age <=32 :
    if graduate_status == "yes":
        if nationality == "Indian":
           print("Eligibal,proceed to prelims")
           score = int(input("Enter your Prelims score : "))
           if score >= 600:
              print("Passed,proceed to Mains")
              score = int(input("Enter your Mains score : "))
              if score >= 1100:
                print("Passed,proceed to Interview")
                score = int(input("Enter your Interview score : "))
                if score >= 1600:
                   print("Congratulation!You have cleared the UPSC")
                else :
                   print("You failed the interview")

              else:
                 print("You failed the Mains")
           else :
            print("You failed the Prelims")
        else :
           print("Your nationality is ineligible")     
    else : 
        print("You graduation is ineligible")
    
else :
    print("your age is ineligible")    