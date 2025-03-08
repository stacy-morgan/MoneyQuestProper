label buy_car:
    scene bg nissan
    mc "My grandpa gave me a car..."
    mc "But it's so ugly."
    mc "I am going to get no girls with this car."
    mc "I want to get something fancy! I've heard that you can get a really fancy car for $50K."
    scene bg porsche
    with wipeleft
    mc "I really want this fancy Porsche to flex my wealth!"
    mc "But I don't know if it's the best thing to do with this money."
    menu:
        mc "What should I do?"

        "Buy the Porsche (-$50,000)":
            jump yes_car
        "Save the money for something more useful":
            jump no_car

label yes_car:
    $ money -= 50000
    mc "This car is so nice! **vroom vroom**"
    scene bg atm
    with dissolve
    mc "But now my bank account is empty..."
    scene bg home
    show character lily
    mc "My parents are furious!! Now they are going to kick me out :("
    mc "They told me to get a job. Ugh!"
    jump get_job

label no_car:
    scene bg home
    show character lily
    mc "Now I have all this money, if I'm not going to buy a car, what should I do with it??"
    mc "Hmm... I could go to college, or maybe put some money in the stock market."
    menu:
        "Get a Bachelor's degree":
            jump degree
        "Invest in stocks":
            jump invest
