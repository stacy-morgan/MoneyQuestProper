init python:
    def wage_calc():
        if job == "Janitor":
            if hs_job_level == 0:
                wage = 16.5
            if hs_job_level >= 1:
                wage = 17.2
        
        if job == "Chef":
            if hs_job_level == 0:
                wage = 20
            
            if hs_job_level == 1:
                job = "Head Chef"
                wage = 23.5
            
            if hs_job_level == 2:
                job = "Franchise Owner"
                wage = 27

    def salary_calc(wage):
        hrs_per_week = 40
        weekly_income = wage * hrs_per_week
        yearly_income = weekly_income * 52

label wcb_chef_job:
    mc "I got the job."
    jump wcb_chef_game_loop

label wcb_janitor_job:
    mc "I got the job."
    jump wcb_janitor_game_loop

label wcb_chef_game_loop:
    hide character animegirl
    show character lily
    mc "I am a WcBonalds chef now,"
    mc "I'm making $20 an hour. Yippee!"
    jump expenses

label wcb_janitor_game_loop:
    hide character animegirl
    show character lily
    mc "Yay, I'm a WcBonalads janitor now *dies inside*"
    mc "I am making $16.50 an hour."
    jump expenses

label expenses:
    scene black with fade
    pause 1.0
    show text "One year has passed..." with dissolve
    $ year += 1
    if year - wcb_year_start == 2:
        $ hs_job_level = 1

    if year - wcb_year_start == 5:
        $ hs_job_level = 2

    $ wage = wage_calc()
    $ money += salary_calc(wage)
    pause 2.0


label conclusion:
    scene bg home
    with dissolve
    mc "I made some money but I am still not making enough."
    mc "I want to make a decision between saving my hard earned money or spending it."
    menu:
        "Save money":
            jump emergency
        "Upgrade lifestyle (Cost: $20,000)":
            jump consequence

label emergency:
    scene bg hospital
    with dissolve
    mc "I got into a car accident."
    mc "I saved my money for a rainy day and was able to pay for my hospital bills."
    $ money -= 10000
    scene black with fade
    "Years passed..."
    $ year = 2070
    pause 1.0
    "Retirement"
    pause 2.0
    jump retirement

label consequence:
    scene bg mansion with fade
    mc "I spent my money on a new lifestyle."
    $ money -= 20000
    scene black with fade
    "Years passed..."
    pause 1.0
    "Retirement"
    pause 2.0
    jump retirement