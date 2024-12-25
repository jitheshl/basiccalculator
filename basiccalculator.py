
from tkinter import *

firstnumber=secondnumber=operator=None

def getdigit(digit):
    current=result['text']
    new = current +str(digit)
    result.config(text=new)

def allclear():
    result.config(text='')

def getoperator(op):
    global firstnumber,operator
    firstnumber=int(result['text'])
    operator=op
    result.config(text='')

def getresult():
    global firstnumber,secondnumber,operator
    secondnumber=int(result['text'])

    if operator =="+":
        result.config(text=str(firstnumber+secondnumber))
    elif operator =="-":
        result.config(text=str(firstnumber - secondnumber))
    elif operator =="x":
        result.config(text=str(firstnumber * secondnumber))
    else:
        if secondnumber==0:
            result.config(text='Error')
        else:
            result.config(text=str(firstnumber / secondnumber))




root = Tk()
root.title(' jithesh calculator')
root.geometry('280x380')
root.resizable(0,0)
root.configure(background='black')


result=Label(root,text='',bg='black',fg='white')
result.grid(row=0,column=0,columnspan=100,pady=(25,50),sticky='w')
result.config(font=('verdana',30,'bold'))


b7=Button(root,text='7',bg='black',fg='white',width=5,height=2,command=lambda :getdigit(7))
b7.grid(row=1,column=0)
b7.config(font=('verdana',14))

b8=Button(root,text='8',bg='black',fg='white',width=5,height=2,command=lambda :getdigit(8))
b8.grid(row=1,column=1)
b8.config(font=('verdana',14))

b9=Button(root,text='9',bg='black',fg='white',width=5,height=2,command=lambda :getdigit(9))
b9.grid(row=1,column=2)
b9.config(font=('verdana',14))

badd=Button(root,text='+',bg='black',fg='blue',width=5,height=2,command=lambda :getoperator('+'))
badd.grid(row=1,column=3)
badd.config(font=('verdana',14))


b4=Button(root,text='4',bg='black',fg='white',width=5,height=2,command=lambda :getdigit(4))
b4.grid(row=2,column=0)
b4.config(font=('verdana',14))

b5=Button(root,text='5',bg='black',fg='white',width=5,height=2,command=lambda :getdigit(5))
b5.grid(row=2,column=1)
b5.config(font=('verdana',14))

b6=Button(root,text='6',bg='black',fg='white',width=5,height=2,command=lambda :getdigit(6))
b6.grid(row=2,column=2)
b6.config(font=('verdana',14))

bsub=Button(root,text='-',bg='black',fg='blue',width=5,height=2,command=lambda :getoperator('-'))
bsub.grid(row=2,column=3)
bsub.config(font=('verdana',14))

b1=Button(root,text='1',bg='black',fg='white',width=5,height=2,command=lambda :getdigit(1))
b1.grid(row=3,column=0)
b1.config(font=('verdana',14))

b2=Button(root,text='2',bg='black',fg='white',width=5,height=2,command=lambda :getdigit(2))
b2.grid(row=3,column=1)
b2.config(font=('verdana',14))

b3=Button(root,text='3',bg='black',fg='white',width=5,height=2,command=lambda :getdigit(3))
b3.grid(row=3,column=2)
b3.config(font=('verdana',14))

bmul=Button(root,text='x',bg='black',fg='blue',width=5,height=2,command=lambda :getoperator('x'))
bmul.grid(row=3,column=3)
bmul.config(font=('verdana',14))

bclear=Button(root,text='AC',bg='black',fg='blue',width=5,height=2,command=lambda :allclear())
bclear.grid(row=4,column=0)
bclear.config(font=('verdana',14))

b0=Button(root,text='0',bg='black',fg='white',width=5,height=2,command=lambda :getdigit(0))
b0.grid(row=4,column=1)
b0.config(font=('verdana',14))

bequal=Button(root,text='=',bg='black',fg='blue',width=5,height=2,command=lambda :getresult())
bequal.grid(row=4,column=2)
bequal.config(font=('verdana',14))

bdiv=Button(root,text='/',bg='black',fg='blue',width=5,height=2,command=lambda :getoperator('/'))
bdiv.grid(row=4,column=3)
bdiv.config(font=('verdana',14))


root.mainloop()
