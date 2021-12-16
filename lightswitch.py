import tkinter as tk
window = tk.Tk()
count = 0
a = 0
# schijf hier tussen je code
def knop(a):
    global button, count
    if count == 0:
        print("licht aan.")
        button.config(text='Light on.', bg="white", fg='Black')
        window.config(bg="yellow")
        count += 1
    else:
        print("licht uit.")
        button.config(text='Light off.', bg='white', fg='black')
        window.config(bg="black")
        count -= 1

button = tk.Button(text='light off.', bg="white", fg="black")
window.config(bg='black')
button.pack(pady = 50, padx = 60)
button.bind('<Button>', knop)
# schijf hier tussen je code

window.mainloop()