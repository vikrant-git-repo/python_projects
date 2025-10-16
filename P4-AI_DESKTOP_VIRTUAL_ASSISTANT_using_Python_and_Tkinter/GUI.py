from tkinter import*
from PIL import Image, ImageTk
import speech_to_text
import action

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")

def ask():
    user_val = speech_to_text.speech_to_text()
    if user_val is None:
        text.insert(END, "User----------> [No input detected]\n")
        text.insert(END, "BOT <---------- Sorry, I couldn't understand what you said.\n")
        return

    bot_val = action.Action(user_val)
    text.insert(END, 'User---------->' + user_val + "\n")
    if bot_val is not None:
        text.insert(END, "BOT <----------" + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()

def send():
    send = entry.get().strip()
    if not send:
        text.insert(END, "User----------> [Empty input]\n")
        text.insert(END, "BOT <---------- Please type something.\n")
        return

    bot = action.Action(send)
    text.insert(END, 'User---------->' + send + "\n")
    if bot is not None:
        text.insert(END, "BOT <----------" + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()


def del_text():
    text.delete('1.0', "end")

# Frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=0, padx=55, pady=10)

# Text Label
text_label = Label(frame, text="AI Assistant", font=("comic sans ms", 14, "bold"), bg="#356696")
text_label.grid(row=0, column=0, padx=20, pady=10)

# Image
image = ImageTk.PhotoImage(Image.open(r"C:\Users\ah85745\OneDrive - Elevance Health\Desktop\VS Code Folders\python_projects\AI_DESKTOP_VIRTUAL_ASSISTANT_using_Python_and_Tkinter\assistant.png"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)

# Adding a Text Widget
text = Text(root, font=('courier 10 bold'), bg="#356696")
text.grid(row=2, column=0)
text.place(x=70, y=300, width=375, height=100)

# Entry Widget
entry = Entry(root, justify=CENTER)
entry.place(x=75, y=450, width=350, height=30)

# Button1
Button1 = Button(root, text="ASK", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=50, y=575)

Button2 = Button(root, text="Send", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=370, y=575)


Button3 = Button(root, text="Delete", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=del_text)
Button3.place(x=205, y=575)


root.mainloop()

