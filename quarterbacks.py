def clean(variable):
    if variable > 2.375:
        return 2.375
    if variable < 0:
        return 0
    return variable

def passerRating(attempts,completions,yards,touchdowns,interceptions):
    A = clean((completions / attempts * 100 - 30) / 20)
    B = clean(((yards / attempts) - 3) / 4)
    C = clean((touchdowns / attempts) * 20)
    D = clean(2.375 - (interceptions / attempts * 25))
        
    passingRating = (A + B + C + D) / 6 * 100

    return(float(round(passingRating,2)))

def ratingCategory(qbr):
    if qbr > 95:
        rating = "Great"
    elif qbr > 90:
        rating = "Good"
    elif qbr > 85:
        rating = "Mediocre"
    else:
        rating = "Bad"

    return(rating)

def addColumns(inputFile,outputFile):
    fin = open(inputFile,"r",encoding="utf-8")
    fout = open(outputFile,"w",encoding="utf-8")

    header=fin.readline()

    fout.write(header[:-1])
    fout.write(",PasserRating,Classification")
    fout.write("\n")

    for qb in fin:
        fout.write(qb[:-1])
        data = qb.split(",")

        attempts=float(data[6])
        completions=float(data[5])
        yards=float(data[7])
        touchdowns=float(data[8])
        interceptions=float(data[9])
        qbr = passerRating(attempts,completions,yards,touchdowns,interceptions)
        rating = ratingCategory(qbr)

        fout.write(",")
        fout.write(str(qbr))
        fout.write(",")
        fout.write(str(rating))
        fout.write("\n")

    fin.close()
    fout.close()
