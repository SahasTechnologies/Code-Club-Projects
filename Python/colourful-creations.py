from turtle import *

screen = Screen()
screen.setup(400, 400)
colours = {
    'verylime': '#A7E30E',
    'reallyraspberry': '#BF3F7F'
}
screen.bgcolor(colours['verylime'])
color(colours['reallyraspberry'])
print(colours['verylime'])
print(colours['reallyraspberry'])
screen.bgcolor("#2d88af")

color("#29359D")
style = ('Arial', 40, 'bold')
write('HELLO', font=style, align='center')
hideturtle()

