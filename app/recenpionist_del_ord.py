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


def delete_order():
    try:
        connection = mysql.connector.connect(**CONFIG)

        cursor = connection.cursor()

        order_id = order_id_entry.get()
        check_query = "SELECT COUNT(*) FROM Orders WHERE orderID = %s"
        cursor.execute(check_query, (order_id,))
        order_exists = cursor.fetchone()[0]

        if order_exists:
            delete_query = "DELETE FROM Orders WHERE orderID = %s"
            cursor.execute(delete_query, (order_id,))
            connection.commit()

            messagebox.showinfo(
                "Success", f"Order with ID {order_id} deleted successfully!"
            )
        else:
            messagebox.showerror("Error", f"Order with ID {order_id} does not exist!")

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to delete order: {error}")


root = tk.Tk()
root.title("Delete Order")

order_id_label = tk.Label(root, text="Order ID:")
order_id_label.grid(row=0, column=0)
order_id_entry = tk.Entry(root)
order_id_entry.grid(row=0, column=1)

submit_button = tk.Button(root, text="Delete Order", command=delete_order)
submit_button.grid(row=1, column=0, columnspan=2)

root.mainloop()
