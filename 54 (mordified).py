# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 19:08:35 2015

@author: ming
1.如果不考虑不同花色的大小，仍然有可能出现平局
2.扑克游戏中常需要做出以下几个判断，宜单独设计为函数
是否是同一种花色
是否是顺子
统计一手牌中各种牌有多少张
3.很有必要像人一样，首先就将牌从小到大排序
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
    
def isSameSuit(kinds):
    """Return True if all cards(kinds) form samw suit"""
    return all(kinds[i]==kinds[i+1] for i in range(len(kinds)-1))


def isFlush(vals):
    """Assume input vals are sorted
    Return True if vals are of consecutive values"""
    return all((vals[i+1]-vals[i])==1 for i in range(len(vals)-1))

def valueFreqs(vals):
    """Return sorted (val,freq) list by frequence"""
    valFreq = {}
    for val in vals:
        valFreq[val] = valFreq.get(val,0) + 1
    return sorted(valFreq.items(),key=lambda x:x[1])

def handVal(cards):
    """Return (rank,[rest cards needed to be compared if the rank is the same]) 
    ranks are defined below:
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
 
    cs = sorted(split(cards), key=lambda x:x[0]) #sort hands by values
    vals = [c[0] for c in cs]
    kinds = [c[1] for c in cs]
    
    valFreqPair = valueFreqs(vals)
    valByFreq = [f[0] for f in valFreqPair]
    valFreqNum = [f[1] for f in valFreqPair]
    
#    print('maxKindNum',maxKindNum,'maxKindVals',maxKindVals)
#    print(valFreqPair)
    
    #9.Royal Flush
    if isSameSuit(kinds) and isFlush(vals) and vals[-1]==14:
        return (9,[14])
    #8.Straight Flush
    elif isSameSuit(kinds) and isFlush(vals):
        return (8,[vals[-1]])
    #7.Four of a Kind
    elif valFreqNum[-1]==4:        
        return (7,valByFreq)
    #6.Full House
    elif valFreqNum==[2,3]:
        return (6,valByFreq)
    #5.Flush
    elif isSameSuit(kinds):
        return (5,[sum(vals)])
    #4.Straight
    elif isFlush(vals):
        return (4,[vals[-1]])
    #3.Three of a kind
    elif valFreqNum[-1]==3:
        temp = valByFreq[valFreqNum.index(3)]
        return (3,sorted(valByFreq[:-1])+[valByFreq[-1]])
    #2.Two Pairs
    elif valFreqNum==[1,2,2]:
        return (2,[valByFreq[0]]+sorted(valByFreq[-2:]))
    #1.One Pair
    elif valFreqNum[-1]==2:
        temp = valByFreq[valFreqNum.index(2)]
        return (1,sorted(valByFreq[:-1])+[valByFreq[-1]])
    #0.High Card
    else:
        return (0, vals)
        
##test
##9.Royal Flush
#print('AC QC JC KC TC',handVal('AC QC JC KC TC'))
##8.Straight Flush
#print('8H 9H TH JH QH',handVal('8H 9H TH JH QH'))
##7.Four of a Kind
#print('5H 5D 5S 7D 5C',handVal('5H 5D 5S 7D 5C'))
##6.Full House
#print('4H 4D 2C 2D 2S',handVal('4H 4D 2C 2D 2S'))
##5.Flush
#print('3D 6D 7D TD QD',handVal('3D 6D 7D TD QD'))
##4.Straight
#print('3C 4H 5H 6S 7D',handVal('3C 4H 5H 6S 7D'))
##3.Three of a kind
#print('KH 2D KS KC AH',handVal('KH 2D KS KC AH'))
##2.Two Pairs
#print('5H 5C 7C 7S TD',handVal('5H 5C 7C 7S TD'))
##1.One Pair
#print('5H 5C 6S KS 7D',handVal('5H 5C 6S KS 7D'))
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