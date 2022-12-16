import tkinter as tk
from tkinter.messagebox import showinfo, showerror
import time
import random


class mybutton(tk.Button):
    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(mybutton, self).__init__(master, font = 'Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
    def __repr__(self):
        return f'MyButton {self.x} {self.y} {self.number} {self.is_mine}'
class game:
    window = tk.Tk()
    row = 11
    col = 11
    IS_GAME_OVER = False
    cells_map = []
    rotation = 'w'
    head = 1
    def __init__(self):
        self.buttons = []
        for i in range (game.row+2):
            temp=[]
            for j in range (game.col+2):
                btn = mybutton(game.window, x=i, y=j, width=3)
#                btn.config(command=lambda button=btn: self.click(button))
                temp.append(btn)
            self.buttons.append(temp)


#   def click(self, clicked_button:mybutton):
#
#        if not clicked_button.is_alive:
#            clicked_button.config(background = 'black', disabledforeground ='black')
#            clicked_button.is_alive = True
#            game.surv = game.surv + 1
#                
#
#        else:
#            clicked_button.config(background = 'white', disabledforeground ='white')
#            clicked_button.is_alive = False
#            game.surv = game.surv - 1
#
#        print(clicked_button)
#        if clicked_button.is_mine:
#            clicked_button.config(text="*", background = 'red', disabledforeground ='black')
#            clicked_button.is_open = True
#            game.IS_GAME_OVER = True
#            showinfo('Game over', 'Вы проиграли')
#            for i in range(1, game.row + 1):
#                for j in range(1, game.col + 1):
#                    btn = self.buttons[i][j]
#                    if btn.is_mine:
#                        btn['text'] = '*'
#        else:
#                            
#            color = colors.get(clicked_button.count_bomb, 'black')
#            if clicked_button.count_bomb:
#                clicked_button.config(text=clicked_button.count_bomb, disabledforeground = color)
#                clicked_button.is_open = True
#            else:
#                self.breadth_first_search(clicked_button)
#        clicked_button.config(state = 'disabled')
#        clicked_button.config(relief=tk.SUNKEN)



    def create_wigets(self):


        menubar = tk.Menu(self.window)
        self.window.config(menu = menubar)

        settings_menu = tk.Menu(menubar, tearoff = 0)
        settings_menu.add_command(label = 'Начало игры', command = self.start_game)
        settings_menu.add_command(label = 'Перезагрузка', command = self.reload)
        settings_menu.add_command(label = 'Выход', command = self.window.destroy)
        menubar.add_cascade(label='Файл', menu = settings_menu)

        
        count = 1
        for i in range (1, game.row+1):
            for j in range (1, game.col+1):
                btn = self.buttons[i][j]
                btn.number = count
                btn.grid(row = i, column = j, stick = 'NWES')
                if type(game.cells_map[i][j]) is int:
                    if game.cells_map[i][j] > 0:
                        btn.config(background = 'black', disabledforeground ='black')
                count += 1
        for i in range (1, game.row+1):
           tk.Grid.rowconfigure(self.window, i, weight = 1)
        for i in range (1, game.col+1):
            tk.Grid.columnconfigure(self.window, i, weight = 1)
                


        
    def start(self):
        self.create_mapp()
        self.create_snake()
        self.create_apple()
        self.create_wigets()
        game.window.mainloop()



                    
    def print_buttons(self):
         for i in range (1, game.row+1):
            for j in range (1, game.col+1):
                btn = self.buttons[i][j]
                game.cells_map[i-1][j-1] = btn.count_neib
    def reload(self):
            [child.destroy() for child in self.window.winfo_children()]
            self.__init__()
            self.create_snake()
            self.create_apple()
            self.create_wigets()

    def start_game(self): 
                surv = False
                #self.print_buttons()
                tmp = game.cells_map
                for i in range (1, game.row+1):
                    for j in range (1, game.col+1):
                        if type(game.cells_map[i][j]) is int:
                            if game.cells_map[i][j] == game.head:
                                surv = True
                                if game.rotation == 'w':
                                    if type(game.cells_map[i-1][j]) is int:
                                        game.cells_map[i-1][j] = game.cells_map[i-1][j] + game.head + 1
                                    else:
                                        game.head = game.head + 1
                                        game.cells_map[i-1][j] = game.head + 1
                                        self.create_apple()

                                if game.rotation == 'a':
                                    if type(game.cells_map[i][j-1]) is int:
                                        game.cells_map[i][j-1] = game.cells_map[i][j-1] + game.head + 1
                                    else:
                                        game.head = game.head + 1
                                        game.cells_map[i][j-1] = game.head + 1
                                        self.create_apple()

                                if game.rotation == 's':
                                    if type(game.cells_map[i+1][j]) is int:
                                        game.cells_map[i+1][j] = game.cells_map[i+1][j] + game.head + 1
                                    else:
                                        game.head = game.head + 1
                                        game.cells_map[i+1][j] = game.head + 1
                                        self.create_apple()

                                if game.rotation == 'd':
                                    if type(game.cells_map[i][j+1]) is int:
                                        game.cells_map[i][j+1] = game.cells_map[i][j+1] + game.head + 1
                                    else:
                                        game.head = game.head + 1
                                        game.cells_map[i][j+1] = game.head + 1
                                        self.create_apple()

                print(game.cells_map)
                for i in range (1, game.row+1):
                    for j in range (1, game.col+1):
                        btn = self.buttons[i][j]
                        if type(game.cells_map[i][j]) is int:
                            if game.cells_map[i][j] > 0:
                                game.cells_map[i][j] = game.cells_map[i][j] - 1
                            if game.cells_map[i][j] > 0:
                                btn.config(background = 'black', disabledforeground ='black')
                            else:
                                btn.config(background = 'white', disabledforeground ='white')
                        else:
                            btn.config(background = 'red', disabledforeground ='red')
                print(game.cells_map)

                        

                                
#                for i in range (1, game.row+1):
#                    for j in range (1, game.col+1):
#                        btn = self.buttons[i][j]
#                        if btn.is_alive:
#                            print('1', end = ' ')
#                        else:
#                            print('0', end = ' ')
#                    print()
#                print()

                if surv == True:
                      game.window.after(1000, self.start_game)
                else:
                    for i in range (1, game.row+1):
                        for j in range (1, game.col+1):
                            btn = self.buttons[i][j]
                            btn.config(background = 'red', disabledforeground ='red')
                
    def create_mapp(self):
        for i in range(game.row+2):
            game.cells_map.append([])
            for j in range (game.col+2):
                game.cells_map[i].append(0)


    def create_snake(self):
        x = (game.col + 1) // 2
        y = (game.row + 1) // 2
        game.cells_map[x][y] = 1
        print (game.cells_map)
        print(x)
        print(y)

    def create_apple(self):
        work = False
        while work == False:
            x = random.randint(1, game.col+1)
            y = random.randint(1, game.row+1)
            if game.cells_map[x][y] == 0:
                work = True
                game.cells_map[x][y] = 'a'
        
        


def press_w(event):
        game.rotation = 'w'


def press_a(event):
        game.rotation = 'a'


def press_s(event):
        game.rotation = 's'


def press_d(event):
        game.rotation = 'd'
        

        
game.window.bind("<w>", press_w)
game.window.bind("<a>", press_a)
game.window.bind("<s>", press_s)
game.window.bind("<d>", press_d)
        
game = game()
#game.create_wigets()
game.start()
