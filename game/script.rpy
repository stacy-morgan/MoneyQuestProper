# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define mc = Character("Player")

$ money = 50000


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    mc "I am fresh out of high school. What will I do?"
    jump label choice1

    menu:
        "What should I do?"

        "Buy a car":
            jump buy_car

        "Get a job":
            jump get_job

        "Bachelor's Degree":
            jump bachelors
    
    label buy_car:
        scene bg lamborghini
        $ money -= 50000
        mc "I just bought a car!"
        jump broke_ass_bitch

    label  broke_ass_bitch:
        mc "I am out of money!"
        mc "You lose."
        jump end

    label get_job:
        mc "Without a college degree, there's only so much I can do."
        mc "The local WcDonald's is hiring..."
        mc "I could get a job as a janitor, or as a regular cook."
        mc "But a chef would probably have more promotional opportunities."
        menu:
            "Janitor ($16.50/yr, $34,320/yr)":
                jump wcd_chef_job_interview
            "WcDonald's Chef":
                jump wcd_chef_job_interview
        
    label wcd_chef_job:
        "I got the job."
        $ yrs_until_promotion = 2
        jump wcd_chef_gameloop

    label wcd_janitor_job:
        "I got the job."
        jump wcd_janitor_gameloop

    label wcd_chef_job_game_loop:
        "I am a chef now. I am making $16.50 an hour."

        

    return
