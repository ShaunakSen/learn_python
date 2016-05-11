print(r"C:\shaunak\noNo");
r->print out the raw string

Access indv characters from string

mini = " little mini"
mini[-1] = i
mini[-2] = n

mini[startPos:stopPos]

>>> len(mini)
11

LISTS
____

>>> players = [13, 16, 26, 4, 8]
>>> players[2]
26
>>> players[2]=28
>>> players
[13, 16, 28, 4, 8]
>>> players + [5, 23]
[13, 16, 28, 4, 8, 5, 23] // temporary concatenation
>>> players
[13, 16, 28, 4, 8]
>>> players.append(120) // permanent concatenation
>>> players
[13, 16, 28, 4, 8, 120]
>>> players[:2]
[13, 16]
>>> players[:2] = [1, 2] //change multiple values at once
>>> players
[1, 2, 28, 4, 8, 120]
>>> players[:2] = [] ///delete first 2 elements
>>> players
[28, 4, 8, 120]
>>> players[:] = []
>>> players
[]
