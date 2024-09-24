import tkinter as tk
from tkinter import ttk, messagebox
from classes.community import Community
from classes.residence import Residence
from datetime import datetime
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

    result_frame = tk.Frame(main_frame)
    result_label = tk.Label(result_frame, text="", fg='#5DADE2', font=('Georgia', 16), anchor='w',
                            justify='left', padx=10)

    def switch_frame(frame):
        frame.tkraise()

    def configure_finances_widgets(menu_option):
        result_label.config(text="")
        for widget in main_frame.winfo_children():
            if isinstance(widget, (tk.Label, tk.Button)):
                widget.destroy()

        residence_ID_entry.pack_forget()
        occupant_ID_entry.pack_forget()
        amount_entry.pack_forget()
        community_name_entry.pack_forget()

        if menu_option == "Pay Service Charges":
            tk.Label(main_frame, text="Community Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            community_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Residence ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_ID_entry.pack(pady=5, padx=10, anchor='w')

            submit_button = tk.Button(main_frame, text="Submit", command=calculate_service_charges,
                                      **submit_button_style)
            submit_button.pack()

        elif menu_option == "Make Payment":
            tk.Label(main_frame, text="Residence ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            residence_ID_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Occupant ID: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            occupant_ID_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Amount: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            amount_entry.pack(pady=5, padx=10, anchor='w')

            submit_button = tk.Button(main_frame, text="Submit", command=make_payment_gui, **submit_button_style)
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

    def calculate_service_charges():
        residence_id = residence_ID_entry.get()
        residence = Residence.fetch_residence_by_id(residence_id)

        if residence:
            community_name = community_name_entry.get()
            base_charge = 100
            location_multiplier = 1.0

            community = Community.fetch_community_by_name(community_name)

            if community:
                if community.location == "NW":
                    location_multiplier = 1.3
                elif community.location == "N":
                    location_multiplier = 1.1
                elif community.location == "NE":
                    location_multiplier = 1.2
                elif community.location == "W":
                    location_multiplier = 1.55
                elif community.location == "C":
                    location_multiplier = 1.50
                elif community.location == "E":
                    location_multiplier = 1.85
                elif community.location == "SW":
                    location_multiplier = 2.3
                elif community.location == "S":
                    location_multiplier = 2.25
                elif community.location == "SE":
                    location_multiplier = 2

                maintenance_charge = 50
                waste_management_charge = 30
                security_charge = 40
                communal_facilities_charge = 20

                total_charges = (
                        base_charge * location_multiplier +
                        maintenance_charge +
                        waste_management_charge +
                        security_charge +
                        communal_facilities_charge
                )

                receipt = f"""
                   Service Charges Receipt
                   ------------------------
                   Community: {community_name}
                   Base Charges: ${base_charge * location_multiplier:.2f}
                   Maintenance Charge: ${maintenance_charge:.2f}
                   Waste Management Charge: ${waste_management_charge:.2f}
                   Security Charge: ${security_charge:.2f}
                   Communal Facilities Charge: ${communal_facilities_charge:.2f}
                   ------------------------
                   Total Service Charges: ${total_charges:.2f}
                   Date: {datetime.now()}
                   ------------------------
                   """

                result_label.config(text=receipt)
            else:
                result_label.config(text="Enter Valid Community Name.")
        else:
            result_label.config(text="Enter Valid Residence ID.")

    def make_payment_gui():
        residence_id = residence_ID_entry.get()
        occupant_id = occupant_ID_entry.get()
        residence = Residence.fetch_residence_by_id(residence_id)
        if residence:
            amount = float(amount_entry.get())
            message = residence.make_payment(amount, occupant_id)
            result_label.config(text=message)
            receipt = residence.generate_payment_receipt(amount, occupant_id)
            result_label.config(text=receipt)

        else:
            result_label.config(text="Residence not found.")

    def view_payment_history_gui():
        residence_id = residence_ID_entry.get()
        occupant_id = occupant_ID_entry.get()
        residence = Residence.fetch_residence_by_id(residence_id)
        if residence:
            history = residence.view_payment_history(occupant_id)
            result_label.config(text=f"Payment History:\n{history}")
        else:
            result_label.config(text="Residence not found.")

    def exit_program():
        root.destroy()

    root.title("Finances Management System")
    root.state('zoomed')

    content_pane = ttk.PanedWindow(root, orient='vertical')
    content_pane.pack(expand=True, fill='both')

    main_frame.pack(expand=True, fill='both')

    header_frame = tk.Frame(main_frame, bg='#2E86C1', height=90)
    header_frame.pack_propagate(False)
    header_frame.pack(side='top', fill='both')

    header_label = tk.Label(header_frame, text="FINANCES MANAGEMENT SYSTEM", font=('Georgia', 30), bg='#2E86C1',
                            fg='#fff', pady=20)
    header_label.pack(fill='both')

    menu_frame = tk.Frame(main_frame, bg='#5DADE2', width=root.winfo_screenwidth() // 4,
                          height=root.winfo_screenheight())
    menu_frame.pack_propagate(False)
    menu_frame.pack(side='left', fill='y')


    tk.Button(menu_frame, text="Pay Service Charges",
              command=lambda: configure_finances_widgets("Pay Service Charges"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Make Payment",
              command=lambda: configure_finances_widgets("Make Payment"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="View Payment History",
              command=lambda: configure_finances_widgets("View Payment History"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Exit",
              command=exit_program,
              **button_style).pack(fill='x')

    result_frame.pack(side='bottom', fill='both', expand=True)
    result_label.pack(side='top', fill='both', expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
