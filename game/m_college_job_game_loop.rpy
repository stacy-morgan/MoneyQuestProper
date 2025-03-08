label cs_job:
    "You're homeless now"
    jump end

label art_job:
    menu:
        "What job do you want?"

        "Get a job at WcBonalds":
            jump get_job
        "Try to be an artist":
            jump art_2

label art_2:
    mc "I've been making art for 10 years now and I'm broke."

    menu:
        "What should I do?"

        "Get a job at WcBonalds":
            jump get_job
        "Suck feet instead":
            jump suck_feet

label suck_feet:
    qqq "Those feet look mighty suckable. ;-}"
    qqq "MMMMhhhhh, ahhhhh, like that"
    jump end

label aerospace_job:
    menu:
        "What job do you want?"

        "Airplane Technician":
            $ job = "Airplane Technician"
        "Rocket Engineer":
            $ job = "Rocket Engineer"
    mc "Vroom imma fly plain"
    jump end
