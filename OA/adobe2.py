#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getScoreDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numSeq as parameter.
#

def getScoreDifference(numSeq):
    # Write your code here
    player_a = 0
    player_b = 0
    round = 0
    
    def pickNum(numSeq, round,player_a,  player_b):
        if  len(numSeq)==0:
            print("end", player_a, player_b)
            return player_a - player_b
        picked = numSeq[0]
        if round%2 == 0:
            player_a += picked
        else:
            player_b += picked
        numSeq = numSeq[1:]
        if picked%2 ==0:
            numSeq = numSeq[::-1]

        return pickNum(numSeq, round+1, player_a, player_b)
    # output = pickNum(numSeq, 0, player_a, player_b)
    
    def pickScore(numSeq):
        player_a = 0
        player_b = 0
        for i in range (len(numSeq)):
            if numSeq[i] % 2 == 0 :
                # player_a += numSeq[i+1]
                if i%2 == 0:
                    player_a += numSeq[len(numSeq)-i-1]
                else:
                    player_b += numSeq[len(numSeq)-i-1]
            elif numSeq[len(numSeq)-i-1]%2 == 0:
                if i%2 == 0:
                    player_b += numSeq[i+1]
                else: 
                    player_a += numSeq[i+1]
            else:
                if i%2 == 0:
                    player_a += numSeq[i]
                else:
                    player_b += numSeq[i]
                
        return player_a-player_b

    output = pickScore(numSeq)
    return output


if __name__ == '__main__':
    print("result", getScoreDifference([3, 6, 2, 3, 5]))
