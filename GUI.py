from tkinter import *

def insertion():
    print("Clicked Button")

def gui_for_project():
    window = Tk()
    window.geometry("500x500")
    window.title("Graham-Hull and QuadTree Algorithms")
    window.configure(bg='grey')

    label1 = Label(window, text="Szymon Rogowski(405244)", font=('NewTimesRoman', 20), bg='black', fg='white')
    label1.pack()
    label2 = Label(window, text="Hubert ()", font=('NewTimesRoman', 20), bg='black', fg='white')
    label2.pack()
    insertion_button = Button(window, text="Insert value of n.", width=40, height=10, command=insertion)
    insertion_button.pack()
    quit_button = Button(window, text="Exit.", width=40, height=10, command=quit)
    quit_button.pack()

    window.mainloop()