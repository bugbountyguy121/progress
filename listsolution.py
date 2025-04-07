if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #like this is new for me its kinda open the list and do an operation inside 
    # it lol by geting some of the items that you want wow
    print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))