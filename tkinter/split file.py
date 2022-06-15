import tkinter as tk
from tkinter import messagebox
import os
from tkinter import  StringVar, filedialog
        
       
window = tk.Tk()
window.resizable(width=True, height=True)
window.geometry('+650+300')
window.title('Разбивка файла')



label = tk.Label(
window, text='Введите количество ролей в окне ниже и нажмите кнопку "OK"',).grid(row=0, column=0)

rols_num = tk.Entry(window)
rols_num.grid(row=1, column=0)


my_entries = []
helplist =[]


def ok_button():
    try:
        for i in range(int(rols_num.get())):
            label_rols = tk.Label(window, text=f'Введите количество кодов в роле № {i+1} здесь ->').grid(row=i+3, column=0)
            entry_mult = tk.Entry(window)
            entry_mult.grid(row=i+3, column=1)
            helplist.append(entry_mult)
            if int(rols_num.get())>=100 or int(rols_num.get())<=0:
                raise messagebox.showerror(title='Error!', message=f"Количество ролей должно быть в диапазоне от 1 до 99!",
                onclick=window.quit())
    except ValueError:
        messagebox.showerror(title='Error!', message=f"Значением количества ролей должно быть целое положительное число!",
        onclick=window.quit())
   
                
        
button_ok = tk.Button(
window, text='OK',command=ok_button,width=8,height=1).grid(row=2, column=0)



def write_values():
    for entries in helplist:
        try:
            my_entries.append(int(entries.get()))
        except ValueError:
                messagebox.showerror(title='Error!', message=f"Значением кодов в роле должно быть целое положительное число!",
                onclick=window.quit())
        for value in my_entries:
            if value<0:
                raise messagebox.showerror(title='Error!', message=f"Значением кодов в роле должно быть целое положительное число!",
                onclick=window.quit())
                

button_apply_values = tk.Button(
window, text='Записать значения всех кодов', command=write_values).grid(row=3, column=2)  


def source_button():
    filename = filedialog.askopenfilename()
    source_path.set(filename)
    
source_path = StringVar()
source_label = tk.Label(textvariable=source_path)
source_label.grid(row=2, column=3)

source_buttn = tk.Button(text="Исходный файл", command=source_button,width=16,height=1)
source_buttn.grid(row=0, column=3)










window.mainloop()
print (my_entries)

