import sqlite3
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, StringVar, OptionMenu, Label, messagebox
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("C:/Users/houtp/OneDrive/Desktop/Final2/AddRoom")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_reservation():
    global window
    subprocess.Popen(["python", "Reservation.py"])
    window.destroy()

def create_database():
    # Create or connect to a SQLite database file
    conn = sqlite3.connect('rooms.db')
    c = conn.cursor()


    # Create a table
    c.execute('''CREATE TABLE IF NOT EXISTS rooms
                 (Roomnumber INTEGER, Bedtype TEXT)''')

    conn.commit()
    conn.close()
create_database()

room_number_var = None
bed_type_var = None

def addroom_check():
    global room_number_var, bed_type_var  
    
    # Connect to the database
    mydb = sqlite3.connect('rooms.db')
    mycursor = mydb.cursor()

    try:
        # Get room number and bed type from UI elements
        room_number = room_number_var.get()
        bed_type = bed_type_var.get()

        # Check if room number and bed type are valid
        if not room_number or not bed_type or bed_type == "- Select -":
            messagebox.showerror('Error', 'Please select both room number and bed type.')
            return 
        
        # Convert room number to integer
        room_number_int = int(room_number)

        # Insert data into the database
        sql = "INSERT INTO rooms (Roomnumber, Bedtype) VALUES (?, ?)"
        val = (room_number_int, bed_type)  
        mycursor.execute(sql, val)
        mydb.commit()

        print('Added')
        messagebox.showinfo('Success', 'Room added successfully!')

        open_reservation()  
    
    except sqlite3.Error as err:
        error_message = err.args[0]
        messagebox.showerror('Error', f'Error inserting data: {error_message}')  

    finally:
        # Always close the database connections
        mycursor.close()
        mydb.close()

        
def main():
    global room_number_var, bed_type_var, window
    window = Tk()
    window.geometry("1728x1117")
    window.configure(bg="#FFFFFF")
    canvas = Canvas(window, bg="#FFFFFF", height=1117, width=1728, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(864.0, 558.0, image=image_image_1)

    canvas.create_rectangle(309.0, 151.0, 1418.0, 952.0, fill="#F6F6F6", outline="")

    def update_price():
        selected_bed_type = bed_type_var.get()
        price_label.config(text="")  
        if selected_bed_type == "Single":
            price_label.config(text="$100", fg="red")
        elif selected_bed_type == "Double":
            price_label.config(text="$200", fg="red")

    def update_room_numbers(*args):
        bed_type = bed_type_var.get()
        if (bed_type == "Single"):
            room_numbers = [str(i) for i in range(1, 6)]
        elif (bed_type == "Double"):
            room_numbers = [str(i) for i in range(6, 11)]
        else:
            room_numbers = ["- Select -"]

        room_number_var.set(room_numbers[0])
        room_number_menu['menu'].delete(0, 'end')

        for room in room_numbers:
            room_number_menu['menu'].add_command(label=room, command=lambda value=room: room_number_var.set(value))
        update_price()
    


    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=addroom_check, relief="flat")
    button_1.place(x=753.0, y=819.0, width=216.0, height=106.0)

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))

    # Entry replaced with a label for price display
    price_label = Label(window, text="", bg="#FDFDFD", fg="#000716", font=("Battambang Bold", 20))
    price_label.place(x=580.0, y=700.0, width=568.0, height=50.0)

    bed_type_var = StringVar()
    bed_type_var.set("- Select -")
    bed_types = ["- Select -", "Single", "Double"]
    bed_type_menu = OptionMenu(window, bed_type_var, *bed_types, command=update_room_numbers)
    bed_type_menu.config(bg="#FDFDFD", fg="#000716", font=("Battambang Bold", 20), highlightthickness=0)
    bed_type_menu.place(x=580.0, y=320.0, width=568.0, height=50.0)

    room_number_var = StringVar()
    room_number_var.set("- Select -")
    room_number_menu = OptionMenu(window, room_number_var, "- Select -")
    room_number_menu.config(bg="#FDFDFD", fg="#000716", font=("Battambang Bold", 20), highlightthickness=0)
    room_number_menu.place(x=580.0, y=500.0, width=568.0, height=50.0)

    canvas.create_text(494.0, 192.0, anchor="nw", text="Bed types", fill="#000000", font=("Battambang Bold", 40))
    canvas.create_text(555.0, 261.0, anchor="nw", text="Single / Double *", fill="#F32323", font=("Battambang Bold", 20))
    canvas.create_text(494.0, 605.0, anchor="nw", text="Price", fill="#000000", font=("Battambang Bold", 40))
    canvas.create_text(494.0, 415.0, anchor="nw", text="Room Number", fill="#000000", font=("Battambang Bold", 40))

    window.resizable(False, False)
    window.mainloop()

   

if __name__ == '__main__':
    create_database()
    main()
