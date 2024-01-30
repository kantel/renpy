# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"

image bg = "background.png"
image sylvia = "sylvia01.png"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define s = Character("Sylvia", color="#c8ffc8")


# Hier beginnt das Spiel.
label start:

    scene bg
    show sylvia

    s "Dies ist Ren'Py 8.2.0 🎉"

    s "Zeit, an »Berlin Attack« weiterzuarbeiten!"


    return
