import tkinter as tk
  
  
class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cursor_position_print()
  
    def cursor_position_print(self):
        x = self.winfo_pointerx() - self.winfo_rootx()
        y = self.winfo_pointery() - self.winfo_rooty()
        print("Курсор находится на позиции х={} y={}".format(x, y))
        self.after(1000, self.cursor_position_print)
  
  
if __name__ == '__main__':
    main = Main()
    main.mainloop()



