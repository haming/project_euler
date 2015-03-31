def permutations(objs,permutes=[[]]):
    if len(objs) == 0:
        return permutes
    else:
        #print objs, permutes
        newPermutes = []
        for permute in permutes:
            for l in range(len(permute)+1):
                newPermutes.append(permute[0:l]+[objs[0]]+permute[l:])
        #newPermutes = [[permute[0:l]+[objs[0]]+permute[l:] for l in range(len(permute)+1)] for permute in permutes]
        return permutations(objs[1:], newPermutes)
        
def toInt(permutes):
    return [int(''.join(permute)) for permute in permutes]
    
allPermutations = toInt(permutations([str(i) for i in range(10)]))
allPermutations.sort()
print allPermutations[999999]