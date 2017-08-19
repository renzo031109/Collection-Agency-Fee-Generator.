from tkinter import*
import tkinter.messagebox

class Cafee:

    def CallComputeClick(self):
        self.CallCompute()

    def CallComputeEnter(self,enter):
        self.CallCompute()

    def cquit(self):
        self.master.destroy()
        
    def cabout(self):
        tkinter.messagebox.showinfo("About Collection Agency Calc",'This Application is Licensed to Avon Angeles Branch \n\n \
        "To GOD be all the glory" \n\n \
        Created by : Renan Rivera :)')

    def CallCompute(self):

        try:
            self.total=0        
            if self.var.get()==1:
                if self.var2.get()==1:
                    self.answer=float(self.PaymentEnt.get())*0.15
                else:
                    self.answer=float(self.PaymentEnt.get())-(float(self.PaymentEnt.get())/1.15)      
            if self.var.get()==2:
                if self.var2.get()==1:
                    self.answer=float(self.PaymentEnt.get())*0.25 
                else: 
                    self.answer=float(self.PaymentEnt.get())-float(self.PaymentEnt.get())/1.25                  
        
            self.total=float(self.PaymentEnt.get())+self.answer
        
            self.TotalLbl.set(round(self.total,2))        
            self.answerLbl.set(round(self.answer,2))        

        except:
            tkinter.messagebox.showinfo("Wrong Input","Please input Numeric only! ")
         
    
    def __init__(self,master):

        self.master=master
        master.title("Collection Agency Fee Calc")
        master.wm_iconbitmap('rlogo.ico')

        #Menu Bar
        self.menubar=Menu(master)
        self.filemenu=Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Exit",command=self.cquit)
        self.menubar.add_cascade(label="File",menu=self.filemenu)

        self.Helpmenu=Menu(self.menubar,tearoff=0)
        self.Helpmenu.add_command(label="About Collection Agency Fee Calc",command=self.cabout)
        self.menubar.add_cascade(label="Help",menu=self.Helpmenu)
        
        master.config(menu=self.menubar)      
                

        self.separator = Frame(height=3, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=5, pady=5)

        self.var=IntVar()
        self.var.set(1)        
        
        Label(window,text="SELECT PASTDUE TYPE",font=("Arial",12),fg="red").pack(anchor=CENTER)
        Radiobutton(window,text="RC-84 (PDA from 15days above/Not yet writteoff)", \
                    variable=self.var,value=1).pack(anchor=W)
        Radiobutton(window,text="RC-02 (Writteoff Account)", \
                    variable=self.var, value=2).pack(anchor=W)


        self.separator = Frame(height=3, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=5, pady=5)
        
        self.var2=IntVar()
        self.var2.set(1)

        Label(window,text="SELECT PAYMENT TYPE",font=("Arial",12),fg="blue").pack(anchor=CENTER)
        Radiobutton(window,text="FULL PAYMENT", \
                    variable=self.var2,value=1).pack(anchor=W)
        Radiobutton(window,text="PARTIAL PAYMENT", \
                    variable=self.var2, value=2).pack(anchor=W)

        self.separator = Frame(height=3, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=5, pady=5)

        Label(window,text="Pastdue Amount :",font=("Arial",12)).pack()

        self.PaymentEnt=Entry(window,width=8,font=("Arial",12))
        self.PaymentEnt.bind("<Return>",self.CallComputeEnter)
        self.PaymentEnt.pack()
        self.PaymentEnt.focus()

        Button(window,text="COMPUTE",bg="GREY",fg="white",command=self.CallComputeClick).pack()
        
        self.separator = Frame(height=3, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=5, pady=5)

        Label(window,text="PENALTY",font=("Arial",10)).pack()
        self.answerLbl=DoubleVar()  
        Entry(window,textvariable=self.answerLbl,width=8,font=("Arial",12),fg="red").pack()

        self.separator = Frame(height=3, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=5, pady=5)

        Label(window,text="TOTAL PAYMENT",font=("Arial",11)).pack()

        self.TotalLbl=DoubleVar()
        Label(window,textvariable=self.TotalLbl,fg="RED").pack()
               
        
window=Tk()       
Cafee(window)
window.mainloop()
