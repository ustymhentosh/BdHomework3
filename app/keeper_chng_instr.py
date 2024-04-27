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


def get_status():
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(**CONFIG)

        # Create cursor
        cursor = connection.cursor()

        # Get instrument serial number from entry field
        instrument_serial_num = instrument_serial_num_entry.get()

        # Fetch current status
        select_query = "SELECT status FROM Instruments WHERE serialNum = %s"
        cursor.execute(select_query, (instrument_serial_num,))
        current_status = cursor.fetchone()

        if current_status:
            current_status_label.config(text=f"Current Status: {current_status[0]}")
        else:
            current_status_label.config(text="Current Status: Not Found")

        # Close cursor and connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to get instrument status: {error}")


def change_status(status):
    try:
        connection = mysql.connector.connect(**CONFIG)

        cursor = connection.cursor()

        instrument_serial_num = instrument_serial_num_entry.get()

        check_query = "SELECT COUNT(*) FROM Instruments WHERE serialNum = %s"
        cursor.execute(check_query, (instrument_serial_num,))
        instrument_exists = cursor.fetchone()[0]

        if instrument_exists:
            update_query = "UPDATE Instruments SET status = %s WHERE serialNum = %s"
            status_data = (status, instrument_serial_num)

            cursor.execute(update_query, status_data)

            connection.commit()

            messagebox.showinfo(
                "Success",
                f"Instrument status changed to {status} for Serial Number: {instrument_serial_num}",
            )
        else:
            messagebox.showerror(
                "Error",
                f"Instrument with Serial Number {instrument_serial_num} not found!",
            )

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to change instrument status: {error}")


root = tk.Tk()
root.title("Change Instrument Status")

instrument_serial_num_label = tk.Label(root, text="Instrument Serial Number:")
instrument_serial_num_label.grid(row=0, column=0)
instrument_serial_num_entry = tk.Entry(root)
instrument_serial_num_entry.grid(row=0, column=1)

current_status_label = tk.Label(root, text="Current Status: Not Found")
current_status_label.grid(row=1, column=0, columnspan=2)

get_status_button = tk.Button(root, text="Get Status", command=get_status)
get_status_button.grid(row=2, column=0, columnspan=2, pady=5)

change_to_1_button = tk.Button(
    root, text="Change Status to 1", command=lambda: change_status(1)
)
change_to_1_button.grid(row=3, column=0, pady=5)

change_to_0_button = tk.Button(
    root, text="Change Status to 0", command=lambda: change_status(0)
)
change_to_0_button.grid(row=3, column=1, pady=5)

root.mainloop()
