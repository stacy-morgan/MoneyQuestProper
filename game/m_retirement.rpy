label retirement:
    mc "Man I've feel like it's time to retire!"
    if money < 10000:
        jump retireLess10000
    elif money >= 10000:
        if money < 100000:
            jump retireBetween
    elif money > 1000000:
        jump retireComfortable

label retireLess10000:
    mc "Nuts, I should have taken some more care with saving money when I had the chance!"
    mc "I'm not sure what I can do now."
    mc "Hopefully it gets better in the future."

    "5 years..."
    "Lily died homeless and broke..."
    "Try again"
    jump end
    #show a picture of a grave stone saying that im homeless or somthing like that

label retireBetween:
    mc "Ok so I'm not to broke, but I don't have that much money saved up."
    if house == True:
        mc "Atleast I have this house, but I wish I could buy whatever I wanted."
        mc "Maybe in the next life, I could make a lot more and travel the world!"

        "Many Years Later"

        "Lily died in her house, hoping to travel the world."

        "Try again"
        jump end

    elif house == False:
        jump retireLess10000

label retireComfortable:
    mc "Let's goo! I saved up over $100,000!"
    mc "I can travel where I want, and live comfortably."
    mc "This should last me a long while, but I still should be cautious."
    mc "I can live a good life, but I'll use what I learned in my past to better my life."

    "Lily lived a long a fufiling life."
    "We won!"
    jump end
