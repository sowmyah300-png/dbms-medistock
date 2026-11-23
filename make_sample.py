# Run this once: python make_sample.py  -> creates messy_data.csv
import pandas as pd

rows = [
    [1, "Amit Sharma", "amit@gmail.com", 24, "Delhi", "2024-05-12"],
    [2, "Priya Rao", "priya@gmail.com", 31, "bengaluru", "12/05/2024"],
    [3, "Rahul Verma", "rahul.gmail.com", 28, "Mumbai", "2024-06-01"],
    [4, "Sneha Iyer", "sneha@gmail.com", None, "Chennai", "2024-06-03"],
    [5, "Karan Singh", "karan@gmail.com", 250, "DELHI", "2024-06-10"],
    [6, "Neha Gupta", "neha@gmail.com", 27, None, "2024-06-11"],
    [7, "Amit Sharma", "amit@gmail.com", 24, "Delhi", "2024-05-12"],   # duplicate of row 1
    [8, "Vikas Jain", "vikas@gmail.com", 35, " mumbai ", "2024-07-01"],
    [9, "Anita Das", "anita@gmail.com", None, "Kolkata", "2024-07-04"],
    [10, "Rohan Mehta", "rohan@gmail.com", 29, "chennai", "2024-07-09"],
]
df = pd.DataFrame(rows, columns=["id", "name", "email", "age", "city", "joined"])
df.to_csv("messy_data.csv", index=False)
print("Created messy_data.csv")
