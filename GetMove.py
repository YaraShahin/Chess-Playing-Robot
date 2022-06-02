PrevBoardState = {
"a1":"r","a2":"n","a3":"b","a4":"q","a5":"k","a6":"b","a7":"n","a8":"r",
"b1":"p","b2":"p","b3":"p","b4":"p","b5":"p","b6":"p","b7":"p","b8":"p",
"c1":"","c2":"","c3":"","c4":"","c5":"","c6":"","c7":"","c8":"",
"d1":"","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",
"e1":"","e2":"","e3":"","e4":"","e5":"","e6":"","e7":"","e8":"",
"f1":"","f2":"","f3":"","f4":"","f5":"","f6":"","f7":"","f8":"",
"g1":"pb","g2":"Pb","g3":"Pb","g4":"Pb","g5":"Pb","g6":"Pb","g7":"Pb","g8":"Pb",
"h1":"Rb","h2":"Nb","h3":"Bb","h4":"Qb","h5":"Kb","h6":"","h7":"","h8":"Rb"}

NewBoardState = {
"a1":"r","a2":"n","a3":"b","a4":"q","a5":"k","a6":"b","a7":"n","a8":"r",
"b1":"p","b2":"p","b3":"p","b4":"p","b5":"p","b6":"p","b7":"p","b8":"p",
"c1":"","c2":"","c3":"","c4":"","c5":"","c6":"","c7":"","c8":"",
"d1":"","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",
"e1":"","e2":"","e3":"","e4":"","e5":"","e6":"","e7":"","e8":"",
"f1":"","f2":"","f3":"","f4":"","f5":"","f6":"","f7":"","f8":"",
"g1":"pb","g2":"Pb","g3":"Pb","g4":"Pb","g5":"Pb","g6":"Pb","g7":"Pb","g8":"Pb",
"h1":"Rb","h2":"Nb","h3":"Bb","h4":"Qb","h5":"","h6":"Rb","h7":"Kb","h8":""}


 
def GetMove(PrevBoardState,NewBoardState):
    MovedPieces = set() 

    OldPos = ""
    NewPos = ""
    movedPiece = ""

    RemovedPieces = []

    OldNumberOfPeices = 32
    CurrentNumberOfPeices = 0

    for pos in NewBoardState:
        if NewBoardState[pos] != "":
            CurrentNumberOfPeices += 1

        if NewBoardState[pos] == PrevBoardState[pos]:
            continue
        else:
            #Player Move
            if NewBoardState[pos] == "":
                OldPos = pos
                print("Old pos",pos)
            else:
                NewPos = pos
                movedPiece = NewBoardState[pos]
                MovedPieces.add(movedPiece)
                print(movedPiece,"change to:",pos)
            

    print("Number of Moved Peices:",len(MovedPieces))
    print(MovedPieces)
    if len(MovedPieces) == 1:
        if CurrentNumberOfPeices < OldNumberOfPeices:
            OldPeice = PrevBoardState[NewPos]
            print(OldPeice,"has been removed")
            RemovedPieces.append(OldPeice)
            
            print("Removed Pieces:",RemovedPieces)
            OldNumberOfPeices = CurrentNumberOfPeices

    elif len(MovedPieces) == 2:
        print("Castle")
    elif len(MovedPieces) == 0:
        print("No Move")
    else:
        print("Exceeded Number of Moves {2}")
    return (OldPos+NewPos),MovedPieces,RemovedPieces

print(GetMove(PrevBoardState,NewBoardState))