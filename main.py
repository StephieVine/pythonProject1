from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("700x500")

def getvals():
    print("Accepted")

#Heading_________________________________________________________________________________________
Label(root, text="Python Registration Form", font="ariel 15 bold").grid(row=0, column=3)

# background pic and size______________________________________________________________________________
root.title("School Management System")
image_0=Image.open('C:\\Users\\Igbon Ifijeh\\Desktop\\St. Scriptures\\images (19).jpeg')
bck_end=ImageTk.PhotoImage(image_0.resize((700,500)))

lbl=Label(root, image=bck_end)
lbl.place(x=1,y=1)

# frame = Frame(root, width=350, height=350, bg='blue')
# frame.place(x=480, y=70)
#
# heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('ALGERIAN', 23, 'bold'))
# heading.place(x=100, y=5)
# ------------------------------------------------------------------------------------------------

# Labels_________________________________________________________________________________________
name = Label(root, text="Name")
phone = Label(root, text="Phone Number")
gender = Label(root, text="Gender")
Emergency = Label(root, text="Emergency")
PaymentMode = Label(root, text="Payment Mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
Emergency.grid(row=4, column=2)
PaymentMode.grid(row=5, column=2)

#Variable storage
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
Emergencyvalue = StringVar
PaymentModevalue = StringVar
checkvalue = IntVar

#creating entry field
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
Emergencyentry = Entry(root, textvariable =Emergencyvalue)
PaymentModeentry = Entry(root, textvariable =PaymentModevalue)

#packing entry Field
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
Emergencyentry.grid(row=4, column=3)
PaymentModeentry.grid(row=5, column=3)

#Creating checkbox
checkbtn = Checkbutton(text="ME", variable = checkvalue)
checkbtn.grid(row=6, column=3)

#Submitting
Button(text="Submit", command=getvals, font="ALGERIAN 20").grid(row=150, column=300,)
root.mainloop()

