import Tkinter

def set_text(text):
    entry.delete(0, Tkinter.END)
    entry.insert(0, text)
    return

def click_button1():
    vmesna_stevilka ="1"
    kar_je_bilo_od_prej = entry.get()
    set_text(kar_je_bilo_od_prej + vmesna_stevilka)

def click_button2():
    vmesna_stevilka ="2"
    set_text(entry.get() + vmesna_stevilka)

def click_button3():
    vmesna_stevilka ="3"
    set_text(entry.get() + vmesna_stevilka)

def click_button4():
    vmesna_stevilka ="4"
    set_text(entry.get() + vmesna_stevilka)

def click_button5():
    vmesna_stevilka ="5"
    set_text(entry.get() + vmesna_stevilka)

def click_button6():
    vmesna_stevilka ="6"
    set_text(entry.get() + vmesna_stevilka)

def click_button7():
    vmesna_stevilka ="7"
    set_text(entry.get() + vmesna_stevilka)

def click_button8():
    vmesna_stevilka ="8"
    set_text(entry.get() + vmesna_stevilka)

def click_button9():
    vmesna_stevilka ="9"
    set_text(entry.get() + vmesna_stevilka)

def click_button0():
    vmesna_stevilka ="0"
    set_text(entry.get() + vmesna_stevilka)

def click_buttonp():
    vmesna_stevilka ="+"
    set_text(entry.get() + vmesna_stevilka)

def click_buttonm():
    vmesna_stevilka ="-"
    set_text(entry.get() + vmesna_stevilka)

def click_buttonj():
    vmesna_stevilka ="="
    set_text(entry.get() + vmesna_stevilka)

def click_buttonj():
    enacba = entry.get()

    rezultat = 0

    stevilke = enacba.split("+")
    if len(stevilke) == 2:
        prva_stevilka = int(stevilke[0])
        druga_stevilka = int(stevilke[1])
        rezultat = prva_stevilka + druga_stevilka

    stevilke = enacba.split("-")
    if len(stevilke) == 2:
        prva_stevilka = int(stevilke[0])
        druga_stevilka = int(stevilke[1])
        rezultat = prva_stevilka - druga_stevilka


    set_text(rezultat)

window = Tkinter.Tk()

entry = Tkinter.Entry(window)
entry.pack()

submit = Tkinter.Button(window, text="1", height=2, width=5, command=click_button1)
submit.pack()

submit = Tkinter.Button(window, text="2", height=2, width=5, command=click_button2)
submit.pack()

submit = Tkinter.Button(window, text="3", height=2, width=5, command=click_button3)
submit.pack()

submit = Tkinter.Button(window, text="4", height=2, width=5, command=click_button4)
submit.pack()

submit = Tkinter.Button(window, text="5", height=2, width=5, command=click_button5)
submit.pack()

submit = Tkinter.Button(window, text="6", height=2, width=5, command=click_button6)
submit.pack()

submit = Tkinter.Button(window, text="7", height=2, width=5, command=click_button7)
submit.pack()

submit = Tkinter.Button(window, text="8", height=2, width=5, command=click_button8)
submit.pack()

submit = Tkinter.Button(window, text="9", height=2, width=5, command=click_button9)
submit.pack()

submit = Tkinter.Button(window, text="0", height=2, width=5, command=click_button0)
submit.pack()

submit = Tkinter.Button(window, text="+", height=2, width=5, command=click_buttonp)
submit.pack()

submit = Tkinter.Button(window, text="-", height=2, width=5, command=click_buttonm)
submit.pack()

submit = Tkinter.Button(window, text="=", height=2, width=5, command=click_buttonj)
submit.pack()

window.mainloop()