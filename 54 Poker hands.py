# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:39:17 2015

@author: ming
"""

cardsStr = '5H 5C 6S 7S KD'

def split(cards):
    """Split cards in to two list of value and kind
    Jack:11,Queen:12,King:13,Ace:14"""
    vals = []
    kinds = []
    for card in cards.split(' '):
        kinds.append(card[1])
        if card[0]=='T':
            vals.append(10)
        elif card[0]=='J':
            vals.append(11)
        elif card[0]=='Q':
            vals.append(12)
        elif card[0]=='K':
            vals.append(13)
        elif card[0]=='A':
            vals.append(14)
        else:
            vals.append(int(card[0]))
    return list(zip(vals,kinds))
    
#print(split(cardsStr)
    
#def sameSuit(kinds):
#    return all(kinds[i]==kinds[i+1] for i in range(len(kinds)-1))

def isConsecutive(vals):
    valSort = sorted(vals)
    return all((valSort[i+1]-valSort[i])==1 for i in range(len(vals)-1))

def ofAKind(cards):
    cardSorted = sorted(cards,key=lambda c:c[1])
    maxKindNum = 0
    maxKind = ''
    
    kindNum = 0
    currentKind = ''
    for card in cardSorted:
        if card[1]==currentKind:
            kindNum += 1
        else:
            currentKind = card[1]
            kindNum = 1
        if kindNum>maxKindNum:
            maxKindNum = kindNum
            maxKind = currentKind

    maxKindVals = []    
    for card in cardSorted:
        if card[1]==maxKind:
            maxKindVals.append(card[0])
    return maxKindNum,sorted(maxKindVals)

def sameVals(vals):
    valDict = {}
    for val in vals:
        valDict[val] = valDict.get(val,0) + 1
    return valDict

def handVal(cards):
    """
    0.High Card: Highest value card.
    1.One Pair: Two cards of the same value.
    2.Two Pairs: Two different pairs.
    3.Three of a Kind: Three cards of the same value.
    4.Straight: All cards are consecutive values.
    5.Flush: All cards of the same suit.
    6.Full House: Three of a kind and a pair.
    7.Four of a Kind: Four cards of the same value.
    8.Straight Flush: All cards are consecutive values of same suit.
    9.Royal Flush: Ten, Jack, Queen, King, Ace, in same suit."""
    cs = split(cards)
    vals = [c[0] for c in cs]
    kinds = [c[1] for c in cs]
    
    maxKindNum,maxKindVals = ofAKind(cs)
    valDict = sameVals(vals)
    sameVal = list(valDict.keys())
    sameValNum = list(valDict.values())
    
    
#    print('maxKindNum',maxKindNum,'maxKindVals',maxKindVals)
#    print('valDict',valDict)
    
    #9.Royal Flush
    if maxKindNum==5 and sorted(vals)==[10,11,12,13,14]:
        return (9,[14])
    #8.Straight Flush
    elif maxKindNum==5 and isConsecutive(vals):
        return (8,[maxKindVals[-1]])
    #7.Four of a Kind
    elif 4 in sameValNum:
        temp = sameVal[sameValNum.index(4)]
        return (7,[sameVal[sameValNum.index(1)],sameVal[sameValNum.index(4)]])
    #6.Full House
    elif sorted(sameValNum)==[2,3]:
        return (6,[sameVal[sameValNum.index(2)],sameVal[sameValNum.index(3)]])
    #5.Flush
    elif maxKindNum==5:
        return (5,[sum(maxKindVals)])
    #4.Straight
    elif isConsecutive(vals):
        return (4,[sorted(vals)[-1]])
    #3.Three of a kind
    elif 3 in sameValNum:
        temp = sameVal[sameValNum.index(3)]
        return (3,sorted(filter(lambda k:k!=temp,vals))+[temp])
    #2.Two Pairs
    elif sorted(sameValNum)==[1,2,2]:
        return (2,[sameVal[sameValNum.index(1)]]+sorted(filter(lambda k:valDict[k]==2,valDict)))
    #1.One Pair
    elif 2 in sameValNum:
        temp = sameVal[sameValNum.index(2)]
        return (1,list(filter(lambda x:x!=temp, sorted(vals)))+[temp])
    #0.High Card
    else:
        return (0, sorted(vals))
        
##test
##9.Royal Flush
#print('AC QC JC KC TC',handVal('AC QC JC KC TC'))
##8.Straight Flush
#print('8H 9H TH JH QH',handVal('8H 9H TH JH QH'))
##7.Four of a Kind
#print('5H 5D 5S 7D 5C',handVal('5H 5D 5S 7D 5C'))
##6.Full House
#print('2H 2D 4C 4D 4S',handVal('2H 2D 4C 4D 4S'))
##5.Flush
#print('3D 6D 7D TD QD',handVal('3D 6D 7D TD QD'))
##4.Straight
#print('3C 4H 5H 6S 7D',handVal('3C 4H 5H 6S 7D'))
##3.Three of a kind
#print('KH 2D KS KC 8H',handVal('KH 2D KS KC 8H'))
##2.Two Pairs
#print('5H 5C 7C 7S TD',handVal('5H 5C 7C 7S TD'))
##1.One Pair
#print('5H 5C 6S 7S KD',handVal('5H 5C 6S 7S KD'))
##0.High Card
#print('5D 8C 9S JS AC',handVal('5D 8C 9S JS AC'))
        
fh = open('54 poker.txt')
win1 = 0
win2 = 0
for hand in fh:
    handVal1 = handVal(hand[:14])
    handVal2 = handVal(hand[15:])
#    print(handVal1)
#    print(handVal2)

    if handVal1[0]>handVal2[0]:
        win1 += 1
#        print('1 win')
    elif handVal1[0]==handVal2[0]:
#        print(handVal1[1][-1],handVal2[1][-1])
        for i in range(1,len(handVal2[1])+1):
            if handVal1[1][-i]>handVal2[1][-i]:
                win1 += 1
#                print('1 win')
                break
            elif handVal1[1][-i]<handVal2[1][-i]:
                win2 += 1
#                print('2 win')
                break
    else:
#        print('2 win')
        win2 += 1
#    print()

print(win1,win2)