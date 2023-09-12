# Alien Invasion
# Autor: Jörg Kantel
# Hintergrundbilder: Visual Novel Backgrounds Office_BG Set by quarkyifu:
# https://quarkyifu.itch.io/visual-novel-backgrounds-office-bg-set
# und eigene Photos
# Avatare: Clarissa Helps' 14 Sprite Pack (CC-BY-SA 4.0):
# https://lemmasoft.renai.us/forums/viewtopic.php?f=52&t=30896


image bg_buero_hans_1 = "buero_hans_1.png"
image bg_buero_hans_2 = "buero_hans_2.png"
image bg_buero_holger = "buero_kern.png"
image bg_buero_sylvia = "buero_sylvia.png"
image bg_im_park_1    = "im_park_1.jpg"

# Character Images
## Hans Blond
image Hans           = "hans.png"
image Hans Talking   = "hans-surprised.png"
image Hans Sad       = "hans-sad.png"
image Hans Angry     = "hans-angry.png"
image Hans Annoyed   = "hans-annoyed.png"
image Hans Concerned = "hans-concerned.png"
## Holger Kern
image Holger         = "holger.png"
image Holger Talking = "holger-talking.png"
image Holger Mad     = "holger-mad.png"
## Sylvia Berlin
image Sylvia         = "sylvia.png"
image Sylvia Upset   = "sylvia-upset.png"
image Sylvia Talking = "sylvia-talking.png"
## Felix Leiter
image Felix          = "felix.png"
image Felix Talking  = "felix_talking.png"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define hans   = Character("Hans", color = "#a62611")
define holger = Character("Holger", color = "#999900")
define sylvia = Character("Sylvia", color = "#990000")
define felix  = Character("Felix", color = "#990099")

# Hier beginnt das Spiel.
label start:

    scene bg_buero_hans_1

    show Hans at center with dissolve
    hans "Mein Name ist Hans, Hans Blond."

    show Hans Talking at center
    hans "Ich arbeite in der IT des Landesamtes für Verfassungsschutz in Berlin"
    show Hans Concerned
    hans "Meine Chefin Sylvia Berlin hat mich zu einem Meeting bestellt."

    show Hans Annoyed at center
    "Hans verläßt den Raum"
    hide Hans with dissolve

    ""

    jump startmeeting

# Start Meeting
# Teilnehmer: Sylvia Berlin, Hans Blond
label startmeeting:

    scene bg_buero_sylvia

    show Sylvia at center with dissolve
    "Klopf, Klopf …"
    sylvia "Herein!"
    show Hans at left 
    with moveinleft
    show Sylvia Talking at center
    sylvia "Mein lieber Herr Blond, die Bürgermeisterin hat mich gebeten, ihr für die anstehende Wahlwiederholung meinen besten IT-Spezialisten zur Verfügung zu stellen."
    sylvia "Und da habe ich natürlich an Sie gedacht. Sie können morgen gleich anfangen."
    show Sylvia Upset at center
    "Hans war sofort klar: Damit wollte Sylvia ihn als Konkurrenten um die Referatsleitung kaltstellen."

    menu:
        "Doch was sollte er tun?"

        "Wütend den Raum verlassen und die Tür hinter sich zuknallen?":
            jump ende1
        "Gute Miene zum bösen Spiel machen und der Versetzung zustimmen?":
            jump versetzung_zugestimmt


label ende1:

    "Hans verließ wütend den Raum und schlug die Tür mit einem lauten Knall hinter sich zu."
    hide Hans with moveoutleft
    ""

    scene bg_buero_hans_2
    with dissolve

    show Hans with moveinright
    "Kaum war Hans wieder in seinem Büro, als er auch schon eine Email bekam."
    "Darin stand in dürren Worten, daß sein Antrag auf Beförderung abgelehnt sei."
    show Hans Sad
    "Tja Hans, zu hoch gepokert."
    hide Hans with dissolve
    "Das ist das viel zu frühe Ende!"

return

label versetzung_zugestimmt:

    show Hans Talking at left
    hans "Dann werde ich mal mein Büro räumen."
    show Hans at left
    ""
    hide Hans with moveoutleft
    ""

    scene bg_buero_hans_2
    with None

    show Hans Annoyed
    with moveinright
    hans "(zu sich) Sylvia ist zwar ein intrigantes Biest, aber süß ist sie dennoch. ❤️"
    hide Hans with dissolve

    "Hans beschloß, Feierabend zu machen und nach Hause zu gehen."

return
