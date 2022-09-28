from tkinter import *

root = Tk()
root.geometry("500x350")
root.iconbitmap('icontest.ico')
root.configure(bg = "khaki")
root.title("Gagets")

def page_2():
    # powered by ~ Zaque
    import pyautogui as auto
    import sys
    import time
    from tkinter import messagebox

    root = Tk()
    root.geometry("450x600")
    root.iconbitmap('icontest.ico')
    root.title("Auto Clicker")
    root.configure(bg="gray")

    def clicks_100():
        INPUT = inputmilliseconds.get("1.0", "end-1c")
        print(INPUT)
        if INPUT == "10":
            def ms_10():
                time.sleep(3)
                auto.click(button='left', clicks=100, interval=0.01)

            ms_10()

        if INPUT == "40":
            def ms_40():
                time.sleep(3)
                auto.click(button='left', clicks=100, interval=0.04)

            ms_40()

        if INPUT == "100":
            def ms_100():
                time.sleep(3)
                auto.click(button='left', clicks=100, interval=0.1)

            ms_100()

        if INPUT == "200":
            def ms_200():
                time.sleep(3)
                auto.click(button='left', clicks=100, interval=0.2)

            ms_200()

            def ms_300():
                time.sleep(3)
                auto.click(button='left', clicks=100, interval=0.3)

            ms_300()

        if INPUT == "400":
            def ms_400():
                time.sleep(3)
                auto.click(button='left', clicks=100, interval=0.4)

            ms_400()

        if INPUT == "500":
            def ms_500():
                time.sleep(3)
                auto.click(button='left', clicks=100, interval=0.5)

            ms_500()

        else:
            messagebox.showerror("!info!", "Succes")

    def clicks_1000():
        INPUT = inputmilliseconds.get("1.0", "end-1c")
        print(INPUT)
        if INPUT == "10":
            def ms_10():
                time.sleep(3)
                auto.click(button='left', clicks=1000, interval=0.01)

            ms_10()

        if INPUT == "40":
            def ms_40():
                time.sleep(3)
                auto.click(button='left', clicks=1000, interval=0.04)

            ms_40()

        if INPUT == "100":
            def ms_100():
                time.sleep(3)
                auto.click(button='left', clicks=1000, interval=0.1)

            ms_100()

        if INPUT == "200":
            def ms_200():
                time.sleep(3)
                auto.click(button='left', clicks=1000, interval=0.2)

            ms_200()

            def ms_300():
                time.sleep(3)
                auto.click(button='left', clicks=1000, interval=0.3)

            ms_300()

        if INPUT == "400":
            def ms_400():
                time.sleep(3)
                auto.click(button='left', clicks=1000, interval=0.4)

            ms_400()

        if INPUT == "500":
            def ms_500():
                time.sleep(3)
                auto.click(button='left', clicks=1000, interval=0.5)

            ms_500()

        else:
            messagebox.showerror("!info!", "Succes")

    def whileTrue():
        INPUT = inputmilliseconds.get("1.0", "end-1c")
        print(INPUT)
        if INPUT == "10":
            def ms_10():
                time.sleep(3)
                auto.click(button='left', clicks=100000000, interval=0.01)

            ms_10()

        if INPUT == "40":
            def ms_40():
                time.sleep(3)
                auto.click(button='left', clicks=100000000, interval=0.04)

            ms_40()

        if INPUT == "100":
            def ms_100():
                time.sleep(3)
                auto.click(button='left', clicks=100000000, interval=0.1)

            ms_100()

        if INPUT == "200":
            def ms_200():
                time.sleep(3)
                auto.click(button='left', clicks=100000000, interval=0.2)

            ms_200()

            def ms_300():
                time.sleep(3)
                auto.click(button='left', clicks=100000000, interval=0.3)

            ms_300()

        if INPUT == "400":
            def ms_400():
                time.sleep(3)
                auto.click(button='left', clicks=100000000, interval=0.4)

            ms_400()

        if INPUT == "500":
            def ms_500():
                time.sleep(3)
                auto.click(button='left', clicks=100000000, interval=0.5)

            ms_500()

        else:
            messagebox.showerror("!info!", "Succes")

    title = Label(root, text="Auto clicker", bg="gray")
    space5 = Label(root, text=" ", bg="gray")
    space = Label(root, text=" ", bg="gray")

    milis = Label(root, text="Please enter the number of milliseconds - corner left", background="gray")
    inputmilliseconds = Text(root, height=1, width=25, background="white")
    space6 = Label(root, text=" ", bg="gray")

    button1 = Button(root, width=12, height=4, command=lambda: clicks_100(), text="100 clicks",
                     activebackground="silver")
    space2 = Label(root, text=" ", bg="gray")

    button2 = Button(root, width=12, height=4, command=lambda: clicks_1000(), text="1000 clicks",
                     activebackground="silver")
    space3 = Label(root, text=" ", bg="gray")

    button3 = Button(root, width=12, height=4, command=lambda: whileTrue(), text="Infinit", activebackground="silver")
    space1 = Label(root, text=" ", bg="gray")

    credit = Label(root, text="powered by ~ Zaque", bg="gray")
    credit.place(x=20, y=400)
    cps10 = Label(root, text="10 Millisecond /0.01 s / 100CPS", bg="gray")
    cps10.place(x=20, y=420)
    cps40 = Label(root, text="40 Millisecond /0.04 s / 25CPS", bg="gray")
    cps40.place(x=20, y=440)
    cps100 = Label(root, text="100 Millisecond /0.1 s / 10CPS", bg="gray")
    cps100.place(x=20, y=460)
    cps200 = Label(root, text="200 Millisecond /0.2 s / 5CPS", bg="gray")
    cps200.place(x=20, y=480)
    cps300 = Label(root, text="300 Millisecond /0.3 s / 3.33CPS", bg="gray")
    cps300.place(x=20, y=500)
    cps400 = Label(root, text="400 Millisecond /0.4 s / 2.5CPS", bg="gray")
    cps400.place(x=20, y=520)
    cps500 = Label(root, text="500 Millisecond /0.5 s / 2CPS", bg="gray")
    cps500.place(x=20, y=540)

    space.pack()
    title.pack()
    space5.pack()

    milis.pack()
    inputmilliseconds.pack()
    space6.pack()

    button1.pack()
    space2.pack()

    button2.pack()
    space3.pack()

    button3.pack()
    space1.pack()

    mainloop()


def page_3():
    import pyautogui as auto
    import time
    root = Tk()
    root.geometry("450x450")
    root.title("Spam Bot")
    root.configure(bg="gray")

    def main():
        INSERT = inputtxt.get("1.0", "end-1c")
        print(INSERT)
        while True:
            auto.write(INSERT)
            auto.press("enter")
            time.sleep(0.5)

    space = Label(root, text=" ", bg="gray")

    title = Label(root, text="Spam Bot", bg="gray")
    inputtxt = Text(root, width=20, height=4, bg="ivory")

    space1 = Label(root, text=" ", bg="gray")

    press = Button(root, text="press", width=14, height=2, command=lambda: main(),  activebackground="silver")
    credit = Label(root, text="powered by ~ Zaque", bg="gray")

    space2 = Label(root, text=" ", bg="gray")
    space3 = Label(root, text=" ", bg="gray")

    credit.place(x=20, y=420)

    space.pack()
    title.pack()
    inputtxt.pack()
    space1.pack()
    press.pack()

    space2.pack()
    space3.pack()

    mainloop()
    
def page_4():
    import random
    from tkinter import messagebox 
    root = Tk()
    root.geometry("450x450")
    root.title(" Passworld Generator ")

    def Take_input():
        INPUT = inputtxt.get("1.0", "end-1c")
        print(INPUT)
        if INPUT == "1":
            string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+=-"
            a = "".join(random.sample(string, k=1))
            Output.insert(END, a, "\n")
        elif INPUT == "2":
            string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+=-"
            a = "".join(random.sample(string, k=2))
            Output.insert(END, a, "\n")
        elif INPUT == "3":
            string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+=-"
            a = "".join(random.sample(string, k=3))
            Output.insert(END, a, "\n")
        elif INPUT == "4":
            string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+=-"
            a = "".join(random.sample(string, k=4))
            Output.insert(END, a, "\n")
        elif INPUT == "5":
            string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+=-"
            a = "".join(random.sample(string, k=5))
            Output.insert(END, a, "\n")
        elif INPUT == "6":
            string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+=-"
            a = "".join(random.sample(string, k=6))
            Output.insert(END, a, "\n")
        elif INPUT == "7":
            string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+=-"
            a = "".join(random.sample(string, k=7))
            Output.insert(END, a, "\n")
        elif INPUT == "8":
            string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+=-"
            a = "".join(random.sample(string, k=8))
            Output.insert(END, a, "\n")
        elif INPUT == "9":
            string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+=-"
            a = "".join(random.sample(string, k=9))
            Output.insert(END, a, "\n")
        else:
            Output.insert(END, "invalid command")
    
    up = Label(root, text="Please enter the number of characters that will be chosen")
    space = Label(root, text=" ")
    inputtxt = Text(root, height=10, width=25, bg="light yellow")
    Output = Text(root, height=5, width=25, bg="light green")
    Display = Button(root, height=2, width=20, text="Generate", command=lambda: Take_input())
    space1 = Label(root, text=" ")


    space1.pack()
    inputtxt.pack()
    Display.pack()
    Output.pack()
    space.pack()
    up.pack()
    mainloop()

def page_5():
    import tkinter.ttk
    from time import strftime

    root = Tk()
    root.title("Digital Clock")

    def time():
        string = strftime("%H: %M: %S: %p")
        label.config(text=string)
        label.after(1000, time)

    label = Label(root, font=("digital-7.ttf", 50), background="black", foreground="cyan")

    label.pack()
    time()
    mainloop()


Button1 = Button(root, text="AutoClicker", command=page_2, bg="#aaaf33", activebackground="darkolivegreen", height=3, width=17)
Button1.place(x=100, y=50)

Button2 = Button(root, text="Spam Bot", command=page_3, bg="#aaaf33", activebackground="darkolivegreen", height=3, width=17)
Button2.place(x=100, y=140)

Button3 = Button(root, text="Passworld Generator", command=page_4, bg="#aaaf33", activebackground="darkolivegreen", height=3, width=17)
Button3.place(x=100, y=230)

Button4 = Button(root, text="Clock", command=page_5, bg="#aaaf33", activebackground="darkolivegreen", height=3, width=17)
Button4.place(x=280, y=50)

mainloop()
