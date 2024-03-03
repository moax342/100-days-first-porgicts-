student_score=input("Enter your students scores \n").split()
mXscore=[]
maxScore =0
for score in student_score:
    mXscore.append(int(score))

for ss in mXscore:
    if ss > maxScore:
        maxScore=ss

print(f"the Hieghst score is : {maxScore}")
