import tkinter as tk
import random
import time
from tkinter import colorchooser


width = 800
height = 400
bar_width = 40
num_bars = width // bar_width


arr = [random.randint(2, height) for _ in range(num_bars)]

root = tk.Tk()
root.title("SelectionSortttt")


current_color = "blue"

canvas = tk.Canvas(root, width=width, height=height, bg="gray")
canvas.pack()


def draw_bars(color="blue", highlight=None):
    canvas.delete("all")
    for i in range(num_bars):
        x1 = i * bar_width
        y1 = height - arr[i]
        x2 = (i + 1) * bar_width
        y2 = height
        fill_color = color
        if highlight and i in highlight:
            fill_color = "red"
        canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
    root.update()


def SelectionSort():

    size = len(arr)
    for i in range(size):
        min_index = i

        for j in range(i + 1, size):
            draw_bars(current_color, highlight=(min_index, j))
            time.sleep(0.1)

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        draw_bars(current_color)
        time.sleep(0.1)

    draw_bars("red")


def choose_color():
    global current_color
    color_code = colorchooser.askcolor(title="Alege Culoarea")
    if color_code[1]:
        current_color = color_code[1]
        draw_bars(current_color)


start_button = tk.Button(root, text="Începe Sortarea", command=SelectionSort)
start_button.pack()

color_button = tk.Button(root, text="Alege Culoarea", command=choose_color)
color_button.pack()


draw_bars(current_color)


root.mainloop()
