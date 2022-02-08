#   ====================
#   ===    IMPORT    ===
#   ====================
from tkinter import *
from tkinter.font import BOLD

#   ====================
#   === xxx ===
#   ====================


# create a root
root = Tk()

# add title to window
root.title(" Dividers of ...")

# root dimensions
root.geometry("1080x720")
root.minsize(720,480)

# customization
root.config(bg='#00bbff')

# add a iconbitmap about maths
root.iconbitmap('pi-icon.ico')

# --- FRAME ---
# Create a app-box with title, button, entry
app_box = Frame(root, bg="#00204a", padx=25, pady=25)

user_entry = Entry(app_box, justify='center', fg="black", bg="#e7eaf6", font=('Courier', 25, BOLD))

divider_output = Label(root, bg="#00bbff", font=("Courier", 20, BOLD))

def divider_list():

    # check if entry is not empty
    # if(user_entry['text'] == ""):
    #     divider_output['fg'] = '#f23557'
    #     divider_output['text'] = "The entry is required!"

    try:
        int(user_entry.get())
    except:
        # print('Empty entry or invalid value!')
        user_entry['text'] = ""
        divider_output['fg'] = '#f23557'
        divider_output['text'] = "Enter a valid value!"

    finally:
        number = int(user_entry.get())
        # core function :
        match number:
        # if user_entry == 0 -> return "INFINITE NUMBER"
            case 0:
                divider_output['fg'] = 'white'
                divider_output['text'] = "INFINITE NUMBER OF DIVIDERS"
            # elif user_entry == 1 -> return "1"
            case 1:
                divider_output['fg'] = 'white'
                divider_output['text'] = number
            # else user_entry > 1
            case _:
                divider_output['fg'] = 'white'
                dividers = [str(i) for i in range(1,number+1) if number % i == 0]
                dividers = " - ".join(dividers)
                divider_output['text'] = dividers

#   ====================
#   === xxx ===
#   ====================

# Add a Main title to the frame
main_title = Label(app_box, text="DIVIDER(S)", fg="white", bg="#00204a", font=('Courier', 50, BOLD))
main_title.pack()

# instruction for the user
instruction = Label(app_box, text="Please, enter an integer", fg="#fdb44b", bg="#00204a", font=('Courier', 18, BOLD))
instruction.pack()

# add a entry field in the frame
user_entry.pack(pady=10)

# add a button to launch the function divider_list
launcher = Button(app_box, text="Launch!", fg="#00204a", bg="#fdb44b", font=('Courier', 25, BOLD), command=divider_list)
launcher.pack(pady=15)

# add app_box frame
app_box.pack(expand=TRUE)

# label to display the divider(s)
divider_output.pack(expand=TRUE, fill=BOTH)

# display the root
root.mainloop()
