from tkinter import *
from itertools import product
from Checkers import *


class Menu(Frame):
    '''Class for creating the menu.'''

    def __init__(self):
        Frame.__init__(self)
        self.menuFrame = Frame(width=240, height=80)
        self.menuFrame.pack(expand=1, fill=BOTH, side=TOP)
        self.menuFrame.pack_propagate(0)
        self.button1 = Button(self.menuFrame, text="Play!", font=("Helvetica", "10", "bold"), width=13, height=2,
                              command=board.start_game, cursor="heart", relief=RIDGE,)
        self.button1.pack()
        self.button2 = Button(self.menuFrame, text="Settings", font=("Helvetica", "10", "bold"), width=13, height=2,
                              command=board.show_settings, relief=RIDGE,)
        self.button2.pack()
        self.button3 = Button(self.menuFrame, text="Highscore", font=("Helvetica", "10", "bold"), width=13, height=2,
                              command=board.show_high_score, relief=RIDGE,)
        self.button3.pack()
        self.button4 = Button(self.menuFrame, text="Exit", font=("Helvetica", "10", "bold"), width=13, height=2,
                              command=board.game_exit, cursor="pirate", relief=RIDGE,)
        self.button4.pack()

        self.settingsFrame = Frame(width=220, height=100)

        self.labelNames1 = Label(self.settingsFrame, text="Player Names", font="bold", relief=RIDGE)
        self.labelNames1.grid(row=0, column=1, sticky=W)
        self.labelNames2 = Label(self.settingsFrame, text="Player 1", font="bold")
        self.labelNames2.grid(row=1, column=0, sticky=W)
        self.labelNames3 = Label(self.settingsFrame, text="Player 2", font="bold")
        self.labelNames3.grid(row=2, column=0, sticky=W)
        self.nameEntry1 = Entry(self.settingsFrame, width=12)
        self.nameEntry1.grid(row=1, column=1, sticky=W)
        self.nameEntry1.rowconfigure(1, pad=2)
        self.nameEntry2 = Entry(self.settingsFrame, width=12)
        self.nameEntry2.grid(row=2, column=1, sticky=W)
        self.nameEntry1.rowconfigure(2, pad=2)

        self.settingsFrame.pack_forget()

        self.mode = IntVar()

        self.labelMode = Label(self.settingsFrame, text="Game Mode", font="bold", relief=RIDGE)
        self.labelMode.grid(row=5, column=1, sticky=W)
        self.radioButtonMode1 = Radiobutton(self.settingsFrame, text="Player vs Player", variable=self.mode, value=1)
        self.radioButtonMode1.grid(row=6, column=1, sticky=W)
        self.radioButtonMode2 = Radiobutton(self.settingsFrame, text="Player vs AI", variable=self.mode, value=2)
        self.radioButtonMode2.grid(row=7, column=1, sticky=W)

        self.board_size_ = IntVar()

        self.labelSize = Label(self.settingsFrame, text="Board Size", font="bold", relief=RIDGE)
        self.labelSize.grid(row=9, column=1, sticky=W)
        self.radioButtonSize1 = Radiobutton(self.settingsFrame, text="8x8", variable=self.board_size_, value=8)
        self.radioButtonSize1.grid(row=10, column=1, sticky=W)
        self.radioButtonSize2 = Radiobutton(self.settingsFrame, text="10x10", variable=self.board_size_, value=10)
        self.radioButtonSize2.grid(row=11, column=1, sticky=W)

        self.piece_color = IntVar()

        self.labelColor = Label(self.settingsFrame, text="Piece Color", font="bold", relief=RIDGE)
        self.labelColor.grid(row=12, column=1, sticky=W)
        self.radioButtonColor1 = Radiobutton(self.settingsFrame, text="Red and Black",
                                             variable=self.piece_color, value=1)
        self.radioButtonColor1.grid(row=13, column=1, sticky=W)
        self.radioButtonColor2 = Radiobutton(self.settingsFrame, text="Gray and Black",
                                             variable=self.piece_color, value=2)
        self.radioButtonColor2.grid(row=14, column=1, sticky=W)
        self.radioButtonColor3 = Radiobutton(self.settingsFrame, text="White and Black",
                                             variable=self.piece_color, value=3)
        self.radioButtonColor3.grid(row=15, column=1, sticky=W)
        self.radioButtonColor4 = Radiobutton(self.settingsFrame, text="Turquoise and Green",
                                             variable=self.piece_color, value=4)
        self.radioButtonColor4.grid(row=16, column=1, sticky=W)