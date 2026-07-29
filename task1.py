import numpy as np
import pandas as pd

tmpArr = []

for i in range(1, 101):
    tmpArr.append(i)

arr = np.array(tmpArr)

mean= np.mean(arr)
median = np.median(arr)
std = np.std(arr)


print("Mean :", mean, "Median :", median, "STD : ", std)


## pandas data frame

data = {
    "name": ["karim", "rahim", "abdullah", "david", "rock", "austin"],
    "age" : [15,65,31,4,45,75],
    "score":[52,12,48,68,45,100]
}

df = pd.DataFrame(data)
df['pass_fail'] =df["score"].apply(lambda x: 'Pass' if x > 50 else 'Fail')

newdf = df[df['score'] > 50 ]

print(newdf)