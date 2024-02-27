# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"
image lilly          = "lilly_neutral.png"
image lilly angry    = "lilly_angry.png"
image lilly blushing = "lilly_blushing.png"
image lilly confused = "lilly_blushing.png"
image lilly crying   = "lilly_crying.png"
image lilly sad      = "lilly_sad.png"
image lilly smiling  = "lilly_smiling.png"
image lilly talking  = "lilly_talking.png"

image kiss           = "kiss.png"

# Backgrounds
image zauberwald23   = "zauberwald23.jpg"
image zauberwald24   = "zauberwald24.jpg"


# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define lilly = Character("Lilly", color="#c8ffc8")


# Hier beginnt das Spiel.
label start:

    scene zauberwald23
    
    show lilly with dissolve
    ""
    lilly "Hallo, Fremder!"

    show lilly talking
    lilly "Es ist nicht immer einfach, eine Figur in einem Spiel zu sein."

    show lilly sad
    lilly "Man ist oft sehr allein, niemand spricht mit einem."

    show lilly smiling
    lilly "Aber jetzt bist Du ja da."
    lilly "Gib mir einen kleinen Kuß. 😘"

    show kiss at top
    ""
    hide kiss
    show lilly blushing
    lilly "Oooh!"
    lilly "Das ist der Beginn einer wunderbaren Freundschaft."

    hide lilly with dissolve
    "Fortsetzung folgt (vielleicht) …"
    return
