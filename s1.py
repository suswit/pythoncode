
python programs:-

1. Tic-Tac-Toe using DFS (Minimax)

def print_board(b):
    for i in range(0,9,3):
        print(b[i],"|",b[i+1],"|",b[i+2])
        print()

wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
winner = lambda b,p: any(b[x]==b[y]==b[z]==p for x,y,z in wins)

def minimax(b, maxi):
    if winner(b,"X"): 
        return 1
    if winner(b,"O"): 
        return -1
    moves = [i for i in range(9) if b[i]==" "]
    if not moves: 
        return 0
    results = []
    for i in moves: 
        b[i]="X" if maxi else "O"
        results.append(minimax(b,not maxi))
        b[i]=" "
    return max(results) if maxi else min(results)

def best_move(b):
    def score(i): 
        b[i]="X"
        s=minimax(b,False)
        b[i]=" "
        return s
    return max((i for i in range(9) if b[i]==" "), key=score)

board = [" "] * 9
while True:
    print_board(board)
    try: 
        p = int(input("Enter position (0-8): "))
    except: 
        print("Invalid input!")
        continue
    if not 0<=p<=8: 
        print("Enter number between 0 and 8")
        continue
    if board[p] != " ": 
        print("Already filled!")
        continue
    board[p] = "O"
    if winner(board,"O"): 
        print_board(board)
        print("Player Wins!")
        break
    if " " not in board: 
        print_board(board)
        print("Draw!")
        break
    c = best_move(board)
    board[c] = "X"
    print("Computer chose:", c)
    if winner(board,"X"): 
        print_board(board)
        print("Computer Wins!")
        break
    if " " not in board: 
        print_board(board)
        print("Draw!")
        break




2. 8-Puzzle Solvability Check

def inversions(s):
    # Fixed indentation: function body must be indented
    p = [x for x in s if x != 0]
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p)))

# Fixed indentation: lambda function properly aligned
solvable = lambda s: inversions(s) % 2 == 0

def show(s):
    # Fixed indentation: function body must be indented
    for i in range(0, 9, 3):
        # Fixed indentation: nested loop body must be further indented
        print(*[" " if x==0 else x for x in s[i:i+3]])

# Main code execution - no indentation needed as it's at module level
s1 = list(map(int, input("State 1: ").split()))
s2 = list(map(int, input("State 2: ").split()))
print("\nState 1"); show(s1)
print("State 2"); show(s2)
print("State 1 Inversions:", inversions(s1))
print("State 2 Inversions:", inversions(s2))
print("\nState 1:", "Solvable" if solvable(s1) else "Unsolvable")
print("State 2:", "Solvable" if solvable(s2) else "Unsolvable")
print("\nBoth are in", "SAME set" if solvable(s1)==solvable(s2) else "DIFFERENT sets")




3. Predicate Logic — Voting Eligibility

people = {"Ravi": 22, "Anu": 17, "Kiran": 19, "Meena": 15}
print("KNOWLEDGE BASE\n")
for p, a in people.items(): print(p, "Age =", a)
print("\nRESULT\n")
for p, a in people.items():
    print(p, "CAN vote" if a >= 18 else "CANNOT vote")  # Added proper indentation here
print("\nRULE")
print("IF Age >= 18 THEN Eligible_to_Vote(Person)")



4. Find-S and Candidate Elimination
from functools import reduce
data = [
['Youth','High','No','Fair','No'], ['Youth','High','No','Excellent','No'],
['Middle','High','No','Fair','Yes'], ['Senior','Medium','No','Fair','Yes'],
['Senior','Low','Yes','Fair','Yes'], ['Senior','Low','Yes','Excellent','No'],
['Middle','Low','Yes','Excellent','Yes'], ['Youth','Medium','No','Fair','No'],
['Youth','Low','Yes','Fair','Yes'], ['Senior','Medium','Yes','Fair','Yes']
]
# FIND-S: reduce over all positive examples
pos = [r[:-1] for r in data if r[-1]=='Yes']
h = reduce(lambda h,x: ['?' if h[i]!='0' and h[i]!=x[i] else x[i] for i in range(len(h))],
pos, ['0'] * (len(data[0])-1))

# CANDIDATE ELIMINATION
def ce(data):
    # Added proper indentation (4 spaces) for all code inside the function
    n = len(data[0])-1; S = ['0']*n; G = [['?']*n]
    for r in data:
        x, y = r[:-1], r[-1]
        if y == 'Yes':
            S = [x[i] if S[i]=='0' else ('?' if S[i]!=x[i] else S[i]) for i in range(n)]
            G = [g for g in G if all(g[i]=='?' or g[i]==x[i] for i in range(n))]
        else:
            G = [g[:i]+[S[i]]+g[i+1:] for g in G for i in range(n) if g[i]=='?' and S[i]!=x[i]]
    return S, G

print("FIND-S ALGORITHM\nFinal Hypothesis:", h)
S, G = ce(data)
print("\nCANDIDATE ELIMINATION\nFinal Specific Hypothesis:", S)
print("\nFinal General Hypothesis:")
for g in G: print(g)



5. ID3 Decision Tree (using Pandas)

import pandas as pd, math

data = {
'StudyHours': ['High','High','Medium','Low','Low','Medium','High','Low','Medium','High'],
'Attendance': ['Good','Poor','Good','Poor','Good','Good','Poor','Poor','Good','Good'],
'Assignment': ['Yes','Yes','Yes','No','No','Yes','No','No','Yes','Yes'],
'Result': ['Pass','Pass','Pass','Fail','Fail','Pass','Fail','Fail','Pass','Pass']
}

df = pd.DataFrame(data)

def entropy(col):
    # Fixed indentation: function body must be indented
    e = 0
    for v in col.unique():
        p = len(col[col==v]) / len(col)
        e -= p * math.log2(p)
    return e

def gain(df, att, tgt):
    # Fixed indentation: function body must be indented and split into multiple lines for readability
    return entropy(df[tgt]) - sum(len(s)/len(df)*entropy(s[tgt]) for _,s in df.groupby(att))

def id3(df, feats, tgt):
    # Fixed indentation: function body must be indented
    if df[tgt].nunique() == 1: 
        return df[tgt].iloc[0]
    if not feats: 
        return df[tgt].mode()[0]
    best = max(feats, key=lambda f: gain(df, f, tgt))
    return {best: {v: id3(df[df[best]==v], [f for f in feats if f!=best], tgt)
                   for v in df[best].unique()}}

print(id3(df, list(df.columns[:-1]), 'Result'))




6. ID3 Decision Tree with Train/Test Split (Raw Lists)

import math, random
from collections import Counter

def entropy(d):
    # Added proper indentation for function body
    c = Counter(r[-1] for r in d)
    return -sum(v/len(d)*math.log2(v/len(d)) for v in c.values())

def gain(d, f):
    # Added proper indentation for function body
    vals = {}
    for r in d: vals.setdefault(r[f], []).append(r)
    return entropy(d) - sum(len(s)/len(d)*entropy(s) for s in vals.values())

def id3(d, feats):
    # Added proper indentation for function body
    labels = [r[-1] for r in d]
    if len(set(labels)) == 1: return labels[0]
    if not feats: return Counter(labels).most_common(1)[0][0]
    best = max(feats, key=lambda f: gain(d, f))
    return {best: {v: id3([r for r in d if r[best]==v], [f for f in feats if f!=best])
            for v in {r[best] for r in d}}}

data = [['Sunny','Hot','No'],['Sunny','Cool','No'],['Rainy','Cool','Yes'],
        ['Rainy','Hot','Yes'],['Cloudy','Hot','Yes'],['Cloudy','Cool','Yes']]
random.shuffle(data)
s = int(len(data) * 0.7)
train, test = data[:s], data[s:]
print(id3(train, [0, 1]))


7. Types of Machine Learning (Demo)

X = [[1],[2],[3],[8],[9],[10]]; y = [0,0,0,1,1,1]
predict = lambda v: 0 if v < 5 else 1
print("SUPERVISED")
print("2 ->", predict(2)); print("9 ->", predict(9))
print("\nUNSUPERVISED")
for v in X: print(v[0], "-> Cluster", "A" if v[0]<5 else "B")
print("\nSEMI-SUPERVISED")
for v in [2, 3, 8, 10]: print(v, "->", predict(v))
print("\nREINFORCEMENT")
score = sum(10 if a=="Correct" else -5 for a in ["Correct","Wrong","Correct"])
print("Score =", score)


8. Find-S and Candidate Elimination (Short Dataset)

data = [['High','Complete','Yes'],['Low','Complete','No'],
['High','Incomplete','Yes'],['High','Complete','Yes']]

# FIND-S
h = ['0', '0']
for r in data:
    if r[-1] == 'Yes':  # Added proper indentation
        for i in range(2):  # Added proper indentation
            h[i] = r[i] if h[i]=='0' else ('?' if h[i]!=r[i] else h[i])  # Added proper indentation
print("FIND-S\nHypothesis :", h)

# CANDIDATE ELIMINATION
S = ['0', '0']; G = ['?', '?']
for r in data:
    if r[-1] == 'Yes':  # Added proper indentation
        for i in range(2):  # Added proper indentation
            S[i] = r[i] if S[i]=='0' else ('?' if S[i]!=r[i] else S[i])  # Added proper indentation
    else:  # Added proper indentation
        for i in range(2):  # Added proper indentation
            if r[i] != S[i]:  # Added proper indentation
                G[i] = S[i]  # Added proper indentation
print("\nCANDIDATE ELIMINATION\nS =", S, "\nG =", G)
print("\nFind-S -> Specific")
print("Candidate Elimination -> Specific + General")


9. Linear Regression (Normal Equation)

import numpy as np
X = np.array([[8.3,41,6.9],[8.3,21,6.2],[7.2,52,8.2],[5.6,52,5.8],
[3.8,52,6.2],[4.0,52,4.7],[3.6,52,4.9],[3.1,52,4.7],
[2.0,42,4.2],[3.6,52,4.9]])
y = np.array([4.5,3.5,3.5,3.4,3.4,2.6,2.9,2.4,2.2,2.6])
tx, vx, ty, vy = X[:8], X[8:], y[:8], y[8:]
m, s = tx.mean(0), tx.std(0)
tx = (tx-m)/s; vx = (vx-m)/s
tx = np.c_[np.ones(len(tx)), tx]; vx = np.c_[np.ones(len(vx)), vx]
theta = np.linalg.inv(tx.T @ tx) @ tx.T @ ty
pred = vx @ theta
mse = np.mean((vy - pred)**2)
print("Predictions\n")
for i in range(len(pred)):
print("Actual :", vy[i]); print("Predicted:", round(pred[i],2)); print()
print("MSE =", round(mse, 2))
print("RMSE =", round(np.sqrt(mse), 2))


10. MNIST Mini Dataset (4x4 Digit Representation)

import numpy as np
X = np.array([
[1,1,1,1, 1,0,0,1, 1,0,0,1, 1,1,1,1], # 0
[0,1,0,0, 1,1,0,0, 0,1,0,0, 1,1,1,0], # 1
[1,1,1,0, 0,0,1,0, 1,1,1,0, 1,0,0,0], # 2
[1,1,1,0, 0,0,1,0, 1,1,1,0, 0,0,1,0], # 3
[1,0,1,0, 1,0,1,0, 1,1,1,0, 0,0,1,0], # 4
])
y = np.array([0, 1, 2, 3, 4])
print("MNIST DATASET\n")
for i in range(len(X)):
    print("Digit :", y[i])  # Added proper indentation (4 spaces)
    print(X[i].reshape(4,4))  # Added proper indentation (4 spaces)
    print()  # Added proper indentation (4 spaces)
print("Shape :", X.shape)
print("Labels:", len(y))
