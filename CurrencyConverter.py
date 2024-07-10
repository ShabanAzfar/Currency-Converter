import tkinter as tk
from tkinter import ttk

# Define the conversion rates
USD_to_PKR = 278.55
USD_to_INR = 83.47
USD_to_TAKA = 117.49
INR_to_PKR = 3.34
TAKA_to_PKR = 2.37
INR_to_TAKA = 1.41

# Function to perform the conversion
def currency_converter():
    amount = float(amount_entry.get())
    currency = currency_var.get()

    if currency == "USD":
        pkr = amount * USD_to_PKR
        inr = amount * USD_to_INR
        taka = amount * USD_to_TAKA
        result_var.set(f"PKR: {pkr:.2f}\nINR: {inr:.2f}\nTAKA: {taka:.2f}")
    elif currency == "PKR":
        usd = amount / USD_to_PKR
        inr = amount / INR_to_PKR
        taka = amount / TAKA_to_PKR
        result_var.set(f"USD: {usd:.2f}\nINR: {inr:.2f}\nTAKA: {taka:.2f}")
    elif currency == "INR":
        usd = amount / USD_to_INR
        pkr = amount * INR_to_PKR
        taka = amount * INR_to_TAKA
        result_var.set(f"USD: {usd:.2f}\nPKR: {pkr:.2f}\nTAKA: {taka:.2f}")
    elif currency == "TAKA":
        usd = amount / USD_to_TAKA
        pkr = amount * TAKA_to_PKR
        inr = amount / INR_to_TAKA
        result_var.set(f"USD: {usd:.2f}\nPKR: {pkr:.2f}\nINR: {inr:.2f}")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

# Create a label for the amount entry
amount_label = ttk.Label(root, text="Enter amount:")
amount_label.pack(pady=10)

# Create an entry widget for the amount
amount_entry = ttk.Entry(root)
amount_entry.pack(pady=10)

# Create a dropdown menu for selecting the currency
currency_var = tk.StringVar()
currency_dropdown = ttk.Combobox(root, textvariable=currency_var)
currency_dropdown['values'] = ("USD", "PKR", "INR", "TAKA")
currency_dropdown.current(0)
currency_dropdown.pack(pady=10)

# Create a button to perform the conversion
convert_button = ttk.Button(root, text="Convert", command=currency_converter)
convert_button.pack(pady=10)

# Create a label to display the results
result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, font=("Helvetica", 12))
result_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
