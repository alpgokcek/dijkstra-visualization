from tkinter import *

black = (0, 0, 0)
white = (255, 255, 255)
radius = 0


def calculate_radius():
    global radius
    radius = 50 + (int(number_of_elements.get())) / int(number_of_elements.get())


def add_vertex(data, x1, y1):
    try:
        x2, y2 = (x1 + radius), (y1 + radius)
        canvas.create_oval(x1, y1, x2, y2, fill="#FFF", outline="black")
        canvas.create_text(x1 + radius // 2, y1 + radius // 2, text=str(data))

    except Exception as e:
        print(e)


def add_v_edge(x1, x2, y1, y2):
    try:
        x1 = x2 = x1 + radius / 2
        y1 = y1 + radius
        canvas.create_line(x1, y1, x2, y2, fill="#000")

    except Exception as e:
        print(e)


def add_h_edge(x1, x2, y1, y2, pos=2):  # pos = 1: only upper edge; else both edge
    try:
        canvas.create_line(x1 - (2 * radius), y1 + radius // 2, x1, y1 + radius // 2, fill="#000")
        if pos != 1:
            canvas.create_line(x2 - (2 * radius), y2 + radius // 2, x2, y2 + radius // 2, fill="#000")

    except Exception as e:
        print(e)


def add_d_edge(x1, y1, pos=2):  # pos = 1: only upper edge; else both edge
    gap = (radius * pow(2, 0.5)) - radius
    xp = yp = gap / pow(2, 0.5)

    print("gap ", gap)
    print("xp ", xp)
    print("yp ", yp)
    try:
        canvas.create_line(x1 - (2 * radius) - xp / 2, (y1 + 3 * radius) + yp / 2, x1 + xp / 2, y1 + (radius) - yp / 2,
                           fill="#000")
        if pos != 1:
            canvas.create_line(x1 - (2 * radius) - xp / 2, y1 + (radius) - yp / 2, x1 + xp / 2, (y1 + 3 * radius) + yp /2, fill="#000")


    except Exception as e:
        print(e)


def runProgram():
    canvas.delete("all")
    calculate_radius()
    noe = int(number_of_elements.get())
    x1 = x2 = 100
    counter = 1
    y1, y2 = (500 - 7 * radius), (500 - 7 * radius) + (radius * 3)
    for i in range(noe // 2):
        add_vertex(counter, x1, y1)
        add_vertex(counter + 1, x2, y2)
        add_v_edge(x1, x2, y1, y2)
        counter += 2
        if counter - 1 > 2 and (counter - 1) % 2 == 0:
            add_h_edge(x1, x2, y1, y2)
            add_d_edge(x1, y1)

        x1 = x2 = 100 + radius * 3 * (i + 1)
    if (noe % 2 == 1):
        add_vertex(noe, x1, y1)
        add_h_edge(x1, x2, y1, y2, 1)
        add_d_edge(x1, y1, 1)


root = Tk()
frame = Frame(root)
frame.grid(row=0, column=0)

root.configure(background='#EFEFEF')
root.title("Dijkstra Visualization")

canvas = Canvas(frame, width="1000", height="500", bd="1", relief='raised')
canvas.grid(row=5, column=0, rowspan=1)

noe_frame = Frame(frame)
noe_frame.grid(row=0, column=0)

number_of_elements = Entry(noe_frame)
number_of_elements.grid(row=0, column=0)

number_of_elements_button = Button(noe_frame, text='Number of Elements', command=lambda: runProgram())
number_of_elements_button.grid(row=0, column=1, columnspan=1)

root.mainloop()
