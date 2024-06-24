import sqlite3
from pathlib import Path
import subprocess
import tkinter as tk
from tkinter import Canvas, Button, PhotoImage, StringVar, OptionMenu
from functools import partial

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\houtp\OneDrive\Desktop\Final2\DeleteRoom")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_addroom():
    subprocess.Popen(["python", "AddRoom.py"])

def open_reservation():
    subprocess.Popen(["python", "Reservation.py"])

def connect_to_database():
    try:
        conn = sqlite3.connect('rooms.db')  # Replace 'rooms.db' with your actual database name
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def get_available_rooms():
    conn = connect_to_database()
    if conn is None:
        return []  # Return an empty list if connection failed

    cursor = conn.cursor()
    cursor.execute("SELECT roomnumber FROM rooms")  # Assuming 'available' is a boolean field
    room_numbers = [row[0] for row in cursor.fetchall()]
    conn.close()
    return room_numbers

def delete_room(window, room_var, room_options_menu):
    selected_room = room_var.get()
    if not selected_room:
        print("Please select a room to delete.")
        return

    conn = connect_to_database()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute("DELETE FROM rooms WHERE roomnumber = ?", (selected_room,))
    conn.commit()
    conn.close()

    # Update dropdown menu after deletion (optional)
    room_var.set('')  # Clear the selected option
    room_options = get_available_rooms()
    room_options_menu['menu'].delete(0, 'end')  # Clear all existing options
    for option in room_options:
        room_options_menu['menu'].add_command(label=option, command=tk._setit(room_var, option))

    open_addroom()


def main(): 
    window = tk.Tk()

    window.geometry("1728x1117")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 1117,
        width = 1728,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        912.0,
        640.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        355.0,
        174.0,
        1506.0,
        866.0,
        fill="#2A2A2A",
        outline="")

    def deleteroom_check():
        if entry_1.get():
            open_addroom()
        else:
            print("Please Enter Room You Wish to Delete")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=deleteroom_check,
        relief="flat"
    )
    button_1.place(
        x=831.0,
        y=691.0,
        width=199.0,
        height=87.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=open_reservation,
        relief="flat"
    )
    button_2.place(
        x=90.0,
        y=1000.0,
        width=213.0,
        height=87.0
    )

    canvas.create_text(
        704.0,
        287.0,
        anchor="nw",
        text="Delete Room\n",
        fill="#FF0000",
        font=("CrimsonText Regular", 80 * -1)
    )

    room_var = tk.StringVar(window)
    room_options = get_available_rooms()

    room_options_menu = tk.OptionMenu(window, room_var, *room_options)
    room_options_menu.place(x=700.5, y=550.0, width=440.0, height=60.0)

    canvas.create_text(
        730.0,
        488.0,
        anchor="nw",
        text="Select Room to Delete",
        fill="#FFFFFF",
        font=("AbrilFatface Regular", 30 * -1)
    )


    delete_button = tk.Button(window, text="Delete Room", command=partial(delete_room, window, room_var, room_options_menu))
    

    delete_button.place(x=831.0, y=691.0, width=199.0, height=87.0) 

    window.resizable(False, False)
    window.mainloop()



    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    main()
    