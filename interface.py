import tkinter as tk

def submit():
    text1 = entry1.get()
    text2 = entry2.get()
    result_label.config(text=f"Text in Box 1: {text1}\nText in Box 2: {text2}")

# Create the main window
root = tk.Tk()
root.title("Two Boxes")

# Create the first Entry widget
entry1 = tk.Entry(root, width=30)
entry1.pack()

# Create the second Entry widget
entry2 = tk.Entry(root, width=30)
entry2.pack()

# Create a button to submit the input
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
