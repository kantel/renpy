# Bilder
image bg abbey_grounds = "bg abbey_grounds.jpg"
image bg abbey_drawing = "bg abbey_drawing.jpg"
image alice = "maid.png"
image hercule = "hercule.png"

# Personen
define a = Character("Alice", color = "#c8ffc8")
define h = Character("Hercule", color = "#ee1100")

# Hier beginnt das Spiel. Label "Start" ist obligatorisch!
label start:

    scene bg abbey_grounds
    show hercule at left
    with slideleft
    show alice at right
    with dissolve

    a "Guten Tag, Monsieur Poirot, die Herrschaften erwarten sie bereits."
    a "Darf ich Sie ins Haus bitten?"
    pause 1.0
    hide alice
    with dissolve
    
    menu:
    
        "Ja, gerne. Ich folge Ihnen.":
            jump hall
            
        "Danke, ich bleibe noch im Garten.":
            jump garden

label hall:

    scene bg abbey_drawing
    show hercule at left
    with slideright
    
    h "Allo, 'ier bin ich."
    h "Sie 'aben mich gerufen?"
    jump endstory

label garden:

    h "Meine kleinen, grauen Zellen brauchen noch ein wenig frische Luft."
    jump endstory
    
label endstory:

    pause 2.0
    hide hercule
    with dissolve

    "Und so endete unsere monumentale Geschichte …"