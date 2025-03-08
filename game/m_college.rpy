label degree:
    mc "I need to apply to colleges now, but before that I need to choose a major."
    menu:
        "Choose a major"

        "Computer Science":
            $ major = "Computer Science"
        "Liberal Arts":
            $ major = "Liberal Arts"
        "Aerospace Engineering":
            $ major = "Aerospace Engineering"
    mc "Now I need to apply to colleges."

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

    show bg college
    show character lily
    mc "I can't believe I'm graduating already. What will I do with my [major] degree?"

    if major == "Computer Science":
        mc "I should probably get a job at a top tech company."
        jump cs_job
    elif major == "Liberal Arts":
        mc "I'm not really sure what to do with this degree, maybe I'll have to work at WcBonalds."
        jump art_job
    elif major == "Aerospace Engineering":
        mc "I heard that as an [major] major, I can work on planes or rockets!"
        jump aerospace_job

    mc "I guess I should probably get a job."
