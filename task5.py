import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 


data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "exam_score" : [35, 45, 50, 55, 65, 70, 75, 85, 90, 95]
}


df = pd.DataFrame(data)
x=df[["study_hours"]]
print(x)
y=df['exam_score']

plt.scatter(x,y)
plt.grid()
plt.show()

model = LinearRegression()

model.fit(x,y)

new_input = [[7.5]]
predicted = model.predict(new_input)
print(f"7.5 ঘণ্টা পড়লে predicted score: {predicted[0]:.2f}")


plt.scatter(x, y, label='Actual')
plt.plot(x, model.predict(x), color='red', label='Predicted Line')
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.legend()
plt.show()