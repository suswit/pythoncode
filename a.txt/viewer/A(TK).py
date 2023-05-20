import tkinter as tk
main=tk.Tk(className="student id card")
main.configure(bg="black")
main.geometry("1000x1000")

label1=tk.Label(main,text="CHRISTIANO RONALDO").grid(row=0,column=0)
txt1=tk.Entry(main).grid(row=0,column=1)  

label1=tk.Label(main,text="LIONEL MESSI").grid(row=1,column=0)
txt1=tk.Entry(main).grid(row=1,column=1)  


label=tk.Label(main,text="NEYMAR JR").grid(row=2,column=0)
txt1=tk.Entry(main).grid(row=2,column=1)

label=tk.Label(main,text="IBRAHIMOVIC").grid(row=3,column=0)
txt1=tk.Entry(main).grid(row=3,column=1)

label=tk.Label(main,text="PAUL POGBA").grid(row=4,column=0)
txt1=tk.Entry(main).grid(row=4,column=1)

label=tk.Label(main,text="PELE").grid(row=5,column=0)
txt1=tk.Entry(main).grid(row=5,column=1)

label=tk.Label(main,text="MBAPPE").grid(row=6,column=0)
txt1=tk.Entry(main).grid(row=6,column=1)

label=tk.Label(main,text="JOO_7").grid(row=7,column=0)
txt1=tk.Entry(main).grid(row=6,column=1)




main.mainloop()