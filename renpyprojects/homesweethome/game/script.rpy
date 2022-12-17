# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"

image heineken = "bierwerbung"
image night = "caratnight"
image milk = "milkman"
image fritz = "onkelfritz"
image eisenbahn = "montparnasse"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define p = Character('Player', color="#c8ffc8")


# Hier beginnt das Spiel.
label start:

    scene night

    "Es geschah in einer dunklen und stürmischen Nacht. Es regnete in Strömen und das Radio spielte alte Swing-Nummern."

    "Plötzlich tauchte im Licht der Scheinwerferkegel ein Wegweiser auf."

    menu:
        "Rechts ging es nach Dinkelsbach":
            jump dinkelsbach

        "Links nach Lüdenscheid":
            jump luedenscheid

        "Geradeaus ging es weiter nach Oberhausen":
            jump oberhausen


label dinkelsbach:

    scene milk

    "Dinkelsbach ist die Stadt der Milchmänner! Du bist hier falsch!"

    menu: 
        "Gutes Bier gibt es nur in Lüdenscheid.":
            jump luedenscheid
    

label luedenscheid:

    scene bierwerbung

    "Doch wer will nach einem Bier noch in Lüdenscheid bleiben? Die Frau an Deiner Seite erinnert Dich an Dein kuscheliges Bett."

    menu:

        "Also ab nach Hause":
            jump home

        "Oder doch lieber noch ein Bier?":
            jump luedenscheid

label oberhausen:

    scene eisenbahn

    "Der Bahnhof in Oberhausen ist eine Sackgasse!"

    menu:
        
        "Schnell zurück an den Start!":
            jump start
   
label home:

    scene fritz

    "Home, Sweet Home!"
    
    return
