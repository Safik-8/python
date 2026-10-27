import seaborn as sns
import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "age": [20, 25, 30, 35, 40],
    "salary": [30000, 40000, 50000, 60000, 70000]
}

df = pd.DataFrame(data)
sns.lineplot(data=df, x="age", y="salary")