# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"

image herbst = "herbst1870.jpg"
image joerg = "joerg2.png"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define me = Character('Jörg', color="#c8ffc8")


# Hier beginnt das Spiel.
label start:
    
    scene herbst
    
    show joerg

    "Es ist der Herbst des Jahres 2022"

    "Die Weltgeschichte sieht beschissen aus."
    
    "In der Ukraine tobt ein Krieg und der deutsche Kanzler reicht den Blutscheichs die Hand."
    
    "In Italien kommen die Faschisten an die Macht."

    return
