print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

questions = ['What does CPU stands for? ','What does GPU stand for? ','What does RAM stands for? ','What does PSU stands for? ']

answers = ['central processing unit','graphics processing unit','random access memory','power supply']

for i in range(len(questions)):
    ans = input(questions[i]).lower()
    if ans == answers[i]:
        print('Correct!')
        score+=1
    else:
        print('Incorrect!')


print("you got "+str(score)+ " question correct")
print("you got "+str((score/4)*100)+ "%.")
