import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def main():
    order = int(input("Вкажіть рівень рекурсії для сніжинки Коха: "))
    size = 300

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(5)  
    t.penup()
    t.goto(-size / 2, size / 2 / 3**0.5)
    t.pendown()

    koch_snowflake(t, order, size)

    t.hideturtle()
    window.mainloop()

if __name__ == "__main__":
    main()
