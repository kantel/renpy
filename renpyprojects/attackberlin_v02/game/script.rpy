# Berlin Attack v0.2
# Prototyp eines Versuchs, die Bilder mit Hilfe von Bildgeneratoren der Künstlichen Intelligenz zu generieren.
# Autor: Jörg Kantel
# Bilder: Erstellt mit Scenario https://app.scenario.com/

image bg_buero_hans  = "office_hans.png"
image bg_buero_syvia = "office_sylvia.png"
image bg_im_park     = "im_park_1.jpg"

# Character Images
## Hans Blond
image Hans         = "hansblond_neutral.png"
image Hans Smiling = "hansblond_smiling.png"
image Hans Angry   = "hansblond_angry.png"
image Hans Sad     = "hansblond_sad.png"
## Sylvia Berlin
image Sylvia         = "sylviaberlin_neutral.png"
image Sylvia Smiling = "sylviaberlin_smiling.png"
image Sylvia Angry   = "sylviaberlin_angry.png"
## Felix Leiter
image Felix = "felixleiter_neutral.png"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define hans   = Character("Hans", color = "#a62611")
define sylvia = Character("Sylvia", color = "#990000")
define felix  = Character("Felix", color = "#990099")


# Hier beginnt das Spiel.
label start:

    scene bg_buero_hans

    show Hans Smiling at center with moveinright
    hans "Mein Name ist Blond, Hans Blond."

    show Hans at center
    hans "Ich arbeite in der IT des Landesamtes für Verfassungsschutz in Berlin"
    hans "Meine Chefin Sylvia Berlin hat mich zu einem Meeting bestellt."

    "Hans verläßt den Raum …"
    hide Hans with moveoutright

    ""

    jump startmeeting

# Start Meeting
# Teilnehmer: Sylvia Berlin, Hans Blond
label startmeeting:

    scene bg_buero_syvia

    show Sylvia at right with dissolve
    "Klopf, Klopf …"
    sylvia "Herein!"
    show Hans at left 
    with moveinleft

    show Sylvia Smiling at right
    sylvia "Mein lieber Herr Blond, die Bürgermeisterin hat mich gebeten, ihr für die anstehende Wahlwiederholung meinen besten IT-Spezialisten zur Verfügung zu stellen."
    sylvia "Und da habe ich natürlich an Sie gedacht. Sie können morgen gleich anfangen."
    show Sylvia at right

    show Hans Angry at left
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
    hide Sylvia with moveoutright

    scene bg_buero_hans
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

    show Hans at left
    hans "Dann werde ich mal mein Büro räumen."
    show Hans Smiling at left
    ""
    hide Hans with moveoutleft
    ""
    hide Sylvia with moveoutright

    scene bg_buero_hans
    with None

    show Hans Smiling
    with moveinright
    hans "(zu sich) Sylvia ist zwar ein intrigantes Biest, aber süß ist sie dennoch. ❤️"
    

    "Hans beschloß, Feierabend zu machen und nach Hause zu gehen."

    hide Hans with moveoutleft
    ""

    jump im_park_1

label im_park_1:

    scene bg_im_park with None

    show Hans at left
    with moveinleft

    "Der Weg nach Hause führte Hans wie jeden Abend durch einen kleinen Park. Dort fiel ihm ein gutgekleideter Mann mit einem riesigen Schnauzbart auf, der ihn zu beobachten schien."

    show Felix at right
    with moveinright

    "Am Rosengarten sprach ihn der Schnauzbart an."

    felix "Junger Mann, was immer in der nächsten Zeit passieren mag, gehen sie in den Untergrund!"

    hide Felix with moveoutright
    show Hans Angry at left

    "Dann verschwand er wieder und lies Hans verwirrt zurück."

    "Hans hatte jetzt genug und beschloß, endgültig nach Hause zu gehen …"

    hide Hans with moveoutright

    jump reginald_home_1

label reginald_home_1:

    scene black
    with None

    show Hans with moveinright

    "Zu Hause angekommen mixte sich Hans erst einmal einen Drink um die Ereignisse des Tages zu verarbeiten."

    hide Hans with dissolve

    "Fortsetzung folgt …"

    return





return
