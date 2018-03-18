from tkinter import messagebox

from Main import main

from tkinter import *
import threading


def exit_prog():
    sys.exit(0)


def check_inputs(directory, threshold):
    error_list = list()

    if len(directory) < 1:
        error_list.append("Please enter a directory of documents to parse.")

    if len(threshold) < 1:
        error_list.append("Please enter a minimum similarity value. (0 - 100)")

    if len(threshold) > 0:
        try:
            threshold = float(threshold)
        except ValueError:
            error_list.append("Please enter a threshold value between 0 and 100")

    return error_list

def calculate():
    errors_encountered = False

    directory = directory_entry.get()
    threshold = threshold_entry.get()

    error_list = check_inputs(directory, threshold)

    if len(error_list) > 0:
        error_popup(error_list)
    else:
        threading.Thread(target=main(directory_entry.get(), threshold_entry.get())).start()

def error_popup(error_list):

    msg = ""

    for error in error_list:
        msg += error + "\n\n"

    messagebox.showinfo("Error encountered", msg.strip())

root = Tk()
root.geometry("600x400")
root.title("Plagiarism Indicition Tool (PIT)")


directory_label = Label(root, text="Directory")
directory_label.grid(row=0, column=0, columnspan=1)

directory_entry = Entry(root)
directory_entry.grid(row=0, column=1, columnspan=1)

threshold_label = Label(root, text="Threshold")
threshold_label.grid(row=1, column=0, columnspan=1)

threshold_entry = Entry(root)
threshold_entry.grid(row=1, column=1, columnspan=1)

# create a menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Calculate similarity", command=calculate)
# filemenu.add_command(label="Open...", command=calculate)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_prog)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=calculate)

process_button = Button(root, text="Calculate similarity", command=calculate)
process_button.grid(row=2, column=0, columnspan=1)


if __name__ == "__main__":
    # path provided
    if len(sys.argv) > 1:
        # threshold provided
        if len(sys.argv) > 2:
            main(sys.argv[1], sys.argv[2])
        # threshold not provided
        else:
            main(sys.argv[1])
    # path not provided
    else:
        mainloop()
