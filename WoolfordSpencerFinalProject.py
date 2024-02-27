"""WARNING: THIS DOES NOT HAVE A TERMINATION YET, from what I know you have to end the program by either closing your text editor or ending the task in task mnanager

This tkinter code is a little burger making game that will right now, lets you customize a burger with condiments
Controls are the up and down arrow keys and "w" and "s"

Spencer Woolford

Last modified 2-26-2024

WoolfordSpencerFinalProject.py

Python version = 3.12

"""


import tkinter as tk

#list of almost everything in the canvas currently and how they are manipulable


#rectangles for the ingredients
def create_rectangle(canvas, x, y, width, height, **kwargs):
    return canvas.create_rectangle(x - width/3, y - height/3, x + width/3, y + height/2, **kwargs)
#creates bun in canvas
def create_top_bun(canvas, x, y, r, **kwargs):
    return canvas.create_arc(x - r/1.5, y - r/1.5, x + r/1.5, y + r/2, start=0, extent=180, **kwargs)
#Converts rectangle color into the color for mayo
def mayo():
    canvas.itemconfig(rectangles[current_rectangle], fill="lemon chiffon")

#Converts rectangle color into the color for mustard
def mustard():
    canvas.itemconfig(rectangles[current_rectangle], fill="gold")

#Converts rectangle color into the color for ketchup
def ketchup():
    canvas.itemconfig(rectangles[current_rectangle], fill="red3")

#Converts rectangle color into the color for lettuce
def lettuce():
    canvas.itemconfig(rectangles[current_rectangle], fill="chartreuse3")

#Converts rectangle color into the color for onion
def onion():
    canvas.itemconfig(rectangles[current_rectangle], fill="medium violet red")

#Converts rectangle color into the color for burger
def burger():
    canvas.itemconfig(rectangles[current_rectangle], fill="sienna4")

    #Converts rectangle color into the color for pickle
def pickle():
    canvas.itemconfig(rectangles[current_rectangle], fill="olive drab")

#Converts rectangle color into the color for cheese
def cheese():
    canvas.itemconfig(rectangles[current_rectangle], fill="orange2")

#Converts rectangle color into the color for bacon
def bacon():
    canvas.itemconfig(rectangles[current_rectangle], fill="brown4")

#Converts rectangle color into the color for tomato
def tomato():
    canvas.itemconfig(rectangles[current_rectangle], fill="indian red")


#The events that let you move up and down in the game, consisting of up and down arrows and w and s for gamers
    
#Moves up one selectable rectangle
def move_up(event=None):
    global current_rectangle
    current_rectangle = (current_rectangle - 1) % len(rectangles)
    highlights_selection()


#Moves down one selectable rectangle
def move_down(event=None):
    global current_rectangle
    current_rectangle = (current_rectangle + 1) % len(rectangles)
    highlights_selection()

#Highlight the the current section of the burger you're hover over

def highlights_selection():
    for i, rectangle in enumerate(rectangles):
        if i == current_rectangle:
            canvas.itemconfig(rectangle, outline="black", width=4)
        else:
            canvas.itemconfig(rectangle, outline="", width=2)

#Starts with what will be the main menu with more buttons
            
def open_main_menu():
    root.withdraw()  # Hide the main window
    main_menu = tk.Toplevel(root)
    main_menu.title("Main menu")
    main_menu.geometry("800x1500")
    main(main_menu)

#Main 

def main(root):
    global canvas, rectangles, current_rectangle
    root.title("Borger master 3000")
    root.minsize
    current_rectangle = 0

    #creates frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.TOP, anchor=tk.N, padx=10, pady=10)

    #creates buttons with labels and commands
    button1 = tk.Button(button_frame, text="Mustard", command=mustard)
    button1.pack(side=tk.TOP)
    button2 = tk.Button(button_frame, text="Ketchup", command=ketchup)
    button2.pack(side=tk.TOP)
    button3 = tk.Button(button_frame, text="Mayo", command=mayo)
    button3.pack(side=tk.TOP)
    button4 = tk.Button(button_frame, text="Lettuce", command=lettuce)
    button4.pack(side=tk.TOP)
    button5 = tk.Button(button_frame, text="Onions", command=onion)
    button5.pack(side=tk.TOP)
    button6 = tk.Button(button_frame, text="Borger", command=burger)
    button6.pack(side=tk.TOP)
    button7 = tk.Button(button_frame, text="Pickle", command=pickle)
    button7.pack(side=tk.TOP)
    button8 = tk.Button(button_frame, text="Cheese", command=cheese)
    button8.pack(side=tk.TOP)
    button9 = tk.Button(button_frame, text="Bacon", command=bacon)
    button9.pack(side=tk.TOP)
    button10 = tk.Button(button_frame, text="Tomato", command=tomato)
    button10.pack(side=tk.TOP)

    #create canvas for the buttons to work
    canvas = tk.Canvas(root, width=500, height=1000, borderwidth=10, relief=tk.GROOVE)
    canvas.pack(expand=True)

    #places "top bun" in the canvas
    create_top_bun(canvas, 260, 237, 100, fill="chocolate1", outline="black")

    #places "bottom bun" in the canvas
    create_rectangle(canvas, 260, 720, 200, 50, fill="chocolate1", outline="black")

    #keybinds for game, binds the move ups and move downs to the keystrokes
    root.bind("<w>", move_up)
    root.bind("<s>", move_down)
    root.bind("<Up>", move_up)
    root.bind("<Down>", move_down)

    #creates rectangles where you "put" the ingredients
    rectangles = []
    vertical_offset = 80
    for i in range(6):
        rectangles.append(create_rectangle(canvas, 260, 260 + i * vertical_offset, 200, 80, fill="gray63", outline=""))

    #highlights. duh
    highlights_selection()

if __name__ == "__main__":
    
    #main menu
    root = tk.Tk()
    root.title("Main Window")

    button = tk.Button(root, text="Play :)", command=open_main_menu)
    button.pack(pady=20)

    root.mainloop()














#Please. if you see anything wrong help me i was and still am losing my mind
