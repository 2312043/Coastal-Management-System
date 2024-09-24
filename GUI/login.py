import tkinter as tk
from tkinter import ttk, messagebox
from classes.community import Community
import manager_dashboard


def main():
    button_style = {'font': ('Georgia', 15), 'bg': '#3498db', 'fg': '#ffffff', 'padx': 10, 'pady': 5}
    submit_button_style = {'font': ('Georgia', 18), 'bg': '#3498db', 'fg': '#ffffff', 'padx': 5, 'pady': 2, 'width': 15}

    root = tk.Tk()
    main_frame = tk.Frame(root)

    community_name_entry = tk.Entry(main_frame, width=30)
    manager_name_entry = tk.Entry(main_frame, width=30)

    result_frame = tk.Frame(main_frame)
    result_label = tk.Label(result_frame, text="", fg='#5DADE2', font=('Georgia', 16), padx=10)

    def switch_frame(frame):
        frame.tkraise()

    root.title("Community Manager Login")
    root.state('zoomed')

    def login():
        result_label.config(text="")
        switch_frame(main_frame)
        community_name = community_name_entry.get()
        manager_name = manager_name_entry.get()
        validate = Community.validate_login(community_name, manager_name)
        if validate:
            result_label.config(text=f"Welcome {manager_name}!")
            root.after(2000, manager_dashboard.main)
        else:
            result_label.config(text="Cannot log you in.")


    content_pane = ttk.PanedWindow(root, orient='vertical')
    content_pane.pack(expand=True, fill='both')

    main_frame.pack(expand=True, fill='both')

    header_frame = tk.Frame(main_frame, bg='#2E86C1', height=90)
    header_frame.pack_propagate(False)
    header_frame.pack(side='top', fill='both')

    header_label = tk.Label(header_frame, text="LOGIN", font=('Georgia', 30), bg='#2E86C1',
                            fg='#fff', pady=20)
    header_label.pack(fill='both')

    result_frame.pack(side='bottom', fill='both', expand=True)
    result_label.pack(side='top', fill='both', expand=True)
    result_label.config(text="")

    for widget in main_frame.winfo_children():
        if isinstance(widget, (tk.Label, tk.Button)):
            widget.destroy()

    community_name_entry.pack_forget()
    manager_name_entry.pack_forget()

    tk.Label(main_frame, text="Community Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
             justify='left').pack(pady=5, padx=10)
    community_name_entry.pack(pady=5, padx=10)
    tk.Label(main_frame, text="Manager Name: ", bg='#5DADE2', fg='#ffffff', font=('Georgia', 18),
             justify='left').pack(pady=5, padx=10)
    manager_name_entry.pack(pady=5, padx=10)

    submit_button = tk.Button(main_frame, text="Submit", command=login, **submit_button_style)
    submit_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
