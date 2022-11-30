import tkinter as tk
from datetime import datetime

def log_data(text_log):
    folder = r'log.txt'
    with open(folder, 'a+', encoding='UTF-8') as file:
        file.write(f'{datetime.now()}:  {text_log}\n')


windows=tk.Tk()
windows.geometry('345x250+100+110')
windows['bg']='#348284'
windows.title('Калькулятор')
windows.resizable(False,False)


def create_number(number):
    value= calcul.get()+str(number)
    if value[0]=='0':
        value=value[1:]
    calcul.delete(0,tk.END)
    calcul.insert(0,value)
    log_data('ввод числа ' +number)

def create_operation(operation):
    value= calcul.get()    
    if value[-1] in '+-*/'and value[-2] in '+-*/' :
        value=value[0:-2]    
    calcul.delete(0,tk.END)
    calcul.insert(0,value+operation)
    log_data('выбор операции ' +operation)


def result_operation():
    value=calcul.get()
    calcul.delete(0,tk.END)
    calcul.insert(0,eval(value))
    log_data('Результат выражение  ' +value)

def clear():
    calcul.delete(0,tk.END)
    calcul.insert(0,'0')
    log_data('очистка на 0')

def make_clear_btn(operation):    
    return tk.Button(text=operation,font=('Monaco',15),command=clear)

def make_number_btn(number):    
    return tk.Button(text=number,font=('Monaco',15),command= lambda : create_number(number))

def make_operation_btn(operation):    
    return tk.Button(text=operation,font=('Monaco',15),command= lambda : create_operation(operation))

def make_result_btn(operation):   
    return tk.Button(text=operation,font=('Monaco',15),command=result_operation)

calcul=tk.Entry(windows,font=('Monaco',20),justify=tk.RIGHT)
calcul.grid(row=0,column=0,columnspan=5,padx=10)

make_number_btn('1').grid(row=1,column=0,sticky='wens',padx=5,pady=5)
make_number_btn('2').grid(row=1,column=1,sticky='wens',padx=5,pady=5)
make_number_btn('3').grid(row=1,column=2,sticky='wens',padx=5,pady=5)
make_number_btn('4').grid(row=1,column=3,sticky='wens',padx=5,pady=5)
make_number_btn('5').grid(row=2,column=0,sticky='wens',padx=5,pady=5)
make_number_btn('6').grid(row=2,column=1,sticky='wens',padx=5,pady=5)
make_number_btn('7').grid(row=2,column=2,sticky='wens',padx=5,pady=5)
make_number_btn('8').grid(row=2,column=3,sticky='wens',padx=5,pady=5)
make_number_btn('9').grid(row=3,column=0,sticky='wens',padx=5,pady=5)
make_number_btn('0').grid(row=3,column=1,sticky='wens',padx=5,pady=5)

make_operation_btn('+').grid(row=1,column=4,sticky='wens',padx=5,pady=5)
make_operation_btn('-').grid(row=2,column=4,sticky='wens',padx=5,pady=5)
make_operation_btn('*').grid(row=3,column=4,sticky='wens',padx=5,pady=5)
make_operation_btn('/').grid(row=4,column=4,sticky='wens',padx=5,pady=5)
make_operation_btn('(').grid(row=3,column=2,sticky='wens',padx=5,pady=5)
make_operation_btn(')').grid(row=3,column=3,sticky='wens',padx=5,pady=5)

make_clear_btn('C').grid(row=4,column=2,sticky='wens',padx=5,pady=5)

make_result_btn('=').grid(row=4,column=3,sticky='wens',padx=5,pady=5)

windows.grid_columnconfigure(0,minsize=40)
windows.grid_columnconfigure(1,minsize=40)
windows.grid_columnconfigure(2,minsize=40)
windows.grid_columnconfigure(3,minsize=40)
windows.grid_columnconfigure(4,minsize=40)


windows.grid_rowconfigure(0,minsize=50)
windows.grid_rowconfigure(1,minsize=50)
windows.grid_rowconfigure(2,minsize=50)
windows.grid_rowconfigure(3,minsize=50)
windows.grid_rowconfigure(4,minsize=50)


windows.mainloop()