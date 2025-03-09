label retire_text:
    "I've worked so hard."
    "I've put in a lot of work, and I've gotten paid well for it."
    "I think it's finally time to retire."
    "*sigh*..."
    scene bg WcB

    mc "I just finished my last day..."
    W "Awww... we're going to miss you, Lily!"
    mc "It's bittersweet, but I\"ll enjoy retirement."
    W "Here's your last paycheck."
    $ last_pay = int((wage*8)*0.91)
    mc "$[last_pay]. My final paycheck."
    $ money += last_pay

    scene bg home
    with wipeleft
    mc "Time to retire."
    jump retirement
    


label ask_about_investing:
    "I should probably check my stocks..."
    menu:
        "Check stocks":
            if noob:
                $ calling_day1 = True
                call day1_invest from _call_day1_invest_3
            else:
                call other_invest from _call_other_invest_3
        "Ignore":
            pass
    return

mc "I think I've worked long enough."
mc "It's much harder, and managing this business takes a toll."
mc "I'm finally going to retire."
label wage_calc:
    python:
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
    return

label salary_calc:
    $ hrs_per_week = 40
    $ weekly_income = wage * hrs_per_week
    $ salary = weekly_income * 52
    return

label wcb_chef_job:
    mc "I got the chef job."
    $ job = "Chef"
    $ wage = 20
    call wage_calc from _call_wage_calc
    call salary_calc from _call_salary_calc

    jump wcb_chef_game_loop

label wcb_janitor_job:
    mc "I got the janitor job."
    $ job = "Janitor"
    $ wage = 16.50

    call wage_calc from _call_wage_calc_1
    call salary_calc from _call_salary_calc_1
    
    jump wcb_janitor_game_loop

label wcb_chef_game_loop:
    scene bg home
    show character lily
    if year - wcb_year_start == 0:
        mc "I am a WcBonalds [job] now."
        mc "I'm making $[wage] an hour. Yippee!"
    scene bg WcB
    "Work is exhausting."
    "But, I have to pay the bills."
    scene bg home
    
    if year == 2060:
        mc "I am thinking about retiring soon."
    elif year == 2070:
        jump retire_text
    else:
        jump ask_about_investing

    jump expenses

label wcb_janitor_game_loop:
    hide character animegirl
    show character lily
    if year - wcb_year_start == 0:
        mc "Yay, I'm a WcBonalads janitor now *dies inside*"
        if wage == 16.5:
            mc "I am making $16.50 an hour."
        else:
            mc "I am making $[wage] an hour."

    if year == 2060:
        mc "I am thinking about retiring soon."
        call ask_about_investing from _call_ask_about_investing_1
    
    elif year == 2070:
        call retire_text from _call_retire_text_1
    
    else:
        call ask_about_investing from _call_ask_about_investing_2

    jump expenses

label expenses:
    call year_over from _call_year_over_3

    scene black with fade

    if year - wcb_year_start == 2:
        $ hs_job_level = 1

    if year - wcb_year_start == 5:
        $ hs_job_level = 2

    call wage_calc from _call_wage_calc_2
    call salary_calc from _call_salary_calc_2
    jump wcb_chef_game_loop