def readData(inFile):
    fin = open(inFile,"r")
    header = fin.readline()

    allData = []
    for player in fin:
        player = player.strip()
        data = player.split(",")
        allData.append(data)

    return allData
    fin.close()

def matchup(inFile):
    importantData = []
    allData = readData(inFile)
    for i in range(len(allData)):
        game = allData[i]
        seedOne = int(game[4])
        scoreOne = int(game[5])
        seedTwo = int(game[9])
        scoreTwo = int(game[8])

        oneGame = [seedOne,seedTwo,scoreOne,scoreTwo]
        importantData.append(oneGame)
    return importantData

def upset(inFile):
    allData = matchup(inFile)
    wins = 0
    total = len(allData)
    
    for i in range(len(allData)):
        game = allData[i]
        if game[0] > game[1] and game[2] > game[3]:
            wins = wins + 1
        elif game[1] > game[0] and game[3] > game[2]:
            wins = wins + 1
        else:
            wins = wins

    upsetPercentage = round((wins/total * 100),2)
    print("An upset in the NCAA Tournament is when a lower seed defeats a higher seed.")
    print("From 1985 to 2019, there were "+str(wins)+"upsets out of "+str(total)+" total games.")
    print("This amounts to an upset win percentage of "+str(upsetPercentage)+"%.")

def seedWins(inFile):
    allData = matchup(inFile)

    #Setup a length 16 list with each value = 0
    wins=[]
    for x in range(16):
        wins.append(0)

    #run through data
    for game in allData:
        #who won
        if (game[2]>game[3]):
            seed=game[0]
        else:
            seed=game[1]

        index=seed-1  #Seeds are 1-16 but we need 0-15 for the list
        wins[index] += 1

    print("The number of NCAA Tournament wins by seed from 1985 to 2019 are listed below: ")

    for index in range(16):
        seed=index+1
        print(str(seed)+"seed = "+str(wins[index])+" wins.")
