from tkinter import messagebox, Tk
from tracemalloc import start
import pygame
import sys

WIDTH = 700
HEIGHT = 700

window = pygame.display.set_mode((WIDTH, HEIGHT))


COLUMNS = 35
ROWS = 35

BOX_WIDTH = 20
BOX_HEIGHT = 20

grid = []
queue = []
path = []

class Box:

    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.isstart = False
        self.isend = False
        self.iswall = False
        self.queued = False
        self.visited = False
        self.prior = None
        self.neighbours = []

    def draw(self, window, color):
        pygame.draw.rect(window, color, (self.x * BOX_WIDTH + 1, self.y * BOX_HEIGHT + 1, BOX_WIDTH-1, BOX_HEIGHT-1))

    def set_neighbours(self):
        if self.x > 0:
            self.neighbours.append(grid[self.x-1][self.y])
        if self.x < COLUMNS - 1:
            self.neighbours.append(grid[self.x+1][self.y])
        if self.y > 0:
            self.neighbours.append(grid[self.x][self.y-1])
        if self.y < ROWS - 1:
            self.neighbours.append(grid[self.x][self.y+1])
        

for i in range(COLUMNS):
    arr = []
    for j in range(ROWS):
        arr.append(Box(i,j))
    grid.append(arr)

for i in range(COLUMNS):
    for j in range(ROWS):
        grid[i][j].set_neighbours()

choosing_start = False
choosing_end = False
begin_search = False
target_set = False
start_set = False
searching = True
target_b = None


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN and choosing_start:
            choosing_start = False
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            i = x // BOX_WIDTH
            j = y // BOX_HEIGHT
            start_box = grid[i][j]
            start_box.isstart = True
            start_box.visited = True
            queue.append(start_box)
            start_set = True
        
        elif event.type == pygame.MOUSEBUTTONDOWN and choosing_end:
            choosing_end = False
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            i = x // BOX_WIDTH
            j = y // BOX_HEIGHT
            target = grid[i][j]
            target.isend = True
            target_set = True
            target_set = True

        elif event.type == pygame.MOUSEMOTION and target_set and start_set:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            if event.buttons[0]:
                i = x // BOX_WIDTH
                j = y // BOX_HEIGHT
                grid[i][j].iswall = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                choosing_start = True
            elif event.key == pygame.K_e:
                choosing_end = True
            elif event.key == pygame.K_SPACE:
                if target_set and start_set:
                    begin_search = True
            elif event.key == pygame.K_r:
                choosing_start = False
                choosing_end = False
                begin_search = False
                target_set = False
                start_set = False
                searching = True
                target_b = None
                for row in grid:
                    for box in row:
                        box.isstart = False
                        box.isend = False
                        box.iswall = False
                        box.queued = False
                        box.visited = False
                        box.prior = None
                queue = []
                path = []

    if begin_search:
        if len(queue) > 0 and searching:
            current = queue.pop(0)
            current.visited = True
            if current == target:
                searching = False
                while current.prior != start_box:
                    path.append(current.prior)
                    current = current.prior
            else:
                for neighbour in current.neighbours:
                    if not neighbour.queued and not neighbour.iswall:
                        neighbour.queued = True
                        queue.append(neighbour)
                        neighbour.prior = current

        else:
            if searching:
                Tk().wm_withdraw()
                messagebox.showinfo("No soultion", "There is no solution!")
                searching = False

    window.fill((60, 60, 60))

    for i in range(COLUMNS):
        for j in range(ROWS):
            if grid[i][j].isstart:
                grid[i][j].draw(window, (0, 150, 200))
            elif grid[i][j].iswall:
                grid[i][j].draw(window, (0, 0, 0))
            elif grid[i][j].isend:
                grid[i][j].draw(window, (20, 250, 20))
            elif grid[i][j] in path:
                grid[i][j].draw(window, (100, 200, 100))
            elif grid[i][j].visited:
                grid[i][j].draw(window, (250, 250, 150))
            elif grid[i][j].queued:
                grid[i][j].draw(window, (250, 150, 150))
            else: 
                grid[i][j].draw(window, (30, 30, 30))

    pygame.display.flip()