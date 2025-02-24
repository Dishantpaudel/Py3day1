max_x=500
max_y =500

x=10
y=10

dx= 1
dy= 1
def draw_circle(x,y):
    print((x,y))
    
while True:
    x += dx
    y +=dy
    
    if x > max_x or x <=0:
        dx = -dx
    if y > max_y or y <=0:
        dy = -dy    
    draw_circle(x,y)     
