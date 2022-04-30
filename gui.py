import tkinter as tk
from random import randint
import os, multi, threading
import multi
from time import sleep


GLOW = 0
FLASH = 0
TRIGGER = 0
config = open('config.md', 'r')
HASH = config.readline()
GLOW = int(config.readline())
FLASH = int(config.readline())
TRIGGER = int(config.readline())
config.close()

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


photo = resource_path('resource/vdk45.png')

window = tk.Tk()
bg_color = '#A0ACB0'
height = 250
weight = 450
photo = tk.PhotoImage(file=photo)
window.iconphoto(False, photo)
window.config(bg=bg_color)
window.title("Option:")
# Высота х ширина + (отступ по x+100) + (отступ по y+100)
window.geometry(f"{height}x{weight}+100+100")
window.minsize(250, 600)
window.maxsize(500, 600)
window.resizable(False, False)



label_1 = tk.Label(window, text="""Enter evry thing 
more 10 symboles!""",
                   bg="#A0ACB0",
                   fg="black",
                   font=("Arial", 12, "bold"),
                   padx=15,  # Отступ текста от крайя по х
                   pady=5,  # Отступ текста от крайя по y
                   width=15,  # Ширина блока в символах
                   height=2,  # Высота блока в символах
                   anchor="center",  # n, ne, e, se, s, sw, w, nw, or center,
                   relief=tk.RAISED,  # Рамка вокруг блока
                   bd=5,  # Ширина рамки
                   justify=tk.RIGHT  # Выровнять тексты по правой стороне

                   )
label_1.place(x=25, y=15)  # Отобразить   # Отобразить 


edit = tk.Entry(window, width = 28)
edit.place(x=35, y=85)


def close_start():
    ed = edit.get()
    file = open('config.md', 'w', encoding="utf-8")
    file.write(ed)
    file.write(f"\n{GLOW}") 
    file.write(f"\n{FLASH}") 
    file.write(f"\n{TRIGGER}") 
    file.close()
    if len(ed) > 10:
        thread_2 = threading.Thread(target=multi.main, args=())
        thread_2.start()
        window.destroy()
    else:
        print("Need more 10 symboles")


button_2 = tk.Button(window, text="Start",
                     command=close_start,
                     bg="#EFCFCF",
                     fg="black",
                     font=("Arial", 8, "bold"),
                     padx=15,
                     pady=5,
                     width=15,
                     height=1,
                     anchor="n",
                     relief=tk.RAISED,
                     bd=10,
                     justify=tk.RIGHT
                     )
button_2.place(x=45, y=120)


def flash_on():
    global FLASH
    FLASH = 1
    label_2.config(text = "Flash: ON")
    label_2.config(bg = "#5CD78D")
    

button_3 = tk.Button(window, text="""Flash: ON""",
                    command=flash_on,
                    bg="#5CD78D",
                    fg="black",
                    font=("Arial", 8, "bold"),
                    padx=5,  
                    pady=5,  
                    width=10,  
                    height=1,  
                    anchor="center",  
                    relief=tk.RAISED,  
                    bd=10,  
                    justify=tk.RIGHT 
                     )
button_3.place(x=15, y=190)


def flash_off():
    global FLASH
    FLASH = 0
    label_2.config(text = "Flash: OFF")
    label_2.config(bg = "#E17E7E")
    

button_4 = tk.Button(window, text="""Flash: OFF""",
                    command=flash_off,
                    bg="#E17E7E",
                    fg="black",
                    font=("Arial", 8, "bold"),
                    padx=5,  
                    pady=5,  
                    width=10,  
                    height=1,  
                    anchor="center",  
                    relief=tk.RAISED,  
                    bd=10,  
                    justify=tk.RIGHT 
                     )
button_4.place(x=135, y=190)


def text_label_2():
    if int(FLASH) == 0:
        return ["OFF", "#E17E7E"]
    else:
        return ["ON", "#5CD78D"]


label_2 = tk.Label(window, text=f"""Flash: {text_label_2()[0]}""",
                    bg=text_label_2()[1],
                    fg="black",
                    font=("Arial", 12, "bold"),
                    padx=15,  # Отступ текста от крайя по х
                    pady=5,  # Отступ текста от крайя по y
                    width=15,  # Ширина блока в символах
                    height=1,  # Высота блока в символах
                    anchor="center",  # n, ne, e, se, s, sw, w, nw, or center,
                    relief=tk.RAISED,  # Рамка вокруг блока
                    bd=10,  # Ширина рамки
                    justify=tk.RIGHT  # Выровнять тексты по правой стороне
                    )
label_2.place(x=25, y=250)  # Отобразить  


def glow_on():
    global GLOW
    GLOW = 1
    label_3.config(text = "Glow: ON")
    label_3.config(bg = "#5CD78D")
    

button_5 = tk.Button(window, text="""Glow: ON""",
                    command=glow_on,
                    bg="#5CD78D",
                    fg="black",
                    font=("Arial", 8, "bold"),
                    padx=5,  
                    pady=5,  
                    width=10,  
                    height=1,  
                    anchor="center",  
                    relief=tk.RAISED,  
                    bd=10,  
                    justify=tk.RIGHT 
                     )
button_5.place(x=15, y=320)


def glow_off():
    global GLOW
    GLOW = 0
    label_3.config(text = "Glow: OFF")
    label_3.config(bg = "#E17E7E")
    

button_6 = tk.Button(window, text="""Glow: OFF""",
                    command=glow_off,
                    bg="#E17E7E",
                    fg="black",
                    font=("Arial", 8, "bold"),
                    padx=5,  
                    pady=5,  
                    width=10,  
                    height=1,  
                    anchor="center",  
                    relief=tk.RAISED,  
                    bd=10,  
                    justify=tk.RIGHT 
                     )
button_6.place(x=135, y=320)


def text_label_3():
    if int(GLOW) == 0:
        return ["OFF", "#E17E7E"]
    else:
        return ["ON", "#5CD78D"]


label_3 = tk.Label(window, text=f"""Glow: {text_label_3()[0]}""",
                    bg=text_label_3()[1],
                    fg="black",
                    font=("Arial", 12, "bold"),
                    padx=15,  # Отступ текста от крайя по х
                    pady=5,  # Отступ текста от крайя по y
                    width=15,  # Ширина блока в символах
                    height=1,  # Высота блока в символах
                    anchor="center",  # n, ne, e, se, s, sw, w, nw, or center,
                    relief=tk.RAISED,  # Рамка вокруг блока
                    bd=10,  # Ширина рамки
                    justify=tk.RIGHT  # Выровнять тексты по правой стороне
                    )
label_3.place(x=25, y=380)  # Отобразить  

## ---------------------------
def trigger_on():
    global TRIGGER
    TRIGGER = 1
    label_4.config(text = "Trigger: ON")
    label_4.config(bg = "#5CD78D")
    

button_7 = tk.Button(window, text="""Trigger: ON""",
                    command=trigger_on,
                    bg="#5CD78D",
                    fg="black",
                    font=("Arial", 8, "bold"),
                    padx=5,  
                    pady=5,  
                    width=10,  
                    height=1,  
                    anchor="center",  
                    relief=tk.RAISED,  
                    bd=10,  
                    justify=tk.RIGHT 
                     )
button_7.place(x=15, y=460)


def trigger_off():
    global TRIGGER
    TRIGGER = 0
    label_4.config(text = "Trigger: OFF")
    label_4.config(bg = "#E17E7E")
    

button_8 = tk.Button(window, text="""Trigger: OFF""",
                    command=trigger_off,
                    bg="#E17E7E",
                    fg="black",
                    font=("Arial", 8, "bold"),
                    padx=5,  
                    pady=5,  
                    width=10,  
                    height=1,  
                    anchor="center",  
                    relief=tk.RAISED,  
                    bd=10,  
                    justify=tk.RIGHT 
                     )
button_8.place(x=135, y=460)


def text_label_4():
    if int(TRIGGER) == 0:
        return ["OFF", "#E17E7E"]
    else:
        return ["ON", "#5CD78D"]


label_4 = tk.Label(window, text=f"""Trigger: {text_label_3()[0]}""",
                    bg=text_label_4()[1],
                    fg="black",
                    font=("Arial", 12, "bold"),
                    padx=15,  # Отступ текста от крайя по х
                    pady=5,  # Отступ текста от крайя по y
                    width=15,  # Ширина блока в символах
                    height=1,  # Высота блока в символах
                    anchor="center",  # n, ne, e, se, s, sw, w, nw, or center,
                    relief=tk.RAISED,  # Рамка вокруг блока
                    bd=10,  # Ширина рамки
                    justify=tk.RIGHT  # Выровнять тексты по правой стороне
                    )
label_4.place(x=25, y=520)  # Отобразить  


if __name__ == "__main__":
    window.mainloop()
    
