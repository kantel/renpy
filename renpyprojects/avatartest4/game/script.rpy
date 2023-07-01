# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define a = Character('Alice', color="#cc6600")

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
image bg kulturbunker = "kulturbunker.jpg"
image alice           = "alice2_neutral.png"
image alice smiling   = "alice2_smiling.png"
image alice mo        = "alice2_mo"
image alice verwirrt  = "alice2_verwirrt.png"

# Hier beginnt das Spiel.
label start:

    scene bg kulturbunker

    show alice at left
    a "Der Berliner Senat hat einen neuen Haushaltsentwurf vorgestellt."

    hide alice
    show alice verwirrt at left
    a "Wenn er in Kraft tritt, muß der Bezirk Neukölln sämtliche Sozialleistungen streichen."

    hide alice
    show alice smiling at left
    a "Doch Franziska Giffey hält das alles nicht für so schlimm, denn Neukölln sei zwar arm, aber sexy."

    hide alice
    show alice mo at left
    a "Dann ist ja alles gut."

    return
