import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "#", "#", "#", "#", "#", "O", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "X", "#", "#", "#", "#", "#", "#", "#"]
]

def print_maze(maze, screen, path = []):
    blue = curses.color_pair(1)
    red = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                screen.addstr(i, j*2, "X", red)
            else:
                screen.addstr(i, j*2, value, blue)

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if(value == start):
                return i, j
    return None




def find_path(maze, screen):
    start = "O"
    end = "X"
    star_posi = find_start(maze, start)
    q = queue.Queue()
    q.put((star_posi, [star_posi]))

    visited = set()

    while not q.empty():
        curren_posi, path = q.get()
        row, col = curren_posi

        screen.clear()
        print_maze(maze, screen, path)
        time.sleep(0.0001)
        screen.refresh()
        

        if(maze[row][col] == end):
            return path
        
        neighbours = find_neighbours(maze, row, col)
        for neighbour in neighbours:
            if neighbour in visited:
                continue
            r, c = neighbour
            if maze[r][c] == "X":
                continue
            new_path = path + [neighbour]
            q.put((neighbour, new_path))
            visited.add(neighbour)
            

def find_neighbours(maze, row, col):
    neighbours = []
    if row > 0:
        neighbours.append((row-1, col))
    if row + 1 < len(maze):
        neighbours.append((row + 1, col))
    if col > 0:
        neighbours.append((row, col-1))
    if col + 1 < len(maze[0]):
        neighbours.append((row, col + 1))
    return neighbours





def main(screen):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    find_path(maze, screen)
    screen.getkey()
    


wrapper(main)



