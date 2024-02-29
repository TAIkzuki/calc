import tkinter as tk
def say_hello(text):
    index= int (3)
    print(index)
    print(type(index))
    return index

def counter():
    global count
    count+=1
    btn3['text']=fcount = 0
win = tk.Tk()
win.title('calculate')
#photo = tk.PhotoImage(file='tt.png')
#win.iconphoto(False, photo)
win.config(bg='#2DFAFF')
label_1 = tk.Label(win,text='v 1.0.0')
label_1.pack()
btn1=tk.Button(win,text=range(1,10,1),command=say_hello)
btn2=tk.Button(win,text="lambda",command=lambda :tk.Label(win,text='new lmbd').pack())
btn3=tk.Button(win,text=f'счетчик: {count}'
               ,command=counter()
               ,
               )


btn1.pack()
btn2.pack()

h=500
w=600
win.geometry(f"{h}x{w}")
#win.minsize(300,400)
win.resizable(False,False)
win.mainloop()