import tkinter

class KortBetaling1:
    def __init__(self):
        
        self.vindu = tkinter.Tk()
        self.vindu.title("PCI- terminal")

        

        self.display_Frame = tkinter.Frame(self.vindu)
        self.display_Frame.grid(column=0, row=1)

        self.buttons_Frame = tkinter.Frame(self.vindu)
        self.buttons_Frame.grid(column=0, row=2)

        
        self.fonten = ("Arial", 14)

        self.title_Label = tkinter.Label(self.vindu, text="Bankterminal", font=self.fonten)
        self.title_Label.grid(column=0, row=0)

    #DISPLAY FRAME:
        self.display_Label = tkinter.Label(self.display_Frame, text="125,59kr", font=self.fonten)
        self.display_Label.grid(column=0, row=0)


    #BUTTONS FRAME:

        x_margin = 5
        y_margin = 5
        x_padding = 20
        y_padding = 10

        tupple_y_margin = (10, 100)
        tupple_x_margin = (50, 10)

        rectangle_padding = 35

        self.numenButton = tkinter.Button(self.buttons_Frame, text="1", width=2, command=lambda: self.numpad("1"), background="#222", fg="#fff", font=self.fonten)
        self.numtoButton = tkinter.Button(self.buttons_Frame, text="2", width=2, command=lambda: self.numpad("2"), background="#222", fg="#fff", font=self.fonten)
        self.numtreButton = tkinter.Button(self.buttons_Frame, text="3", width=2, command=lambda: self.numpad("3"), background="#222", fg="#fff", font=self.fonten)

        self.numfireButton = tkinter.Button(self.buttons_Frame, text="4", width=2, command=lambda: self.numpad("4"), background="#222", fg="#fff", font=self.fonten)
        self.numfemButton = tkinter.Button(self.buttons_Frame, text="5", width=2, command=lambda: self.numpad("5"), background="#222", fg="#fff", font=self.fonten)
        self.numseksButton = tkinter.Button(self.buttons_Frame, text="6", width=2, command=lambda: self.numpad("6"), background="#222", fg="#fff", font=self.fonten)

        self.numsyvButton = tkinter.Button(self.buttons_Frame, text="7", width=2, command=lambda: self.numpad("7"), background="#222", fg="#fff", font=self.fonten)
        self.numotteButton = tkinter.Button(self.buttons_Frame, text="8", width=2, command=lambda: self.numpad("8"), background="#222", fg="#fff", font=self.fonten)
        self.numniButton = tkinter.Button(self.buttons_Frame, text="9", width=2, command=lambda: self.numpad("9"), background="#222", fg="#fff", font=self.fonten)
        
        self.numnullButton = tkinter.Button(self.buttons_Frame, text="O", width=2, command=lambda: self.numpad("0"), background="#222", fg="#fff", font=self.fonten)
        self.numnull_nullButton = tkinter.Button(self.buttons_Frame, text="0", width=2, command=lambda: self.numpad("00"), background="#222", fg="#fff", font=self.fonten)
        self.numkommaButton = tkinter.Button(self.buttons_Frame, text="#", width=2, command=lambda: self.numpad("."), background="#222", fg="#fff", font=self.fonten)

        self.redButton = tkinter.Button(self.buttons_Frame, text="X", width=2, command=lambda: self.numpad("0"), background="#d60000", fg="#960000", font=self.fonten)
        self.yellowButton = tkinter.Button(self.buttons_Frame, text="<-", width=2, command=lambda: self.numpad("00"), background="#fff23d", fg="#bfb532", font=self.fonten)
        self.greenButton = tkinter.Button(self.buttons_Frame, text="O", width=2, command=lambda: self.numpad("."), background="#00d916", fg="#029c11", font=self.fonten)

        
        row = 0
        self.numenButton.grid(column=0, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numtoButton.grid(column=1, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numtreButton.grid(column=2, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        row += 1
        self.numfireButton.grid(column=0, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numfemButton.grid(column=1, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numseksButton.grid(column=2, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        row += 1
        self.numsyvButton.grid(column=0, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numotteButton.grid(column=1, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numniButton.grid(column=2, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        row += 1
        self.numnullButton.grid(column=0, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numnull_nullButton.grid(column=1, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numkommaButton.grid(column=2, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        row += 1
        self.redButton.grid(column=0, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.yellowButton.grid(column=1, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.greenButton.grid(column=2, row=row, ipadx=20, ipady=10, padx=5, pady=5)



        tkinter.mainloop()

    def gjorIngenting(self):
        pass

    def numpad(self, num):
        pass

if __name__ == '__main__':
    kortterminal = KortBetaling()
    