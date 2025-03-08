# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define qqq = Character("???")

define mc = Character("Lily")

image bg nissan = "Nissan.jpeg"
image bg porsche = "Porsche.jpeg"
image bg atm = "BrokeAhh.jpeg"
image bg mcd = "McD.jpeg"
image bg home = "Home.jpeg"
image bg college = "College.jpeg"

image character eileen = "AnimeGirl.png"
image character lily = "Lily.png"

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
    jump buy_car

    # jump choice1

# label choice1:
#     menu:
#         "Buy a car":
#             jump buy_car

#         "Get a job":
#             jump get_job

#         "Bachelor's Degree":
#             jump bachelors

label broke_ass_bitch:
    mc "I am out of money!"
    mc "You lose."
    jump end

label end:
    return
