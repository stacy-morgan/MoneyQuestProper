init python:
    def format_money(value):
        return "${:,.0f}".format(value)

label retirement:
    mc "I've been working for so long, I feel like it's time to retire!"
    $ total_assets = money + calculate_portfolio_value()
    $ total_assets_str = format_money(total_assets)
    if house:
        jump retireComfortable
    if total_assets < 10000:
        jump retireLess10000
    elif total_assets < 100000:
        jump retireBetween
    else:
        jump retireComfortable

label retireLess10000:
    scene bg broke_art_room
    if year != 2025:
        show character oldlily
    else:
        show character lily
    mc "Aw man, I really should have taken some more care with saving money when I had the chance!"
    mc "I only have [total_assets_str] in total assets. I'm basically broke."
    mc "I'm not sure what I can do now."
    mc "Hopefully it gets better in the future."

    scene black with fade
    pause 1.0
    $ year += 5
    show text "5 years later..." with dissolve
    pause 2.0

    scene bg lily_rip
    "Lily died homeless and broke..."
    "R.I.P."
    "You have lost, try to play again."
    jump end

label retireBetween:
    scene bg winter_room
    show character oldlily
    mc "Ok so I'm not too broke, but I don't have that much money saved up."
    mc "I ended up with [total_assets_str] in total assets."
    mc "At least I have this place, but I wish I could buy whatever I wanted."
    mc "Maybe in the next life, I could make a lot more and travel the world!"

    scene black with fade
    pause 1.0
    show text "Many years later..." with dissolve
    pause 2.0

    scene bg winter_room
    "Lily died peacefully in her house,"
    "She missed out on an opportunity to travel the world, but at least she had a place to live."
    "Try to play again so Lily can travel the world in her retirement."
    jump end

label retireComfortable:
    scene bg expensive_room
    show character oldlily
    mc "Yay! I saved up a ton of money and assets!"
    mc "I ended up with [total_assets_str] in total assets."

    scene bg beach_vacation
    show character oldlily
    mc "I can travel where I want, and live comfortably."

    scene bg expensive_room
    show character oldlily
    mc "This should last me a long while, but I still should be cautious."
    mc "I can have a long and relaxing retirement."

    "Lily lived a long a fulfilling life."
    jump end
