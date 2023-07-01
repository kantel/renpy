# Alien Invasion
# Autor: Jörg Kantel
# Hintergrundbilder: Visual Novel Backgrounds Office_BG Set by quarkyifu:
# https://quarkyifu.itch.io/visual-novel-backgrounds-office-bg-set
# und eigene Photos
# Characters: Selbsterstellt mit Framic: https://framiq.com/

# Background Images
image bg_buero_reginald_1 = "buero_reginald_1.png"
image bg_buero_reginald_2 = "buero_reginald_2.png"
image bg_buero_sylvia     = "buero_sylvia.png"
image bg_im_park_1           = "im_park_1.jpg"

# Character Images
## Reginald Blond
image Reginald          = "reginald_neutral.png"
image Reginald Talking  = "reginald_neutral_talking.png"
image Reginald Sad      = "reginald_sad.png"
image Reginald Very Sad = "reginald_very_sad.png"
image Reginald Curious  = "reginald_curious.png"
## Sylvia Berlin
image Sylvia            = "sb_neutral.png"
image Sylvia Happy      = "sb_happy.png"
image Sylvia Talking    = "sb_talking"
## Felix Leiter
image Felix             = "felix_leiter_neutral.png"
image Felix Talking     = "felix_leiter_talking.png"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define reginald = Character("Reginald", color = "#a62611")
define sylvia   = Character("Sylvia", color = "#990000")
define felix    = Character("Felix Leiter", color = "#990099")

# Hier beginnt das Spiel.
label start:

    scene bg_buero_reginald_1
    
    show Reginald at right with dissolve
    reginald "Mein Name ist Reginald, Reginald Blond."

    show Reginald Talking at right
    reginald "Ich arbeite in der IT des Landesamtes für Verfassungsschutz in Berlin"
    reginald "Meine Chefin Sylvia Berlin hat mich zu einem Meeting gerufen."

    show Reginald at right
    "Reginald verläßt den Raum."
    hide Reginald with dissolve
    ""

    jump startmeeting

# Start Meeting
# Teilnehmer: Sylvai Berlin, Reginald Blond
label startmeeting:

    scene bg_buero_sylvia

    show Sylvia at right with dissolve
    "Klopf, Klopf …"
    sylvia "Herein!"
    show Reginald at left 
    with moveinleft
    show Sylvia Talking at right
    sylvia "Mein lieber Herr Blond, die Bürgermeisterin hat mich gebeten, ihr für die anstehende Wahlwiederholung meinen besten IT-Spezialisten zur Verfügung zu stellen."
    sylvia "Und da habe ich natürlich an Sie gedacht. Sie können morgen gleich anfangen."
    show Sylvia at right
    "Reginald war sofort klar: Damit wollte Sylvia ihn als Konkurrenten um die Referatsleitung kaltstellen."

    menu:
        "Doch was sollte er tun?"

        "Wütend den Raum verlassen und die Tür hinter sich zuknallen?":
            jump ende1
        "Gute Miene zum bösen Spiel machen und der Versetzung zustimmen?":
            jump versetzung_zugestimmt

label ende1:

    "Reginald verließ wütend den Raum und schlug die Tür mit einem lauten Knall hinter sich zu."
    hide Reginald with moveoutleft
    ""
    scene bg_buero_reginald_2
    with dissolve

    show Reginald with moveinright
    "Kaum war Reginald wieder in seinem Büro, als er auch schon eine Email bekam."
    "Darin stand in dürren Worten, daß sein Antrag auf Beförderung abgelehnt sei."
    show Reginald Very Sad
    "Tja Reginald, zu hoch gepokert."
    hide Reginald with dissolve
    "Das ist das viel zu frühe Ende!"


return

label versetzung_zugestimmt:

    show Reginald Talking at left
    reginald "Dann werde ich mal mein Büro räumen."
    show Reginald at left
    ""
    hide Reginald with dissolve
    ""

    scene bg_buero_reginald_2
    with None

    show Reginald Curious
    with moveinright
    reginald "(zu sich) Sylvia ist zwar ein intrigantes Biest, aber süß ist sie dennoch. ❤️"
    hide Reginald with dissolve

    "Reginald beschloß, Feierabend zu machen und nach Hause zu gehen."

    jump im_park_1

label im_park_1:

    scene bg_im_park_1
    with None

    show Reginald at left
    with moveinleft

    "Der Weg nach Hause führte Reginald wie jeden Abend durch einen kleinen Park. Dort fiel ihm ein gutgekleideter Mann auf, der ihn zu beobachten schien."

    show Felix at right
    with moveinright

    "In der Nähe einer zufällig dort stehenden Baumaschiene sprach ihn der Fremde an."

    show Felix Talking at right

    felix "Junger Mann, was immer in der nächsten Zeit passieren mag, gehen sie in den Untergrund!"

    hide Felix with moveoutright
    hide Reginald
    show Reginald Curious at right
    with move 

    "Dann verschwand er wieder und lies Reginald verwirrt zurück."

    "Reginald hatte jetzt genug und beschloß, endgültig nach Hause zu gehen …"

    hide Reginald with moveoutright

    jump reginald_home_1

label reginald_home_1:

    scene black
    with None

    show Reginald with moveinright

    "Zu Hause angekommen mixte sich Reginald erst einmal einen Drink um die Ereignisse des Tages zu verarbeiten."

    hide Reginald with dissolve

    "Fortsetzung folgt …"

    return
