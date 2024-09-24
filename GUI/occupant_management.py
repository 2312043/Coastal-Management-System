import tkinter as tk
from tkinter import ttk, messagebox
from classes.occupant import Occupant
from classes.residence import Residence
from PIL import Image, ImageTk


def main():
    button_style = {'font': ('Georgia', 15), 'bg': '#3498db', 'fg': '#ffffff', 'padx': 10, 'pady': 5}
    submit_button_style = {'font': ('Georgia', 18), 'bg': '#3498db', 'fg': '#ffffff', 'padx': 5, 'pady': 2, 'width': 15}

    root = tk.Tk()
    main_frame = tk.Frame(root)

    occupant_ID_entry = tk.Entry(main_frame, width=30)
    first_name_entry = tk.Entry(main_frame, width=30)
    last_name_entry = tk.Entry(main_frame, width=30)
    govt_ID_entry = tk.Entry(main_frame, width=30)
    gender_entry = tk.Entry(main_frame, width=30)
    email_entry = tk.Entry(main_frame, width=30)
    phone_entry = tk.Entry(main_frame, width=30)
    family_members_entry = tk.Entry(main_frame, width=30)
    occupant_status_entry = tk.Entry(main_frame, width=30)
    payment_methods_entry = tk.Entry(main_frame, width=30)

    result_frame = tk.Frame(main_frame)
    result_label = tk.Label(result_frame, text="", fg='#5DADE2', font=('Georgia', 18), anchor='w',
                            justify='left', padx=10)

    def switch_frame(frame):
        frame.tkraise()

    def configure_occupant_widgets(menu_option):
        result_label.config(text="")
        for widget in main_frame.winfo_children():
            if isinstance(widget, (tk.Label, tk.Button)):
                widget.destroy()

        occupant_ID_entry.pack_forget()
        first_name_entry.pack_forget()
        last_name_entry.pack_forget()
        govt_ID_entry.pack_forget()
        gender_entry.pack_forget()
        email_entry.pack_forget()
        phone_entry.pack_forget()
        family_members_entry.pack_forget()
        occupant_status_entry.pack_forget()
        payment_methods_entry.pack_forget()

        if menu_option == "Create New Occupant":
            tk.Label(main_frame, text="Occupant ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            occupant_ID_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="First Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            first_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Last Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            last_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Government ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            govt_ID_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Gender: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            gender_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Email: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            email_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Phone: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            phone_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Family Members: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            family_members_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Occupant Status: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            occupant_status_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Payment Methods: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            payment_methods_entry.pack(pady=5, padx=10, anchor='w')

            submit_button = tk.Button(main_frame, text="Submit", command=create_new_occupant, **submit_button_style)
            submit_button.pack()

        elif menu_option == "View Occupant Details":
            tk.Label(main_frame, text="Occupant ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            occupant_ID_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=view_occupant_details, **submit_button_style)
            submit_button.pack()

        elif menu_option == "Update Occupant Details":
            tk.Label(main_frame, text="Occupant ID to update: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            occupant_ID_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="First Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            first_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Last Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            last_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Government ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            govt_ID_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Gender: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            gender_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Email: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            email_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Phone: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            phone_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Family Members: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            family_members_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Occupant Status: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            occupant_status_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Payment Methods: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 6),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            payment_methods_entry.pack(pady=5, padx=10, anchor='w')

            submit_button = tk.Button(main_frame, text="Submit", command=update_occupant_details, **submit_button_style)
            submit_button.pack()

        elif menu_option == "Delete Occupant":
            tk.Label(main_frame, text="Occupant ID to delete: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            occupant_ID_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=delete_occupant, **submit_button_style)
            submit_button.pack()

    def create_new_occupant():
        result_label.config(text="")
        configure_occupant_widgets("Create New Occupant")
        switch_frame(main_frame)
        occupant_ID = occupant_ID_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        govt_ID = govt_ID_entry.get()
        gender = gender_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        family_members = family_members_entry.get()
        occupant_status = occupant_status_entry.get()
        payment_methods = payment_methods_entry.get()

        new_occupant = Occupant(occupant_ID, first_name, last_name, govt_ID, gender, email, phone, family_members,
                                occupant_status, payment_methods)

        if new_occupant:
            new_occupant.write_to_csv()
            result_label.config(text="New occupant created and added successfully.")
        else:
            result_label.config(text="Occupant cannot be created.")

    def view_occupant_details():
        result_label.config(text="")
        configure_occupant_widgets("View Occupant Details")
        switch_frame(main_frame)
        occupant_id = occupant_ID_entry.get()
        occupant_details = Residence.fetch_occupant_details(occupant_id)
        if occupant_details:
            result_label.config(text="\nOccupant Details:")
            for key, value in occupant_details.items():
                result_label.config(text=result_label.cget("text") + f"\n{key}: {value}")
        else:
            result_label.config(text="Occupant not found.")

    def update_occupant_details():
        result_label.config(text="")
        configure_occupant_widgets("Update Occupant Details")
        switch_frame(main_frame)
        occupant_id = occupant_ID_entry.get()
        occupant = Occupant.fetch_occupant_by_id(occupant_id)
        if occupant:
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            govt_ID = govt_ID_entry.get()
            gender = gender_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()
            family_members = family_members_entry.get()
            occupant_status = occupant_status_entry.get()
            payment_methods = payment_methods_entry.get()
            occupant.update_occupant_details(first_name, last_name, govt_ID, gender, email, phone, family_members,
                                             occupant_status, payment_methods)
            result_label.config(text=f"Occupant {occupant_id} details updated.")
        else:
            result_label.config(text="Occupant not found.")

    def delete_occupant():
        result_label.config(text="")
        configure_occupant_widgets("Delete Occupant")
        switch_frame(main_frame)
        occupant_id = occupant_ID_entry.get()
        occupant = Occupant.fetch_occupant_by_id(occupant_id)
        if occupant:
            occupant.delete_occupant()
            result_label.config(text=f"Occupant {occupant_id} deleted.")
        else:
            result_label.config(text="Occupant not found.")

    def exit_program():
        root.destroy()

    root.title("Occupant Management System")
    root.state('zoomed')

    content_pane = ttk.PanedWindow(root, orient='vertical')
    content_pane.pack(expand=True, fill='both')

    main_frame.pack(expand=True, fill='both')

    header_frame = tk.Frame(main_frame, bg='#2E86C1', height=90)
    header_frame.pack_propagate(False)
    header_frame.pack(side='top', fill='both')

    header_label = tk.Label(header_frame, text="OCCUPANT MANAGEMENT SYSTEM", font=('Georgia', 30), bg='#2E86C1',
                            fg='#fff', pady=20)
    header_label.pack(fill='both')

    menu_frame = tk.Frame(main_frame, bg='#5DADE2', width=root.winfo_screenwidth() // 4,
                          height=root.winfo_screenheight())
    menu_frame.pack_propagate(False)
    menu_frame.pack(side='left', fill='y')



    tk.Button(menu_frame, text="Create New Occupant",
              command=lambda: configure_occupant_widgets("Create New Occupant"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="View Occupant Details",
              command=lambda: configure_occupant_widgets("View Occupant Details"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Update Occupant Details",
              command=lambda: configure_occupant_widgets("Update Occupant Details"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Delete Occupant",
              command=lambda: configure_occupant_widgets("Delete Occupant"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Exit",
              command=exit_program,
              **button_style).pack(fill='x')

    result_frame.pack(side='bottom', fill='both', expand=True)
    result_label.pack(side='top', fill='both', expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
