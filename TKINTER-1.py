import tkinter

window = tkinter.Tk()
# window = tkinter.Tk(className="The First Window")
window.title("My First Window")
window.geometry("400x400")
# window.resizable(width=False, height=False)
window.maxsize(width=500, height=500)
window.configure(background="#0e6b78")

label1 = tkinter.Label(window, text="Welcome", bg="black", fg="white")
label1.pack(side="top", fill="x", expand=True)
window.mainloop()
