import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from GUI import community_management, street_management, residence_management, occupant_management, finances_management, \
    login


def open_community():
    community_management.main()


def open_street():
    street_management.main()


def open_residence():
    residence_management.main()


def open_occupant():
    occupant_management.main()


def open_finances():
    finances_management.main()


def open_dashboard():
    login.main()


def on_enter(event):
    event.widget.config(bg='#2E86C1')


def on_leave(event):
    event.widget.config(bg='#3498db')


def main():
    root = tk.Tk()
    content_pane = ttk.PanedWindow(root, orient='vertical')
    content_pane.pack(expand=True, fill='both')

    root.title("STMARY'S COASTAL MANAGEMENT SYSTEM")

    root.state('zoomed')

    header_frame = tk.Frame(root, bg='#2E86C1', height=90)
    header_frame.pack_propagate(False)
    header_frame.pack(side='top', fill='both')

    header_label = tk.Label(header_frame, text="STMARY'S COASTAL MANAGEMENT SYSTEM", font=('Georgia', 30), bg='#2E86C1',
                            fg='#fff', pady=20)
    header_label.pack(fill='both')

    menu_frame = tk.Frame(root, bg='#5DADE2', width=root.winfo_screenwidth() // 4, height=root.winfo_screenheight())
    menu_frame.pack_propagate(False)
    menu_frame.pack(side='left', fill='y')

    image_path = "../coastal.jpg"
    img = Image.open(image_path)
    img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    img = ImageTk.PhotoImage(img)
    image_label = tk.Label(root, image=img)
    image_label.image = img
    image_label.pack(side='right', fill='y')

    button_style = {'font': ('Georgia', 16), 'bg': '#3498db', 'fg': '#ffffff', 'padx': 10, 'pady': 5}

    btn_community = tk.Button(menu_frame, text="Community Management", command=open_community, **button_style)
    btn_community.pack(fill='x')
    btn_community.bind("<Enter>", on_enter)
    btn_community.bind("<Leave>", on_leave)

    btn_street = tk.Button(menu_frame, text="Street Management", command=open_street, **button_style)
    btn_street.pack(fill='x')
    btn_street.bind("<Enter>", on_enter)
    btn_street.bind("<Leave>", on_leave)

    btn_residence = tk.Button(menu_frame, text="Residence Management", command=open_residence, **button_style)
    btn_residence.pack(fill='x')
    btn_residence.bind("<Enter>", on_enter)
    btn_residence.bind("<Leave>", on_leave)

    btn_occupant = tk.Button(menu_frame, text="Occupant Management", command=open_occupant, **button_style)
    btn_occupant.pack(fill='x')
    btn_occupant.bind("<Enter>", on_enter)
    btn_occupant.bind("<Leave>", on_leave)

    btn_finances = tk.Button(menu_frame, text="Finances Management", command=open_finances, **button_style)
    btn_finances.pack(fill='x')
    btn_finances.bind("<Enter>", on_enter)
    btn_finances.bind("<Leave>", on_leave)

    btn_dashboard = tk.Button(menu_frame, text="Dashboard Login", command=open_dashboard, **button_style)
    btn_dashboard.pack(fill='x')
    btn_dashboard.bind("<Enter>", on_enter)
    btn_dashboard.bind("<Leave>", on_leave)

    def exit_program():
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            root.destroy()

    btn_exit = tk.Button(menu_frame, text="Exit", command=exit_program, **button_style)
    btn_exit.pack(fill='x')
    btn_exit.bind("<Enter>", on_enter)
    btn_exit.bind("<Leave>", on_leave)

    root.mainloop()


if __name__ == "__main__":
    main()
