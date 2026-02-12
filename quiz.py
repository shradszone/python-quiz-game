print('welcome')
playing = input('do you want to play?')
if playing !='yes':
    quit()
print('okay lets play')
score = 0
answer = input("what is the full form of aiml?")
if answer.lower() == 'artifical intelligence and machine learning':
    print("correct")
    score +=1
else:
    print("incorrect")    

answer = input("what is full form of os?")
if answer.lower() == 'operating systems':
    print("correct")
    score +=1
else:
    print("incorrect")    

answer = input("is apple healthy?")
if answer.lower() == 'yes':
    print("correct")
    score +=1
else:
    print("incorrect")        
print('you got ' + str(score)+ 'question correct')    