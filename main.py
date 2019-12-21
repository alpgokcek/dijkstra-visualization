from tkinter import *
from dijkstra import Graph

black = (0, 0, 0)
white = (255, 255, 255)
radius = 0
graph = None

root = Tk()
frame = Frame(root, width="1000", height="550")
frame.grid(row=0, column=0)
root.configure(background='#EFEFEF')
root.title("Dijkstra Visualization")

canvas = Canvas(frame, width="1000", height="500", bd="1", relief='raised', scrollregion=(0, 0, 100000, 0))
canvas.grid(row=5, column=0, rowspan=1)
canvas.configure(scrollregion=canvas.bbox("all"))

hbar = Scrollbar(frame, orient=HORIZONTAL, activebackground="black")
hbar.grid(row=6, columnspan=6, sticky='ew')
hbar.config(command=canvas.xview)
canvas.config(xscrollcommand=hbar.set)


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


def add_h_edge(x1, x2, y1, y2, pos=0):  # pos = 1: only upper edge; else both edge
    try:
        if pos == 2:
            canvas.create_line(x1 - (2 * radius), y1 + radius // 2, x1, y1 + radius // 2, fill="#ff0000")
            return None


        canvas.create_line(x1 - (2 * radius), y1 + radius // 2, x1, y1 + radius // 2, fill="#000")
        if pos != 1:
            canvas.create_line(x2 - (2 * radius), y2 + radius // 2, x2, y2 + radius // 2, fill="#000")

    except Exception as e:
        print(e)


def add_d_edge(x1, y1, pos=0):  # pos = 1: only upper edge; else both edge
    gap = (radius * pow(2, 0.5)) - radius
    xp = yp = gap / pow(2, 0.5)
    try:
        if pos == 2:
            canvas.create_line(x1 - (2 * radius) - xp / 2, (y1 + 3 * radius) + yp / 2, x1 + xp / 2,
                               y1 + (radius) - yp / 2, fill="#ff0000")
            return None

        canvas.create_line(x1 - (2 * radius) - xp / 2, (y1 + 3 * radius) + yp / 2, x1 + xp / 2, y1 + (radius) - yp / 2,
                           fill="#000")
        if pos != 1:
            canvas.create_line(x1 - (2 * radius) - xp / 2, y1 + (radius) - yp / 2, x1 + xp / 2,
                               (y1 + 3 * radius) + yp / 2, fill="#000")


    except Exception as e:
        print(e)


def calculate_weight(i, j):
    return i + j


def create_graph(number_of_elements):
    global graph
    graph = Graph(number_of_elements)
    for i in range(1, number_of_elements):
        for j in range(i, number_of_elements + 1):
            if i % 2 == 1:
                if max(i - j, j - i) <= 3 and i != j:
                    graph.add_edge(i, j, calculate_weight(i, j))
            else:
                if max(i - j, j - i) <= 2 and i != j:
                    graph.add_edge(i, j, calculate_weight(i, j))
    # graph.print_graph()
    # graph.dijkstra_shortest_path_distances()
    output = graph.dijkstra_shortest_path(int(from_entry.get()), int(to_entry.get()))
    visualize_shortest_path(output[0])


def visualize_shortest_path(path):
    path = list(path)
    print(path)


    for i in range(len(path) - 1):
        current = path[i]
        next = path[i+1]
        if current % 2 == 0 and next % 2 == 1:
            x1 = x2 = 100 + radius * 3 * (i + 1)
            y1, y2 = (500 - 7 * radius), (500 - 7 * radius) + (radius * 3)
            add_d_edge(x1, y1, 2)
        elif current % 2 == 1 and next % 2 == 0:
            pass
        elif current % 2 == next % 2:
            print(current, next)
            x1 = x2 = 100 + radius * 3 * (i + 1)
            y1, y2 = (500 - 7 * radius), (500 - 7 * radius) + (radius * 3)
            add_h_edge(x1, x2, y1, y2, 2)


def runProgram():
    global canvas
    canvas.delete("all")
    calculate_radius()
    noe = int(number_of_elements.get())
    canvas.configure(scrollregion=(0, 0, 100 + noe * 78, 0))
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
    create_graph(noe)


from_frame = Frame(frame)
from_frame.grid(row=0, column=0)

number_of_elements = Entry(from_frame)
number_of_elements.grid(row=0, column=0)
number_of_elements.insert(0, "Number of Elements")
number_of_elements.configure(state=DISABLED)


def on_click_from_noe(event):
    number_of_elements.configure(state=NORMAL)
    number_of_elements.delete(0, END)
    number_of_elements.unbind('<Button-1>', on_click_id_noe)


on_click_id_noe = number_of_elements.bind('<Button-1>', on_click_from_noe)

from_entry = Entry(from_frame)
from_entry.grid(row=0, column=1)
from_entry.insert(0, "From")
from_entry.configure(state=DISABLED)


def on_click_from_entry(event):
    from_entry.configure(state=NORMAL)
    from_entry.delete(0, END)
    from_entry.unbind('<Button-1>', on_click_id_from)


on_click_id_from = from_entry.bind('<Button-1>', on_click_from_entry)

to_entry = Entry(from_frame)
to_entry.grid(row=0, column=2)
to_entry.insert(0, "To")
to_entry.configure(state=DISABLED)


def on_click_to_entry(event):
    to_entry.configure(state=NORMAL)
    to_entry.delete(0, END)
    to_entry.unbind('<Button-1>', on_click_id_to)


on_click_id_to = to_entry.bind('<Button-1>', on_click_to_entry)

from_entry_button = Button(from_frame, text='Set From and To', command=lambda: runProgram())
from_entry_button.grid(row=0, column=3, columnspan=1)

root.mainloop()
