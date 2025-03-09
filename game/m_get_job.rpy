label get_job_with_intro:
    mc "Without a college degree, there's only so much I can do."
    mc "The local WcBonald's is hiring..."

label get_job:
    scene bg mcb
    mc "I could get a job as a janitor, or as a regular cook."
    mc "But a chef would probably have more promotional opportunities."
    menu:
        "Janitor":
            jump wcb_janitor_job_interview

        "WcDonald's Chef":
            jump wcb_chef_job_interview

label wcb_janitor_job_interview:
    show character animegirl:
        xpos 0.5  ypos 0
    qqq "Hi, I'm Eileen! I'll be interviewing you today."
    e "The question is..."
    menu:
        e "What do you get when you mix ammonia and bleach?"

        "A) Mustard gas":
            jump jji_a

        "B) A very strong soap":
            jump jji_b

label jji_a:
    hide character animegirl
    show character animegirl:
        xpos 0.5  ypos 0
        yoffset 0
        easein 0.25 yoffset -100
        easeout 0.25 yoffset 0
        easein 0.2 yoffset -30
        easeout 0.2 yoffset 0
        easein 0.15 yoffset -10
        easeout 0.15 yoffset 0
        easein 0.1 yoffset -4
        easeout 0.1 yoffset 0
    e "MUSTAAAAAAAAAAARD!!!!!!"
    e "Ok, thank god."
    e "We had an... incident regarding cleaning supplies at our previous location."
    e "As you know, it does not exist anymore. It was a biohazard."
    e "You're hired."
    $ job = "Janitor"
    $ wcb_year_start = year
    jump wcb_janitor_game_loop

label jji_b:
    e "That's... not true. Unfortunately, we will not proceed with your hiring at this time."
    scene bg home
    show character lily
    mc "Aw man, I didn't get the job,"
    mc "They said I had to \'go back to high school chemistry\' or something."
    mc "I guess Mr. White wasn't the best teacher..."
    mc "Well, there's nothing I can do besides trying again."
    jump get_job

label wcb_chef_job_interview:
    show character animegirl:
        xpos 0.5  ypos 0
    qqq "Hi, I'm Eileen! I'll be interviewing you today."
    e "The question is..."
    menu: 
        e "Fill in the blank. Put the _____ in the bag?"

        "A) fries":
            jump cji_a

        "B) money":
            jump cji_b
    jump end

label cji_a:
    hide character animegirl
    show character animegirl:
        xpos 0.5  ypos 0
        yoffset 0
        easein 0.25 yoffset -100
        easeout 0.25 yoffset 0
        easein 0.2 yoffset -30
        easeout 0.2 yoffset 0
        easein 0.15 yoffset -10
        easeout 0.15 yoffset 0
        easein 0.1 yoffset -4
        easeout 0.1 yoffset 0
    e "Correct! You're hired."
    $ job = "Chef"
    $ wcb_year_start = year
    jump wcb_chef_game_loop

label cji_b:
    e "That's... not true. Unfortunately, we will not proceed with your hiring at this time."
    scene bg home
    show character lily
    mc "I wish I knew how to put the fries in the bag..."
    mc "Well, there's nothing I can do besides trying again."
    jump get_job
