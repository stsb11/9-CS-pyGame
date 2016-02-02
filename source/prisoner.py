import random
# Iterative Prisoner's dilemma simulator
# --------------------------------------

# Tariff...
# Betray (one goes free, other serves 5 years) 4 for betrayer, -1 for loser
# Mutual coop   (you both serve 1 year)        2pts each,
# Mutual betray:(you both serve 3 years)       1pt each,

# Silver: Write a new strategy in structured English.
# Gold: Make a reasonable attempt to write it.
# Platinum: Implement a new strategy.

# Strategies are Devil, Angel, Flipper, Random, Tit4Tat
p1strat='Devil'  # Player 1 strategy
p2strat='Flipper'  # Player 2 strategy
numOfRounds=50    # How many games?

p1move='Cooperate'
p2move='Cooperate'
p1score=0
p2score=0
youBetray=0
mutualCoop=0
mutualBetray=0
gotBetrayed=0

#############################
###  Strategies go here   ###
#############################

def Angel():
    # Always cooperate with the 
    # other criminal, never betraying them.
    return 'Cooperate'

def Devil():
    # Always betray the other criminal.
    return 'Betray'

def RandomPick():
    # Choose at random every time.
    pickNumber=random.randrange(1,101)

    # Lower the number to lower the percentage
    # chance of cooperating (use 1-100).
    if pickNumber<=50:
        mymove='Cooperate'
    else:
        mymove='Betray'

    return mymove

def Flipper(whichgame):
    # Alternate between cooperation and betrayal every turn.
    mymove='Betray'
        
    if whichgame%2==0:
        mymove='Cooperate'

    return mymove

def Tit4Tat(theirLastMove,whichGame):
    # Cooperate in game 1, then for all others do whatever
    # the other criminal did to you in their previous game.
    if whichGame==0:
        mymove='Cooperate'
    else:
        mymove=theirLastMove

    return mymove

def Grudge():
    # Cooperate until you're betrayed, then
    # betray every time.
    return mymove

def Random4Tat(theirLastMove,whichGame):
    # Use the Tit4Tat strategy, but
    # betray randomly 25% of the time.
    return mymove

###################################

def decideWinner(p1move,p2move):
    # Decide the outcome, and assign points.
    global youBetray
    global mutualCoop
    global mutualBetray
    global gotBetrayed
    global p1score,p2score
    
    if p1move=='Betray' and p2move=='Cooperate':
        p1score+=4
        p2score-=1
        youBetray+=1
    elif p1move=='Cooperate' and p2move=='Cooperate':
        p1score+=2
        p2score+=2
        mutualCoop+=1
    elif p1move=='Betray' and p2move=='Betray':
        p1score+=1
        p2score+=1
        mutualBetray+=1
    elif p1move=='Cooperate' and p2move=='Betray':
        p1score-=1
        p2score+=4
        gotBetrayed+=1

    # Comment this out for faster gameplay.
    print('Game ' + str(game) + '. P1 chooses ' + p1move + ', and P2 chooses ' + p2move + '.')

for game in range(1,numOfRounds+1):
    p1LastMove=p1move
    p2LastMove=p2move
    
    if p1strat=='Angel': p1move=Angel()
    if p2strat=='Angel': p2move=Angel()

    if p1strat=='Devil': p1move=Devil()
    if p2strat=='Devil': p2move=Devil()
    
    if p1strat=='Random': p1move=RandomPick()
    if p2strat=='Random': p2move=RandomPick()

    if p1strat=='Flipper': p1move=Flipper(game)
    if p2strat=='Flipper': p2move=Flipper(game)
    
    if p1strat=='Tit4Tat': p1move=Tit4Tat(p2LastMove,game)
    if p2strat=='Tit4Tat': p2move=Tit4Tat(p1LastMove,game)
    
    # Calculate outcome
    decideWinner(p1move,p2move)

# Show the results
maxPossScore=numOfRounds * 4
print('')
print('Player 1 strategy: ' + p1strat)
print('Player 2 strategy: ' + p2strat)
print('')

print('You mutually cooperated (1 year each):  ' + str(mutualCoop))
print('You betrayed each other (3 years each): ' + str(mutualBetray))
print('')

percentageOfScore=(p1score / maxPossScore) * 100
print('Player 1:')
print('You betrayed (and were set free):       ' + str(youBetray))
print('You were betrayed (and served 5 years): ' + str(gotBetrayed))
print('Final score:' + str(p1score) + ' (' + str(int(percentageOfScore)) + '%)')
print('')
percentageOfScore=(p2score / maxPossScore) * 100
print('Player 2:')
print('You betrayed (and were set free):       ' + str(gotBetrayed))
print('You were betrayed (and served 5 years): ' + str(youBetray))
print('Final score:' + str(p2score) + ' (' + str(int(percentageOfScore)) + '%)')

if p1score>p2score:
    print('Player 1 wins')
elif p1score==p2score:
    print("It's a draw")
else:
    print('Player 2 wins')
