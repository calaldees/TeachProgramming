radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber >= 0 && receivedNumber <= 2) {
        if (isWinner(myHand, receivedNumber)) {
            radio.sendNumber(4)
            iWin()
        } else {
            if (isWinner(receivedNumber, myHand)) {
                radio.sendNumber(5)
                iLoose()
            } else {
                radio.sendNumber(6)
                iDraw()
            }
        }
    }
    if (receivedNumber == 4) {
        iLoose()
    }
    if (receivedNumber == 5) {
        iWin()
    }
    if (receivedNumber == 6) {
        iDraw()
    }
    clearHand()
})
input.onButtonPressed(Button.A, function () {
    myHand = (myHand + 1) % 3
    displayHand(myHand)
})
function clearHand () {
    myHand = -1
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
}
input.onButtonPressed(Button.AB, function () {
    basic.showString("Win")
    basic.showNumber(myWins)
    basic.showString("Loss")
    basic.showNumber(myLooses)
    basic.showString("Draw")
    basic.showNumber(myDraws)
})
function iLoose () {
    myLooses += 1
    basic.showIcon(IconNames.No)
}
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(myHand)
})
function iDraw () {
    myDraws += 1
    basic.showIcon(IconNames.Chessboard)
}
function isWinner (player1: number, player2: number) {
    if (player1 == 0 && player2 == 1) {
        return 1
    }
    if (player1 == 1 && player2 == 2) {
        return 1
    }
    if (player1 == 2 && player2 == 0) {
        return 1
    }
    return 0
}
function iWin () {
    myWins += 1
    basic.showIcon(IconNames.Yes)
}
function displayHand (hand: number) {
    if (hand == 0) {
        basic.showLeds(`
            # # # . .
            # . . # .
            # . . . #
            # . . . #
            # # # # #
            `)
    } else if (hand == 1) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    } else if (hand == 2) {
        basic.showLeds(`
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            `)
    } else {
        basic.showLeds(`
            . # # . .
            . . . # .
            . . # . .
            . . . . .
            . . # . .
            `)
    }
}
let myHand = 0
let myDraws = 0
let myLooses = 0
let myWins = 0
radio.setGroup(1)
myWins = 0
myLooses = 0
myDraws = 0
clearHand()
