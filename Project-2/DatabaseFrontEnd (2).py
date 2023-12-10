import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3

class RiskAssessmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Risk Assessment Application")

        # Create a connection to the SQLite database
        self.connection = sqlite3.connect("risk_factors.db")
        self.cursor = self.connection.cursor()

        # Open the image using Pillow
        image = Image.open("bg.png")
        # Resize the image to match the window size
        self.bg = ImageTk.PhotoImage(image.resize((root.winfo_screenwidth(), root.winfo_screenheight())))

        # Create GUI components
        self.background_label = ttk.Label(root, image=self.bg)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.company1_label = ttk.Label(root, text="Enter First Company:")
        self.company1_entry = ttk.Entry(root)
        self.company2_label = ttk.Label(root, text="Enter Second Company:")
        self.company2_entry = ttk.Entry(root)
        self.compare_button = ttk.Button(root, text="Compare", command=self.compare_companies)
        self.result_label = ttk.Label(root, text="Risk Assessment Results:")
        self.result_text = tk.Text(root, wrap="word", width=55, height=30, state="disabled")

        # Place GUI components on the grid
        self.company1_label.grid(row=0, column=0, padx=10, pady=10)
        self.company1_entry.grid(row=0, column=1, padx=10, pady=10)
        self.company2_label.grid(row=0, column=2, padx=10, pady=10)
        self.company2_entry.grid(row=0, column=3, padx=10, pady=10)
        self.compare_button.grid(row=0, column=4, padx=10, pady=10)
        self.result_label.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
        self.result_text.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

    def compare_companies(self):
    # Retrieve company names from the entry widgets
        company1_name = self.company1_entry.get()
        company2_name = self.company2_entry.get()

    # Execute a SQL query to compare the two companies
        query = f"""
            SELECT risk_factor FROM risk_factors WHERE company_name = '{company1_name}'
            UNION
            SELECT risk_factor FROM risk_factors WHERE company_name = '{company2_name}'
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()

    # Display results in the text widget
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        for i, result in enumerate(results):
            self.result_text.insert(tk.END, f"Risk factor {i+1}: {result[0]}\n")
        self.result_text.config(state="disabled")




if __name__ == "__main__":
    root = tk.Tk()
    app = RiskAssessmentApp(root)
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")  
    # Set window size to full screen
    root.mainloop()


  