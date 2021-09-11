import tkinter as tkr
app = tkr.Tk(__name__)
app.title('My GUI App')
app.geometry('400x400')

##tkr.Label(app, text='Hello Python').pack()
##tkr.Label(app, text='A String').pack()
##tkr.Label(app, text='Welcome Home').pack()
##tkr.Label(app, text='It was nice').pack()

##tkr.Label(app, text='Hello Python').grid(row=0,column=1)
##tkr.Label(app, text='A String').grid(row=1,column=2)
##tkr.Label(app, text='Welcome Home').grid(row=2, column=0)
##tkr.Label(app, text='It was nice').grid(row=0,column=2)


v = tkr.Variable(app)
t = tkr.Variable(app)

tkr.Label(app, text='Hello Python').place(x=10, y=10)
tkr.Label(app, text='A String').place(x=250, y =10)
tkr.Label(app, text='Welcome Home').place(x=100,y=50)
tkr.Label(app, text='It was nice').place(x=10, y=50)
tkr.Label(app, textvariable=t).place(x=150, y=175)

tkr.Entry(app, textvariable=v).place(x=150, y = 200)

def func():
    print('button click ho gaya')
    print(v.get()) # v.set('koi bhi value')
    t.set('You wrote:'+v.get())

tkr.Button(app, text='Click Me', command=func).place(x=150, y=250)


app.mainloop()



















































##import test
##
##test.abc()

