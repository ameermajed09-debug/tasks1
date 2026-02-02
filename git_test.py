from typing import List,Dict,Tuple
import pandas as pd
# task 1
cat_a=[1,2,3,4,5]
cat_b=[10,20,30]
def calculate_data(data):
    mean=sum(data) / len(data)
    max1=max(data)
    return {"mean": mean,"max":max1}
stats_a=calculate_data(cat_a)
stats_b=calculate_data(cat_b)
print("A:",stats_a)
print("B:",stats_b)

# task 2

data2=[66,65,353,53]
data1=[5353,736,242,242]
def calculate_statistics(data: List[float]) -> Dict[str, float]:
    print("max :",max(data))
    print("min :",min(data))
    print("mean :",sum(data) / len(data))
    return "thanks for using"
print(calculate_statistics(data1))
def normalize_data(data: List[float], method: str = "minmax") -> List[float]:
    return [(x - min(data)) / (max(data) - min(data)) for x in data]
print(normalize_data(data1))
def remove_outliers(data: List[float], threshold: float) -> List[float]:
    mean = sum(data) / len(data)
    stdv = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    cleand = list(filter(lambda x: abs(x - mean) <= threshold * stdv, data))
    return cleand
print(remove_outliers(data2,threshold=1.0 ))

def train_test_split(data: List[float], ratio: float = 0.8) -> Tuple[List[float], List[float]]:
    lim=int(len(data) * ratio)
    traind=data[:lim]
    test=data[lim:]
    return traind , test
print(train_test_split(data1,ratio=0.6))
def encode_labels(labels: List[str]) -> Dict[str, int]:
    uni = sorted(list(set(labels)))
    return {label: i for i, label in enumerate(uni)}
test_l = ["Apple", "Orange", "Apple", "Banana", "Orange"]
encoded = encode_labels(test_l)
print(encoded)

# task 3

raw = {
    "product": ["Widget A", "Widget B", "Widget C"],
    "price": ["$1,234.50", "$567.89", "$2,345.00"],
    "quantity": [10, 5, None],
}
df = pd.DataFrame(raw)
df['price'] = df['price'].str.replace(r'[$,]', '', regex=True).astype(float)
df['quantity'] = df['quantity'].fillna(0)
df['total'] = df['price'] * df['quantity']

def categorize(p):
    if p < 1000: return 'low'
    if p < 2000: return 'med'
    return 'high'

df['price_category'] = df['price'].apply(categorize)
raw_data = {
    "product": ["Widget A", "Widget B", "Widget C"],
    "price": ["$1,234.50", "$567.89", "$2,345.00"],
    "quantity": [10, 5, None],
}
df = pd.DataFrame(raw_data)

df['price'] = df['price'].apply(lambda x: float(x.replace('$', '').replace(',', '')))
df['quantity'] = df['quantity'].fillna(0)
df['total'] = df['price'] * df['quantity']
df['price_category'] = df['price'].apply(categorize)


print(" Results ")
print(df)


# task 4
students = {
    "S001": {
        "name": "Alice",
        "courses": {
            "CS101": {"grade": 85, "credits": 3},
            "AI301": {"grade": 92, "credits": 4}
        }
    },
    "S002": {
        "name": "Bob",
        "courses": {
            "CS101": {"grade": 70, "credits": 3},
            "MATH202": {"grade": 88, "credits": 3}
        }
    }
}

alice_g= students["S001"]["courses"]["AI301"]["grade"]

bobc = students["S002"]["courses"]
totalp = sum(c["grade"] * c["credits"] for c in bobc.values())
totalc = sum(c["credits"] for c in bobc.values())
bobgp= totalp / totalc

cs101s = [info["name"] for info in students.values() if "CS101" in info["courses"]]

all_g = [c["grade"] for s in students.values() for c in s["courses"].values()]

top_s=max(students.values(),key=lambda s:sum(c["grade"] * c["credits"] for c in s["courses"].values()) / sum(c["credits"] for c in s["courses"].values()))

avg_g = sum(all_g) / len(all_g)
print(f"Alice AI Grade: {alice_g}")
print(f"Bob GPA: {bobgp:.2f}")
print(f"Students in CS101: {cs101s}")
print(f"Overall Average: {avg_g:.2f}")
print(f"The Student with the highest gpa is {top_s["name"]}")



def process(df: pd.DataFrame) -> pd.DataFrame:
    df['price'] = df['price'].apply(lambda x: float(x.replace('$', '').replace(',', '')))
    df['quantity'] = df['quantity'].fillna(0)
    df['total_value'] = df['price'] * df['quantity']
    df['price_category'] = df['price'].apply(
        lambda x: 'low' if x < 1000 else ('med' if x < 2000 else 'high')
    )

    return df
if __name__ == "__main__":
    raw_data = {
        "product": ["Widget A", "Widget B", "Widget C", "Widget D"],
        "price": ["$1,234.50", "$567.89", "$2,345.00", "$150.00"],
        "quantity": [10, 5, None, 20],
    }

    inven = pd.DataFrame(raw_data)

    print()
    print(inven)

    c_df = process(inven)

    print("data after cleaned:")
    print(c_df)





# Task 5
import json
from pathlib import Path
cn=Path("config.json")
with open (cn,"r") as f:
    data=json.load(f)
print(data)
dict={" model : Amer_Ai,"
     "epochs" : 60,
     "lr":0.002}
file=Path("result.json")
with open ("result.json","w") as f:
    json.dump(dict,f,indent=4)


