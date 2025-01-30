def min_max_normalisation (my_list):
    x_min=min(my_list)
    x_max=max(my_list)
    for i in my_list:
        x_scaled=(i-x_min)/(x_max-x_min)
    return [x_scaled for i in my_list]

mylist=list(map(int,input("Enter number separated by space").split()))

x_scaled = min_max_normalisation(mylist)
print(x_scaled)