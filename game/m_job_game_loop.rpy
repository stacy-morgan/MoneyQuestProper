label wcb_chef_job:
    mc "I got the job."
    $ yrs_until_promotion = 2
    jump wcb_chef_game_loop

label wcb_janitor_job:
    mc "I got the job."
    $ yrs_until_promotion = 2
    jump wcb_janitor_game_loop

label wcb_chef_game_loop:
    hide character animegirl
    show character lily
    mc "I am a WcBonalads chef now,"
    mc "I'm making $20 an hour. Yippee!"
    jump expenses_chef

label wcb_janitor_game_loop:
    hide character animegirl
    show character lily
    mc "Yay, I'm a WcBonalads janitor now *dies inside*"
    mc "I am making $16.50 an hour."
    jump expenses_janitor

label expenses_janitor:
    scene black with fade
    pause 1.0
    show text "One year has passed..." with dissolve
    $ year += 1
    $ money += 10320
    pause 2.0
    jump summary_janitor

label expenses_chef:
    scene black with fade
    pause 1.0
    show text "One year has passed..." with dissolve
    $ year += 1
    $ money += 17600
    pause 2.0
    jump summary_chef

label summary_janitor:
    pause 1.0
    show bg home
    "You make approximately $10k a year, which is not ideal."
    "More income would be nice, but it might not be a great idea."
    "Since you're not making much money, you won't have much to put in."
    "Less in means lower returns, so you might be better off living on what you have now."
    "Would you like to get a side hobby?"
    menu:
        "Learn high-paying skills (Work 5 hours less)":
            jump learn_skills
        "Start career on social media (Work 5 hours less)":
            jump social_media
        "Continue working":
            jump expenses_janitor_keep

label summary_chef:
    pause 1.0
    show bg home
    "You make approximately $17k a year, which is not ideal."
    "Would you like to get a side hobby?"
    menu:
        "Learn high-paying skills (Work 5 hours less)":
            jump learn_skills_c
        "Start career on social media (Work 5 hours less)":
            jump social_media_c
        "Continue working":
            jump expenses_chef_keep

label learn_skills:
    scene bg LearnToCode
    with dissolve
    "You have learned high-paying skills."
    "However, it took a couple hours off your job."
    $ year += 1
    $ money += 6030
    jump probability_learn_skills

label social_media:
    scene bg SocialMedia
    with dissolve
    "You try to become a social media influencer."
    "However, it took a couple hours off your job."
    $ year += 1
    $ money += 6030
    jump probability_social_media

label learn_skills_c:
    scene bg LearnToCode
    with dissolve
    "You have learned high-paying skills."
    "However, it took a couple hours off your job."
    $ year += 1
    $ money += 12400
    jump probability_learn_skills_c

label social_media_c:
    scene bg SocialMedia
    with dissolve
    "You have learned high-paying skills."
    "However, it took a couple hours off your job."
    $ year += 1
    $ money += 12400
    jump probability_social_media_c

label expenses_janitor_keep:
    "You continue to work as a janitor. You must use your budget wisely, barely surviving on $10k."
    jump conclusion

label expenses_chef_keep:
    "You continue to work as a chef. You must use your budget wisely, barely surviving on $17k."
    jump conclusion

label probability_learn_skills:
    $ import random
    $ chance = random.random()

    scene black with fade
    pause 1.0
    show text "Another year has passed..." with dissolve
    if chance < 0.5:  
        pause 2.0
        show text "You have no success in finding a job with your new skills." with dissolve
        pause 2.0
        show text "You return to your normal hours." with dissolve
        pause 2.0
        show text "On the bright side, you got promoted." with dissolve
        $ year += 1
        $ money += 13440
        jump conclusion
    else:
        pause 2.0
        show text "You found a new job with your new skills." with dissolve
        $ year += 1
        $ money += 13440
        pause 2.0
        jump conclusion

label probability_social_media:
    $ import random
    $ chance = random.random()

    scene black with fade
    pause 1.0
    show text "Another year has passed..." with dissolve
    if chance < 0.5:  
        pause 2.0
        show text "You have no success in becoming a social media influencer." with dissolve
        pause 2.0
        show text "You return to your normal hours." with dissolve
        pause 2.0
        show text "On the bright side, you got promoted." with dissolve
        $ money += 13440
        $ year += 1
        pause 2.0
        jump conclusion
    else:
        pause 2.0
        show text "You have become a successful social media influencer." with dissolve
        pause 2.0
        $ money += 17740
        $ year += 1
        jump conclusion

label probability_learn_skills_c:
    $ import random
    $ chance = random.random()

    scene black with fade
    pause 1.0
    show text "Another year has passed..." with dissolve
    if chance < 0.5:  
        pause 2.0
        show text "You have no success in finding a job with your new skills." with dissolve
        pause 2.0
        show text "You return to your normal hours." with dissolve
        pause 2.0
        show text "On the bright side, you got promoted." with dissolve
        $ money += 21760
        $ year += 1
        pause 2.0
        jump conclusion
    else:
        pause 2.0
        show text "You found a new job with your new skills." with dissolve
        $ money += 22990
        $ year += 1
        pause 2.0
        jump conclusion

label probability_social_media_c:
    $ import random
    $ chance = random.random()

    scene black with fade
    pause 1.0
    show text "Another year has passed..." with dissolve
    if chance < 0.5:  
        pause 2.0
        show text "You have no success in becoming a social media influencer." with dissolve
        pause 2.0
        show text "You return to your normal hours." with dissolve
        pause 2.0
        show text "On the bright side, you got promoted." with dissolve
        $ money += 21760
        $ year += 1
        pause 2.0
        jump conclusion
    else:
        pause 2.0
        show text "You have become a successful social media influencer." with dissolve
        $ money += 21990
        $ year += 1
        pause 2.0
        jump conclusion

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