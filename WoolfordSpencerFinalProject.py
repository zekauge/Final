"""Burger making game, increases in speed for every order you complete, trust me it is NOT 10 minutes. Use numbers for each ingredient if you want to go as fast as you can.

Spencer Woolford

Last modified 3-10-2024

WoolfordSpencerFinalProject.py

Python version = 3.12

"""


import tkinter as tk
import random

#just global variables
current_rectangle = 0
order = [] #stores current order
time_left = 600  #time left in seconds
completed_orders = 0  #counts completed orders

#just a dictionary, lets the colors chosen actuallY be the ingredients
ingredient_colors = {
    "lemon chiffon": "Mayo",
    "gold": "Mustard",
    "red3": "Ketchup",
    "chartreuse3": "Lettuce",
    "medium violet red": "Onions",
    "sienna4": "Burger",
    "olive drab": "Pickle",
    "orange2": "Cheese",
    "brown4": "Bacon",
    "indian red": "Tomato"
}

#rectangles for canvas
def create_rectangle(canvas, x, y, width, height, **kwargs):
    return canvas.create_rectangle(x - width/3, y - height/3, x + width/3, y + height/2, **kwargs)

#top bun (maverick like the movie) 
def create_top_bun(canvas, x, y, r, **kwargs):
    return canvas.create_arc(x - r/1.5, y - r/1.5, x + r/1.5, y + r/2, start=0, extent=180, **kwargs)

#colors for the ingredients
def mayo():
    canvas.itemconfig(rectangles[current_rectangle], fill="lemon chiffon")

def mustard():
    canvas.itemconfig(rectangles[current_rectangle], fill="gold")

def ketchup():
    canvas.itemconfig(rectangles[current_rectangle], fill="red3")

def lettuce():
    canvas.itemconfig(rectangles[current_rectangle], fill="chartreuse3")

def onion():
    canvas.itemconfig(rectangles[current_rectangle], fill="medium violet red")

def burger():
    canvas.itemconfig(rectangles[current_rectangle], fill="sienna4")

def pickle():
    canvas.itemconfig(rectangles[current_rectangle], fill="olive drab")

def cheese():
    canvas.itemconfig(rectangles[current_rectangle], fill="orange2")

def bacon():
    canvas.itemconfig(rectangles[current_rectangle], fill="brown4")

def tomato():
    canvas.itemconfig(rectangles[current_rectangle], fill="indian red")

#records key presses for if you use numpad/numbers
def select_ingredient(event, color):
    canvas.itemconfig(rectangles[current_rectangle], fill=color)

#lets you select, making you go up or down based off of which variant of controls you use
def move_up(event=None):
    global current_rectangle
    current_rectangle = (current_rectangle - 1) % len(rectangles)
    highlights_selection()

def move_down(event=None):
    global current_rectangle
    current_rectangle = (current_rectangle + 1) % len(rectangles)
    highlights_selection()

#highlights your current selection
def highlights_selection():
    for i, rectangle in enumerate(rectangles):
        if i == current_rectangle:
            canvas.itemconfig(rectangle, outline="black", width=4)
        else:
            canvas.itemconfig(rectangle, outline="", width=2)

#submitting order function, determines if the order you input is the correct one
def submit_order():
    global completed_orders
    user_ingredients = [ingredient_colors[canvas.itemcget(rectangle, "fill")] for rectangle in rectangles if canvas.itemcget(rectangle, "fill") != "gray63"]
    if user_ingredients == order:
        completed_orders += 1
        result_label.config(text="Your order is correct! Next :)")
        generate_order()
        start_game() #starts another order
    else:
        result_label.config(text="WRONG ORDER TRY AGAIN")


#updates/multiplies displayed timer for difficulty
def update_timer():
    global time_left
    time_left -= 1
    timer_label.config(text=f"{time_left//60}:{time_left%60:02d}")  #updates the timer label with the new time
    if time_left > 0:
        root.after(1000, update_timer)
    else:
        end_game()

#displays score at game over
def end_game():
    result_label.config(text=f"Time moves fast huh, You finsihed: {completed_orders}")

#starts game and creates window
def start_game():
    global order
    order = generate_order()
    order_window = tk.Toplevel(root)
    order_window.title("Order")
    order_window.geometry("300x300")

    #tells you your order
    order_label = tk.Label(order_window, text="Hello I'd like this on my burger:")
    order_label.pack(pady=10)

    for ingredient in order:
        ingredient_label = tk.Label(order_window, text=ingredient)
        ingredient_label.pack()

    #timer in order window
    global timer_label
    timer_label = tk.Label(order_window, text="1:00")
    timer_label.pack(side=tk.BOTTOM, pady=10)  # Adjust position as needed

    global result_label
    result_label = tk.Label(order_window, text="")
    result_label.pack()

    update_timer()


#random order generation
def generate_order():
    ingredients = ["Mustard", "Ketchup", "Mayo", "Lettuce", "Onions", "Burger", "Pickle", "Cheese", "Bacon", "Tomato"]
    new_order = random.sample(ingredients, 6)
    return new_order

#just main
def main():
    global root, canvas, rectangles, current_rectangle
    root = tk.Tk()
    root.title("Main Window")
    root.minsize(width=800, height=700)
    current_rectangle = 0

    #frame for buttons on right side
    button_frame_right = tk.Frame(root)
    button_frame_right.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10, pady=10)

    #buttons for the chef (ingredients)
    button1 = tk.Button(button_frame_right, text="Mustard",  command=mustard)
    button1.pack(side=tk.TOP)
    button2 = tk.Button(button_frame_right, text="Ketchup", command=ketchup)
    button2.pack(side=tk.TOP)
    button3 = tk.Button(button_frame_right, text="Mayo", command=mayo)
    button3.pack(side=tk.TOP)
    button4 = tk.Button(button_frame_right, text="Lettuce", command=lettuce)
    button4.pack(side=tk.TOP)
    button5 = tk.Button(button_frame_right, text="Onions", command=onion)
    button5.pack(side=tk.TOP)
    button6 = tk.Button(button_frame_right, text="Burger", command=burger)
    button6.pack(side=tk.TOP)
    button7 = tk.Button(button_frame_right, text="Pickle", command=pickle)
    button7.pack(side=tk.TOP)
    button8 = tk.Button(button_frame_right, text="Cheese", command=cheese)
    button8.pack(side=tk.TOP)
    button9 = tk.Button(button_frame_right, text="Bacon", command=bacon)
    button9.pack(side=tk.TOP)
    button10 = tk.Button(button_frame_right, text="Tomato", command=tomato)
    button10.pack(side=tk.TOP)

    #exit button
    exit_button = tk.Button(button_frame_right, text="Exit", bg="red", command=root.destroy)
    exit_button.pack(side=tk.BOTTOM, pady=10)

    #submit button
    submit_button = tk.Button(button_frame_right, text="Submit", bg="lightblue", command=submit_order)
    submit_button.pack(side=tk.TOP, pady=10)

    #canvas to show borger
    canvas = tk.Canvas(root, width=500, height=1000, borderwidth=10, relief=tk.GROOVE)
    canvas.pack(expand=True, side=tk.LEFT)

    #top bun (maverick (again yes i made the reference to the movie haha funny))
    create_top_bun(canvas, 260, 237, 100, fill="chocolate1", outline="black")

    #bottom bun
    create_rectangle(canvas, 260, 720, 200, 50, fill="chocolate1", outline="black")

    #just keybinds, configurable if you'd like to change it
    root.bind("<w>", move_up)
    root.bind("<s>", move_down)
    root.bind("<Up>", move_up)
    root.bind("<Down>", move_down)

    #dont configure this though, unless you know what you're doing. this adds a "learning curve" so if you learn all of the ingredients you can go faster or a higher score YES I ADDED A META
    root.bind("1", lambda event: select_ingredient(event, "lemon chiffon"))  # Mayo
    root.bind("2", lambda event: select_ingredient(event, "gold"))  # Mustard
    root.bind("3", lambda event: select_ingredient(event, "red3"))  # Ketchup
    root.bind("4", lambda event: select_ingredient(event, "chartreuse3"))  # Lettuce
    root.bind("5", lambda event: select_ingredient(event, "medium violet red"))  # Onions
    root.bind("6", lambda event: select_ingredient(event, "sienna4"))  # Burger
    root.bind("7", lambda event: select_ingredient(event, "olive drab"))  # Pickle
    root.bind("8", lambda event: select_ingredient(event, "orange2"))  # Cheese
    root.bind("9", lambda event: select_ingredient(event, "brown4"))  # Bacon
    root.bind("0", lambda event: select_ingredient(event, "indian red"))  # Tomato

    #rectangles for ingredients
    rectangles = []
    vertical_offset = 80
    for i in range(6):
        rectangles.append(create_rectangle(canvas, 260, 260 + i * vertical_offset, 200, 80, fill="gray63", outline=""))

    #highlights
    highlights_selection()

    #starts the game
    start_game()

    root.mainloop()

if __name__ == "__main__":
    main()
