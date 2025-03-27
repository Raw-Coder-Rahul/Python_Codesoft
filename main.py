import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = {}

        # Add Contact Section
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone Number:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.pack()
        self.address_entry = tk.Entry(root)
        self.address_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        # Search Section
        self.search_label = tk.Label(root, text="Search Contact by Name or Phone Number:")
        self.search_label.pack()
        self.search_entry = tk.Entry(root)
        self.search_entry.pack()

        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.pack()

        # Contact List
        self.contact_list_label = tk.Label(root, text="Contact List:")
        self.contact_list_label.pack()

        self.contact_listbox = tk.Listbox(root)
        self.contact_listbox.pack()

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            self.update_contact_list()
            messagebox.showinfo("Success", "Contact added successfully")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and phone number are required")

    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for name, details in self.contacts.items():
            self.contact_listbox.insert(tk.END, f"{name} - {details['phone']}")

    def search_contact(self):
        search_query = self.search_entry.get()
        found = False
        self.contact_listbox.delete(0, tk.END)

        for name, details in self.contacts.items():
            if search_query.lower() in name.lower() or search_query in details["phone"]:
                self.contact_listbox.insert(tk.END, f"{name} - {details['phone']}")
                found = True

        if not found:
            messagebox.showinfo("No Results", "No contacts found")

    def update_contact(self):
        selected_contact = self.contact_listbox.get(tk.ACTIVE)
        if selected_contact:
            name = selected_contact.split(" - ")[0]
            contact = self.contacts[name]

            self.name_entry.insert(0, name)
            self.phone_entry.insert(0, contact["phone"])
            self.email_entry.insert(0, contact["email"])
            self.address_entry.insert(0, contact["address"])

            self.delete_contact()
        else:
            messagebox.showerror("Error", "No contact selected")

    def delete_contact(self):
        selected_contact = self.contact_listbox.get(tk.ACTIVE)
        if selected_contact:
            name = selected_contact.split(" - ")[0]
            del self.contacts[name]
            self.update_contact_list()
            messagebox.showinfo("Success", "Contact deleted successfully")
        else:
            messagebox.showerror("Error", "No contact selected")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
