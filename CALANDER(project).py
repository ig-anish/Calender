from tkinter import ttk
import ttkbootstrap

#setup the window
root = ttkbootstrap.Window(themename="cyborg")
root.title("Calender")

#function to get the date
def see_date():
    date = cal.entry.get()
    date_label.config(text=date)

#date entry widget
cal = ttkbootstrap.DateEntry(root, dateformat="%d/%m/%Y", bootstyle="info")
cal.pack(padx=40,pady=40)

#button to get the selected date
btn = ttk.Button(root, text="Show Date", bootstyle="light-outline", command=see_date)
btn.pack(pady=40, padx=45)

date_label = ttk.Label(root, text="No date selected")
date_label.pack(padx=40,pady=50)

root.mainloop()


