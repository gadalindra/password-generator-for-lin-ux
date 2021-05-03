from tkinter import *
from random import choice
import string


def passwordGenerator():

    def save_info():
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.printable
        password = ""
        lenghtX = lenght.get()

        for s in range(lenghtX):
            password += choice(characters)
        
        file = open("password.txt", "w")
        file.write(f"Your password is: {password} \n")
        file.close()
        print("User", lenghtX, "has been registered successfully.")

    screen = Tk()
    screen.geometry("500x500")
    screen.title('Password Generator')
    heading = Label(text='Password Generator', bg='grey', fg='black', width="500", height="3")
    heading.pack()

    lenght_text = Label(text="Length")
    lenght_text.place(x=140, y=85)

    lenght = IntVar()

    lenght_entry = Entry(textvariable = lenght, width="3")

    lenght_entry.place(x=210, y=85)

    generate = Button(screen, text="Generate", width="22", command=save_info)
    generate.place(x=110, y=135)

    screen.mainloop()

if __name__ == '__main__':
    passwordGenerator()
