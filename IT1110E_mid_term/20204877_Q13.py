def box_compare(a,b,c,d,e,f):
    box1 = [a,b,c]
    box2 = [d,e,f]
    box1.sort()
    box2.sort()
    if box1 == box2:
        return 'Boxes are equal'
    elif box1[0] >= box2[0] and box1[1] >= box2[1] and box1[2] >= box2[2]:
        return 'The first box is larger than the second one'
    elif box1[0] <= box2[0] and box1[1] <= box2[1] and box1[2] <= box2[2]:
        return 'The first box is smaller than the second one'
    else:
        return ('Boxes are incomparable')
