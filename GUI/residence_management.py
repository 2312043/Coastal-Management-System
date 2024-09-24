import tkinter as tk
from tkinter import ttk, messagebox
from classes.residence import Residence
from PIL import Image, ImageTk


def main():
    button_style = {'font': ('Georgia', 15), 'bg': '#3498db', 'fg': '#ffffff', 'padx': 10, 'pady': 5}
    submit_button_style = {'font': ('Georgia', 18), 'bg': '#3498db', 'fg': '#ffffff', 'padx': 5, 'pady': 2, 'width': 15}

    root = tk.Tk()
    main_frame = tk.Frame(root)

    residence_ID_entry = tk.Entry(main_frame, width=30)
    residence_type_entry = tk.Entry(main_frame, width=30)
    occupant_ID_entry = tk.Entry(main_frame, width=30)
    occupant_type_entry = tk.Entry(main_frame, width=30)

    result_frame = tk.Frame(main_frame)
    result_label = tk.Label(result_frame, text="", fg='#5DADE2', font=('Georgia', 18), anchor='w',
                            justify='left', padx=10)

    def switch_frame(frame):
        frame.tkraise()

    def configure_residence_widgets(menu_option):
        result_label.config(text="")
        for widget in main_frame.winfo_children():
            if isinstance(widget, (tk.Label, tk.Button)):
                widget.destroy()

        residence_ID_entry.pack_forget()
        residence_type_entry.pack_forget()
        occupant_ID_entry.pack_forget()
        occupant_type_entry.pack_forget()

        if menu_option == "Create New Residence":
            tk.Label(main_frame, text="Residence ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_ID_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Residence Type: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_type_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Occupant ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            occupant_ID_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Occupant Type: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            occupant_type_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=create_new_residence, **submit_button_style)
            submit_button.pack()

        elif menu_option == "View Residence Details":
            tk.Label(main_frame, text="Residence ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_ID_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=view_residence_details, **submit_button_style)
            submit_button.pack()

        elif menu_option == "Add Occupant for Residence":
            tk.Label(main_frame, text="Residence ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_ID_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Occupant ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            occupant_ID_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=add_occupant_for_residence,
                                      **submit_button_style)
            submit_button.pack()

        elif menu_option == "Delete Occupant for Residence":
            tk.Label(main_frame, text="Residence ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_ID_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Occupant ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            occupant_ID_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=delete_occupant_for_residence,
                                      **submit_button_style)
            submit_button.pack()

        elif menu_option == "Get Occupant Details":
            tk.Label(main_frame, text="Residence ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_ID_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Occupant ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            occupant_ID_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=get_occupant_details, **submit_button_style)
            submit_button.pack()

        elif menu_option == "View Occupancy Status":
            tk.Label(main_frame, text="Residence ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_ID_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=view_occupancy_status, **submit_button_style)
            submit_button.pack()

    def create_new_residence():
        result_label.config(text="")
        configure_residence_widgets("Create New Residence")
        switch_frame(main_frame)
        residence_ID = residence_ID_entry.get()
        residence_type = residence_type_entry.get()
        occupant_ID = occupant_ID_entry.get()
        occupant_type = occupant_type_entry.get()

        occupant_exists = Residence.validate_occupant_id(str(occupant_ID))
        if occupant_exists:
            new_residence = Residence(residence_ID, residence_type, occupant_ID, occupant_type)
            if new_residence:
                new_residence.write_to_csv()
                result_label.config(text="New residence created and added successfully.")
            else:
                result_label.config(text="Residence creation failed.")
        else:
            result_label.config(text="Occupant ID is invalid.")

    def view_residence_details():
        result_label.config(text="")
        configure_residence_widgets("View Residence Details")
        switch_frame(main_frame)
        residence_ID = residence_ID_entry.get()
        residence = Residence.fetch_residence_by_id(residence_ID)
        if residence:
            details = residence.get_residence_details()
            result_label.config(text="\nResidence Details:")
            for key, value in details.items():
                result_label.config(text=result_label.cget("text") + f"\n{key}: {value}")
        else:
            result_label.config(text="Residence not found.")

    def add_occupant_for_residence():
        result_label.config(text="")
        configure_residence_widgets("Add Occupant for Residence")
        switch_frame(main_frame)
        residence_ID = residence_ID_entry.get()
        residence = Residence.fetch_residence_by_id(residence_ID)
        if residence:
            occupant_ID = occupant_ID_entry.get()
            add = residence.add_occupant(occupant_ID)
            if add:
                result_label.config(text=f"Occupant {occupant_ID} added to the residence.")
            else:
                result_label.config(text="Occupant does not exist or is invalid.")
        else:
            result_label.config(text="Residence not found.")

    def delete_occupant_for_residence():
        result_label.config(text="")
        configure_residence_widgets("Delete Occupant for Residence")
        switch_frame(main_frame)
        residence_ID = residence_ID_entry.get()
        residence = Residence.fetch_residence_by_id(residence_ID)
        if residence:
            occupant_ID = occupant_ID_entry.get()
            delete = residence.delete_occupant(occupant_ID)
            if delete:
                result_label.config(text="Occupant removed from the residence.")
            else:
                result_label.config(text="Occupant not found in the residence.")
        else:
            result_label.config(text="Residence not found.")

    def get_occupant_details():
        result_label.config(text="")
        configure_residence_widgets("Get Occupant Details")
        switch_frame(main_frame)
        occupant_ID = occupant_ID_entry.get()
        occupant_details = Residence.fetch_occupant_details(occupant_ID)
        if occupant_details:
            result_label.config(text="\nOccupant Details:")
            for key, value in occupant_details.items():
                result_label.config(text=result_label.cget("text") + f"\n{key}: {value}")
        else:
            result_label.config(text="Occupant not found.")

    def view_occupancy_status():
        result_label.config(text="")
        configure_residence_widgets("View Occupancy Status")
        switch_frame(main_frame)
        residence_ID = residence_ID_entry.get()
        residence = Residence.fetch_residence_by_id(residence_ID)
        if residence:
            status = residence.get_occupancy_status()
            result_label.config(text=f"Occupancy Status: {status}")
        else:
            result_label.config(text="Residence not found.")

    def exit_program():
        root.destroy()

    root.title("Residence Management System")
    root.state('zoomed')

    content_pane = ttk.PanedWindow(root, orient='vertical')
    content_pane.pack(expand=True, fill='both')

    main_frame.pack(expand=True, fill='both')

    header_frame = tk.Frame(main_frame, bg='#2E86C1', height=90)
    header_frame.pack_propagate(False)
    header_frame.pack(side='top', fill='both')

    header_label = tk.Label(header_frame, text="RESIDENCE MANAGEMENT SYSTEM", font=('Georgia', 30), bg='#2E86C1',
                            fg='#fff', pady=20)
    header_label.pack(fill='both')

    menu_frame = tk.Frame(main_frame, bg='#5DADE2', width=root.winfo_screenwidth() // 4,
                          height=root.winfo_screenheight())
    menu_frame.pack_propagate(False)
    menu_frame.pack(side='left', fill='y')


    tk.Button(menu_frame, text="Create New Residence",
              command=lambda: configure_residence_widgets("Create New Residence"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="View Residence Details",
              command=lambda: configure_residence_widgets("View Residence Details"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Add Occupant for Residence",
              command=lambda: configure_residence_widgets("Add Occupant for Residence"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Delete Occupant for Residence",
              command=lambda: configure_residence_widgets("Delete Occupant for Residence"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Get Occupant Details",
              command=lambda: configure_residence_widgets("Get Occupant Details"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="View Occupancy Status",
              command=lambda: configure_residence_widgets("View Occupancy Status"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Exit", command=exit_program, **button_style).pack(fill='x')

    result_frame.pack(side='bottom', expand=True, fill='both')
    result_label.pack(expand=True, fill='both')

    root.mainloop()


if __name__ == "__main__":
    main()
