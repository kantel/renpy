# Bilder
image startszene  = "alice1.jpg"
image kitchen     = "alice2.jpg"
image schweinchen = "alice3.jpg"
image teeparty    = "alice4.jpg"
image raupe       = "alice5.jpg"
image endszene    = "alice6.jpg"

# Charaktere
define a = Character("Alice", color="#c8ffc8")
define g = Character("Grinsekatze", color="#f39c12")
define r = Character("Raupe", color="#6495ed")

# Hier beginnt das Spiel.
label start:

    scene startszene

    "Es war ein sonniger Tag. Alice schlenderte gedankenverloren durch das Wunderland. Sie hatte sich ein wenig verirrt. Plötzlich materialisierte sich im Gestrüpp über ihrem Weg die Grinsekatze."

    a "Würdest Du mir bitte sagen, wie ich von hier aus weitergehen soll?"

    g "Das hängt zum großen Teil davon ab, wohin Du möchtest."

    menu:
        "Aber ich will Dir weiterhelfen:"

        "Geradeaus geht es zum Haus der Herzogin":
            jump herzogin
        
        "Links zur Teeparty des verrückten Hutmachers":
            jump teaparty

        "Rechts triffst Du die kiffende Raupe auf ihrem Pilz":
            jump caterpillar

label herzogin:

    scene kitchen

    "Im Haus der Herzogin herrschte Chaos. Die Herzogin warf erst mit einem Topf nach Alice, doch dann drückte sie ihr ein plärrendes Baby in den Arm."

    jump ferkel

label ferkel:

    scene schweinchen

    "Alice verließ das Haus. Das Plärren des Babys veränderte sich langsam zu einem Grunzen und Quieken. Als Alice nachsah, merkte sie, daß sie ein kleines Ferkelchen im Arm hielt."

    "Erschreckt setzte Alice das Ferkelchen ab. Es lief davon."

    "Und Alice ging verwirrt zurück an den Start."

    jump start

label teaparty:

    scene teeparty

    "Alice erreichte die Teeparty vor dem Haus des verrückten Hutmachers. Dieser deklamierte gerade ein langes, dafür um so langweiligeres Gedicht."

    menu:

        "Alice hatte sehr schnell genug davon. Also überlegte sie …"

        "ob sie nicht doch die Raupe aufsuchen":
            jump caterpillar
        
        "oder gleich nach Hause gehen sollte.":
            jump ende

label caterpillar:

    scene raupe

    "Die Raupe war zu bekifft, um ein vernünftiges Gespräch zu führen. Sie murmelte nur immerzu etwas vom »Reich der Ringe« und daß Alice dieses dringend besuchen müßte. Sie sagte noch:"

    r "Komm morgen wieder, dann erzähle ich Dir mehr."

    "Alice beschloß, daß sie für heute genug habe und ging nach Hause."

label ende:

    scene endszene

    menu:

        "Damit ist die Geschichte zu Ende."

        "Zurück an den Start?":
            jump start
        "Oder die Geschichte verlassen?":
            return
        