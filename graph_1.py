a, b, c, d, e, f, g, h = range(8)
_ = float('inf')



N = [
    {b, c, d, e, f},        #a
    {c, e},                 #b
    {d},                    #c
    {e},                    #d
    {f},                    #e
    {c, g, h},              #f
    {f, h},                 #g
    {f, g}                  #h
]

N_withweights = [
    {b:2, c:1, d:3, e:9, f:4},          #a
    {c:4, e:3},                         #b
    {d:8},                              #c
    {e:7},                              #d
    {f:5},                              #e
    {c:2, g:2, h:2},                    #f
    {f:1, h:6},                         #g
    {f:9, g:8}                          #h
]

N_adjmatrix = [[0,1,1,1,1,1,0,0], # a 
                [0,0,1,0,1,0,0,0], # b 
                [0,0,0,1,0,0,0,0], # c 
                [0,0,0,0,1,0,0,0], # d 
                [0,0,0,0,0,1,0,0], # e 
                [0,0,1,0,0,0,1,1], # f 
                [0,0,0,0,0,1,0,1], # g 
                [0,0,0,0,0,1,1,0]] # h 

W = [[0,2,1,3,9,4,_,_], # a 
    [_,0,4,_,3,_,_,_], # b 
    [_,_,0,8,_,_,_,_], # c 
    [_,_,_,0,7,_,_,_], # d 
    [_,_,_,_,0,5,_,_], # e 
    [_,_,2,_,_,0,2,2], # f 
    [_,_,_,_,_,1,0,6], # g 
    [_,_,_,_,_,9,8,0]] # h

print("****** N no weights")
if b in N[a]:
    print(True)

print(len(N[f]))

print("****** N with weights")
if b in N_withweights[a]:
    print(True)

print(len(N_withweights[f]))

print(N_withweights[a][b])

print("****** N adj matrix")
print(N_adjmatrix[a][b])

print(sum(N_adjmatrix[f]))

print("****** adj matrix with weights")
print(W[a][b] < float('inf'))
print(W[c][e] < float('inf'))

print(sum(1 for w in W[a] if w < float('inf')) - 1)
