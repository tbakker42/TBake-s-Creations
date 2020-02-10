def spayedDogs(inputFile,outputFile):
    fin = open(inputFile,"r",encoding="utf-8")
    fout = open(outputFile,"w",encoding="utf-8")

    header=fin.readline()

    counter = {}
    
    for dog in fin:
        data = dog.split(",")
        breed = data[2]
        spayed = data[7]

        if not breed in counter.keys():
            counter[breed] = [0,0]

        spayedList = counter[breed]
        if spayed=="Yes":
            spayedList[0] = spayedList[0] + 1
        else:
            spayedList[1] = spayedList[1] + 1

    breedList = []
    for breed in counter.keys():
        data = counter[breed]
        percent = round(data[0]/(data[0]+data[1]) * 100,2)
        oneBreed = [percent,data[0],data[1],breed]
        breedList.append(oneBreed)

    breedList.sort()
    breedList.reverse()

    for i in range(len(breedList)):
        data = breedList[i]
        percent = str(data[0])
        yessir = str(data[1])
        nope = str(data[2])
        breed = data[3]
        fout.write(breed+","+yessir+","+nope+","+percent)
        fout.write("\n")

    fout.close()
        



    
