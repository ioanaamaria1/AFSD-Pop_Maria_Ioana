import tkinter as tk
import random
import time
from tkinter import colorchooser

width = 800
height = 400
bar_width = 30
num_bars = width // bar_width

arr = [random.randint(2, height) for _ in range(num_bars)]

root = tk.Tk()
root.title("Vizualizare Sortare prin Metoda Bulelor")

current_color="blue"

canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()


def draw_bars(color="blue"):
    canvas.delete("all")
    for i in range(num_bars):
        x1 = i * bar_width
        y1 = height - arr[i]
        x2 = (i + 1) * bar_width
        y2 = height
        canvas.create_rectangle(x1, y1, x2, y2, fill=color)


def bubble_sort():
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_bars(current_color)
                root.update()
                time.sleep(0.05)


def choose_color():
    global current_color
    color_code = colorchooser.askcolor(title="Alege Culoarea")


    if color_code[1]:
        current_color = color_code[1]  # Obținem codul hex al culorii
        draw_bars(current_color)


start_button = tk.Button(root, text="Începe Sortarea", command=bubble_sort)
start_button.pack()

color_button = tk.Button(root, text="Alege Culoarea", command=choose_color)
color_button.pack()

draw_bars(current_color)



root.mainloop()
