
print("welcome!")
name= str(input("enter your name "))

grade = int(input("enter your test score(0-100)"))
if grade> 100:
    print("invalid score. try again")
elif grade >90:
    print ("Excellent work! You have mastered this material.✨ ")
elif grade >80:
    print("Good job! You understand most of the concepts.👍")
elif grade >70:
    print("You did okay. A little more practice would help.📚")
elif grade> 60:
    print("You need to study more to improve your understanding.💪")
elif grade> 50:
    print("You barely passed. Focus on the weak areas.⚠️")    
else:
    print("You did not pass. Please meet with me to discuss a study plan.")   


if grade> 50<100:
      print("passed") 
else: print("failed")   