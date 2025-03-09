# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define qqq = Character("???")
define news_reporter = Character("News Report")

define robintrade = Character("Robintrade Automated E-Mail")
define bank = Character("Bank Automated E-Mail")
define mc = Character("Lily")
define W = Character ("WcBonald's Employees")

image bg nissan = "bg/Nissan.jpeg"
image bg porsche = "bg/Porsche.jpeg"
image bg atm = "bg/BrokeAhh.jpeg"
image bg mcb = "bg/McB.jpeg"
image bg home = "bg/Home.jpeg"
image bg college = "bg/College.jpeg"
image bg stocks_up = "bg/StocksGoUp.jpeg"
image bg LearnToCode = "bg/LearnToCode.jpeg"
image bg graduation = "bg/Graduation.jpeg"
image bg broke_art_room = "bg/BrokeArtRoom.jpeg"
image bg SocialMedia = "bg/SocialMedia.jpeg"
image bg rocket_office = "bg/RocketOffice.jpeg"
image bg airplane_office = "bg/AirplaneOffice.jpeg"
image bg hospital = "bg/Hospital.jpeg"
image bg mansion = "bg/Mansion.jpeg"
image bg winter_room = "bg/WinterRoom.jpeg"
image bg winter_room_stocks = "bg/WinterRoomStocks.jpeg"
image bg time_passes = "bg/TimePasses.jpeg"
image bg lily_rip = "bg/LilyRip.jpeg"
image bg beach_vacation = "bg/BeachVacation.jpeg"
image bg expensive_room = "bg/ExpensiveRoom.jpeg"
image bg model_3d = "bg/Model3d.jpeg"
image character animegirl = "chars/AnimeGirl.png"
image character lily = "chars/Lily.png"
image character oldlily = "chars/OldLily.png"

init python:
    config.overlay_screens.append("money_display")
    config.overlay_screens.append("stock_buy_display")

# The game starts here.

label start:
    if persistent.highscore != 0:
        "High score: $[persistent.highscore]"
    default debug = False
    default noob = True
    default salary = 0
    default held_stocks = {}
    default major = ""
    default money = 0
    default year = 2025
    default job = "none"
    default house = False
    default show_stock_prices = False
    default gone_to_college = False

    default spy_price = 500
    default wcb_price = 150
    default investment_level = 0

    define wage = 0

    default tutorial_buy_sp = 0
    default tutorial_buy_wcb = 0
    default calling_day1 = False

    default hasSkillandInfluencer = False
    default hasSecondaryJob = False
    default promoted = False

    default hs_job_level = 0
    default wcb_year_start = 0

    default sp_change = [
        1.11,  # New Year 2026
        1.092, # New Year 2027
        1.095, # New Year 2028
        1.081, # New Year 2029
        0.72,  # New Year 2030
        1.89,  # New Year 2035
        1.76,  # New Year 2040
        1.91,  # New Year 2050
        1.96,  # New Year 2060
        2.03   # New Year 2070
    ]

    scene bg home
    show lily

    # These display lines of dialogue.

    mc "Hii, I'm Lily."
    mc "I just graduated high school."
    $ money = 50000
    mc "I recently inherited a large amount of money from my great aunt. (+$50,000)"
    mc "What should I do with it?"
    if debug:
        jump debug_choice
    else:
        jump buy_car

label debug_choice:
    menu:
        "Buy a car THIS WILL ALWAYS HAPPEN IN THE GAME. THIS MENU IS FOR TESTING ONLY.":
            jump buy_car

        "Get a job":
            jump get_job_with_intro

        "Bachelor's Degree":
            jump degree

        "Retire":
            jump retirement
            
        "Invest":
            jump day1_invest

        "Other Invest":
            jump other_invest

label broke_ass_bitch:
    mc "I am out of money!"
    mc "You lose."
    jump end

label end:
    return
