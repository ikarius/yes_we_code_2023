# Action : tourner à 90 degrés (angle droit) pour le carré
def tourner_90_degres():
    Rover.motor_run_dual(100, 0)
    basic.pause(1100)


# Action : tourner de 60 degrés (pour le triangle)
def tourner_60_degres():
    Rover.motor_run_dual(100, 0)
    basic.pause(1600)


# La danse de la joie :
# le robot tourne sur lui-même en changeant de couleurs
def danse_de_la_joie():
    Rover.motor_run_dual(200, 20)
    for index in range(16):
        Rover.set_allrgb(Rover.colors(RoverColors.INDIGO))
        basic.pause(200)
        Rover.set_allrgb(Rover.colors(RoverColors.PURPLE))
        basic.pause(200)
        Rover.set_allrgb(Rover.colors(RoverColors.WHITE))
        basic.pause(200)
    Rover.motor_stop_all(MotorActions.STOP)


# Action : selon l'ordre que le robot reçoit, on dessine une figure différente
def on_received_number(receivedNumber):
    if receivedNumber == 1:
        cercle()
    elif receivedNumber == 2:
        triangle()
    elif receivedNumber == 3:
        carre()
    else:
        danse_de_la_joie()


# Action : si on appuie sur ce bouton, les moteurs s'arretent
def on_button_pressed_a():
    Rover.move(0)
    Rover.motor_stop_all(MotorActions.STOP)


# Action : fait avancer le moteur en ligne droite
# sert pour tracer le carré et le triangle
def avancer():
    Rover.motor_stop_all(MotorActions.STOP)
    Rover.motor_run_dual(100, 77)
    basic.pause(1200)
    Rover.motor_stop_all(MotorActions.STOP)


# Action : trace un carré en tournant plusieurs fois de 90 degrés et en avançant
def carre():
    Rover.set_allrgb(Rover.colors(RoverColors.RED))
    avancer()
    tourner_90_degres()
    avancer()
    tourner_90_degres()
    avancer()
    tourner_90_degres()
    avancer()


# Action : tracer un triangle
# on tourne deux fois de 60 degrés et on avance a chaque fois
def triangle():
    Rover.set_allrgb(Rover.colors(RoverColors.BLUE))
    avancer()
    tourner_60_degres()
    avancer()
    tourner_60_degres()
    avancer()


# Action : trace un cercle en faisant tourner le robot sur lui meme
# on peut faire tourner le robot en rond une vitesse de moteur plus grande d'un coté que de l'autre
def cercle():
    Rover.set_allrgb(Rover.colors(RoverColors.YELLOW))
    avancer()
    basic.pause(400)
    Rover.motor_run_dual(220, 60)
    basic.pause(9000)
    Rover.motor_stop_all(MotorActions.STOP)


# Ce sont des constantes, ces chiffres seront utilisé à plusieurs endroits
# du programme sans que l'on ai a réécrire les valeurs
ratio_moteur = 1.3
rotation_60 = 1600
rotation_90 = 1200

# On ecoute les ordres recu sur le canal 1
radio.set_group(1)

# Evenement : si on recoit quelque chose sur le canal 1
# alors on utilise la fonction 'on_receiverd_number' pour executer un ordre
radio.on_received_number(on_received_number)

input.on_button_pressed(Button.A, on_button_pressed_a)


def on_forever():
    pass


# Boucle principale du programme
basic.forever(on_forever)
