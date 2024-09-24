import tkinter as tk
from tkinter import ttk, messagebox
from classes.street import Street
from PIL import Image, ImageTk


def main():
    button_style = {'font': ('Georgia', 15), 'bg': '#3498db', 'fg': '#ffffff', 'padx': 10, 'pady': 5}
    submit_button_style = {'font': ('Georgia', 18), 'bg': '#3498db', 'fg': '#ffffff', 'padx': 5, 'pady': 2, 'width': 15}

    root = tk.Tk()
    main_frame = tk.Frame(root)

    street_name_entry = tk.Entry(main_frame, width=30)
    representative_entry = tk.Entry(main_frame, width=30)
    residence_id_entry = tk.Entry(main_frame, width=30)

    result_frame = tk.Frame(main_frame)
    result_label = tk.Label(result_frame, text="", fg='#5DADE2', font=('Georgia', 18), anchor='w',
                            justify='left', padx=10)

    def switch_frame(frame):
        frame.tkraise()

    def configure_street_widgets(menu_option):
        result_label.config(text="")
        for widget in main_frame.winfo_children():
            if isinstance(widget, (tk.Label, tk.Button)):
                widget.destroy()

        street_name_entry.pack_forget()
        representative_entry.pack_forget()
        residence_id_entry.pack_forget()

        if menu_option == "Create New Street":
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Representative: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            representative_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Residence ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_id_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=create_new_street, **submit_button_style)
            submit_button.pack()

        elif menu_option == "View Street Details":
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_name_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=view_street_details, **submit_button_style)
            submit_button.pack()

        elif menu_option == "Update Representative for Street":
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="New Representative: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            representative_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=update_representative_for_street,
                                      **submit_button_style)
            submit_button.pack()

        elif menu_option == "Add Residence to Street":
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Residence ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_id_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=add_residence_to_street, **submit_button_style)
            submit_button.pack()

        elif menu_option == "Remove Residence from Street":
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Residence ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_id_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=remove_residence_from_street,
                                      **submit_button_style)
            submit_button.pack()

        elif menu_option == "Get Residence Details in Street":
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Residence ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_id_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=get_residence_details_in_street,
                                      **submit_button_style)
            submit_button.pack()

        elif menu_option == "Notify Residents in Street":
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Message: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            representative_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=notify_residents_in_street,
                                      **submit_button_style)
            submit_button.pack()

        elif menu_option == "View Notifications in Street":
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_name_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=view_notifications_in_street,
                                      **submit_button_style)
            submit_button.pack()

    def create_new_street():
        result_label.config(text="")
        configure_street_widgets("Create New Street")
        switch_frame(main_frame)
        street_name = street_name_entry.get()
        representative = representative_entry.get()
        residence_id = residence_id_entry.get()

        residence_exists = Street.validate_residence_id(residence_id)
        if residence_exists:
            new_street = Street(street_name, representative, residence_id)
            if new_street:
                new_street.write_to_csv()
                result_label.config(text="New street created and added successfully.")
            else:
                result_label.config(text="Street creation failed.")
        else:
            result_label.config(text="Residence ID is invalid.")

    def view_street_details():
        result_label.config(text="")
        configure_street_widgets("View Street Details")
        switch_frame(main_frame)
        street_name = street_name_entry.get()
        street = Street.fetch_street_by_name(street_name)
        if street:
            details = street.get_street_details()
            result_label.config(text="\nStreet Details:")
            for key, value in details.items():
                result_label.config(text=result_label.cget("text") + f"\n{key}: {value}")
        else:
            result_label.config(text="Street not found.")

    def update_representative_for_street():
        result_label.config(text="")
        configure_street_widgets("Update Representative for Street")
        switch_frame(main_frame)
        street_name = street_name_entry.get()
        street = Street.fetch_street_by_name(street_name)
        if street:
            new_representative = representative_entry.get()
            street.update_representative(new_representative)
            result_label.config(text="Representative updated for the street.")
        else:
            result_label.config(text="Street not found.")

    def add_residence_to_street():
        result_label.config(text="")
        configure_street_widgets("Add Residence to Street")
        switch_frame(main_frame)
        street_name = street_name_entry.get()
        street = Street.fetch_street_by_name(street_name)
        if street:
            residence_id = residence_id_entry.get()
            add = street.add_residence(residence_id)
            if add:
                result_label.config(text=f"Residence {residence_id} added to the street.")
            else:
                result_label.config(text="Residence does not exist or is invalid.")
        else:
            result_label.config(text="Street not found.")

    def remove_residence_from_street():
        result_label.config(text="")
        configure_street_widgets("Remove Residence from Street")
        switch_frame(main_frame)
        street_name = street_name_entry.get()
        street = Street.fetch_street_by_name(street_name)
        if street:
            residence_id = residence_id_entry.get()
            remove = street.remove_residence(residence_id)
            if remove:
                result_label.config(text=f"Residence {residence_id} removed from the street.")
            else:
                result_label.config(text=f"Residence {residence_id} not found in the street.")
        else:
            result_label.config(text="Street not found.")

    def get_residence_details_in_street():
        result_label.config(text="")
        configure_street_widgets("Get Residence Details in Street")
        switch_frame(main_frame)
        street_name = street_name_entry.get()
        residence_id = residence_id_entry.get()
        street = Street.fetch_street_by_name(street_name)
        if street:
            residence_details = street.get_residence(residence_id)
            if residence_details:
                result_label.config(text="\nResidence Details in Street:")
                for key, value in residence_details.items():
                    result_label.config(text=result_label.cget("text") + f"\n{key}: {value}")
            else:
                result_label.config(text="Residence details not found.")
        else:
            result_label.config(text="Street not found.")

    def notify_residents_in_street():
        result_label.config(text="")
        configure_street_widgets("Notify Residents in Street")
        switch_frame(main_frame)
        street_name = street_name_entry.get()
        street = Street.fetch_street_by_name(street_name)
        if street:
            message = representative_entry.get()
            street.notify_residents(message)
            result_label.config(text="Notification sent to residents in the street.")
        else:
            result_label.config(text="Street not found.")

    def view_notifications_in_street():
        result_label.config(text="")
        configure_street_widgets("View Notifications in Street")
        switch_frame(main_frame)
        street_name = street_name_entry.get()
        street = Street.fetch_street_by_name(street_name)
        if street:
            notifications = street.get_notifications()
            if notifications:
                result_label.config(text=f"Notifications for {street_name}:")
                for notification in notifications:
                    result_label.config(text=result_label.cget("text") + f"\nDate: {notification['Date']}\n"
                                                                         f"Representative: {notification['Representative']}\n"
                                                                         f"Message: {notification['Notification']}\n"
                                                                         f"-----------------------------")
            else:
                result_label.config(text="No notifications found for this street.")
        else:
            result_label.config(text="Street not found.")

    def exit_program():
        root.destroy()

    root.title("Street Management System")
    root.state('zoomed')

    content_pane = ttk.PanedWindow(root, orient='vertical')
    content_pane.pack(expand=True, fill='both')

    main_frame.pack(expand=True, fill='both')

    header_frame = tk.Frame(main_frame, bg='#2E86C1', height=90)
    header_frame.pack_propagate(False)
    header_frame.pack(side='top', fill='both')

    header_label = tk.Label(header_frame, text="STREET MANAGEMENT SYSTEM", font=('Georgia', 30), bg='#2E86C1',
                            fg='#fff', pady=20)
    header_label.pack(fill='both')

    menu_frame = tk.Frame(main_frame, bg='#5DADE2', width=root.winfo_screenwidth() // 4,
                          height=root.winfo_screenheight())
    menu_frame.pack_propagate(False)
    menu_frame.pack(side='left', fill='y')


    tk.Button(menu_frame, text="Create New Street", command=lambda: configure_street_widgets("Create New Street"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="View Street Details",
              command=lambda: configure_street_widgets("View Street Details"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Update Representative for Street",
              command=lambda: configure_street_widgets("Update Representative for Street"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Add Residence to Street",
              command=lambda: configure_street_widgets("Add Residence to Street"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Remove Residence from Street",
              command=lambda: configure_street_widgets("Remove Residence from Street"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Get Residence Details in Street",
              command=lambda: configure_street_widgets("Get Residence Details in Street"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Notify Residents in Street",
              command=lambda: configure_street_widgets("Notify Residents in Street"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="View Notifications in Street",
              command=lambda: configure_street_widgets("View Notifications in Street"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Exit", command=exit_program, **button_style).pack(fill='x')

    result_frame.pack(side='bottom', expand=True, fill='both')
    result_label.pack(expand=True, fill='both')

    root.mainloop()


if __name__ == "__main__":
    main()
