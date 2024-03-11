import turtle

# Create a turtle pen
pen = turtle.Turtle()
turtle.tracer(n=0)

def draw_map():
    x = 720
    y = int(x/2) # Ratio 2:1
    screen = turtle.Screen()
    screen.setup(x, y)
    screen.setworldcoordinates(-180, -90, 180, 90) # Translate the coordinates to pixels
    screen.bgpic('images/equirectancular.png')  # Set the background image
    screen.colormode(255)

def draw_points(data):
    pen.penup()

    # Get the min and max values of the magnitude
    max = data['magnitude'].max()
    min = data['magnitude'].min()

    for index, row in data.iterrows():
        # print(row['magnitude'])
        pen.goto(row['longitude'], row['latitude']) # Go to the coordinates

        size = row['magnitude']  # Scale the magnitude

        color = interpolate_color(min, max, size) # Interpolate the color based on the magnitude

        pen.color(color[0], color[1], color[2])  # RGB color
        pen.pendown()
        if size <= 0: # Skip the point if the magnitude is 0
            continue
        pen.dot(size)  # Draw the point
        pen.penup()

    turtle.done() # Keep the window open


# Interpolate the color based on the magnitude. Yellow for low values, red for high values
def interpolate_color(min_value, max_value, value):
    # Define the RGB values for yellow and red
    yellow = (255, 255, 0)  # RGB for yellow
    red = (255, 0, 0)  # RGB for red

    # Calculate the proportion of value between min and max
    proportion = (value - min_value) / (max_value - min_value)

    # Interpolate the color based on the proportion
    r = int((1 - proportion) * yellow[0] + proportion * red[0])
    g = int((1 - proportion) * yellow[1] + proportion * red[1])
    b = int((1 - proportion) * yellow[2] + proportion * red[2])

    return (r, g, b)
