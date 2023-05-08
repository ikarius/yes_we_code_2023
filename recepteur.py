def tourner_90_degres():
    Rover.motor_run_dual(100, 0)
    basic.pause(1100)

def on_received_number(receivedNumber):
    if receivedNumber == 1:
        cercle()
    elif receivedNumber == 2:
        triangle()
    elif receivedNumber == 3:
        carre()
    else:
        danse_de_la_joie()
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    Rover.move(0)
    Rover.motor_stop_all(MotorActions.STOP)
input.on_button_pressed(Button.A, on_button_pressed_a)

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
def tourner_60_degres():
    Rover.motor_run_dual(100, 0)
    basic.pause(1600)

def on_button_pressed_ab():
    Rover.motor_stop_all(MotorActions.STOP)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def cercle():
    Rover.set_allrgb(Rover.colors(RoverColors.YELLOW))
    avancer()
    basic.pause(500)
    Rover.motor_run_dual(150, 60)
    basic.pause(11000)
    Rover.mot:with(MotorActions.STOP)

def on_button_pressed_b():
    cercle()
    Rover.set_allrgb(Rover.colors(RoverColors.BLACK))
input.on_button_pressed(Button.B, on_button_pressed_b)

def avancer():
    Rover.motor_stop_all(MotorActions.STOP)
    Rover.motor_run_dual(100, 77)
    basic.pause(2000)
    Rover.motor_stop_all(MotorActions.STOP)
def carre():
    Rover.set_allrgb(Rover.colors(RoverColors.RED))
    tourner_90_degres()
    avancer()
    tourner_90_degres()
    avancer()
    tourner_90_degres()
    avancer()
    tourner_90_degres()
    avancer()
def triangle():
    Rover.set_allrgb(Rover.colors(RoverColors.BLUE))
    tourner_60_degres()
    avancer()
    tourner_60_degres()
    avancer()
    tourner_60_degres()
    avancer()
ratio_moteur = 1.3
rotation_60 = 1600
rotation_90 = 1200
radio.set_group(1)

def on_forever():
    pass
basic.forever(on_forever)
