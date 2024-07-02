from tkinter import Tk, Canvas
import random

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Worley Noise View")
        #self.root.geometry("400x400")

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb  

if __name__ == '__main__':
    width = 400
    height = 400
    points = []
    for i in range(0,7):
        points.append([random.randrange(0, width), random.randrange(0, height)])
    root = Tk()
    colors = ["black", "white"]
    canvas = Canvas(root, width = width, height = height);canvas.pack()
    
    for x in range(width):
        for y in range(height):
            distances = []
            index = 0
            for i in points:
                dx = i[0] - x
                dy = i[1] - y
                d = abs(dx) + abs(dy)
                distances.append(d)
                index+=1
            n = 0;
            distances.sort()
            noise = distances[n]
            canvas.create_line(x, y, x + 1, y, fill=_from_rgb((noise,noise,noise)))
    obj = Main(root)
    root.mainloop()
