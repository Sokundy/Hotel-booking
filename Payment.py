from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, Label
import sqlite3
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\houtp\OneDrive\Desktop\Final2\Payment")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def open_view():
    global window
    subprocess.Popen(["python", "View.py"])
    window.destroy()


def show_success_alert():
    if all(entry.get() for entry in [entry_1, entry_2, entry_4, entry_5, entry_6, entry_7]):
        messagebox.showinfo("Success", "Success!")
    else:
        messagebox.showwarning("Input required", "Please fill all the fields")

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
# Function to check if a string is a valid float
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def create_database():
    conn = sqlite3.connect('payment1.db')  # Connect to payment1.db
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            name TEXT,
            user_id TEXT,  
            room_number TEXT,
            phone_number TEXT,
            night_stays INTEGER,
            total_price REAL
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

create_database()

def button_click():
    print("Button clicked")  

    # Assuming your Entry widgets are defined outside the button_click function
    if all(entry.get() for entry in [entry_1, entry_2, entry_4, entry_5, entry_6, entry_7]):
        name = entry_1.get()
        user_id = entry_5.get()
        room_number = entry_7.get()
        phone_number = entry_6.get()

        # Type conversion and error handling for numerical values
        try:
            night_stays = int(entry_2.get())
            total_price = float(entry_4.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Night Stays and Total Price must be numbers.")
            return  

        print("Inserting into database:")
        print("Name:", name)
        print("ID:", user_id)
        # ... (rest of print statements)

        conn = sqlite3.connect('payment1.db')  # Connect to payment1.db
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO payments (name, user_id, room_number, phone_number, night_stays, total_price) 
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, user_id, room_number, phone_number, night_stays, total_price))  # Use user_id here
            conn.commit()
            messagebox.showinfo("Success", "Data inserted successfully!")
        except sqlite3.Error as e:
            print("Error inserting data:", e)
            messagebox.showerror("Error", f"Error inserting into database: {e}")
        finally:
            cursor.close()
            conn.close()

        # Clear the Entry widgets regardless of deletion success/failure
        for entry in [entry_1, entry_2, entry_4, entry_5, entry_6, entry_7]:
            entry.delete(0, 'end')
    else:
        print("Not all fields filled")
        messagebox.showwarning("Missing Information", "Please fill in all fields.")   

def main():
    global window
    window = Tk()

    window.geometry("1728x1117")
    window.configure(bg = "#FFFFFF")
    global entry_1, entry_2, entry_4, entry_5, entry_6, entry_7

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
        94.0,
        304.0,
        anchor="nw",
        text="Customer Details",
        fill="#000000",
        font=("AbrilFatface Regular", 43 * -1)
    )

    canvas.create_text(
        648.0,
        309.0,
        anchor="nw",
        text="Price Summary",
        fill="#000000",
        font=("AbrilFatface Regular", 43 * -1)
    )

    canvas.create_text(
        94.0,
        437.0,
        anchor="nw",
        text="Name",
        fill="#000000",
        font=("Abel Regular", 23 * -1)
    )

    canvas.create_text(
        649.0,
        480.0,
        anchor="nw",
        text="Night Stays",
        fill="#000000",
        font=("Abel Regular", 23 * -1)
    )

    canvas.create_text(
        649.0,
        615.0,
        anchor="nw",
        text="Total Prices",
        fill="#000000",
        font=("Abel Regular", 23 * -1)
    )

    canvas.create_text(
        94.0,
        570.0,
        anchor="nw",
        text="ID",
        fill="#000000",
        font=("Abel Regular", 23 * -1)
    )

    canvas.create_text(
        94.0,
        703.0,
        anchor="nw",
        text="Room Number",
        fill="#000000",
        font=("Abel Regular", 23 * -1)
    )

    canvas.create_text(
        94.0,
        836.0,
        anchor="nw",
        text="Phone Number",
        fill="#000000",
        font=("Abel Regular", 23 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        299.5,
        495.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=121.0,
        y=468.0,
        width=357.0,
        height=52.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        899.0,
        495.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=831.0,
        y=468.0,
        width=136.0,
        height=52.0
    )

 
    entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(899.0, 630.0, image=entry_image_4)
    entry_4 = Entry(window, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_4.place(x=831.0, y=603.0, width=136.0, height=52.0)
    
    #ID
    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        299.5,
        628.0,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=121.0,
        y=601.0,
        width=357.0,
        height=52.0
    )
    

    #phone
    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        299.5,
        894.0,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=121.0,
        y=867.0,
        width=357.0,
        height=52.0
    )
    #room number
    entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(299.5, 761.0, image=entry_image_7)
    entry_7 = Entry(window, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_7.place(x=121.0, y=734.0, width=357.0, height=52.0)
 

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_view,
        relief="flat"
    )
    button_1.place(
        x=461.0,
        y=1013.0,
        width=337.0,
        height=81.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=button_click,  # Call the button_click function when the button is clicked
        relief="flat"
    )
    button_2.place(
        x=728.0,
        y=860.0,
        width=406.0,
        height=81.0
    )


    
    canvas.create_rectangle(
        629.0,
        823.0,
        1047.0,
        824.0000003677764,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        153.0,
        78.0,
        155.0,
        216.0,
        fill="#000000",
        outline="")

    canvas.create_text(
        188.0,
        80.0,
        anchor="nw",
        text="PAYMENT",
        fill="#000000",
        font=("AbrilFatface Regular", 100 * -1)
        )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        1989.0,
        584.0,
        image=image_image_1
    )

    
    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    main()