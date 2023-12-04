import tkinter as tk
from tkinter import messagebox

class DanceEventApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Dance Event Booking System")
        self.root.configure(bg="black")  # Set background color to black


        self.dance_styles = ["Natyanjali Dance", "Western Dance", "Folk Dance", "Semi Classic", "Kathakali"]
        self.dancers = ["Mayuri", "Shobana", "Waltz", "Chandralekha", "Malliga Saraperi"]
        self.concert_places = ["Chennai", "Mumbai", "Delhi", "Bangalore", "Hyderabad"]

        self.style_var = tk.StringVar()
        self.dancer_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.place_var = tk.StringVar()
        self.seat_var = tk.IntVar()

        self.style_label = tk.Label(root, text="Select Dance Style:", bg="black", fg="white")  # Set label text and color
        self.style_label.pack()
        self.style_dropdown = tk.OptionMenu(root, self.style_var, *self.dance_styles)
        self.style_dropdown.pack()

        self.dancer_label = tk.Label(root, text="Select Dancer:", bg="black", fg="white")  # Set label text and color
        self.dancer_label.pack()
        self.dancer_dropdown = tk.OptionMenu(root, self.dancer_var, *self.dancers)
        self.dancer_dropdown.pack()

        self.date_label = tk.Label(root, text="Concert Date:", bg="black", fg="white")  # Set label text and color
        self.date_label.pack()
        self.date_entry = tk.Entry(root, textvariable=self.date_var)
        self.date_entry.pack()

        self.place_label = tk.Label(root, text="Concert Place:", bg="black", fg="white")  # Set label text and color
        self.place_label.pack()
        self.place_dropdown = tk.OptionMenu(root, self.place_var, *self.concert_places)
        self.place_dropdown.pack()

        self.seat_label = tk.Label(root, text="Seat Number:", bg="black", fg="white")  # Set label text and color
        self.seat_label.pack()
        self.seat_entry = tk.Entry(root, textvariable=self.seat_var)
        self.seat_entry.pack()

        self.book_button = tk.Button(root, text="Book Concert", command=self.show_confirmation, bg="blue", fg="white")  # Set button color
        self.book_button.pack()

        self.ticket_listbox = tk.Listbox(root)  # Add Listbox to display booked tickets
        self.ticket_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    def show_confirmation(self):
        style = self.style_var.get()
        dancer = self.dancer_var.get()
        date = self.date_var.get()
        place = self.place_var.get()
        seat = self.seat_var.get()

        confirmation_message = f"Congratulations!\nYou have successfully booked a seat for the {style} concert by {dancer} on {date} at {place}. Your seat number is {seat}."

        confirmation_window = tk.Toplevel(self.root)
        confirmation_window.title("Booking Confirmation")
        confirmation_window.configure(bg="black")  # Set background color to black

        confirmation_label = tk.Label(confirmation_window, text=confirmation_message, bg="black", fg="white")
        confirmation_label.pack()

        ok_button = tk.Button(confirmation_window, text="OK", command=confirmation_window.destroy, bg="blue", fg="white")
        ok_button.pack()

root = tk.Tk()
app = DanceEventApp(root)
root.mainloop()