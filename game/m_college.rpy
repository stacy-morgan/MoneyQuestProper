label degree:
    mc "If I'm going to college I need to choose my major."
    mc "I've heard that you can make a lot of money with a Computer Science or Aerospace Engineering degree,"
    mc "But I've always had a passion for doing art."
    menu:
        mc "What major should I apply for?"

        "Computer Science":
            $ major = "Computer Science"
        "Liberal Arts":
            $ major = "Liberal Arts"
        "Aerospace Engineering":
            $ major = "Aerospace Engineering"
    mc "Now I need to apply to colleges..."

    scene black with fade
    pause 1.0
    show text "A few months later..." with dissolve
    pause 2.0

    show bg home
    show character lily

    mc "I got accepted to Sigma College!"
    mc "I can't wait to learn [major] there."

    show bg college
    show character lily
    mc "It's my first day, I'm so excited!"

    scene black with fade
    pause 1.0
    show text "A few years later..." with dissolve
    pause 2.0

    show bg graduation
    mc "I can't believe I'm graduating already. What will I do with my [major] degree?"

    show character lily

    if major == "Computer Science":
        mc "I should probably get a job at a top tech company."
        jump cs_job
    elif major == "Liberal Arts":
        jump art_job
    elif major == "Aerospace Engineering":
        jump aerospace_job

    mc "I guess I should probably get a job."
