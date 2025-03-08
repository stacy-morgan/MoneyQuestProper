label cs_job:
    "You're homeless now."
    jump end

label art_job:
    mc "I really want to make art now, but I'm worried that I won't make enough money to pay for an apartment."
    menu:
        mc "Should I get a job at WcBonalds to make some money or put my full focus on my art?"

        "Work at WcBonalds":
            jump get_job
        "Try to be an artist":
            jump art_2

label art_2:
    show bg broke_art_room
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
    mc "Vroom imma fly plain"
    jump end
