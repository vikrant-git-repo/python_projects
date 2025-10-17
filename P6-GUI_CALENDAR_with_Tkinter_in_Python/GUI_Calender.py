from tkinter import *
import calendar

def Calendar_See():
    window = Tk()
    window.config(background="light pink")
    window.title("Complete year calendar")
    window.geometry("570x640")
    get_year = int(year_entry.get())
    window_content = calendar.calendar(get_year)
    year_cal = Label(window, text=window_content, font=("Arial", 12, "bold"))
    year_cal.grid(row=5, column=1)
    window.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.config(background="yellow")
    root.title("GUI Calendar")
    root.geometry("280x170")

    name = Label(root, text="Calendar", bg="light pink", font=("Arial", 28, "bold"))
    name.grid(row=1, column=1)

    year = Label(root, text="Enter the year", bg="light blue", font=("Arial", 15, "bold"))
    year.grid(row=2, column=1)

    year_entry = Entry(root, font=("Arial", 15, "bold"))
    year_entry.grid(row=3, column=1)

    show_button = Button(root, text="Show Calendar!", fg="red", bg="black", font=("Arial", 15, "bold"), command=Calendar_See)
    show_button.grid(row=4, column=1)

    root.mainloop()
