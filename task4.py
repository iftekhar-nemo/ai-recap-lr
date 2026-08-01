import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

data = {
    "name": [
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Frank", "Grace", "Henry", "Isabella", "Jack"
    ],
    "age": [20, 22, 21, 23, 20, 24, 22, 21, 23, 20],
    "city": [
        "Dhaka", "Chattogram", "Khulna", "Rajshahi", "Sylhet",
        "Barishal", "Rangpur", "Cumilla", "Mymensingh", "Dhaka"
    ],
    "math_score":     [95, 82, 58, 47, 33, 76, 62, 39, 55, 28],
    "english_score":  [91, 74, 54, 42, 35, 80, 67, 31, 49, 25],
    "science_score":  [88, 79, 60, 45, 38, 72, 64, 36, 52, 30]
}
df = pd.DataFrame(data)

df["total_score"] = df[["math_score", "english_score", "science_score"]].sum(1)
df['avg_score'] = (df['total_score']/3).round(2)


df.plot(x='name', y='total_score', marker='o', ls='dotted')
plt.title("Avg Number graph", fontdict=font1, loc='left')
plt.xlabel("Student Name", fontdict=font2)
plt.ylabel("Avg Number", fontdict=font2)
plt.legend(['Avarage Number'])
plt.grid()
plt.show()

""" x=df[df['name']] """

plt.plot(df['name'], df['math_score'], marker='o', label='math')
plt.plot(df['name'], df['english_score'], marker='o', label='english')
plt.plot(df['name'], df['science_score'], marker='o', label='science')
plt.legend(['Math', 'English', 'Science'])

plt.show()

plt.hist(df['avg_score'], bins=5)
plt.show()




""" plt.subplot(1,3,1)
plt.title("Avg Number")
df.plot(x='name', y='total_score', marker='o', ls='dotted')
plt.xlabel("Student Name")
plt.ylabel("Avg Number")
plt.legend(['Avarage Number'])

plt.subplot(1,3,2)
plt.title("Indivisual Subject Score")
plt.plot(df['name'], df['math_score'], marker='o', label='math')
plt.plot(df['name'], df['english_score'], marker='o', label='english')
plt.plot(df['name'], df['science_score'], marker='o', label='science')
plt.legend(['Math', 'English', 'Science'])

plt.subplot(1,3,3)
plt.title("Avg Score Histogram")
plt.hist(df['avg_score'], bins=5) """


fig, axes = plt.subplots(1,3, figsize=(15,5))

axes[0].bar(df['name'], df['total_score'])
axes[0].set_title("Total Score")
axes[0].set_xlabel("Student Name")
axes[0].set_ylabel("Total Score")

axes[1].plot(df['math_score'], marker='o', label='Math')
axes[1].plot(df['english_score'], marker='o', label='English')
axes[1].plot(df['science_score'], marker='o', label='Science')
axes[1].set_title("Subject Scores")
axes[1].legend()

axes[2].hist(df['avg_score'], bins=5)
axes[2].set_title("Avg Score Distribution")












plt.show()