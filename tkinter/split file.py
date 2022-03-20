import tkinter as tk
from tkinter import CENTER, RIGHT, Y, Scrollbar

window = tk.Tk()
window.resizable(width=False, height=True)
window.title('Split file')

scrollbar =Scrollbar(window)
# scrollbar.pack(side=RIGHT, fill = Y)


label = tk.Label(
                window, text='Введите количество готовых ролей: '
                ).grid(row=0, column=0)

rols_num = tk.Entry(window)
rols_num.grid(column=1, row=0)

def rol_button():
    lst_of_codes = []
    for i in range(int(rols_num.get())):
        label1 = tk.Label(window, text=f'Введите значения роля {i+1}').grid(row=i+1, column=0)
        entry = tk.Entry(window)
        entry.grid(row=i+1, column=1)
        lst_of_codes.append(entry)

button_rols = tk.Button(
                       window, text="Ввод количества ролей",command=rol_button).grid(row=0, column=2)


window.mainloop()

