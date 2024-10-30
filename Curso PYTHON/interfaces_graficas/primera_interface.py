from tkinter import *

raiz = Tk()
raiz.geometry("500x500")

raiz.title("I'm Hamel")

#frame 1
miFrame = Frame(raiz, width=70, height=70)
miFrame.pack(side="left", anchor="n")
miFrame.config(bg="#287548")
Label(miFrame, text="Frame 1", font=("Arial", 10)).place(x=10, y=10)

#frame 2
miFrame2 = Frame(raiz, width=70, height=70)
miFrame2.place(relx=0.5, rely=0.5, anchor="center")
miFrame2.config(bg="#0C0C0C")
Label(miFrame2, text="Frame 1", font=("Arial",10)).place(x=10, y=5)

#frame 3
miFrame3 = Frame(raiz, width=70, height=70)
miFrame3.pack(side="right", anchor="s")
miFrame3.config(bg="#99EBFF")
Label(miFrame3, text="Frame 1", fg="black", font=("Arial", 10)).place(x=10, y=5)

raiz.mainloop()