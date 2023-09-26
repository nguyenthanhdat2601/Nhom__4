import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

def calculate_grade_percentages():
    # Load data from the CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            df = pd.read_csv(file_path, index_col=0, header=0)
            diem = df.iloc[:, 3].values  # Assuming Diem A is in column 3
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {str(e)}")
            return

        # Define grade categories
        grade_categories = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
        grade_counts = {category: np.sum(diem == category) for category in grade_categories}

        # Calculate percentages
        total_students = len(diem)
        percentages = {category: (count / total_students) * 100 for category, count in grade_counts.items()}

        # Display the percentages
        message = "Grade Percentages:\n"
        for category in grade_categories:
            message += f"{category}: {percentages[category]:.2f}%\n"

        messagebox.showinfo("Grade Percentages", message)

# Create the GUI
root = tk.Tk()
root.title("Grade Percentage Calculator")

calculate_button = tk.Button(root, text="Calculate Percentages", command=calculate_grade_percentages)
calculate_button.pack()

root.mainloop()
