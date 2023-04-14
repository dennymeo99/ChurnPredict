import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import ttk
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
window = tk.Tk()
window.geometry("800x600")
window.title("ChurnPredict")
window.configure(background="#ffbf00")


def start():
    inputs = [int(w1.get()), w2.get(), int(w3.get()), int(w4.get()), int(w5.get()), w6.get(), int(w7.get()), w8.get(), int(w9.get()), int(w10.get()), int(w11.get()), int(w12.get()), float(w13.get()), w14.get(), w15.get(), w16.get(), w17.get(), w18.get()]
    inputs_fixed = adjust_record(inputs)
    res = calculate(inputs_fixed)
    if res == 0:
        text_output.config(text="No churn risk", fg="green")
    else:
        text_output.config(text="Churn risk detected!", fg="red")
    text_output.grid(row=13, column=0, columnspan=4)


def calculate(inputs):
    df = pd.read_csv('Ecommerce_filled.csv')
    X = df.drop("Churn", axis=1)
    y = df['Churn']
    rfc = RandomForestClassifier()
    pipe = Pipeline([('sampling', SMOTE(random_state = 123)), ('classification', rfc)])
    pipe.fit(X, y)
    inputs_array = np.array(inputs)
    inputs_reshaped = inputs_array.reshape(1, -1)
    res = pipe.predict(inputs_reshaped)
    return res


def adjust_record(inputs):
    if inputs[7] == "No":
        complained = 0
    else:
        complained = 1

    if inputs[13] == "Computer":
        dummy_login = [1, 0]
    else:
        dummy_login = [0, 1]

    if inputs[14] == "Cash on Delivery":
        dummy_payment = [1, 0, 0, 0, 0]
    elif inputs[14] == "Credit Card":
        dummy_payment = [0, 1, 0, 0, 0]
    elif inputs[14] == "Debit Card":
        dummy_payment = [0, 0, 1, 0, 0]
    elif inputs[14] == "E Wallet":
        dummy_payment = [0, 0, 0, 1, 0]
    else:
        dummy_payment = [0, 0, 0, 0, 1]

    if inputs[15] == "Female":
        dummy_gender = [1, 0]
    else:
        dummy_gender = [0, 1]

    if inputs[16] == "Fashion":
        dummy_category = [1, 0, 0, 0, 0]
    elif inputs[16] == "Grocery":
        dummy_category = [0, 1, 0, 0, 0]
    elif inputs[16] == "Laptop & Accessory":
        dummy_category = [0, 0, 1, 0, 0]
    elif inputs[16] == "Mobile Phone":
        dummy_category = [0, 0, 0, 1, 0]
    else:
        dummy_category = [0, 0, 0, 0, 1]

    if inputs[17] == "Divorced":
        dummy_status = [1, 0, 0]
    elif inputs[17] == "Married":
        dummy_status = [0, 1, 0]
    else:
        dummy_status = [0, 0, 1]

    res = [5630, inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5], inputs[6], complained, inputs[8], inputs[9], inputs[10], inputs[11], inputs[12], dummy_login[0], dummy_login[1], dummy_payment[0], dummy_payment[1], dummy_payment[2], dummy_payment[3], dummy_payment[4], dummy_gender[0], dummy_gender[1], dummy_category[0], dummy_category[1], dummy_category[2], dummy_category[3], dummy_category[4], dummy_status[0], dummy_status[1], dummy_status[2]]
    return res


title = tk.Label(text="ChurnPredict", anchor="center", background="#ffbf00", font=("Arial", 20, "bold"))
title.grid(row=0, columnspan=4, padx=40)

l1 = tk.Label(text="Tenure:", anchor="center", background="#ffbf00", font=("arial", 10))
l1.grid(row=1, column=0, padx=20)

w1 = tk.Entry(background="white")
w1.grid(row=2, column=0, padx=20)

l2 = tk.Label(text="City tier:", anchor="center", background="#ffbf00", font=("arial", 10))
l2.grid(row=1, column=1, padx=20)

w2 = ttk.Combobox(values=(1, 2, 3))
w2.grid(row=2, column=1, padx=20)

l3 = tk.Label(text="Warehouse to home:", anchor="center", background="#ffbf00", font=("arial", 10))
l3.grid(row=1, column=2, padx=20)

w3 = tk.Entry(background="white")
w3.grid(row=2, column=2, padx=20)

l4 = tk.Label(text="Hours spent on app:", anchor="center", background="#ffbf00", font=("arial", 10))
l4.grid(row=1, column=3, padx=20)

w4 = tk.Entry(background="white")
w4.grid(row=2, column=3, padx=20)

l5 = tk.Label(text="Number of devices registered:", anchor="center", background="#ffbf00", font=("arial", 10))
l5.grid(row=3, column=0, padx=20)

w5 = tk.Entry(background="white")
w5.grid(row=4, column=0, padx=20)

l6 = tk.Label(text="Satisfaction score:", anchor="center", background="#ffbf00", font=("arial", 10))
l6.grid(row=3, column=1, padx=20)

w6 = ttk.Combobox(values=(1, 2, 3, 4, 5))
w6.grid(row=4, column=1, padx=20)

l7 = tk.Label(text="Number of addresses:", anchor="center", background="#ffbf00", font=("arial", 10))
l7.grid(row=3, column=2, padx=20)

w7 = tk.Entry(background="white")
w7.grid(row=4, column=2, padx=20)

l8 = tk.Label(text="Complained:", anchor="center", background="#ffbf00", font=("arial", 10))
l8.grid(row=3, column=3, padx=20)

w8 = ttk.Combobox(values=("No", "Yes"))
w8.grid(row=4, column=3, padx=20)

l9 = tk.Label(text="Order amount hike last year:", anchor="center", background="#ffbf00", font=("arial", 10))
l9.grid(row=5, column=0, padx=20)

w9 = tk.Entry(background="white")
w9.grid(row=6, column=0, padx=20)

l10 = tk.Label(text="Coupon used:", anchor="center", background="#ffbf00", font=("arial", 10))
l10.grid(row=5, column=1, padx=20)

w10 = tk.Entry(background="white")
w10.grid(row=6, column=1, padx=20)

l11 = tk.Label(text="Order count:", anchor="center", background="#ffbf00", font=("arial", 10))
l11.grid(row=5, column=2, padx=20)

w11 = tk.Entry(background="white")
w11.grid(row=6, column=2, padx=20)

l12 = tk.Label(text="Day since last order:", anchor="center", background="#ffbf00", font=("arial", 10))
l12.grid(row=5, column=3, padx=20)

w12 = tk.Entry(background="white")
w12.grid(row=6, column=3, padx=20)

l13 = tk.Label(text="Cashback amount:", anchor="center", background="#ffbf00", font=("arial", 10))
l13.grid(row=7, column=0, padx=20)

w13 = tk.Entry(background="white")
w13.grid(row=8, column=0, padx=20)

l14 = tk.Label(text="Preferred login device:", anchor="center", background="#ffbf00", font=("arial", 10))
l14.grid(row=7, column=1, padx=20)

w14 = ttk.Combobox(values=("Computer", "Mobile phone"))
w14.grid(row=8, column=1, padx=20)

l15 = tk.Label(text="Preferred payment mode:", anchor="center", background="#ffbf00", font=("arial", 10))
l15.grid(row=7, column=2, padx=20)

w15 = ttk.Combobox(values=("Cash on delivery", "Credit Card", "Debit Card", "E Wallet", "UPI"))
w15.grid(row=8, column=2, padx=20)

l16 = tk.Label(text="Gender:", anchor="center", background="#ffbf00", font=("arial", 10))
l16.grid(row=7, column=3, padx=20)

w16 = ttk.Combobox(values=("Female", "Male"))
w16.grid(row=8, column=3, padx=20)

l17 = tk.Label(text="Preferred order Category:", anchor="center", background="#ffbf00", font=("arial", 10))
l17.grid(row=9, column=1, padx=20)

w17 = ttk.Combobox(values=("Fashion", "Grocery", "Laptop & Accessory", "Mobile Phone", "Others"))
w17.grid(row=10, column=1, padx=20)

l18 = tk.Label(text="Marital Status:", anchor="center", background="#ffbf00", font=("arial", 10))
l18.grid(row=9, column=2, padx=20)

w18 = ttk.Combobox(values=("Divorced", "Married", "Single"))
w18.grid(row=10, column=2, padx=20)

first_button = tk.Button(text="Confirm", command=start)
first_button.grid(row=11, column=0, columnspan=4, pady=20, padx=40)

text_output = tk.Label(background="#ffbf00", font=("Helvetica", 16))
text_output.grid(row=13, column=0, columnspan=4)

icon_image = tk.PhotoImage(file='icon.png')
icon = tk.Label(image=icon_image, background="#ffbf00")
icon.grid(row=15, column=0, columnspan=4, padx=30)

if __name__ == "__main__":
    window.mainloop()