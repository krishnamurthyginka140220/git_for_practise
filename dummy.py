import pandas as pd
import numpy as np

# Create a DataFrame
emp_df = pd.DataFrame({
    'emp_id': range(1, 11),
    'emp_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ian', 'Jane'],
    'emp_age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'emp_salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000]
})
print("Using items():")
for label, content in emp_df.items():
    print(f"Column: {label}")
    print(f"Values:\n{content}\n")
