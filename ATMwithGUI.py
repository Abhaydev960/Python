
import tkinter as tk
from tkinter import messagebox, simpledialog

balance = 5000.0

def show_balance():
    messagebox.showinfo("Balance", f"Available balance: Rs. {balance:.2f}")


def deposit():
    global balance
    amount = simpledialog.askfloat("Deposit", "Enter amount (Rs.):")

    if amount is not None:
        if amount > 0:
            balance += amount
            messagebox.showinfo("Success", "Deposit successful.")
        else:
            messagebox.showwarning("Invalid", "Enter a positive amount.")


def withdraw():
    global balance
    amount = simpledialog.askfloat("Withdraw", "Enter amount (Rs.):")

    if amount is not None:
        if 0 < amount <= balance:
            balance -= amount
            messagebox.showinfo("Success", "Please collect your cash.")
        else:
            messagebox.showwarning(
                "Invalid", "Insufficient balance or invalid amount."
            )


# Main window
root = tk.Tk()
root.title("Simple ATM")
root.geometry("320x260")

# Heading
tk.Label(
    root,
    text="WELCOME TO PYTHON ATM",
    font=("Arial", 14, "bold")
).pack(pady=15)

# ATM buttons
tk.Button(
    root, text="Check Balance", width=22,
    command=show_balance
).pack(pady=5)

tk.Button(
    root, text="Deposit", width=22,
    command=deposit
).pack(pady=5)

tk.Button(
    root, text="Withdraw", width=22,
    command=withdraw
).pack(pady=5)

tk.Button(
    root, text="Exit", width=22,
    command=root.destroy
).pack(pady=5)

# Run the application
root.mainloop()
