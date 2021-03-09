def remove_duplicates(inputlist):
    if inputlist == []:
        return []

    inputlist = sorted(inputlist)

    outputlist = [inputlist[0]]

    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)

    return outputlist

print (remove_duplicates([1, 1, 2, 2]))