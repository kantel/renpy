# Bilder
image bg summer_park = "bg summer_park.png"
image alice = "alice.png"

# Personen
define a = Character("Alice", color = "#c8ffc8")

# Hier beginnt das Spiel. Label "Start" ist obligatorisch!
label start:

    scene bg summer_park
    
    show alice
    with dissolve
    
    a "Guten Morgen. Mein Name ist Alice. Ich begleite Dich durch dieses kleine Ren'Py Tutorial."
    
    a "Möchtes Du mir folgen?"

    menu:
    
        "Ja, gerne. Ich möchte Ren'Py lernen.":
            jump tut
        
        "Nein danke, ich habe kein Interesse an Ren'Py.":
            jump badend
        
label tut:
    
    show alice happy
    
    a "Das ist schön, wir werden viel Spaß haben."
    
    return
    
label badend:

    show alice sad
    
    a "Das ist schade. Auf Wiedersehen."
    
    return
    