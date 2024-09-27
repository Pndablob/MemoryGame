import time
import tkinter as tk
import tkinter.ttk as ttk
import random


class GameFrame:
    def __init__(self, master=None):
        # vars
        self.colors = [
            "#3cb371",  # green
            "#3cb371",  # green
            "#ee82ee",  # pink
            "#ee82ee",  # pink
            "#6a5acd",  # purple
            "#6a5acd",  # purple
            "#ffa500",  # yellow
            "#ffa500",  # yellow
            "#ff002b",  # red
            "#ff002b",  # red
            "#007fcb",  # blue
            "#007fcb",  # blue
            "#3c2b12",  # brown
            "#3c2b12",  # brown
            "#00ffff",  # aqua
            "#00ffff",  # aqua
        ]
        self.shuffled = []

        self.first = None
        self.second = None


        # build ui
        root = tk.Tk(master)
        root.geometry("1200x1000")
        root.title("Memory Game")
        self.GameFrame = tk.Frame(root, name="gameframe")
        self.GameFrame.configure(height=1600, width=900)
        self.GridFrame = tk.Frame(self.GameFrame, name="gridframe")
        self.GridFrame.configure(height=1600, width=900)

        # button layout
        # 1  5  9   13
        # 2  6  10  14
        # 3  7  11  15
        # 4  8  12  16
        self.button1 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(1))
        self.button1.grid(column=0, ipadx=80, ipady=80, padx=1, pady=1, row=0)
        self.button2 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(2))
        self.button2.grid(column=0, ipadx=80, ipady=80, padx=1, pady=1, row=1)
        self.button3 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(3))
        self.button3.grid(column=0, ipadx=80, ipady=80, padx=1, pady=1, row=2)
        self.button4 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(4))
        self.button4.grid(column=0, ipadx=80, ipady=80, padx=1, pady=1, row=3)
        self.button5 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(5))
        self.button5.grid(column=1, ipadx=80, ipady=80, padx=1, pady=1, row=0)
        self.button6 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(6))
        self.button6.grid(column=1, ipadx=80, ipady=80, padx=1, pady=1, row=1)
        self.button7 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(7))
        self.button7.grid(column=1, ipadx=80, ipady=80, padx=1, pady=1, row=2)
        self.button8 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(8))
        self.button8.grid(column=1, ipadx=80, ipady=80, padx=1, pady=1, row=3)
        self.button9 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(9))
        self.button9.grid(column=2, ipadx=80, ipady=80, padx=1, pady=1, row=0)
        self.button10 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(10))
        self.button10.grid(column=2, ipadx=80, ipady=80, padx=1, pady=1, row=1)
        self.button11 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(11))
        self.button11.grid(column=2, ipadx=80, ipady=80, padx=1, pady=1, row=2)
        self.button12 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(12))
        self.button12.grid(column=2, ipadx=80, ipady=80, padx=1, pady=1, row=3)
        self.button13 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(13))
        self.button13.grid(column=3, ipadx=80, ipady=80, padx=1, pady=1, row=0)
        self.button14 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(14))
        self.button14.grid(column=3, ipadx=80, ipady=80, padx=1, pady=1, row=1)
        self.button15 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(15))
        self.button15.grid(column=3, ipadx=80, ipady=80, padx=1, pady=1, row=2)
        self.button16 = tk.Button(self.GridFrame, command=lambda: self.button_clicked(16))
        self.button16.grid(column=3, ipadx=80, ipady=80, padx=1, pady=1, row=3)
        self.button_list = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9,
            self.button10,
            self.button11,
            self.button12,
            self.button13,
            self.button14,
            self.button15,
            self.button16,
        ]

        self.GridFrame.grid(column=0, row=1)
        self.TitleFrame = tk.Frame(self.GameFrame, name="titleframe")
        self.Title = tk.Label(self.TitleFrame, name="title")
        self.Title.configure(text='label2')
        self.Title.pack(pady=40, side="top")
        self.TitleFrame.grid(column=0, row=0)
        self.ScoreFrame = tk.Frame(self.GameFrame, name="scoreframe")
        self.Score = tk.Label(self.ScoreFrame, name="score")
        self.Score.configure(text='label3')
        self.Score.pack(pady=10, side="top")
        self.LowestScore = tk.Label(self.ScoreFrame, name="lowestscore")
        self.LowestScore.configure(text='label4')
        self.LowestScore.pack(pady=10, side="top")
        self.ScoreFrame.grid(column=0, pady=40, row=2)
        self.GameFrame.pack(side="top")

        # Main widget
        self.mainwindow = root

        self.reset()
        self.shuffle()

    def run(self):
        self.mainwindow.mainloop()

    def shuffle(self):
        self.shuffled = random.sample(range(16), 16)

    def show_color(self, b: int):
        self.button_list[b - 1].configure(background=self.colors[self.shuffled[b - 1]])
        print(f"changing color for button {b} to {self.colors[self.shuffled[b-1]]}")

    def clear_color(self, b: int):
        self.button_list[b - 1].configure(background='white')
        print(f"clearing color for button {b}")

    def enable_button(self, b: int):
        self.button_list[b-1].configure(state='normal')
        print(f"enabling button {b}")

    def reset(self):
        for i in range(16):
            self.button_list[i].configure(background='white', state='normal')

    def check_match(self, b1, b2) -> bool:
        if b1 is None or b2 is None:
            return False

        self.first = None
        self.second = None

        if self.colors[self.shuffled[b1-1]] == self.colors[self.shuffled[b2-1]]:
            return True
        else:
            self.clear_color(b1)
            self.enable_button(b1)
            self.clear_color(b2)
            self.enable_button(b2)

            return False

    def button_clicked(self, b: int):
        if self.first is None:
            self.first = b
            self.show_color(b)
        elif self.second is None:
            self.second = b
            self.show_color(b)

        self.button_list[b - 1].configure(state='disabled')

        self.check_match(self.first, self.second)

        print(f"button {b} clicked")


if __name__ == "__main__":
    app = GameFrame()
    app.run()
