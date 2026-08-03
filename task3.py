#name, age, city, math_score, english_score, science_score

import numpy as np
import pandas as pd

#help(pd.DataFrame.head)

#dataframe data

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


#output
df = pd.DataFrame(data)

df["total_score"] = df[["math_score", "english_score", "science_score"]].sum(1)
df['avg_score'] = (df['total_score']/3).round(2)

condition = [
    (df["avg_score"] > 60),
    (df["avg_score"] >= 40) & (df["avg_score"] <= 60 ),
    (df["avg_score"] < 40)
]

grade = ['A', 'B', 'C']

df["grade"] = np.select(condition, grade, default="none")

print("First 5info using head method: ",df.head(5))
print("Use info method: ",df.info())
print("Usinf describe method :",df.describe())



print("Sorted by math score:\n", df.sort_values("math_score", ascending=False))
print("show Grade A Student: ", df[df["grade"] == "A"])

citygrp = df.groupby("city")["avg_score"].mean()
print("Group by: ", citygrp)