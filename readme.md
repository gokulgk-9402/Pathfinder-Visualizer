# Pathfinding Visualizer
This is a simple visualizer for path finder using pygame mostly and small bits of tkinter for popups. The path finder is based on [A * search](https://en.wikipedia.org/wiki/A*_search_algorithm) algorithm.

## Steps to run the code:
* Run the file ``main.py``.
* As soon as the pygame window opens, press 's' on your keyboard and click some square on the pygame window to set it as start point.
* Then press 'e' on your keyboard and click some square on the pygame window to set it as end point (target).
* You can now start drawing barriers (walls) using just clicking and moving mouse over the pygame window.
* If you want to reset the window, press 'R' in your keyboard.
* If you press 'spacebar' after the previous steps, the path finder algorithm will start, and you can have visuals of it in the pygame window.
* If the algorithm finds a path between start and target, you will be prompted with a tkinter message box saying that its successful and the number of steps for that path will be displayed.
* If the algorithm couldn't find a path between start and target, you will be prompted with a tkinter message box saying that path doesn't exist between the points.
* After closing the tkinter message box or pressing ok, you can press 'R', reset the pygame window and start drawing the next start, target, walls.

The images of the pygame window, tkinter messageboxes are there in the repository, you can check them out. I know I'm not good with colors, feel free to share your thoughts to me on discord, gk#9402 .