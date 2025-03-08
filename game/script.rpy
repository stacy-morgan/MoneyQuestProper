# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define qqq = Character("???")

define mc = Character("Lily")

image bg nissan = "bg/Nissan.jpeg"
image bg porsche = "bg/Porsche.jpeg"
image bg atm = "bg/BrokeAhh.jpeg"
image bg mcd = "bg/McD.jpeg"
image bg home = "bg/Home.jpeg"
image bg college = "bg/College.jpeg"
image bg stocks_up = "bg/StocksGoUp.jpeg"
image bg stocks_down = "bg/StocksGoDown.jpeg"
image character eileen = "chars/AnimeGirl.png"
image character lily = "chars/Lily.png"

default major = ""

# The game starts here.

label start:
    $ money = 50000
    $ year = 2025
    $ job = "none"

    scene bg home
    show lily

    # These display lines of dialogue.

    mc "Hii, I'm Lily."
    mc "I just graduated high school."
    mc "I recently inherited a large amount of money from my great aunt."
    mc "What should I do with it?"
    # jump buy_car

    jump choice1

label choice1:
    menu:
        "Buy a car":
            jump buy_car

        "Get a job":
            jump get_job

        "Bachelor's Degree":
            jump bachelors

        "Retire":
            jump retirement

label broke_ass_bitch:
    mc "I am out of money!"
    mc "You lose."
    jump end

label end:
    return
