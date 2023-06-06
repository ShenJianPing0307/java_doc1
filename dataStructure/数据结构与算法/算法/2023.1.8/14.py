def merge(X,Y):
    Z = []
    while X and Y:
        if X[0] < Y[0]:
            Z.append(X[0])
            del X[0]
        else:
            Z.append(Y[0])
            del Y[0]
    if X:
        Z.extend(X)
    if Y:
        Z.extend(Y)
    print(Z)
    return Z

list1 = [3,4,7,9,11]
list2 = [1,2,5,8,13,20]
merge(list1, list2)

