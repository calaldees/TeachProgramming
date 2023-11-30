"""
https://makecode.microbit.org/#editor
Set language to Python and paste this code

MicroBit - Rock, Paper, Scissors
2 Player with radio
Keeps track of win, loose and draw

Select hand with 'A Button'
Send your hand with 'B Button'

On receive of hand number (0 to 2) - check if won - set local machine win state + send inverse of that state back remote
On receive of state (4 to 6) - display and update score
"""

# Main ------------------------------------------------------
radio.set_group(1)
myHand = -1
myDraws = 0
myLooses = 0
myWins = 0
clearHand()

# Radio Recieve ----------------------------------------------

def on_received_number(receivedNumber):
    if receivedNumber >= 0 and receivedNumber <= 2:
        if isWinner(myHand, receivedNumber):
            radio.send_number(4)  # Send 'Loose' to other device
            iWin()
        elif isWinner(receivedNumber, myHand):
            radio.send_number(5)  # Send 'Win' to other device
            iLoose()
        else:
            radio.send_number(6)  # Send 'Draw' to other device
            iDraw()
    if receivedNumber == 4:
        iLoose()
    if receivedNumber == 5:
        iWin()
    if receivedNumber == 6:
        iDraw()
    clearHand()
radio.on_received_number(on_received_number)

def isWinner(player1: number, player2: number):
    if player1 == 0 and player2 == 1:
        return 1
    if player1 == 1 and player2 == 2:
        return 1
    if player1 == 2 and player2 == 0:
        return 1
    return 0

# Buttons ---------------------------------------------------

def on_button_pressed_a():
    global myHand
    myHand = (myHand + 1) % 3
    displayHand(myHand)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(myHand)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    displayScores()
input.on_button_pressed(Button.AB, on_button_pressed_ab)


# Set Status -------------------------------------------------

def clearHand():
    global myHand
    myHand = -1
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)

def iLoose():
    global myLooses
    myLooses += 1
    basic.show_icon(IconNames.NO)

def iDraw():
    global myDraws
    myDraws += 1
    basic.show_icon(IconNames.CHESSBOARD)

def iWin():
    global myWins
    myWins += 1
    basic.show_icon(IconNames.YES)

# Display ---------------------------------------------

def displayScores():
    basic.show_string("Win")
    basic.show_number(myWins)
    basic.show_string("Loss")
    basic.show_number(myLooses)
    basic.show_string("Draw")
    basic.show_number(myDraws)

def displayHand(hand: number):
    if hand == 0:
        basic.show_leds("""
            # # # . .
            # . . # .
            # . . . #
            # . . . #
            # # # # #
            """)
    elif hand == 1:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
    elif hand == 2:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
    else:
        basic.show_leds("""
            . # # . .
            . . . # .
            . . # . .
            . . . . .
            . . # . .
            """)
