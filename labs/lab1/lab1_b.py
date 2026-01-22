''''hello world with input as thinker program'''
from struct import pack
from thinker import Tk, Frame, Label, Entry, Button, messagebox

window=Tk()
window.title("Hello")


frame=Frame(window)
Label(frame, text="What is your name?", padx=10, pady=10).pack(side="left")
entry=Entry(frame)
entry.pack(side="right")

frame.pack(side="top")
Button(window, text="press me",
       command=lambda: (messagebox.showinfo("hello", f"Nice to see you, {entry.get()}."), entry.delete(0,"end"))).pack(side="bottom")

window.mainloop()