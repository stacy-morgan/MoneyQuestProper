# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define qqq = Character("???")
define news_reporter = Character("News Report")

define mc = Character("Lily")

define held_stocks = []
image bg nissan = "bg/Nissan.jpeg"
image bg porsche = "bg/Porsche.jpeg"
image bg atm = "bg/BrokeAhh.jpeg"
image bg mcb = "bg/McB.jpeg"
image bg home = "bg/Home.jpeg"
image bg college = "bg/College.jpeg"
image bg stocks_up = "bg/StocksGoUp.jpeg"
image bg stocks_down = "bg/StocksGoDown.jpeg"
image bg LearnToCode = "bg/LearnToCode.jpeg"
image bg graduation = "bg/Graduation.jpeg"
image bg broke_art_room = "bg/BrokeArtRoom.jpeg"
image bg SocialMedia = "bg/SocialMedia.jpeg"
image bg rocket_office = "bg/RocketOffice.jpeg"
image bg airplane_office = "bg/AirplaneOffice.jpeg"
image bg hospital = "bg/Hospital.jpeg"
image bg mansion = "bg/Mansion.jpeg"
image character animegirl = "chars/AnimeGirl.png"
image character lily = "chars/Lily.png"
image character oldlily = "chars/OldLily.png"

default major = ""
default money = 0
default year = 2025
default job = "none"
default house = False

init python:
    config.overlay_screens.append("money_display")

# The game starts here.

label start:

    scene bg home
    show lily

    # These display lines of dialogue.

    mc "Hii, I'm Lily."
    mc "I just graduated high school."
    $ money = 50000
    mc "I recently inherited a large amount of money from my great aunt. (+$50,000)"
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
            jump degree

        "Retire":
            jump retirement

label broke_ass_bitch:
    mc "I am out of money!"
    mc "You lose."
    jump end

label end:
    return
