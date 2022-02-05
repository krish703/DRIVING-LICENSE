from tkinter import *
root = Tk()

root.title("Driving LIcense")
root.geometry("400x200")

label_TITLE=Label(root, text="DRIVING LICENSE ")

label_ID=Label(root, text="ID:19827198349 ")

label_NAME=Label(root, text="NAME=Wnnie The Pooh")

label_Dateofbirth=Label(root, text="21 AUGUST 1921")

label_PIN=Label(root, text="PIN NO:451478")

label_ADDRESS=Label(root, text="ADDRESS: DISNEYLAND,HONG KONG")

label_AUTHORISATION=Label(root, text="AUTHORISATION TO DRIVE THE FOLLOWING VEHICLES:TWO FOUR")

label_TITLE.pack()

label_ID.pack()

label_NAME.pack()

label_Dateofbirth.pack()

label_PIN.pack()

label_ADDRESS.pack()

label_AUTHORISATION.pack()

root.mainloop()


