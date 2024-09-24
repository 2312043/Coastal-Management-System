import tkinter as tk
from tkinter import ttk, messagebox
from classes.community import Community
from PIL import Image, ImageTk


def main():
    button_style = {'font': ('Georgia', 15), 'bg': '#3498db', 'fg': '#ffffff', 'padx': 10, 'pady': 5}
    submit_button_style = {'font': ('Georgia', 18), 'bg': '#3498db', 'fg': '#ffffff', 'padx': 5, 'pady': 2, 'width': 15}
    root = tk.Tk()
    main_frame = tk.Frame(root)

    community_name_entry = tk.Entry(main_frame, width=30)
    community_manager_entry = tk.Entry(main_frame, width=30)
    location_entry = tk.Entry(main_frame, width=30)
    street_entry = tk.Entry(main_frame, width=30)

    result_frame = tk.Frame(main_frame)
    result_label = tk.Label(result_frame, text="", fg='#5DADE2', font=('Georgia', 18), anchor='w',
                            justify='left', padx=10)

    def switch_frame(frame):
        frame.tkraise()

    def configure_entry_widgets(menu_option):
        result_label.config(text="")
        for widget in main_frame.winfo_children():
            if isinstance(widget, (tk.Label, tk.Button)):
                widget.destroy()

        community_name_entry.pack_forget()
        community_manager_entry.pack_forget()
        location_entry.pack_forget()
        street_entry.pack_forget()

        if menu_option == "Create New Community":
            tk.Label(main_frame, text="Community Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            community_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Community Manager: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            community_manager_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Location: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(
                pady=5, padx=10, anchor='w')
            location_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=create_new_community, **submit_button_style)
            submit_button.pack()

        elif menu_option == "View Community Details":
            tk.Label(main_frame, text="Community Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            community_name_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=view_community_details, **submit_button_style)
            submit_button.pack()

        elif menu_option == "Update Community":
            tk.Label(main_frame, text="Community Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            community_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="New Community Manager: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            community_manager_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="New Location: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            location_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=update_community, **submit_button_style)
            submit_button.pack()

        elif menu_option == "Delete Community":
            tk.Label(main_frame, text="Community Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            community_name_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=delete_community, **submit_button_style)
            submit_button.pack()

        elif menu_option == "Add Street to Community":
            tk.Label(main_frame, text="Community Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            community_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=add_street_to_community, **submit_button_style)
            submit_button.pack()

        elif menu_option == "Remove Street from Community":
            tk.Label(main_frame, text="Community Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            community_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=remove_street_from_community,
                                      **submit_button_style)
            submit_button.pack()

        elif menu_option == "Get Street Details":
            tk.Label(main_frame, text="Community Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            community_name_entry.pack(pady=5, padx=10, anchor='w')
            tk.Label(main_frame, text="Street Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
                     justify='left').pack(pady=5, padx=10, anchor='w')
            street_entry.pack(pady=5, padx=10, anchor='w')
            submit_button = tk.Button(main_frame, text="Submit", command=get_street_details, **submit_button_style)
            submit_button.pack()

    def configure_button_style(button):
        button.config(font=('Georgia', 16), bg='#3498db', fg='#ffffff', padx=10, pady=5)

    def create_new_community():
        result_label.config(text="")
        configure_entry_widgets("Create New Community")
        switch_frame(main_frame)
        community_name = community_name_entry.get()
        community_manager = community_manager_entry.get()
        location = location_entry.get()
        street_name = street_entry.get()

        street_exists = Community.validate_street(street_name)
        if street_exists:
            new_community = Community(community_name, community_manager, location, street_name)
            if new_community:
                new_community.write_to_csv()
                result_label.config(text="New community created and added successfully.")
            else:
                result_label.config(text="Community creation failed.")
        else:
            result_label.config(text="Street is invalid.")

    def view_community_details():
        result_label.config(text="")
        configure_entry_widgets("View Community Details")
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

    def update_community():
        result_label.config(text="")
        configure_entry_widgets("Update Community")
        switch_frame(main_frame)
        community_name = community_name_entry.get()
        community = Community.fetch_community_by_name(community_name)
        if community:
            new_manager = community_manager_entry.get()
            new_location = location_entry.get()
            community.update_community_detail(new_manager, new_location)
            result_label.config(text="Community Updated.")
        else:
            result_label.config(text="Community not found.")

    def delete_community():
        result_label.config(text="")
        configure_entry_widgets("Delete Community")
        switch_frame(main_frame)
        community_name = community_name_entry.get()
        community = Community.fetch_community_by_name(community_name)
        if community:
            Community.delete_community(community_name)
            result_label.config(text=f"Community '{community_name}' deleted.")
        else:
            result_label.config(text=f"Community '{community_name}' not found.")

    def add_street_to_community():
        result_label.config(text="")
        configure_entry_widgets("Add Street to Community")
        switch_frame(main_frame)
        community_name = community_name_entry.get()
        community = Community.fetch_community_by_name(community_name)
        if community:
            street_name = street_entry.get()
            add = community.add_street(street_name)
            if add:
                result_label.config(text=f"Street '{street_name}' added to the community.")
            else:
                result_label.config(text="Invalid street name.")
        else:
            result_label.config(text="Community not found.")

    def remove_street_from_community():
        result_label.config(text="")
        configure_entry_widgets("Remove Street from Community")
        switch_frame(main_frame)
        community_name = community_name_entry.get()
        community = Community.fetch_community_by_name(community_name)
        if community:
            street_name = street_entry.get()
            remove = community.remove_street(street_name)
            if remove:
                result_label.config(text=f"Street '{street_name}' removed from the community.")
            else:
                result_label.config(text=f"Street '{street_name}' not found in the community.")
        else:
            result_label.config(text="Community not found.")

    def get_street_details():
        result_label.config(text="")
        configure_entry_widgets("Get Street Details")
        switch_frame(main_frame)
        community_name = community_name_entry.get()
        street_name = street_entry.get()
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

    def exit_program():
        root.destroy()

    root.title("STMARY'S COASTAL MANAGEMENT SYSTEM")
    root.state('zoomed')

    content_pane = ttk.PanedWindow(root, orient='vertical')
    content_pane.pack(expand=True, fill='both')

    main_frame.pack(expand=True, fill='both')

    header_frame = tk.Frame(main_frame, bg='#2E86C1', height=90)
    header_frame.pack_propagate(False)
    header_frame.pack(side='top', fill='both')

    header_label = tk.Label(header_frame, text="COMMUNITY MANAGEMENT SYSTEM", font=('Georgia', 30), bg='#2E86C1',
                            fg='#fff', pady=20)
    header_label.pack(fill='both')

    menu_frame = tk.Frame(main_frame, bg='#5DADE2', width=root.winfo_screenwidth() // 4,
                          height=root.winfo_screenheight())
    menu_frame.pack_propagate(False)
    menu_frame.pack(side='left', fill='y')

    tk.Button(menu_frame, text="Create New Community", command=lambda: configure_entry_widgets("Create New Community"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="View Community Details",
              command=lambda: configure_entry_widgets("View Community Details"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Update Community", command=lambda: configure_entry_widgets("Update Community"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Delete Community", command=lambda: configure_entry_widgets("Delete Community"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Add Street to Community",
              command=lambda: configure_entry_widgets("Add Street to Community"), **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Remove Street from Community",
              command=lambda: configure_entry_widgets("Remove Street from Community"), **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Get Street Details", command=lambda: configure_entry_widgets("Get Street Details"),
              **button_style).pack(fill='x')
    tk.Button(menu_frame, text="Exit", command=exit_program, **button_style).pack(fill='x')

    result_frame.pack(side='bottom', expand=True, anchor='w')

    result_label.pack(fill='both', expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
