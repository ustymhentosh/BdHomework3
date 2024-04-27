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


def add_photo():
    try:
        connection = mysql.connector.connect(**CONFIG)

        cursor = connection.cursor()

        img_id = img_id_entry.get()
        latitude = latitude_entry.get()
        longitude = longitude_entry.get()
        instrument_serial_num = instrument_serial_num_entry.get()
        storage_id = storage_id_entry.get()
        order_id = order_id_entry.get()
        resolution = resolution_entry.get()
        time = time_entry.get()
        date = date_entry.get()
        title = title_entry.get()

        insert_query = "INSERT INTO Images (imgID, latitude, longitude, instrumentSerialNum, storageID, orderID, resolution, time, date, title) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        photo_data = (
            img_id,
            latitude,
            longitude,
            instrument_serial_num,
            storage_id,
            order_id,
            resolution,
            time,
            date,
            title,
        )

        cursor.execute(insert_query, photo_data)

        connection.commit()

        cursor.close()
        connection.close()

        messagebox.showinfo("Success", "Photo added successfully!")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to add photo: {error}")


root = tk.Tk()
root.title("Add Photo")

img_id_label = tk.Label(root, text="Image ID:")
img_id_label.grid(row=0, column=0)
img_id_entry = tk.Entry(root)
img_id_entry.grid(row=0, column=1)

latitude_label = tk.Label(root, text="Latitude:")
latitude_label.grid(row=1, column=0)
latitude_entry = tk.Entry(root)
latitude_entry.grid(row=1, column=1)

longitude_label = tk.Label(root, text="Longitude:")
longitude_label.grid(row=2, column=0)
longitude_entry = tk.Entry(root)
longitude_entry.grid(row=2, column=1)

instrument_serial_num_label = tk.Label(root, text="Instrument Serial Num:")
instrument_serial_num_label.grid(row=3, column=0)
instrument_serial_num_entry = tk.Entry(root)
instrument_serial_num_entry.grid(row=3, column=1)

storage_id_label = tk.Label(root, text="Storage ID:")
storage_id_label.grid(row=4, column=0)
storage_id_entry = tk.Entry(root)
storage_id_entry.grid(row=4, column=1)

order_id_label = tk.Label(root, text="Order ID:")
order_id_label.grid(row=5, column=0)
order_id_entry = tk.Entry(root)
order_id_entry.grid(row=5, column=1)

resolution_label = tk.Label(root, text="Resolution:")
resolution_label.grid(row=6, column=0)
resolution_entry = tk.Entry(root)
resolution_entry.grid(row=6, column=1)

time_label = tk.Label(root, text="Time:")
time_label.grid(row=7, column=0)
time_entry = tk.Entry(root)
time_entry.grid(row=7, column=1)

date_label = tk.Label(root, text="Date:")
date_label.grid(row=8, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=8, column=1)

title_label = tk.Label(root, text="Title:")
title_label.grid(row=9, column=0)
title_entry = tk.Entry(root)
title_entry.grid(row=9, column=1)

submit_button = tk.Button(root, text="Submit", command=add_photo)
submit_button.grid(row=10, column=0, columnspan=2)

root.mainloop()
