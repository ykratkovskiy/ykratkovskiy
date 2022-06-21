import tkinter as tk
from tkinter import messagebox
import os
from tkinter import  StringVar, filedialog
from turtle import bgcolor
from os import path
import time
from webbrowser import open_new

from click import open_file

        
       
window = tk.Tk()
window.resizable(width=True, height=True)
window.geometry('+350+100')
window.title('Split file')



source_label_msg = tk.Label(window, text='Выберите исходный файл для разбивки',foreground='maroon',font=18)
source_label_msg.grid(row=0, columnspan=3)

def source_button():
    filename = filedialog.askopenfilename()
    source_path.set(filename)
source_buttn = tk.Button(text="Выбрать", command=source_button,width=16,height=1,foreground='maroon')
source_buttn.grid(row=1, columnspan=3)

source_path = StringVar()
source_label = tk.Label(textvariable=source_path,foreground='maroon')
source_label.grid(row=2, columnspan=3)



target_label_msg = tk.Label(window, text='Выберите директорию для готовых файлов',foreground='royalblue1',font=18)
target_label_msg.grid(row=3, columnspan=3)

def target_button():
    pathdirectory = filedialog.askdirectory()
    target_path.set(pathdirectory)
target_buttn = tk.Button(text="Выбрать", command=target_button,width=16,height=1,foreground='royalblue1')
target_buttn.grid(row=4, columnspan=3)

target_path = StringVar()
target_label = tk.Label(textvariable=target_path,foreground='royalblue1')
target_label.grid(row=5, columnspan=3)


label = tk.Label(window, text='Введите количество ролей и нажмите кнопку "OK"',foreground='darkgreen',font=18)
label.grid(row=6, columnspan=3,)

rols_num = tk.Entry(window)
rols_num.grid(row=7, columnspan=3)


my_entries = []
helplist =[]



def write_and_run():
    try:
        start_time = time.time()
        global full_name
        global name
        c=0
        for entries in helplist:
            try:
                my_entries.append(int(entries.get()))
            except ValueError:
                messagebox.showerror(title='Error!', message=f"Значением кодов в роле должно быть целое положительное число!",
                onclick=window.quit())
            for value in my_entries:
                if value < 0:
                    raise messagebox.showerror(title='Error!', message=f"Значением кодов в роле должно быть целое положительное число!",
                    onclick=window.quit())
    
        src = source_path.get()
        trg = target_path.get()
    
        full_name = path.basename(f'{src}')
        name = path.splitext(full_name)[0]
    
        dir_path = path.dirname(src)
    
    
        original_file = open(f'{dir_path}/{full_name}','r')
        for i in range(len(my_entries)):
            new_file = open(f'{trg}/{name} rol {i+1}.txt', 'w')
            c = my_entries[i]
            for j in range (1,c+1):
                new_file.write(original_file.readline())
        original_file.close()
        new_file.close()
        messagebox.showinfo(title='Файл разбит', message=f'Успешно выполнено за {round (time.time()-start_time,2)} сек',onclick=window.quit())
    
    except Exception:
        messagebox.showerror(title='Ошибка!', message=f"Что-то пошло не так...")





def ok_button():
    try:
        for i in range(int(rols_num.get())):
            label_rols = tk.Label(window, text=f'Введите количество кодов в роле № {i+1}').grid(row=i+10, column=0)
            entry_mult = tk.Entry(window)
            entry_mult.grid(row=i+10, column=1)
            helplist.append(entry_mult)
            button_apply_values = tk.Button(
            window, text='Запустить программу', command=write_and_run).grid(row=(int(rols_num.get())+10), columnspan=3)  
            
            if int(rols_num.get())>=100 or int(rols_num.get())<=0:
                raise messagebox.showerror(title='Error!', message=f"Количество ролей должно быть в диапазоне от 1 до 99!",
                onclick=window.quit())
    
    except ValueError:
        messagebox.showerror(title='Error!', message=f"Значением количества ролей должно быть целое положительное число!",
        onclick=window.quit())
   
button_ok = tk.Button(
window, text='OK',command=ok_button,width=8,height=1,foreground='darkgreen').grid(row=9, columnspan=3)



window.mainloop()
