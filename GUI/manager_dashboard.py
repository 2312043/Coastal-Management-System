import tkinter as tk
from tkinter import ttk, messagebox
from classes.community import Community
from classes.residence import Residence
from classes.street import Street
from PIL import Image, ImageTk


def main():
    button_style = {'font': ('Georgia', 15), 'bg': '#3498db', 'fg': '#ffffff', 'padx': 10, 'pady': 5}
    submit_button_style = {'font': ('Georgia', 18), 'bg': '#3498db', 'fg': '#ffffff', 'padx': 5, 'pady': 2, 'width': 15}

    root = tk.Tk()
    main_frame = tk.Frame(root)

    residence_ID_entry = tk.Entry(main_frame, width=30)
    occupant_ID_entry = tk.Entry(main_frame, width=30)
    amount_entry = tk.Entry(main_frame, width=30)
    community_name_entry = tk.Entry(main_frame, width=30)
    street_name_entry = tk.Entry(main_frame, width=30)

    result_frame = tk.Frame(main_frame)
    result_label = tk.Label(result_frame, text="", fg='#5DADE2', font=('Georgia', 16), anchor='w',
                            justify='left', padx=10)

    def switch_frame(frame):
        frame.tkraise()

    def configure_dashboard_widgets(menu_option):
        result_label.config(text="")
        for widget in main_frame.winfo_children():
            if isinstance(widget, (tk.Label, tk.Button)):
                widget.destroy()

        residence_ID_entry.pack_forget()
        occupant_ID_entry.pack_forget()
        amount_entry.pack_forget()
        community_name_entry.pack_forget()
        street_name_entry.pack_forget()

        if menu_option == "View Community Details":
            tk.Label(main_frame, text="Community Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            community_name_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=view_community_details, **submit_button_style)
            submit_button.pack()

        elif menu_option == "Get Street Details":
            tk.Label(main_frame, text="Community Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            community_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_name_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=get_street_details, **submit_button_style)
            submit_button.pack()

        elif menu_option == "Get Residence Details in Street":
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Residence ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_ID_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=get_residence_details_in_street,
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

        elif menu_option == "View Payment History":
            tk.Label(main_frame, text="Residence ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_ID_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Occupant ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            occupant_ID_entry.pack(pady=5, padx=10, anchor='w')

            submit_button = tk.Button(main_frame, text="Submit", command=view_payment_history_gui,
                                      **submit_button_style)
            submit_button.pack()

        elif menu_option == "View Notifications in Street":
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_name_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=view_notifications_in_street,
                                      **submit_button_style)
            submit_button.pack()

    def view_community_details():
        result_label.config(text="")
        configure_dashboard_widgets("View Community Details")
        switch_frame(main_frame)
        community_name = community_name_entry.get()
        community = Community.fetch_community_by_name(community_name)
        if community:
            details = community.get_community_details()
            result_label.config(text="\nCommunity Details:")
            for key, value in details.items():
                result_label.config(text=result_label.cget("text") + f"\n{key}: {value}")
        else:
            result_label.config(text="Community not found.")

    def get_street_details():
        result_label.config(text="")
        configure_dashboard_widgets("Get Street Details")
        switch_frame(main_frame)
        community_name = community_name_entry.get()
        street_name = street_name_entry.get()
        community = Community.fetch_community_by_name(community_name)
        if community:
            street_details = community.get_street(street_name)
            if street_details:
                result_label.config(text="\nStreet Details in Community:")
                for key, value in street_details.items():
                    result_label.config(text=result_label.cget("text") + f"\n{key}: {value}")
            else:
                result_label.config(text="Street details not found.")
        else:
            result_label.config(text="Community not found.")

    def get_residence_details_in_street():
        result_label.config(text="")
        configure_dashboard_widgets("Get Residence Details in Street")
        switch_frame(main_frame)
        street_name = street_name_entry.get()
        residence_id = residence_ID_entry.get()
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

    def get_occupant_details():
        result_label.config(text="")
        configure_dashboard_widgets("Get Occupant Details")
        switch_frame(main_frame)
        occupant_ID = occupant_ID_entry.get()
        occupant_details = Residence.fetch_occupant_details(occupant_ID)
        if occupant_details:
            result_label.config(text="\nOccupant Details:")
            for key, value in occupant_details.items():
                result_label.config(text=result_label.cget("text") + f"\n{key}: {value}")
        else:
            result_label.config(text="Occupant not found.")

    def view_payment_history_gui():
        result_label.config(text="")
        configure_dashboard_widgets("Get Occupant Details")
        switch_frame(main_frame)
        residence_id = residence_ID_entry.get()
        occupant_id = occupant_ID_entry.get()
        residence = Residence.fetch_residence_by_id(residence_id)
        if residence:
            history = residence.view_payment_history(occupant_id)
            result_label.config(text=f"Payment History:\n{history}")
        else:
            result_label.config(text="Residence not found.")

    def view_notifications_in_street():
        result_label.config(text="")
        configure_dashboard_widgets("View Notifications in Street")
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

    root.title("Community Manager Dashboard")
    root.state('zoomed')

    content_pane = ttk.PanedWindow(root, orient='vertical')
    content_pane.pack(expand=True, fill='both')

    main_frame.pack(expand=True, fill='both')

    header_frame = tk.Frame(main_frame, bg='#2E86C1', height=90)
    header_frame.pack_propagate(False)
    header_frame.pack(side='top', fill='both')

    header_label = tk.Label(header_frame, text="COMMUNITY MANAGER DASHBOARD", font=('Georgia', 30), bg='#2E86C1',
                            fg='#fff', pady=20)
    header_label.pack(fill='both')

    menu_frame = tk.Frame(main_frame, bg='#5DADE2', width=root.winfo_screenwidth() // 4,
                          height=root.winfo_screenheight())
    menu_frame.pack_propagate(False)
    menu_frame.pack(side='left', fill='y')



    tk.Button(menu_frame, text="View Community Details",
              command=lambda: configure_dashboard_widgets("View Community Details"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="View Street Details in Community",
              command=lambda: configure_dashboard_widgets("Get Street Details"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="View Residence Details in Street",
              command=lambda: configure_dashboard_widgets("Get Residence Details in Street"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="View Occupant Details in Residence",
              command=lambda: configure_dashboard_widgets("Get Occupant Details"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="View Payment History",
              command=lambda: configure_dashboard_widgets("View Payment History"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="View Notifications",
              command=lambda: configure_dashboard_widgets("View Notifications in Street"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Exit",
              command=exit_program,
              **button_style).pack(fill='x')

    result_frame.pack(side='bottom', fill='both', expand=True)
    result_label.pack(side='top', fill='both', expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
