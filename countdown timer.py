import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        
        # Initialize time variables
        self.time_left = 0
        self.timer_running = False
        
        # Create labels and buttons
        self.time_label = tk.Label(self.root, text="Enter time in seconds:", font=("Arial", 14))
        self.time_label.pack(pady=10)
        
        self.time_entry = tk.Entry(self.root, font=("Arial", 14))
        self.time_entry.pack(pady=10)
        
        self.start_button = tk.Button(self.root, text="Start Timer", font=("Arial", 14), command=self.start_timer)
        self.start_button.pack(pady=10)
        
        self.reset_button = tk.Button(self.root, text="Reset Timer", font=("Arial", 14), command=self.reset_timer)
        self.reset_button.pack(pady=10)
        
        self.timer_display = tk.Label(self.root, text="00:00", font=("Arial", 40), fg="red")
        self.timer_display.pack(pady=20)
    
    def start_timer(self):
        if not self.timer_running:
            try:
                self.time_left = int(self.time_entry.get())
                if self.time_left <= 0:
                    raise ValueError
                self.timer_running = True
                self.countdown()
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid positive integer for the time.")
        else:
            messagebox.showinfo("Timer Running", "The timer is already running.")
    
    def countdown(self):
        if self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            time_format = f"{mins:02}:{secs:02}"
            self.timer_display.config(text=time_format)
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        else:
            self.timer_display.config(text="00:00")
            self.timer_running = False
            messagebox.showinfo("Time's up", "The countdown has finished!")
    
    def reset_timer(self):
        self.time_left = 0
        self.timer_display.config(text="00:00")
        self.time_entry.delete(0, tk.END)
        self.timer_running = False

# Set up the GUI
root = tk.Tk()
countdown_timer = CountdownTimer(root)
root.mainloop()
# Set up the GUI
root = tk. Tk()
countdown_timer = CountdownTimer(root)
root.mainloop()
