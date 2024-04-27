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


def add_experience():
    try:
        connection = mysql.connector.connect(**CONFIG)

        cursor = connection.cursor()

        photographer_id = photographer_id_entry.get()

        check_query = (
            "SELECT EXISTS(SELECT 1 FROM Photographers WHERE photographerID = %s)"
        )
        cursor.execute(check_query, (photographer_id,))
        photographer_exists = cursor.fetchone()[0]

        if photographer_exists:
            select_query = (
                "SELECT experience FROM Photographers WHERE photographerID = %s"
            )
            cursor.execute(select_query, (photographer_id,))
            current_experience = cursor.fetchone()[0]

            new_experience = current_experience + 1

            update_query = (
                "UPDATE Photographers SET experience = %s WHERE photographerID = %s"
            )
            experience_data = (new_experience, photographer_id)

            cursor.execute(update_query, experience_data)

            connection.commit()

            messagebox.showinfo(
                "Success",
                f"One year of experience added to photographer {photographer_id}!",
            )
        else:
            messagebox.showerror(
                "Error", f"Photographer with ID {photographer_id} does not exist!"
            )
        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to add experience: {error}")


root = tk.Tk()
root.title("Modify Experience")

photographer_id_label = tk.Label(root, text="Photographer ID:")
photographer_id_label.grid(row=0, column=0)
photographer_id_entry = tk.Entry(root)
photographer_id_entry.grid(row=0, column=1, sticky="ew")

submit_button = tk.Button(root, text="Add Experience", command=add_experience)
submit_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
