import turtle

# Function to draw a burger with specified options
def draw_burger(cheese, lettuce, tomatoes, onions):
    burger_color = "saddlebrown"
    cheese_color = "yellow"
    lettuce_color = "green"
    tomato_color = "red"
    onion_color = "purple"

    # Draw the burger bun
    BurgerBun_image = "BurgerBun.gif"
    wn.addshape(BurgerBun_image)
    BurgerBun = turtle.Turtle()
    BurgerBun.shape(BurgerBun_image)
    BurgerBun.penup()
    BurgerBun.goto(0, -50)

    # Draw the burger patty
    UncookedPatty_image = "UncookedPatty.gif"
    wn.addshape(UncookedPatty_image)
    UncookedPatty = turtle.Turtle()
    UncookedPatty.shape(UncookedPatty_image)
    UncookedPatty.penup()
    UncookedPatty.goto(0, -20)

    # Draw cheese
    if cheese:
        Cheese_image = "Cheese.gif"
        wn.addshape(Cheese_image)
        Cheese = turtle.Turtle()
        Cheese.shape(Cheese_image)
        Cheese.penup()
        Cheese.goto(0, -100)

    # Draw lettuce
    if lettuce:
        Lettuce_image = "Lettuce.gif"
        wn.addshape(Lettuce_image)
        Lettuce = turtle.Turtle()
        Lettuce.shape(Lettuce_image)
        Lettuce.penup()
        Lettuce.goto(0, 0)
        Lettuce.color(lettuce_color)

    # Draw tomatoes
    if tomatoes:
        Tomato_image = "Tomato.gif"
        wn.addshape(Tomato_image)
        Tomato = turtle.Turtle()
        Tomato.shape(Tomato_image)
        Tomato.penup()
        Tomato.goto(0, 50)

    # Draw onions
    if onions:
        onion_image = "onions.gif"
        wn.addshape(onion_image)
        onion = turtle.Turtle()
        onion.shape(onion_image)
        onion.penup()
        onion.pensize(5)
        onion.goto(0, -20)
        onion.pendown()

    # Hide the turtle and display the burger
    turtle.hideturtle()
    turtle.done()

def main():
    print("Welcome to the Burger Builder!")
    print("Let's start by grilling the patty...")
    
    # Setting up the burger
    want_burger = input("Do you want a burger? (y/n): ").lower() == 'y'
    if want_burger:
        turtle.goto(0, 30)
        turtle.begin_fill()
        turtle.color("lightcoral")
        turtle.circle(80)
        turtle.end_fill()
        input("Press Enter to flip the patty...")
        turtle.penup()
        turtle.goto(0, 30)
        turtle.pensize(5)
        turtle.begin_fill()
        turtle.color("brown")
        turtle.circle(85)
        turtle.end_fill()
        print("Patty flipped!")

        # Questions for what user wants on the burger
        cheese = input("Do you want cheese? (y/n): ").lower() == 'y'
        lettuce = input("Do you want lettuce? (y/n): ").lower() == 'y'
        tomatoes = input("Do you want tomatoes? (y/n): ").lower() == 'y'
        onions = input("Do you want onions? (y/n): ").lower() == 'y'

        print("Building your burger...")

        # Draw the customized burger
        turtle.speed(1)  # Set the drawing speed (1 is slowest)
        draw_burger(cheese, lettuce, tomatoes, onions)
        print("Here's your burger!")

    else:
        print("No burger for you! Enjoy your day!")

if __name__ == "__main__":
    wn = turtle.Screen()
    main()
    wn.mainloop()
