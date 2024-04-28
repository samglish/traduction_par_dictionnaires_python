import re
import tkinter as tk
gui = tk.Tk()
gui.geometry("500x500")
gui.title("Samglish Translator")
gui.configure(background="lightblue")
def Translate(phrase):
    motsFR = ["bonjour", "salut"]
    motsFB = ["bjr", "slt"]
    for i in range(len(motsFR)):
        phrase = re.sub(motsFR[i], motsFB[i], phrase)
    return phrase

myLabel=tk.Label(gui, text="Wadjonautes translator", font=("Arial", 15),background="lightblue")
myLabel.pack()
myLabel1=tk.Label(gui, text="FR to FB",background="lightblue")
myLabel1.pack()
myEntry = tk.Entry(gui, width=40)
myEntry.pack(pady=20)

btn = tk.Button(gui, height=1, width=10, text="Lire", command=Translate('salut'))
btn.pack()


gui.mainloop()