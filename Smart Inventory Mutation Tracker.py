import copy
def create_inventory():
    return [
        {
            "items": "Laptop",
            "details":{
                "price":50000,
                "stock": 10,
                "supplier": {"name": "Dell", "rating": 4.5}
            }
        },
        {
            "items": "Phone",
            "details":{
                "price":20000,
                "stock": 25,
                "supplier": {"name": "Samsung", "rating": 4.2}
            }
        }
    ]

def apply_discount(data, roll):
    idx= roll % len(data)
    for i in range(len(data)):
        data[i]["details"]["price"] = int(data[i]["details"]["price"] * 0.9)
        if i == idx:
            data[i]["details"]["stock"] -= 5
            data[i]["details"]["supplier"]["rating"] += 0.1

def compare_data(original, modified):
    changed = unchanged = 0
    for i in range(len(original)):
        if original[i] != modified[i]:
            changed += 1
        else:
            unchanged += 1
    return  (changed, unchanged)

roll = int(input("Enter roll number: "))
original = create_inventory()
backup = copy.deepcopy(original)
shallow = original.copy()
deep = copy.deepcopy(original)
apply_discount(shallow, roll)
apply_discount(deep, roll)
print("\n---- ORIGINAL INVENTORY ----")
for i,item in enumerate(original):
    print(f"{i}-> {item}")
print("\n---- SHALLOW COPY ----")
for i,item in enumerate(shallow):
    print(f"{i}-> {item}")
print("\n---- DEEP COPY ----")
for i,item in enumerate(deep):
    print(f"{i}-> {item}")
s = compare_data(backup, shallow)
d = compare_data(backup, deep)
print("\n---- DIFFERENCES ----")
print(f"Shallow Copy : {s}")
print(f"Deep Copy : {d}")
print("\n---- EXPLANATION ----")
print("Shallow copy shares nested data, so changes affected the original.")
print("Deep copy creates independent data, so original remains unchanged.")