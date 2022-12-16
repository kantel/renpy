# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"
image abbey = "bg abbey_drawing.jpg"
image gothic_girl_ful = "gothic_ful.png"
image gothic_girl_half = "gothic_half.png"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define g = Character('Goth Girl', color="#eba20e")


# Hier beginnt das Spiel.
label start:

    scene abbey

    show gothic_girl_ful

    g "Es ist ein wenig unheimlich hier …"
    g "Sollten wir nicht besser verschwinden?"

    return
