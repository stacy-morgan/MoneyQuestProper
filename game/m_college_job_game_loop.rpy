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
    mc "Wow, I'm at work."
    mc "Its quite boring, but I get paid $120,000 a year, minus the $24,000 in expenses."
    jump cs_boring

label cs_boring:
    scene black with fade
    pause 1.0
    show text "Years passed, and you are starting to get burnt out." with dissolve
    pause 2.0
    show text "You decide to spend your hard earned money." with dissolve
    pause 2.0
    jump bach_choices

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

    mc "Wow, I'm at work."
    mc "Its quite boring, but I get paid $150,000 a year, minus the $24,000 in expenses."
    jump aero_boring

label aero_boring:
    scene black with fade
    pause 1.0
    show text "Years passed, and you are starting to get burnt out." with dissolve
    pause 2.0
    show text "You decide to spend your hard earned money." with dissolve
    pause 1.0
    jump bach_choices

label bach_choices:
    scene bg home
    mc "I have many choices to make."
    menu:
        "Buy mansion ($10,000,000)":
            jump mansion
        "Go on vacation ($100,000)":
            jump vacation

label mansion:
    scene black with fade
    pause 1.0
    show text "Risks: Buying a mansion comes at the risk of property tax and maintenance fees. Additionally, if you get laid off, then foreclosure is a possibility." with dissolve
    pause 3.0
    show text "Benefits: If the housing market booms, the house value appreciates, and you can live a happy life." with dissolve
    pause 3.0
    scene bg mansion
    "Buy, rent, or mortgage?"
    menu:
        "Buy":
            $ house = True
            jump ending_mansion
        "Rent":
            jump ending_mansion
        "Mortgage":
            jump ending_mansion

label ending_mansion:
    mc "I live in a mansion now!"
    scene black with fade
    pause 1.0
    show text "A couple of centuries passed..." with dissolve
    pause 2.0
    jump retirement

label vacation:
    scene black with fade
    pause 1.0
    show text "Risks: Spending too much results in lower savings for emergencies and you are prioritizing vacation over work."
    pause 3.0
    show text "Benefits: Vacation reduces stress and burn out, and you get to record your best memories."
    pause 3.0
    scene bg beach_vacation
    "Should you go on vacation?"
    menu:
        "Yes":
            jump ending_vacation
        "No":
            jump ending_vacation2

label ending_vacation:
    mc "I went on vacation!"
    scene black with fade
    pause 1.0
    show text "A couple of centuries passed..." with dissolve
    pause 2.0
    jump retirement

label ending_vacation2:
    mc "I believe that I should focus on work and saving money."
    scene black with fade
    pause 1.0
    show text "A couple of centuries passed..." with dissolve
    pause 2.0
    jump retirement
