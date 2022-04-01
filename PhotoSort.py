from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os
from datetime import datetime

root = Tk()

root.title('PhotoSort')
root.geometry('500x150+500+300')

s = ttk.Style()
s.configure('my.TButton', font=("Helvetica", 15))


def start():
    cur_path = entry_path.get() #обращаемся к функции , что бы взять путь
    if cur_path:
        for folder , subfolders , files in os.walk(cur_path): #Для каких файлов эта функция
            for file in files:
                path = os.path.join(folder,file) # Получаем путь к каждой фотке
                mtime = os.path.getmtime(path) # Узнаем сколько времени прошло с создания в секундах
                date = datetime.fromtimestamp(mtime) # Получаем дату в формате год . месяц  . день + секунды
                date = date.strftime('%Y-%m') #Дата в формате год ю месяц ю день
                date_folder = os.path.join(cur_path , date) # получаем путь к файлу + дата создания

                if not os.path.exists(date_folder): # Ф-ия : если нет папки с датой фотографии - то мы её создаем
                    os.mkdir(date_folder)# Создаем
                os.rename(path , os.path.join(date_folder,file)) # Перемещаем файл в созаную папку меняя путь методом Rename
        messagebox.showinfo('Success' , 'Сортировка завершена ')
        entry_path.delete(0,END)
    else:
        messagebox.showwarning('Error','Выберите папку с фотографиями')






def choose_dir():
    path = filedialog.askdirectory()
    entry_path.delete(0, END)
    entry_path.insert(0, path)


m_frame = Frame(root, bg='#56ADFF', bd=5)
m_frame.pack(pady=10, padx=10, fill=X)
entry_path = ttk.Entry(m_frame)
entry_path.pack(side=LEFT, expand=1, fill=X)
Btn_choose = ttk.Button(m_frame, text='Выбрать папку', command=choose_dir).pack(fill=X, side=LEFT, padx=8)

start = ttk.Button(root, text=' Start', style="my.TButton", command=start).pack(fill=X, padx=10)

root.mainloop()
