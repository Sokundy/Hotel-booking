import sqlite3
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import subprocess
    
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("C:/Users/houtp/OneDrive/Desktop/Final2/Reservation")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_deleteroom():

    global window
    subprocess.Popen(["python", "DeleteRoom.py"])
    window.destroy()

def open_payment():
    global window
    subprocess.Popen(["python", "Payment.py"])
    window.destroy()

# Function to create the SQLite database
def create_database():
    conn = sqlite3.connect('reservation.db')
    c = conn.cursor()
    # Create table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS reservations
                 (name TEXT, email TEXT, id TEXT, phone_number TEXT,
                  room_number TEXT, check_in_date TEXT, check_out_date TEXT)''')
    conn.commit()
    conn.close()

create_database()

def insert_reservation(name, email, id, phone_number, room_number, check_in_date, check_out_date):
  try:
    conn = sqlite3.connect('reservation.db')
    c = conn.cursor()
    c.execute("INSERT INTO reservations (name, email, id, phone_number, room_number, check_in_date, check_out_date) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (name, email, id, phone_number, room_number, check_in_date, check_out_date))
    conn.commit()

    # Success message using tkinter.messagebox
    messagebox.showinfo(title="Success", message="Reservation successfully inserted!")

  except sqlite3.Error as err:
    # Error handling with informative message
    messagebox.showerror(title="Error", message=f"An error occurred: {err}")
  finally:
    conn.close()



def main():
    global name_var, email_var, ID_var, phone_number_var, room_number_var, check_in_date_var, check_out_date, window
    window = Tk()
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
    canvas.create_text(
        910.0,
        65.0,
        anchor="nw",
        text="RESERVATION",
        fill="#000000",
        font=("Avenir Roman", 100 * -1)
    )

    canvas.create_text(
        913.0,
        267.0,
        anchor="nw",
        text="Name",
        fill="#000000",
        font=("Avenir Roman", 30 * -1)
    )

    canvas.create_text(
        1290.0,
        411.0,
        anchor="nw",
        text="Phone Number",
        fill="#000000",
        font=("Avenir Roman", 30 * -1)
    )

    canvas.create_text(
        913.0,
        411.0,
        anchor="nw",
        text="ID",
        fill="#000000",
        font=("Avenir Roman", 30 * -1)
    )

    canvas.create_text(
        1138.0,
        577.0,
        anchor="nw",
        text="Room Number",
        fill="#000000",
        font=("Avenir Roman", 30 * -1)
    )

    canvas.create_text(
        913.0,
        729.0,
        anchor="nw",
        text="Check-in Date",
        fill="#000000",
        font=("Avenir Roman", 30 * -1)
    )

    canvas.create_text(
        1290.0,
        729.0,
        anchor="nw",
        text="Check-out Date",
        fill="#000000",
        font=("Avenir Roman", 30 * -1)
    )

    canvas.create_text(
        1290.0,
        267.0,
        anchor="nw",
        text="Email",
        fill="#000000",
        font=("Avenir Roman", 30 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        1053.5,
        344.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FAFAFA",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=943.5,
        y=314.0,
        width=220.0,
        height=59.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        1430.5,
        488.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=1320.5,
        y=458.0,
        width=220.0,
        height=59.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        1053.5,
        488.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=943.5,
        y=458.0,
        width=220.0,
        height=59.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        1242.0,
        654.5,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=1208.5,
        y=624.0,
        width=67.0,
        height=59.0
    )
    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        1430.5,
        806.5,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=1320.5,
        y=776.0,
        width=220.0,
        height=59.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        1053.5,
        806.5,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=943.5,
        y=776.0,
        width=220.0,
        height=59.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        1423.5,
        344.5,
        image=entry_image_7
    )
    entry_7 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_7.place(
        x=1313.5,
        y=314.0,
        width=220.0,
        height=59.0
    )

    button_image_1 = PhotoImage(                 #DELETE ROOM
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        text="DELETE ROOM",
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_deleteroom,
        relief="flat"
    )
    button_1.place(
        x=953.0,
        y=912.0,
        width=260.0,
        height=105.0
    )

    def reservation_check():
        if entry_1.get() and entry_2.get() and entry_3.get() and entry_4.get() and entry_5.get() and entry_6.get() and entry_7.get():
            # Extract reservation details from entry variables
            name = entry_1.get()
            email = entry_7.get()
            id = entry_3.get()
            phone_number = entry_2.get()
            room_number = entry_4.get()
            check_in_date = entry_6.get()
            check_out_date = entry_5.get()

            # Insert reservation into the database
            insert_reservation(name, email, id, phone_number, room_number, check_in_date, check_out_date)
            
            # Open the payment page
            open_payment()
        else:
            messagebox.showwarning("Missing Information", "Please fill in all reservation details.")

    button_image_2 = PhotoImage(                  #Reserve
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        text="Reserve",
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=reservation_check,
        relief="flat"
    )
    button_2.place(
        x=1336.0,
        y=912.0,
        width=260.0,
        height=105.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        439.0,
        564.0,
        image=image_image_1
    )

    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    create_database()
    main()