import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(password_length_entry.get())
    if length < 8:
        messagebox.showinfo("Information", "Minimum Password length is 8")
        return

    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    symbols = "!@#$%^&*(){}?_=+-"
    numbers = "0123456789"

    all_characters = upper_alphabet + lower_alphabet + symbols + numbers

    password = ''.join(random.choices(all_characters, k=length))
    encrypted_password = caesar_cipher(password)
    password_label.config(text=encrypted_password)

def caesar_cipher(password, shift=3):
    encrypted = []
    for char in password:
        if char.isalpha():
            if char.islower():
                start = ord('a')
                encrypted.append(chr((ord(char) - start + shift) % 26 + start))
            else:
                start = ord('A')
                encrypted.append(chr((ord(char) - start + shift) % 26 + start))
        elif char.isdigit():
            start = ord('0')
            encrypted.append(chr((ord(char) - start + shift) % 10 + start))
        else:
            encrypted.append(char)
    return ''.join(encrypted)

def main():
    global password_length_entry, password_label
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("400x300")
    window.configure(bg="#F0F0F0")

    title_label = tk.Label(window, text="Password Generator", font=("Helvetica", 18, "bold"), bg="#F0F0F0")
    title_label.pack(pady=10)

    label = tk.Label(window, text="Enter the password length:", font=("Helvetica", 12), bg="#F0F0F0")
    label.pack(pady=5)

    password_length_entry = tk.Entry(window, font=("Helvetica", 12))
    password_length_entry.pack(pady=5)

    generate_button = tk.Button(window, text="Generate Password", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", command=generate_password)
    generate_button.pack(pady=10)

    password_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#F0F0F0")
    password_label.pack(pady=10)

    window.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":
    main()
