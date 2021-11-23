def exam() :
    with open("exam.txt") as f :
        exams = [line.strip().split() for line in f]
    return exams

def solution() :
    with open("sol.txt") as f :
        sol = f.readline().split()
    return sol

sol = solution()
exams = exam()
scores = list()
each = [0 for _ in range(len(exams[0]))]
for i in range(len(exams)) :
    score = 0
    for j in range(len(exams[i])) :
        if(sol[j]==exams[i][j]) :
            each[j] += 1
            score += 1
    scores.append(score)

print("Student score:")
print(scores)
maxx = max(each)
minn = min(each)
max_l = list()
min_l = list()
for i in range(len(each)) :
    print(f"Question {i+1} :{each[i]/len(exams)}")
    if each[i] == maxx :
        max_l.append(str(i+1))
    if each[i] == minn :
        min_l.append(str(i+1))
for i in range(len(min_l)) :
    print(min_l[i],end=' ')
print('is the hardest question.')
for i in range(len(max_l)) :
    print(max_l[i],end=' ')
print('is the easiest question.')


