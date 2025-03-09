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
    $ salary = 120000

    scene bg LearnToCode
    with fade
    mc "This is my work,"
    mc "Its quite boring, but I get paid $120,000 a year, minus the $24,000 in expenses."

    scene black with fade
    pause 1.0
    show text "One year has passed..." with dissolve
    pause 2.0
    call year_over

    scene bg LearnToCode

    jump batch_choices

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
        "Go homeless":
            jump model

label model:
    "kys"
    jump end
    scene bg model_3d
    mc "Wow, I'm at work."
    mc "Its quite boring, but I get paid $60,000 a year, minus the $24,000 in expenses."
    jump model_boring

label model_boring:
    scene black with fade
    pause 1.0
    show text "Years passed, and you are starting to get burnt out, and decide to go on vaction" with dissolve
    pause 2.0
    show text "However, as a 3D modeler, you do not make enough money." with dissolve
    pause 1.0
    jump vacation

label aerospace_job:
    mc "I heard that as an [major] major, I can work on planes or rockets!"
    menu:
        "What job do you want?"

        "Airplane Technician":
            $ job = "Airplane Technician"
        "Rocket Engineer":
            $ job = "Rocket Engineer"
    $ salary = 90000

    if job == "Airplane Technician":
        scene bg airplane_office
        with fade
    else:
        scene bg rocket_office
        with fade

    mc "Wow, I'm at work."
    mc "Its quite boring, but I get paid $90,000 a year, minus the $24,000 in expenses."

    scene black with fade
    pause 1.0
    show text "One year has passed..." with dissolve
    pause 2.0
    call year_over

    if job == "Airplane Technician":
        scene bg airplane_office
        with fade
    else:
        scene bg rocket_office
        with fade
    
    jump batch_choices

label batch_choices:
    show character lily
    mc "I have a lot of money now, maybe I should invest some."
    
    menu:
        "Invest some money":
            if noob:
                $ calling_day1 = True
                call day1_invest
                $ calling_day1 = False
            else:
                call other_invest

            jump continue_0223
        "I don't believe in the stock market":
            jump continue_0223

label continue_0223:

    scene black with fade
    pause 1.0
    show text "Five years passed, and you earned a lot." with dissolve
    pause 2.0
    call year_over

    if year >= 2060:
        jump retirement

    scene black with fade
    show text "You decide to use your hard earned money." with dissolve
    pause 1.0

    scene bg home

    $ total_assets = money + calculate_portfolio_value()

    menu:
        mc "I have a lot of money now, what should I do with it?"

        "Buy mansion ($10,000,000)" if money >= 10000000:
            jump mansion
        "Go on vacation ($10,000)" if money >= 10000:
            jump vacation
        "Invest money" if money >= 3000:
            if noob:
                $ calling_day1 = True
                call day1_invest
                $ calling_day1 = False
            else:
                call other_invest

            jump batch_choices_end
        "Keep working":
            jump batch_choices_end
        "Retire" if total_assets >= 1000000:
            jump retirement

label batch_choices_end:
    if job == "Airplane Technician" or job == "Rocket Engineer":
        if job == "Airplane Technician":
            scene bg airplane_office
            with fade
        else:
            scene bg rocket_office
            with fade
        jump continue_0223
    elif job == "Database Manager" or job == "Full Stack Web Developer" or job == "Machine Learning Engineer":
        scene bg LearnToCode
        jump continue_0223
    else:
        jump artist_game_loop

label mansion:
    $ money -= 10000000
    $ house = True
    scene bg mansion
    mc "I live in a super nice mansion now!"
    mc "These windows are so pretty."
    jump retirement

label vacation:
    $ money -= 10000
    scene bg beach_vacation
    mc "This was a super relaxing vacation, definitely worth the money!"
    jump batch_choices_end
