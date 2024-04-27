import tkinter as tk
from tkinter import messagebox
import mysql.connector

CONFIG = {
    "user": "root",
    "password": "dRqUS7eVC9rc9RPtfiLl",
    "host": "localhost",
    "port": 3305,
    "database": "photography",
    "auth_plugin": "mysql_native_password",
    "ssl_disabled": True,
}


def add_order():
    try:
        connection = mysql.connector.connect(**CONFIG)

        cursor = connection.cursor()

        order_id = order_id_entry.get()
        agency_id = agency_id_entry.get()
        total_price = total_price_entry.get()
        client_id = client_id_entry.get()
        description = description_entry.get()
        status = status_entry.get()
        assigned_photographer = assigned_photographer_entry.get()

        insert_query = "INSERT INTO Orders (orderID, agencyID, totalPrice, clientID, description, status, assignedPhotographer) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        order_data = (
            order_id,
            agency_id,
            total_price,
            client_id,
            description,
            status,
            assigned_photographer,
        )

        cursor.execute(insert_query, order_data)

        connection.commit()

        cursor.close()
        connection.close()

        messagebox.showinfo("Success", "Order added successfully!")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to add order: {error}")


root = tk.Tk()
root.title("Add Order")

order_id_label = tk.Label(root, text="Order ID:")
order_id_label.grid(row=0, column=0)
order_id_entry = tk.Entry(root)
order_id_entry.grid(row=0, column=1)

agency_id_label = tk.Label(root, text="Agency ID:")
agency_id_label.grid(row=1, column=0)
agency_id_entry = tk.Entry(root)
agency_id_entry.grid(row=1, column=1)

total_price_label = tk.Label(root, text="Total Price:")
total_price_label.grid(row=2, column=0)
total_price_entry = tk.Entry(root)
total_price_entry.grid(row=2, column=1)

client_id_label = tk.Label(root, text="Client ID:")
client_id_label.grid(row=3, column=0)
client_id_entry = tk.Entry(root)
client_id_entry.grid(row=3, column=1)

description_label = tk.Label(root, text="Description:")
description_label.grid(row=4, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=4, column=1)

status_label = tk.Label(root, text="Status:")
status_label.grid(row=5, column=0)
status_entry = tk.Entry(root)
status_entry.grid(row=5, column=1)

assigned_photographer_label = tk.Label(root, text="Assigned Photographer:")
assigned_photographer_label.grid(row=6, column=0)
assigned_photographer_entry = tk.Entry(root)
assigned_photographer_entry.grid(row=6, column=1)
submit_button = tk.Button(root, text="Submit", command=add_order)
submit_button.grid(row=7, column=0, columnspan=2)

root.mainloop()
