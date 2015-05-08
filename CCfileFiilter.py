from Tkinter import *
import tkFileDialog
import glob, os

master = Tk()

master.resizable(width=FALSE, height=FALSE)
#master.geometry('{}x{}'.format(400, 500))


"""
Label(master, text="First").grid(row=0)
Label(master, text="Second").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
button1=Button(master, height=1, width=20,text="hello")
button1.grid(row=2, column=2)
#button2.grid(row=2, column=3)
"""
    
    
def callback(value):
    
    def openDoc(evt):
        value=str((data.get(data.curselection())))
        print value
        text_window= Text(master)
        files_con = open(value)
        dd=files_con.read()
        top = Toplevel()
        top.title(value)
        text = Text(top)
        text.insert(INSERT,dd)
        text.grid( row=0,column=0)
        yscroll = Scrollbar(top,command=text.yview, orient=VERTICAL)
        yscroll.grid(row=0, column=1, sticky='ns')
        text.configure(yscrollcommand=yscroll.set)
        print dd
        files_con.close()
        

        
    
    data = Listbox(master, width=20, height=10)
    data.grid(row=0, column=1)
    # create a vertical scrollbar to the right of the data
    yscroll = Scrollbar(command=data.yview, orient=VERTICAL)
    yscroll.grid(row=0, column=2, sticky='ns')
    data.configure(yscrollcommand=yscroll.set)
    data.bind('<<ListboxSelect>>',openDoc)
      
    for file in glob.glob("*"+value):
        print(file)
        data.insert('end', file)
        

def CurSelet(evt):
    value=str((listbox.get(listbox.curselection())))
    callback(value)

listbox =Listbox(master, width=20, height=10)
listbox.grid(row=0, column=0)
listbox.bind('<<ListboxSelect>>',CurSelet)

file_types=['.cpp','.py','.js']
for i in file_types:
    listbox.insert('end', i)
    


callback("33")
"""def chooseDir():
    dirname = tkFileDialog.askdirectory(parent=master,initialdir="/",title='Please select a directory')
    if len(dirname ) > 0:
        print "You chose %s" % dirname """

"""
button1=Button(master, height=1, width=20,text="Change Directory",command=chooseDir,bg="red")
button1.grid(row=3, column=0)"""


master.mainloop()
