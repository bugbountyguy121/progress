# i didnt get this to be honest but  still a solution to another question who knows hhhh
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #the first problem iv'e faced is that you have to know that the list is a variable 
    # so thats why you have to use the "=" aypmbole this part of the code works suuuuuuu
    nb = [x,y,z]
    valid_position = []
    for i in range(0, nb[0]+1):
        first_coordinate = i
    for j in range(0, nb[1]+1):
        second_coordinate = j
    for k in range(0, nb[1]+1):
        third_coordinate = k
    suming = first_coordinate + second_coordinate + third_coordinate
    if suming != n:
        cor = [i,j,k]
        valid_position.append(cor)
print(valid_position)
# at this point like by jsut writing an interacting code and its runnig even it not the correct
#  answer i feel grate lets go and thin about it 
