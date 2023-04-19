# import tkinter
# m=tkinter .Tk()
# '''
# widgets are added here 
# '''
# m.mainloop()

import tkinter as tk

main=tk.Tk(className="emi calculator")
main.geometry("600x600")

label1=tk.Label(main,text="python")
txt1=tk.Entry(main)
btn1=tk.Button(main,text="submit")

label1.grid(row=0,column=0)
txt1.grid(row=0,column=1)
btn1.grid(row=1,column=1)

main.mainloop()