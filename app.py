# --- IMPORT ---
from tkinter import *
from tkinter.font import BOLD

# --- DIVIDER LIST function ---
def divider_list():
    """Set output an error message or informations about dividers of entry value

    No key argument
    """
    # Try get 'wrapper_entry' into integer
    try:
        number = int(wrapper_entry.get())

    # Raised exception :
    # reset 'wrapper_entry', show error message
    # stop the function
    except:
        wrapper_entry['text'] = ''
        output['fg'] = '#f23557'
        output['text'] = "Please enter a valid value!"
        return

    # No exception
    output['fg'] = 'white' # In visible color

    # In function number value
    # execute corresponding statement
    match number:
        case 0:
            output['text'] = 'INFINITE NUMBER OF DIVIDERS'
        case 1:
            output['text'] = f'Unique divider:\n {number}'
        case _:
            # Convert integer into string
            # to use join method on 'dividers'
            dividers = [str(i) for i in range(1,number+1) if number % i == 0]
            dividers = " - ".join(dividers)
            output['text'] = f'List of dividers:\n {dividers}'


# ************** CORE OF THE APPLICATION **************

# --- MAIN WINDOW ---
# Create window and set title
window = Tk()
window.title(" Dividers of ...")

# Set default and minimal dimensions of the window
window.geometry("1080x720")
window.minsize(720,480)

# Customization of window
window.config(bg='#00bbff')
window.iconbitmap('img/pi-icon.ico')


# --- FRAME AND COMPONENTS ---
wrapper = Frame(window, bg="#00204a", padx=25, pady=25)

# Give wrapper a title
wrapper_title = Label(wrapper, text="DIVIDER(S)", fg="white", bg="#00204a", font=('Courier', 50, BOLD))
wrapper_title.pack()

# Say user what to do
wrapper_instruction = Label(wrapper, text="Please, enter an integer", fg="#fdb44b", bg="#00204a", font=('Courier', 18, BOLD))
wrapper_instruction.pack()

# Create a entry for user
wrapper_entry = Entry(wrapper, justify='center', fg="black", bg="#e7eaf6", font=('Courier', 25, BOLD))
wrapper_entry.pack(pady=10)

# Add a launcher of 'divider_list' function
wrapper_btn = Button(wrapper, text="Launch!", fg="#00204a", bg="#fdb44b", font=('Courier', 25, BOLD), command=divider_list)
wrapper_btn.pack(pady=15)

# Add wrapper and all its components into main window
wrapper.pack(expand=TRUE)

# Display divider(s)
output = Label(window, bg="#00bbff", font=("Courier", 20, BOLD))
output.pack(expand=TRUE, fill=BOTH)

# Display main window
window.mainloop()
