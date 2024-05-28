#Zechariah Prieshoff
#May 25th, 2024
#Text Adventure Editor
#Program that allows the user to load and save previous or current game files, play the current game file,
# and add/edit fields and nodes.

import json
import time

def main():
    gameData = getDefaultGame()
    keepGoing = True
    while keepGoing:
        userChoice = getMenuChoice()
        if userChoice == '0':
            print("================================================\nExiting")
            keepGoing = False
        elif userChoice == '1':
            print("================================================\nLoad the default game")
            gameData = getDefaultGame()
        elif userChoice == '2':
            print("================================================\nLoad a game file")
            gameData = loadGame()
        elif userChoice == '3':
            print("================================================\nSave the current game")
            saveGame(gameData)
        elif userChoice == '4':
            print("================================================\nEdit or add a node")
            editNode(gameData)
        elif userChoice == '5':
            print("================================================\nPlaying the game")
            playGame(gameData)
        else:
            print("Sorry, that's an invalid choice. Please try again.")

def getMenuChoice():
    print("  0) Exit \n  1) Load default game \n  2) Load a game file \n  3) Save the current game \n  4) Edit or add a node \n  5) Play the current game")
    choice = input(" Please enter your choice (0, 1, 2, 3, 4, 5): ")
    return choice

def getDefaultGame():
    defaultGame = {'start': ["This is the default node", "Start over", 'start', "Quit", 'quit']}
    return defaultGame

def playGame(gameData):
    node = 'start'
    while node != 'quit':
        node = playNode(node, gameData)
        if node == 'quit':
            break

def playNode(node, gameData):
    (description, menuA, nodeA, menuB, nodeB) = gameData[node]
    print(f"{description} \n1.{menuA} \n2.{menuB}")
    userChoice = input("Please enter your choice: ")
    if userChoice == '1':
        newNode = (nodeA)
    elif userChoice == '2':
        newNode = (nodeB)
    else:
        print("Sorry, that's an invalid choice. Please enter 1 or 2.")
        newNode = playNode(node, gameData)
    return newNode

def editNode(gameData):
    print("Here are the current nodes: ")
    for node in gameData:
        print(node)
    nodeName = input("Please enter an existing node to edit or enter a new node to add: ")
    if nodeName in gameData:
        newNode = gameData[nodeName]
    else:
        newNode = ["", "", "", "", ""]
    newNode = editField(newNode)
    gameData[nodeName] = newNode

def editField(node):
    description = input("Description (" + node[0] + "): ")
    if description:
        node[0] = description
    else:
        node[0] = node[0]

    menuA = input("MenuA (" + node[1] + "): ")
    if menuA:
        node[1] = menuA
    else:
        node[1] = node[1]

    nodeA = input("NodeA (" + node[2] + "): ")
    if nodeA:
        node[2] = nodeA
    else:
        node[2] = node[2]

    menuB = input("MenuB (" + node[3] + "): ")
    if menuB:
        node[3] = menuB
    else:
        node[3] = node[3]

    nodeB = input("NodeB (" + node[4] + "): ")
    if nodeB:
        node[4] = nodeB
    else:
        node[4] = node[4]
    return node

def saveGame(gameData):
    with open('game.dat', 'w') as f:
        json.dump(gameData, f,)
    print("\nSaving game")
    buffer("One moment please", 0.15)
    buffer(".\n", 0.2, 3)
    print("Game saved!\n")

def loadGame():
    try:
        with open('game.dat', 'r') as f:
            gameData = json.load(f)
        print("Loading game with json.")
        return gameData
    except FileNotFoundError:
        print("Sorry, cannot find any saved games. Loading default game")
        return getDefaultGame()

def buffer(text, delay = 0.1, repetitions = 1):
    for _ in range(repetitions):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()


main()