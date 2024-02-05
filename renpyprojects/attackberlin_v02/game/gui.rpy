################################################################################
## Initialisierung
################################################################################

## Die Anweisung init offset bewirkt, dass die Initialisierungsanweisungen in
## dieser Datei vor den init-Anweisungen in allen anderen Dateien ausgeführt
## werden.
init offset = -2

## Der Aufruf von gui.init setzt die Stile auf sinnvolle Standardwerte zurück
## und setzt die Breite und Höhe des Spiels.
init python:
    gui.init(1280, 720)

## Prüfungen auf ungültige oder instabile Eigenschaften in Bildschirmen oder
## Transformationen aktivieren
define config.check_conflicting_properties = True


################################################################################
## GUI-Konfigurationsvariablen
################################################################################


## Farben ######################################################################
##
## Die Farben des Textes in der Schnittstelle.

## Eine Akzentfarbe, die in der gesamten Benutzeroberfläche zur Beschriftung und
## Hervorhebung von Text verwendet wird.
define gui.accent_color = '#cc6600'

## Die Farbe, die für eine Textschaltfläche verwendet wird, wenn sie weder
## ausgewählt ist noch mit dem Mauszeiger bewegt wird.
define gui.idle_color = '#888888'

## Die kleine Farbe wird für kleinen Text verwendet, der heller/dunkler sein
## muss, um den gleichen Effekt zu erzielen.
define gui.idle_small_color = '#aaaaaa'

## Die Farbe, die für Schaltflächen und Balken verwendet wird, die mit dem
## Mauszeiger bewegt werden.
define gui.hover_color = '#e0a366'

## Die Farbe, die für eine Textschaltfläche verwendet wird, wenn sie ausgewählt,
## aber nicht fokussiert ist. Eine Schaltfläche ist ausgewählt, wenn sie der
## aktuelle Bildschirm oder Einstellungswert ist.
define gui.selected_color = '#ffffff'

## Die Farbe, die für eine Textschaltfläche verwendet wird, wenn sie nicht
## ausgewählt werden kann.
define gui.insensitive_color = '#8888887f'

## Farben für die Teile der Balken, die nicht ausgefüllt sind. Diese
## Farben werden nicht direkt verwendet, aber bei der Neuerstellung von
## Balkenbilddateien eingesetzt.
define gui.muted_color = '#512800'
define gui.hover_muted_color = '#7a3d00'

## Die Farben, die für Dialog- und Menüauswahltext verwendet werden.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Schriftarten und Schriftgrößen ##############################################

## Die für den Text im Spiel verwendete Schriftart.
define gui.text_font = "DejaVuSans.ttf"

## Die für Zeichennamen verwendete Schriftart.
define gui.name_text_font = "DejaVuSans.ttf"

## Die Schriftart, die für den Text außerhalb des Spiels verwendet wird.
define gui.interface_text_font = "DejaVuSans.ttf"

## Die Größe des normalen Dialogtextes.
define gui.text_size = 22

## Die Größe der Zeichennamen.
define gui.name_text_size = 30

## Die Größe des Textes in der Benutzeroberfläche des Spiels.
define gui.interface_text_size = 22

## Die Größe der Beschriftungen in der Benutzeroberfläche des Spiels.
define gui.label_text_size = 24

## Die Größe des Textes auf dem Benachrichtigungsbildschirm.
define gui.notify_text_size = 16

## Die Größe des Titels des Spiels.
define gui.title_text_size = 50


## Haupt- und Spielmenü ########################################################

## Die Bilder, die für das Haupt- und das Spielmenü verwendet werden.
define gui.main_menu_background = "images/office_hans.png"
define gui.game_menu_background = "gui/game_menu.png"


## Dialog ######################################################################
##
## Diese Variablen steuern, wie der Dialog zeilenweise auf dem Bildschirm
## angezeigt wird.

## Die Höhe des Textfeldes, das den Dialog enthält.
define gui.textbox_height = 185

## Die Platzierung des Textfeldes vertikal auf dem Bildschirm. 0.0 ist der obere
## Rand, 0.5 ist die Mitte und 1.0 ist der untere Rand.
define gui.textbox_yalign = 1.0


## Die Platzierung des Namens des sprechenden Charakters, relativ zum Textfeld.
## Dies kann eine ganze Anzahl von Pixeln von links oder oben sein, oder 0,5 bis
## zur Mitte.
define gui.name_xpos = 240
define gui.name_ypos = 0

## Die horizontale Ausrichtung des Namens des Zeichens. Dies kann 0.0 für
## linksbündig, 0.5 für zentriert und 1.0 für rechtsbündig sein.
define gui.name_xalign = 0.0

## Die Breite, die Höhe und die Ränder des Feldes, das den Namen des Zeichens
## enthält, oder None, um es automatisch zu vergrößern.
define gui.namebox_width = None
define gui.namebox_height = None

## Die Ränder des Feldes, das den Namen des Zeichens enthält, in der Reihenfolge
## links, oben, rechts, unten.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Wenn True, wird der Hintergrund des Namensfeldes gekachelt, wenn False, wird
## der Hintergrund des Namensfeldes skaliert.
define gui.namebox_tile = False


## Die Platzierung des Dialogs relativ zum Textfeld. Dies kann eine ganze Anzahl
## von Pixeln relativ zur linken oder oberen Seite des Textfeldes oder 0,5 zur
## Mitte sein.
define gui.dialogue_xpos = 268
define gui.dialogue_ypos = 50

## Die maximale Breite des Dialogtextes, in Pixeln.
define gui.dialogue_width = 744

## Die horizontale Ausrichtung des Dialogtextes. Dies kann 0.0 für linksbündig,
## 0.5 für zentriert und 1.0 für rechtsbündig sein.
define gui.dialogue_text_xalign = 0.0


## Schaltflächen ###############################################################
##
## Diese Variablen, zusammen mit den Bilddateien in gui/button, steuern Aspekte
## der Darstellung von Schaltflächen.

## Die Breite und Höhe einer Schaltfläche, in Pixeln. Falls keine, berechnet
## Ren'Py eine Größe.
define gui.button_width = None
define gui.button_height = None

## Die Ränder auf jeder Seite der Schaltfläche, in der Reihenfolge links, oben,
## rechts, unten.
define gui.button_borders = Borders(4, 4, 4, 4)

## Wenn True, wird das Hintergrundbild gekachelt. Wenn False, wird das
## Hintergrundbild linear skaliert.
define gui.button_tile = False

## Die von der Schaltfläche verwendete Schriftart.
define gui.button_text_font = gui.interface_text_font

## Die Größe des von der Schaltfläche verwendeten Textes.
define gui.button_text_size = gui.interface_text_size

## Die Farbe des Schaltflächentextes in verschiedenen Zuständen.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Die horizontale Ausrichtung des Schaltflächentextes. (0.0 ist links, 0.5 ist
## mittig, 1.0 ist rechts).
define gui.button_text_xalign = 0.0


## Diese Variablen überschreiben die Einstellungen für verschiedene Arten von
## Schaltflächen. Bitte lesen Sie in der Gui-Dokumentation nach, welche Arten
## von Schaltflächen verfügbar sind und wofür sie jeweils verwendet werden.
##
## Diese Anpassungen werden von der Standardschnittstelle verwendet:

define gui.radio_button_borders = Borders(18, 4, 4, 4)

define gui.check_button_borders = Borders(18, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)

define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Sie können auch Ihre eigenen Anpassungen hinzufügen, indem Sie Variablen mit
## den richtigen Namen hinzufügen. Zum Beispiel können Sie die folgende Zeile
## auskommentieren, um die Breite einer Navigationsschaltfläche festzulegen.

# define gui.navigation_button_width = 250


## Auswahltasten ###############################################################
##
## Wahltasten werden in den Menüs im Spiel verwendet.

define gui.choice_button_width = 790
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Datei Slot Schaltflächen ####################################################
##
## Eine Dateislot-Schaltfläche ist eine besondere Art von Schaltfläche. Er
## enthält ein Miniaturbild und einen Text, der den Inhalt des Speicherplatzes
## beschreibt. Ein Speicherslot verwendet Bilddateien in gui/button, wie die
## anderen Arten von Schaltflächen.

## Die Schaltfläche "Slot speichern".
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Die Breite und Höhe der Miniaturbilder, die von den Speicherplätzen verwendet
## werden.
define config.thumbnail_width = 256
define config.thumbnail_height = 144

## Die Anzahl der Spalten und Zeilen im Raster der Speicherplätze.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Positionierung und Abstände #################################################
##
## Diese Variablen steuern die Positionierung und den Abstand der verschiedenen
## Elemente der Benutzeroberfläche.

## Die Position der linken Seite der Navigationstasten, relativ zur linken Seite
## des Bildschirms.
define gui.navigation_xpos = 40

## Die vertikale Position des Überspringungsanzeigers.
define gui.skip_ypos = 10

## Die vertikale Position des Benachrichtigungsbildschirms.
define gui.notify_ypos = 45

## Die Abstände zwischen den Menüoptionen.
define gui.choice_spacing = 22

## Schaltflächen im Navigationsbereich des Haupt- und Spielmenüs.
define gui.navigation_spacing = 4

## Steuert den Abstand zwischen den Einstellungen.
define gui.pref_spacing = 10

## Steuert den Abstand zwischen den Einstellungsschaltflächen.
define gui.pref_button_spacing = 0

## Der Abstand zwischen den Schaltflächen der Dateiseite.
define gui.page_spacing = 0

## Der Abstand zwischen den Dateislots.
define gui.slot_spacing = 10

## Die Position des Hauptmenütextes.
define gui.main_menu_text_xalign = 1.0


## Frames ######################################################################
##
## Diese Variablen steuern das Aussehen von Frames, die Komponenten der
## Benutzeroberfläche enthalten können, wenn kein Overlay oder Fenster vorhanden
## ist.

## Allgemeine Rahmen.
define gui.frame_borders = Borders(4, 4, 4, 4)

## Der Rahmen, der als Teil des Bestätigungsbildschirms verwendet wird.
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

## Der Rahmen, der als Teil des Überspringungsbildschirms verwendet wird.
define gui.skip_frame_borders = Borders(16, 5, 50, 5)

## Der Rahmen, der als Teil des Benachrichtigungsbildschirms verwendet wird.
define gui.notify_frame_borders = Borders(16, 5, 40, 5)

## Sollen Rahmenhintergründe gekachelt werden?
define gui.frame_tile = False


## Balken, Bildlaufleisten und Schieberegler ###################################
##
## Diese steuern das Aussehen und die Größe von Balken, Bildlaufleisten und
## Schiebereglern.
##
## Die Standard-GUI verwendet nur Schieberegler und vertikale Bildlaufleisten.
## Alle anderen Leisten werden nur in vom Ersteller geschriebenen Bildschirmen
## verwendet.

## Die Höhe der horizontalen Balken, Bildlaufleisten und Schieberegler. Die
## Breite der vertikalen Balken, Rollbalken und Schieberegler.
define gui.bar_size = 25
define gui.scrollbar_size = 12
define gui.slider_size = 25

## True, wenn die Balkenbilder gekachelt werden sollen. False, wenn sie linear
## skaliert werden sollen.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontale Grenzen.
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

## Vertikale Ränder.
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

## Was man mit nicht scrollbaren Bildlaufleisten in der Benutzeroberfläche
## macht. "hide" blendet sie aus, während "None" sie anzeigt.
define gui.unscrollable = "hide"


## Geschichte ##################################################################
##
## Der Verlaufsbildschirm zeigt Dialoge an, die der Spieler bereits verworfen
## hat.

## Die Anzahl der Blöcke des Dialogverlaufs, die Ren'Py behält.
define config.history_length = 250

## Die Höhe eines Eintrags im Verlaufsbildschirm, oder None, um die Höhe auf
## Kosten der Leistung variabel zu machen.
define gui.history_height = 140

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## Die Position, Breite und Ausrichtung der Beschriftung, die den Namen des
## sprechenden Zeichens angibt.
define gui.history_name_xpos = 155
define gui.history_name_ypos = 0
define gui.history_name_width = 155
define gui.history_name_xalign = 1.0

## Die Position, Breite und Ausrichtung des Dialogtextes.
define gui.history_text_xpos = 170
define gui.history_text_ypos = 2
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0


## NVL-Modus ###################################################################
##
## Der NVL-Modus-Bildschirm zeigt den Dialog an, der von den Charakteren im NVL-
## Modus gesprochen wird.

## Die Grenzen des Hintergrunds des Hintergrundfensters im NVL-Modus.
define gui.nvl_borders = Borders(0, 10, 0, 20)

## Die maximale Anzahl der Einträge im NVL-Modus, die Ren'Py anzeigt. Wenn mehr
## Einträge als diese Zahl angezeigt werden sollen, wird der älteste Eintrag
## entfernt.
define gui.nvl_list_length = 6

## Die Höhe eines Eintrags im NVL-Modus. Setzen Sie dies auf None, um die Höhe
## der Einträge dynamisch anzupassen.
define gui.nvl_height = 115

## Der Abstand zwischen NVL-Mode-Einträgen, wenn gui.nvl_height None ist, und
## zwischen NVL-Mode-Einträgen und einem NVL-Mode-Menü.
define gui.nvl_spacing = 10

## Die Position, Breite und Ausrichtung der Beschriftung, die den Namen des
## sprechenden Zeichens angibt.
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0

## Die Position, Breite und Ausrichtung des Dialogtextes.
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0

## Die Position, Breite und Ausrichtung des nvl_thought-Textes (der Text, der
## vom nvl_narrator-Zeichen gesprochen wird).
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0

## Die Position der nvl menu_buttons.
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0


## Lokalisierung ###############################################################

## Dies steuert, wo ein Zeilenumbruch zulässig ist. Der Standardwert ist für die
## meisten Sprachen geeignet. Eine Liste der verfügbaren Werte finden Sie unter
## https://www.renpy.org/doc/html/style_properties.html#style-property-language.

define gui.language = "unicode"


################################################################################
## Mobile Geräte
################################################################################

init python:

    ## Dadurch werden die Schnellschaltflächen größer, damit sie auf Tablets und
    ## Handys leichter zu erreichen sind.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(40, 14, 40, 0)

    ## Dies ändert die Größe und die Abstände verschiedener GUI-Elemente, um
    ## sicherzustellen, dass sie auf Handys gut sichtbar sind.
    @gui.variant
    def small():

        ## Schriftgrößen.
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 34

        ## Passen Sie die Position des Textfeldes an.
        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.dialogue_xpos = 90
        gui.dialogue_width = 1100

        ## Ändern Sie die Größe und die Abstände verschiedener Dinge.
        gui.slider_size = 36

        gui.choice_button_width = 1240
        gui.choice_button_text_size = 30

        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10

        gui.history_height = 190
        gui.history_text_width = 690

        gui.quick_button_text_size = 20

        ## Layout der Schaltfläche Datei.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-Modus.
        gui.nvl_height = 170

        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325

        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5

        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20

        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
