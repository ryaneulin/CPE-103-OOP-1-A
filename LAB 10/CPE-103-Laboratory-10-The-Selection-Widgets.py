import tkinter as tk
from random import choice
from tkinter import ttk
from tkinter.messagebox import showinfo


window = tk.Tk()
window.title("Birthday Selector")
window.geometry("500x500+830+50") # w, h, x-axis, y-axis

#Storage
selected_month = tk.StringVar()
selected_date = tk.StringVar()
selected_year = tk.StringVar()

#for month
ttk.Label(window, text= "Select Your Birth Month: ", font= ("Times New Roman", 12 )).grid(column=0, row=0, padx= 10, pady= 10, sticky='w')
month_cb = ttk.Combobox(window, width= 25, textvariable= selected_month)
month_cb['values'] = (
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August','September', 'October','November','December'
)
month_cb.grid(column= 1, row= 0)
month_cb.current() #nothing much will change even if I remove it, but still it will give the code the
                    # decision to present whenever it's run on the other device

# for date
ttk.Label(window, text= "Select Your Birthdate: ", font=("Times New Roman", 12)).grid(column= 0, row= 1, padx= 10, pady= 10, sticky= 'w')
date_cb = ttk.Combobox(window, width= 25, textvariable= selected_date)
date_cb.grid(column= 1, row=1)

# for year
ttk.Label(window, text= "Select Your Birth Year: ", font= ("Times New Roman", 12)).grid(column= 0, row=2, padx= 10, pady= 10, sticky= 'w')
year_cb =ttk.Combobox(window, width= 25, textvariable= selected_year)
year_cb['values'] = [str(y) for y in range (1950, 2026)]
year_cb.grid(column=1, row=2)
year_cb.current()

def update_date(event=None):
    #Default
    month = selected_month.get()
    date = [str(d)for d in range(0, 32)]

        # If Choice
    if month == 'February':
        date = [str(d) for d in range(0, 30)]
    elif choice == ['April', 'June', 'September', 'November']:
        date = [str(d) for d in range(0, 31)]

    date_cb['values'] = date
    if selected_date.get() not in date:
        selected_date.set('')
month_cb.bind("<<ComboboxSelected>>", update_date)

def show_information():
    if selected_month.get() and selected_date.get() and selected_year.get():
        showinfo(
            title= "Birth Information",
            message= f"You were born on {selected_month.get()} {selected_date.get()},{selected_year.get()}"
        )
    else:
        showinfo(title= "Incomplete Information", message= "Please select month, date and year. ")

submit_btn = ttk.Button(window, text= "Show Birth Information", command= show_information)
submit_btn.grid(column=1, row=3, pady= 20)

window.mainloop()