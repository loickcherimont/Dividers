# --- IMPORT ---
from tkinter import *
from tkinter.font import BOLD

# --- FUNCTIONS ---
def find_dividers(n):
    """Return a joined of dividers of n"""

    # Convert int into str to use join list method later
    pos_div = [str(i) for i in range(1, abs(n)+1) if n % i == 0]
    neg_div = [str(i) for i in range(-abs(n), 0) if n % i == 0]

    # Create a list of all dividers
    dividers = neg_div + pos_div
    return ", ".join(dividers)  # string of dividers

def divider_list():
    """Set output an error message or informations about dividers of entry value

    No key argument
    """

    try:
        num = int(wrapper_entry.get())
    except:
        wrapper_entry["text"] = ""                      # Reset entry
        output["fg"] = "#f23557"
        output["text"] = "Please enter a valid value!"  # Error message
        return # Stop function

    # No exception
    output["fg"] = "white"
    if num == 0:
        output["text"] = "INFINITE NUMBER OF DIVIDERS"
    else:
        output["text"] = f"Dividers are:\n{find_dividers(num)}"


# ************** CORE OF THE APPLICATION **************

# --- MAIN WINDOW ---
# Create window and set title
window = Tk()
window.title("Dividers")

# Set default and minimal dimensions of the window
window.geometry("1080x720")
window.minsize(720,480)

# Customization of window
window.config(bg="#2082d8")
window.iconbitmap("img/pi-icon.ico")


# --- FRAME AND COMPONENTS ---
wrapper = Frame(window, bg="#184e76", padx=25, pady=25)

# Give wrapper a title
wrapper_title = Label(wrapper, text="DIVIDERS", fg="white", bg="#184e76", font=("Courier", 50, BOLD))
wrapper_title.pack()

# Add a instruction label
# to say user what to do
wrapper_instruction = Label(wrapper, text="Please, enter an integer", fg="#fdb44b", bg="#184e76", font=("Courier", 18, BOLD))
wrapper_instruction.pack()

# Create a entry for user
wrapper_entry = Entry(wrapper, justify="center", fg="black", bg="#e7eaf6", font=("Courier", 25, BOLD))
wrapper_entry.pack(pady=10)

# Add a launcher of "divider_list" function
wrapper_btn = Button(wrapper, text="Launch!", fg="#184e76", bg="#fdb44b", font=("Courier", 25, BOLD), command=divider_list)
wrapper_btn.pack(pady=15)

# Add wrapper
# and all its components into main window
wrapper.pack(expand=TRUE)

# Output for dividers
output = Label(window, bg="#2082d8", font=("Courier", 20, BOLD))
output.pack(expand=TRUE, fill=BOTH)

# Display main window
window.mainloop()
