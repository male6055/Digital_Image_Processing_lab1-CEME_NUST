def min_max_normalisation (my_list):
    x_min=min(my_list)
    x_max=max(my_list)
    for i in my_list:
        scaled=(i-x_min)/(x_max-x_min)
        x_scaled.append(round(scaled,3))
    return x_scaled

mylist=list(map(int,input("Enter number separated by space: ").split()))
x_scaled=[]
min_max_normalisation(mylist)
print("Scaled List: ",x_scaled)