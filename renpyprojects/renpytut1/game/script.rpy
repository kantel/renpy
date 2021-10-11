# Bilder
image bg abbey_grounds = "bg abbey_grounds.jpg"
image maid = "maid.png"

# Personen
define a = Character('Alice', color="#c8ffc8")

# Hier beginnt das Spiel. Label "Start" ist obligatorisch!
label start:

    scene bg abbey_grounds
    show maid

    a "Das ist alles so kurios hier."

    a "Kurios und noch kurioser!"

    return
