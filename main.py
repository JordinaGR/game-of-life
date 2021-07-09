from tkinter import *
import time

# change this three variables to change the size of all widgets
n = 80
m = 100
square_size = 11

dead = 'white'
alive = 'black'
arr = [[0 for i in range(m)] for i in range(n)]
adj_x = [-1, -1, -1, 0, 0, 1, 1, 1]
adj_y = [-1, 0, 1, -1, 1, -1, 0, 1]

root = Tk()
root.config(bg='white')
root.minsize(1100, n*square_size+100)
canvas = Canvas(root, width=m*square_size, height=n*square_size, bg='white')
canvas.pack(side=TOP)

def drawdata(x, y, col):
    global canvas
    canvas.create_rectangle(x*square_size, y*square_size, (x*square_size)+square_size, (y*square_size)+square_size, fill=col)

def print_matrix(matrix):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                drawdata(j, i, dead)
            elif matrix[i][j] == 1:
                drawdata(j, i, alive)

def start_func():
    global arr
    temp = [[0 for i in range(m)] for i in range(n)]    
    for i in range(n):
        for j in range(m):
            nei = 0
            for k in range(8):
                x2 = i + adj_x[k]
                y2 = j + adj_y[k]

                if x2 >= 0 and x2 < n and y2 >= 0 and y2 < m and arr[x2][y2] == 1:
                    nei += 1

            if arr[i][j] == 1 and (nei == 2 or nei == 3):
                temp[i][j] = 1

            elif arr[i][j] == 0 and nei == 3:
                temp[i][j] = 1

            else:
                temp[i][j] = 0

    arr = list(temp)
    print_matrix(arr)


def bind_auto(event):
    mx = event.x
    my = event.y

    if mx >= 0 and my >= 0 and mx <= m*square_size and my <= n*square_size:
        cordy = mx // square_size
        cordx = my // square_size

        if arr[cordx][cordy] == 1:
            arr[cordx][cordy] = 0
            drawdata(cordy, cordx, dead)
        else:
            arr[cordx][cordy] = 1
            drawdata(cordy, cordx, alive)

def clear_func():
    global arr
    arr = [[0 for i in range(m)] for i in range(n)]
    print_matrix(arr)

print_matrix(arr)

start_but = Button(root, text='NEXT', bg='white', font=('arial', 12),command=start_func)
start_but.place(y=square_size*n+15, x=10)

clear_all_button = Button(root, text='KILL ALL\nALIVE CELLS', font=('arial', 10), bg='white', command=clear_func)
clear_all_button.place(y=square_size*n+10, x=100)

canvas.bind('<B1-Motion>', bind_auto)
root.mainloop()