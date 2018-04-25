from tkinter import messagebox
from tkinter import filedialog

from pipeline import process

from tkinter import *


# opens pop up with information about application

def launch_about_window():
    msg = "Plagiarism Indication Tool (PIT)" \
          "\nVersion 1.0" \
          "\nCreated by Owen Daynes" \
          "\n\nThe Plagiarism Indication Tool has been created to compare a collection of documents and report the similarities back to the user."

    messagebox.showinfo("About", msg)


# opens pop up with error messages

def error_popup(error_list):

    msg = ""

    for error in error_list:
        msg += error + "\n\n"

    messagebox.showerror("Error encountered", msg.strip())


# kills application

def exit_prog():
    sys.exit(0)


# launches file explorer, enters selected directory into appropriate field

def get_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, END)
    directory_entry.insert(0, directory)

# launches file explorer, enters selected directory into appropriate field

def get_save_location():
    location = filedialog.askdirectory()
    save_loc_entry.delete(0, END)
    save_loc_entry.insert(0, location)


# checks inputs to see if all inputs are valid, returns errors in list

def check_inputs(directory, save, threshold):
    error_list = list()

    if len(directory) < 1:
        error_list.append("Please enter a directory of documents to parse.")

    if len(save) < 1:
        error_list.append("Please enter a directory to save the similarity report.")

    if len(threshold) < 1:
        error_list.append("Please enter a minimum similarity value. (0 - 100)")

    if len(threshold) > 0:
        try:
            threshold = float(threshold)
        except ValueError:
            error_list.append("Please enter a threshold value between 0 and 100")

    return error_list


# gathers required data and calls main method to calculate similarity

def calculate():

    directory = directory_entry.get()
    threshold = threshold_entry.get()
    save = save_loc_entry.get()
    include = included_check.get()
    search = subdirs_check.get()

    error_list = check_inputs(directory, save, threshold)

    if len(error_list) > 0:
        error_popup(error_list)
    else:
        result = process(directory, save, threshold, include, search)
        if result == "Success":
            messagebox.showinfo("Success", "Report generated!")
        else:
            messagebox.showerror("Error", result)


root = Tk()
root.configure(background="#a1dbcd")
root.geometry("550x200")
root.title("Plagiarism Indicition Tool (PIT)")

title_label = Label(root, text="Plagiarism Indication Tool", background="#a1dbcd", font=("Helvetica", 18))
title_label.grid(row=0, column=3, columnspan=1)

directory_label = Label(root, text="Directory", background="#a1dbcd")
directory_label.grid(row=1, column=1, columnspan=1)

directory_entry = Entry(root)
directory_entry.grid(row=1, column=2, columnspan=2)

directory_button = Button(root, text="Select read directory", command=get_directory)
directory_button.grid(row=1, column=4, columnspan=1)


save_loc_label = Label(root, text="Save location", background="#a1dbcd")
save_loc_label.grid(row=2, column=1, columnspan=1)

save_loc_entry = Entry(root)
save_loc_entry.grid(row=2, column=2, columnspan=2)

save_loc_button = Button(root, text="Select save directory", command=get_save_location)
save_loc_button.grid(row=2, column=4, columnspan=1)

threshold_label = Label(root, text="Threshold", background="#a1dbcd")
threshold_label.grid(row=3, column=1, columnspan=1)

threshold_entry = Entry(root)
threshold_entry.grid(row=3, column=2, columnspan=2)

include_not_plagiarism_label = Label(root, text="Include inoffensive pairs", background="#a1dbcd")
include_not_plagiarism_label.grid(row=4, column=1, columnspan=1)

included_check = IntVar()
include_not_plagiarism_entry = Checkbutton(root, variable=included_check, background="#a1dbcd")
include_not_plagiarism_entry.grid(row=4, column=3, columnspan=1)

search_subdirs_label = Label(root, text="Search sub-directories", background="#a1dbcd")
search_subdirs_label.grid(row=5, column=1, columnspan=1)

subdirs_check = IntVar()
subdirs_check_entry = Checkbutton(root, variable=subdirs_check, background="#a1dbcd")
subdirs_check_entry.grid(row=5, column=3, columnspan=1)

process_button = Button(root, text="Calculate similarity", command=calculate)
process_button.grid(row=6, column=3, columnspan=1)

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Calculate similarity", command=calculate)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_prog)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=launch_about_window)

if __name__ == "__main__":
    # read path provided
    if len(sys.argv) > 1:
        # write path provided
        if len(sys.argv) > 2:
            # threshold provided
            if len(sys.argv) > 3:
                # include inoffensive provided
                if len(sys.argv) > 4:
                    # include sub directories provided
                    if len(sys.argv) > 5:
                        process(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
                    else:
                        process(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
                else:
                    process(sys.argv[1], sys.argv[2], sys.argv[3])
            else:
                process(sys.argv[1], sys.argv[2])
        else:
            process(sys.argv[1])
    # path not provided
    else:
        mainloop()
