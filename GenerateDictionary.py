
def ReadWeights(filename):
    weightfile=open(filename,'r')
    dictx=dict()
    for line in weightfile:
        info=line.split("\t")
        dictx[info[0]]=int(info[1])
    weightfile.close()
    return dictx

def CountSimplicity(sent,dictx):
    learned=0
    unlearned=0
    over=0
    for w in sent:
        if w in dictx:
            if dictx[w]>1:
                learned+=dictx[w]
            else:
                unlearned+=dictx[w]
        else:
            over+=10
    return learned/(learned+unlearned+over)