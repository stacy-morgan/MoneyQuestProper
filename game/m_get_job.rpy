label get_job:
    if job == "":
        mc "Without a college degree, there's only so much I can do."
        mc "The local WcBonald's is hiring..."

    scene bg mcb
    mc "I could get a job as a janitor, or as a regular cook."
    mc "But a chef would probably have more promotional opportunities."
    menu:
        "Janitor":
            jump wcb_janitor_job_interview

        "WcDonald's Chef":
            jump wcb_chef_job_interview

label wcb_janitor_job_interview:
    show character eileen
    qqq "Hi, I'm Eileen! I'll be interviewing you today."
    e "The question is..."
    menu:
        e "What do you get when you mix ammonia and bleach?"

        "A) Mustard gas":
            jump jji_a

        "B) A very strong soap":
            jump jji_b

label jji_a:
    e "Ok, thank god."
    e "We had an... incident regarding cleaning supplies at our previous location."
    e "As you know, it does not exist anymore. It was a biohazard."
    e "You're hired."
    jump wcb_janitor_game_loop

label jji_b:
    e "That's... not true. Unfortunately, we will not proceed with your hiring at this time."
    scene bg home
    mc "Aw man, I didn't get the job,"
    mc "They said I had to \'go back to high school chemistry\' or something."
    mc "I guess Mr. White wasn't the best teacher..."
    mc "Well, there's nothing I can do besides trying again."
    jump get_job

label wcb_chef_job_interview:
    e "Hi, I'm Eileen! I'll be interviewing you today."
    jump end
