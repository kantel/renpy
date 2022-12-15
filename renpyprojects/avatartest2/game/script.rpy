# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"

image herbst = "herbst1870.jpg"
image joerg = "joerg_confused.png"


# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define me = Character('Jörg', color="#c8ffc8")


# Hier beginnt das Spiel.
label start:

    scene herbst
    
    show joerg

    "Es ist der Dezember 2022,"

    "Eine schöne, aber korrupte Vizepräsidentin des Europa-Parlaments wurde verhaftet."

    return
