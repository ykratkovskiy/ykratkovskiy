import tkinter as tk
from tkinter import StringVar, filedialog
import os
from os import path
from tkinter import messagebox
import shutil


window = tk.Tk()
window.title('Report manager')
window.geometry('400x350')
window.resizable(width=False, height=False)


def source_button():
    global source_path
    filename = filedialog.askdirectory()
    source_path.set(filename)
    
source_path = StringVar()
lbl1 = tk.Label(textvariable=source_path)
lbl1.place(relx=0.3, rely=0.21)
button1 = tk.Button(text="Select source folder", command=source_button,width=15,height=1)
button1.place(relx=0, rely=0.21)


def target_button():
    target_path
    filename = filedialog.askdirectory()
    target_path.set(filename)
    
target_path = StringVar()
lbl2 = tk.Label(textvariable=target_path)
lbl2.place(relx=0.3, rely=0.35)
button2 = tk.Button(text="Select target folder", command=target_button,width=15,height=1)
button2.place(relx=0, rely=0.35)


lbl3 = tk.Label(
                text='<<<NOREAD\'S delete from Lake Image\'s report>>>', 
                bg='gray90', font=24,
                fg='indianred',
                )
lbl3.pack()




def report_manager():
    path = source_path.get()
    list_of_files = sorted(os.listdir(path))
    

    global num_of_codes
    global num_of_noreads
    num_of_codes = []
    num_of_noreads = []
    lst_of_rols = []
    
    global src
    global trg
    src = source_path.get()
    trg = target_path.get()
    
    for file in list_of_files:
        if 'vse' in file:
            name = (file.split('.')[0])
            ext = (file.split('.')[1])
            global name_for_rep
            name_for_rep = name.split('rol')[0]
            rol_number = name.split('_')[-2]
            noread_count=0
            count_of_codes = 0
            original_file = open(f'{src}/{file}','r')
            new_file = open(f'{trg}/{name}MOD.{ext}', 'w')
            for line in original_file:
                if not line.startswith('NOREAD'):
                    count_of_codes+=1
                    new_file.write(line)
                else:
                    noread_count+=1
            new_file.close()
            num_of_codes.append(count_of_codes)
            num_of_noreads.append(noread_count)
            lst_of_rols.append(rol_number)
    stat_file = open (f'{trg}/{name_for_rep}_stat.txt', 'w')
    for rol_id,codes in zip (lst_of_rols,num_of_codes):
        stat_file.writelines(f'Rol {rol_id} - {codes} codes\n')
    stat_file.write(f'Total codes used: {sum(num_of_codes)}\n')
    stat_file.write(f'Total number of NOREAD\'s deleted: {sum(num_of_noreads)}')
    stat_file.close()
    original_file.close()
    messagebox.showinfo(title='Done', message=f'Total codes used: {sum(num_of_codes)}')
    

button = tk.Button(
                text = 'Start',
                font=20,
                width = 13,
                height = 1,
                bg = 'gray85',
                fg = 'gray10', 
                command=report_manager)
button.place(relx=0.35, rely=0.6)


def archive_button():
    shutil.make_archive(f'{trg}/{name_for_rep}','zip', root_dir=None, base_dir=trg)

button3 = tk.Button(text="Archive files", 
                    command=archive_button,
                    width=13,
                    height=1,
                    )
button3.place(relx=0.37, rely=0.75)


window.mainloop()