from tkinter import*
logo_root=Tk()
logo_root.geometry("455x244")
photo=PhotoImage(file="tnplogo.png")
logo_label=Label(image=photo)
logo_label.pack()
logo_root.mainloop()