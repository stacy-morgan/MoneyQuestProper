label cs_job:
    mc "I should probably get a job at a top tech company."
    menu:
        "What tech job do you want?"

        "Database Manager":
            $ job = "Database Manager"
        "Full Stack Web Developer":
            $ job = "Full Stack Web Developer"
        "Machine Learning Engineer":
            $ job = "Machine Learning Engineer"
    jump cs_game_loop

label cs_game_loop:
    scene bg LearnToCode
    with fade
    mc "Wow I'm at work...."
    jump end

label art_job:
    mc "I really want to make art now, but I'm worried that I won't make enough money to pay for an apartment."
    menu:
        mc "Should I get a job at WcBonalds to make some money or put my full focus on my art?"

        "Work at WcBonalds":
            jump get_job
        "Try to be an artist":
            $ job = "Artist"
            jump artist_game_loop

label artist_game_loop:
    scene bg broke_art_room
    with fade
    show character lily
    mc "I've been making art for 6 months now and I'm totally out of money."
    mc "Since art is not working out, it looks like I only have two options,"

    menu:
        mc "What should I do?"

        "Get a job at WcBonalds":
            jump get_job
        "Suck feet instead":
            jump suck_feet

label suck_feet:
    qqq "Those feet look mighty suckable. ;-}"
    qqq "MMMMhhhhh, ahhhhh, like that"
    jump end

label aerospace_job:
    mc "I heard that as an [major] major, I can work on planes or rockets!"
    menu:
        "What job do you want?"

        "Airplane Technician":
            $ job = "Airplane Technician"
        "Rocket Engineer":
            $ job = "Rocket Engineer"
    jump aerospace_game_loop

label aerospace_game_loop:
    if job == "Airplane Technician":
        scene bg airplane_office
        with fade
    else:
        scene bg rocket_office
        with fade

    mc "I'm at work now!"
    jump end
