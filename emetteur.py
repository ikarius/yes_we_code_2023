def selectionner_carre():
    basic.show_leds(
        """
        . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
    """
    )


def selectionner_inconnu():
    basic.show_leds(
        """
        . . # . .
                . . # . .
                . . # . .
                . . . . .
                . . # . .
    """
    )


def on_button_pressed_a():
    global choix
    choix += 1
    if choix == 1:
        selectionner_cercle()
    elif choix == 2:
        selectionner_triangle()
    elif choix == 3:
        selectionner_carre()
    else:
        choix = 0
        selectionner_inconnu()


input.on_button_pressed(Button.A, on_button_pressed_a)


def selectionner_triangle():
    basic.show_leds(
        """
        . . . . .
                . . # . .
                . # # # .
                # # # # #
                . . . . .
    """
    )


def on_button_pressed_b():
    basic.show_leds(
        """
        # . # . .
                . . . # .
                # # # # #
                . . . # .
                # . # . .
    """
    )
    envoyer_donnee()


input.on_button_pressed(Button.B, on_button_pressed_b)


def envoyer_donnee():
    basic.show_string("" + str(choix))
    radio.send_number(choix)


def selectionner_cercle():
    basic.show_leds(
        """
        . # # # .
                # # # # #
                # # # # #
                # # # # #
                . # # # .
    """
    )


choix = 0
radio.set_group(1)
radio.send_value("start", 1)
basic.show_leds(
    """
    . . . . .
        . . . . .
        # . # . #
        . . . . .
        . . . . .
"""
)


def on_forever():
    pass


basic.forever(on_forever)
