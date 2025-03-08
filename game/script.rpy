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

image character eileen = "AnimeGirl.png"
image character lily = "Lily.png"

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
        mc "My grandpa gave me a car..."
        mc "But it's so ugly."
        mc "I am going to get no girls with this car."
        mc "I want to get something fancy! I've heard that you can get a really fancy car for around this price."
        scene bg porsche
        with wipeleft
        mc "I really want this fancy Porsche to flex my wealth!"
        mc "But I don't know if it's the best thing to do with this money."
        menu:
            "Buy the Porsche (-$50,000)":
                jump yes_car
            "Save the money for something more useful":
                jump no_car
    
    label yes_car:
        $ money -= 50000
        mc "This car is so nice! **vroom vroom**"
        scene bg atm
        with dissolve
        mc "But now my bank account is empty..."
        scene bg home
        show character lily
        mc "My parents are furious!! Now they are going to kick me out :("
        mc "They told me to get a job. Ugh!"
        jump get_job
    
    label no_car:
        scene bg home
        show character lily
        mc "Now I have all this money, if I'm not going to buy a car, what should I do with it??"
        mc "Hmm... I could go to college, or maybe put it in the stock market."
        menu:
            "Get a Bachelors Degree":
                jump degree
            "Invest the money":
                jump invest
    
    label degree:
        mc "We still need to write this route uwu."
        jump end

    label broke_ass_bitch:
        mc "I am out of money!"
        mc "You lose."
        jump end

    label get_job:
        mc "Without a college degree, there's only so much I can do."
        mc "The local WcDonald's is hiring..."
        scene bg mcd
        show character lily
        mc "I could get a job as a janitor, or as a regular cook."
        mc "But a chef would probably have more promotional opportunities."
        menu:
            "Janitor ($16.50/hr, $34,320/yr)":
                jump wcd_janitor_job_interview

            "WcDonald's Chef ($20.00/hr, $41,600/yr)":
                jump wcd_chef_job_interview

    label wcd_janitor_job_interview:
        show character eileen
        qqq "Hi, I'm Eileen! I'll be interviewing you today."
        e "The question is..."
        menu:
            e "What do you get when you mix ammonia and bleach?"

            "A) Mustard gas.":
                jump jji_a

            "B) A very strong soap":
                jump jji_b

    label jji_a:
        e "Ok, thank god."
        e "We had an... incident regarding cleaning supplies at our previous location."
        e "As you know, it does not exist anymore. It was a biohazard."
        e "You're hired."

    label jji_b:
        e "That's... not true. Unfortunately, we will not proceed with your hiring at this time."
        "Aw man, I didn't get the job,"
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
