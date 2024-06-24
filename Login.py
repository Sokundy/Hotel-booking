from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import subprocess


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\houtp\OneDrive\Desktop\Final2\Login")


def relative_to_assets(path: str) -> Path:
    
    return ASSETS_PATH / Path(path)
    
def open_addroom():
    global window
    subprocess.Popen(["python", "AddRoom.py"])
    window.destroy()


def main():
    global window
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
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        864.0,
        558.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        669.0,
        295.0,
        1058.0,
        822.0,
        fill="#656464",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        863.5,
        584.0,
        image=entry_image_1
    )

    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        show="*"
    )
    entry_1.place(
        x=730.0,
        y=554.0,
        width=269.0,
        height=50.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        863.5,
        486.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=730.0,
        y=460.0,
        width=269.0,
        height=50.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        740.0,
        486.0,
        image=image_image_2
    )
            
    canvas.create_text(
        769.0,
        567.0,
        anchor="nw",
        text="Password",
        fill="#B7B7B7",
        font=("Avenir Roman", 30 * -1)
    )

    canvas.create_text(
        769.0,
        465.0,
        anchor="nw",
        text="Username",
        fill="#B7B7B7",
        font=("Avenir Roman", 30 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        740.0,
        587.0,
        image=image_image_3
    )

    def login_check():
        if entry_2.get() and entry_1.get():
            open_addroom()
        else:
            print("Invalid")


    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=login_check,
        relief="flat"
    )
    button_1.place(
        x=788.0,
        y=676.0,
        width=152.0,
        height=60.0
    )
    
    canvas.create_text(
        742.0,
        361.0,
        anchor="nw",
        text="ACCOUNT",
        fill="#FFFFFF",
        font=("Avenir Roman", 45 * -1)
    )
    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    main()
