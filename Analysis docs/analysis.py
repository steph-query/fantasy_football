from scipy.stats import binom

##This function gives the expected loss by waiting a round. dframe should be that data
##that is being passed through; it looks like it will be the variable "players" that is 
##defined in draft_room.py. playpos should be a character string specifying the position.
##dround is the current round of the draft. playpos and dround are the same in function 2.

def losscalc(dframe, playpos, dround):
    ##Subsetting expected points of all players of the specified position
    points = dframe.points.filter(postion == playpos)
    
    ##Getting the probability that a player of that position would be picked this round and next round
    thisround = weightmatrix.playpos.filter(round == dround)
    nextround = weightmatrix.playpos.filter(round == dround+1)
    
    ##Setting picks by round (we can define a variable for this beforehand instead of this method)
    if dRound % 2 == 0:
        m = 8
        n = 4
    else:
        m = 10
        n = 5
    
    ##Calculating differences
    diff = []
    for i in range(m+1):
        diff.append(points[0]-points[i])
    
    ##Calculating weights based on binomial probability
    if dRound % 2 == 0:
    	weights = []
    	for i in range(m+1):
        	prob = 0
        	for l in range(max(0,i-4),min(4,i)+1):
            	prob = prob + binom.pmf(l,n,thisround)*binom.pmf(i-l,m-n,nextround)
        	weights.append(prob)
    else:
        weights = []
    	for i in range(m+1):
        	prob = 0
        	for l in range(max(0,i-5),min(5,i)+1):
            	prob = prob + binom.pmf(l,n,thisround)*binom.pmf(i-l,m-n,nextround)
        	weights.append(prob)
    
    ##Calculating expected loss
    loss = []
    while len(loss)<len(diff):
    	loss.append(0)
    for i in range(len(diff)):
    	loss[i] = diff[i]*weights[i]
    loss = sum(loss)
    return loss

##This function creates a vector of probabilities that the next few players of that position
##will be available by next round

def nextround(playpos, dround):
    
    thisround = weightmatrix.playpos.filter(round == dround)
    nextround = weightmatrix.playpos.filter(round == dround+1)
    
    ##Setting picks by round
    if dRound % 2 == 0:
        m = 9
        n = 4
    else:
        m = 11
        n = 5
    
    ##Calculating weighting system using binomial probability
    pickprob = []
    for i in range(m+1):
        prob = 0
        for l in range(max(0,i-6),min(5,i)+1):
            prob = prob + binom.pmf(l,n,thisround)*binom.pmf(i-l,m-n,nextround)
        pickprob.append(prob)
    
    ##Setting probabilities to be cumulative, i.e. now it will describe the probability that
    ##that player will still be available by next round
    for i in range(1,len(pickprob)):
    	pickprob[i] = pickprob[i-1] + pickprob[i]
    return pickprob
