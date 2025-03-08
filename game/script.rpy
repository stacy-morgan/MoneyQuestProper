# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define mc = Character("Player")

image bg nissan = "Nissan.jpeg"
image bg porsche = "Porsche.jpeg"
image bg atm = "BrokeAhh.jpeg"
image bg mcd = "McD.jpeg"

image character animegirl = "AnimeGirl.png"

# The game starts here.

label start:
    $ money = 50000
    $ year = 2025
    $ job = "unused"

    scene bg room
    show eileen happy

    # These display lines of dialogue.

    mc "I am fresh out of high school. What will I do?"
    jump choice1

    label choice1:
        menu:
            "Buy a car":
                jump buy_car

            "Get a job":
                jump get_job

            "Bachelor's Degree":
                jump bachelors
    
    label buy_car:
        scene bg nissan
        "My grandpa gave me a car..."
        "But it's so ugly."
        "I am going to get no girls with this car."
        "I'm going to get something fancy! I've heard that you can get a really fancy car for around this price."
        scene bg porsche
        with wipeleft
        "Time to get a fancy Porsche to flex my wealth!" 
        $ money -= 50000
        mc "I just bought a car!"
        scene bg atm
        with dissolve
        mc "But now my wallet is empty..."
        jump broke_ass_bitch

    label  broke_ass_bitch:
        mc "I am out of money!"
        mc "You lose."
        jump end

    label get_job:
        mc "Without a college degree, there's only so much I can do."
        mc "The local WcDonald's is hiring..."
        scene bg mcd
        mc "I could get a job as a janitor, or as a regular cook."
        mc "But a chef would probably have more promotional opportunities."
        menu:
            "Janitor ($16.50/yr, $34,320/yr)":
                jump wcd_janitor_job_interview

            "WcDonald's Chef":
                jump wcd_chef_job_interview

    label wcd_janitor_job_interview:
        menu:
            "What do you get when you mix ammonia and bleach?"

            "A) Mustard gas.":
                jump jji_a

            "B) A very strong soap":
                jump jji_b

    label jji_a:
        "Unformtunately, I didn't get the job,"
        "They said I had to \'go back to high school chemistry\' or something."
        "I guess Mr. White wasn't the best teacher..."
        "Well, there's nothing I can do besides trying again."

    scene bg room
    jump get_job
        
    label wcd_chef_job:
        "I got the job."
        $ yrs_until_promotion = 2
        jump wcd_chef_gameloop

    label wcd_janitor_job:
        "I got the job."
        $ yrs_until_promotion = 2
        jump wcd_janitor_gameloop

    label wcd_chef_job_game_loop:
        "I am a chef now. I am making $16.50 an hour."
        "Yippee!"

label end:
    return
return
