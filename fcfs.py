import pandas as pd

pid = ["p1", "p2", "p3", "p4", "p5"]
at = [0, 3, 4, 5, 5]
bt = [2, 4, 3, 3, 1]
n = len(pid)
for i in range(n):
    for j in range(0,n-i-1):
       if at[j]>at[j+1]:
                at[j],at[j+1]=at[j+1],at[j]
                pid[j],pid[j+1]=pid[j+1],pid[j]
                bt[j],bt[j+1]=bt[j+1],bt[j]
df = pd.DataFrame({"PID":pid,"AT":at,"BT":bt})
ct = []
tat = []
wt = []

for i in range(n):
    if i == 0:
        ct.append(at[0] + bt[0])
    else:
        ct.append(bt[i] + max(ct[i - 1], at[i]))

for i in range(n):
    tat.append(ct[i] - at[i])
    wt.append(tat[i] - bt[i])

df2 = pd.DataFrame({"PID": pid, "AT": at, "BT": bt, "CT": ct, "TAT": tat, "WT": wt})
avg_wt = sum(wt) / n
avg_tat = sum(tat) / n

print(df2)
print("Average Waiting Time:", avg_wt)
print("Average Turnaround Time:", avg_tat)