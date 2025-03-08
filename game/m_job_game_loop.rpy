label wcb_chef_job:
    mc "I got the job."
    $ yrs_until_promotion = 2
    jump wcb_chef_game_loop

label wcb_janitor_job:
    mc "I got the job."
    $ yrs_until_promotion = 2
    jump wcb_janitor_game_loop

label wcb_chef_game_loop:
    mc "I am a chef now."
    mc "I am making $20 an hour. Yippee!"
    jump expenses_chef

label wcb_janitor_game_loop:
    mc "Yay, I'm a WcBonalads janitor now *dies inside*"
    mc "I am making $16.50 an hour."
    jump expenses_janitor

label expenses_janitor:
    
    "One year has passed..."
    "Yearly savings: $34,320"
    "Yearly expenses: $24,000" 
    "Remaining savings: $10,320"
    jump summary_janitor

label expenses_chef:
    "One year has passed..." 
    "Yearly savings: $41,600" 
    "Yearly expenses: $24,000" 
    "Remaining savings: $17,600"
    jump end

label summary_janitor:
    "You make approximately $10k a year, which is not ideal."
    "Would you like to get do a side hobby?"
    menu:
        "Learn high-paying skills (Take time off job)":
            jump learn_skills
        "Start career on social media (Take time off job)":
            jump social_media
        "Continue working":
            jump expenses_janitor_keep

label learn_skills:
    scene bg LearnToCode
    with dissolve
    "You have learned high-paying skills."
    "However, it took a couple hours off your job."
    "Your new yealy earnings is $6,030."
    jump probability_learn_skills

label social_media:
    "You have try to become a social media influencer."
    "However, it took a couple hours off your job."
    "Your new yealy earnings is $6,030."
    jump probability_social_media

label expenses_janitor_keep:
    "You continue to work as a janitor. You must use your budget wisely, barely surviving on $10k."
    jump conclusion

label probability_learn_skills:
    $ import random
    $ chance = random.random()

    if chance < 0.5:  
        "You have no success in finding a job with your new skills."
    else:
        "You found a new job with your new skills."
        "You are now making $18,740 after expenses."
    jump end

label probability_social_media:
    $ import random
    $ chance = random.random()

    if chance < 0.5:  
        "You have no success in becoming a social media influencer."
    else:
        "You have become a successful social media influencer."
        "You are now making $17,740 after expenses."
    jump end

label conclusion:
    mc "I made some money but I am still poor."