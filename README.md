
## Smart Inventory Mutation Tracker

This project demonstrates how data behaves when copied and modified in Python using **shallow copy and deep copy**. It simulates a warehouse inventory system where each product contains nested details such as price, stock, and supplier information.
The program applies controlled mutations based on a **roll number–based logic** and compares how changes affect the original data structure.

---

## Features

* Stores inventory using **nested dictionaries inside lists**
* Implements **modular functions** for clean structure
* Uses both:

  * Shallow Copy
  * Deep Copy
* Applies:

  * **10% price reduction** for all items
  * **Selective stock & rating update** based on roll number
* Compares original and modified data
* Displays differences using tuple summary

---

## Key Concept

* **Shallow Copy** shares nested references → changes affect original
* **Deep Copy** creates independent data → original remains unchanged

---

## Personalization Logic

Mutation is applied using:

```
index = roll_number % length_of_inventory
```

For roll number **24110011636**,
→ Selected index = **0 (Laptop)**

---

## Tech Used

* Python
* Lists & Dictionaries
* Functions
* Copy Module

---

## Learning Outcome

* Understanding of **data copying behavior**
* Importance of **deep copy in real-world applications**
* Handling **nested data structures safely**
