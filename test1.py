
import tkinter as tk
gui = tk.Tk()
gui.geometry("500x500")
gui.title("Samglish Translator")
gui.configure(background="lightblue")

sms_dictionnary = {' ': ' ', 'bonjour': 'bjr', 'salut': 'slt'}  # completer le dictionnaire

def sms_translator():
    phrase = myEntry.get()
    sms_message = ""
    for x in phrase:
        try: # on éssait de traduire
            sms_message += sms_dictionnary[x]
            sms_message += " "
            print(sms_message) 
        except KeyError:# sinon on restitue le mot tel qu'il est.
            sms_message += phrase[phrase.index(x)]
            sms_message += " "
            print(sms_message)
def trados():
    sms_translator
    sms_translator.phrase += ""
    sms_translator.phrase = [mot for mot in sms_translator.phrase.split(" ")]
    sms_translator

myLabel=tk.Label(gui, text="Wadjonautes translator", font=("Arial", 15),background="lightblue")
myLabel.pack()
myLabel1=tk.Label(gui, text="FR to FB",background="lightblue")
myLabel1.pack()
myEntry = tk.Entry(gui, width=40)
myEntry.pack(pady=20)

btn = tk.Button(gui, height=1, width=10, text="Lire", command=trados)
btn.pack()


gui.mainloop()