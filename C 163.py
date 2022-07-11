from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("900x500")
question1_radiobutton=StringVar(value="0")
label_Q1=Label(root,text="Do You Have A Headache and A Sore Throat  ?")
label_Q1.pack()
q1_r1=Radiobutton(root,text="Yes",variable=question1_radiobutton,value="Yes")
q1_r1.pack()
q1_r2=Radiobutton(root,text="No",variable=question1_radiobutton,value="No")
q1_r2.pack()

question2_radiobutton=StringVar(value="0")
label_Q2=Label(root,text="Is Your Body Temparature High ?")
label_Q2.pack()
q2_r1=Radiobutton(root,text="Yes",variable=question2_radiobutton,value="Yes")
q2_r1.pack()
q2_r2=Radiobutton(root,text="No",variable=question2_radiobutton,value="No")
q2_r2.pack()

question3_radiobutton=StringVar(value="0")
label_Q3=Label(root,text="Are There Any Symptoms Of Eye Redness ?")
label_Q3.pack()
q3_r1=Radiobutton(root,text="Yes",variable=question3_radiobutton,value="Yes")
q3_r1.pack()
q3_r2=Radiobutton(root,text="No",variable=question3_radiobutton,value="No")
q3_r2.pack()
def feverscore():
    score=0
    if question1_radiobutton.get()=="Yes":
        score=score+20
    if question2_radiobutton.get()=="Yes":
        score=score+20
    if question3_radiobutton.get()=="Yes":
        score=score+20
    if score<=20:
        messagebox.showinfo("report","You Don't Need To Visit A Doctor")
    elif score>20 and score<=40:
        messagebox.showinfo("report","You Perhaps Have To Visit A Doctor")
    else :
        messagebox.showinfo("report","You Have To Visit A Doctor , It's Mandatory")
button_1=Button(root,text="Click Me",command=feverscore)
button_1.pack()
root.mainloop()