from tkinter import *

root = Tk()

# set geometry
root.title("Dictionary")
root.geometry("600x400+50+50")


# Add labels, buttons and frame
Label(root, text="STATEMENT TOKENIZER", font=(
    "CASTELLAR, 20 "), bg="cyan4").pack(pady=20)

# Frame 1
frame = Frame(root)
Label(frame, font=(
    "Helvetica, 15 bold")).pack(side="left")
word = Entry(frame, font=("Helvetica, 15 bold"), width=30)
word.pack()
frame.pack(pady=10)

# Frame 2
frame1 = Frame(root)
Label(frame1, text="Total words: ", font=("Aerial, 15 bold")).pack(side=LEFT)
Total = Entry(frame1, text="", font=("Poppins, 15"), width=10)
Total.pack()
frame1.pack(pady=10)


root.mainloop()

