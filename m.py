list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grjhbhbhbbbbbbbbbnnhbjjhn khjb nhjmb nubhjnnjjjjjjjjjjjjill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
indext=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            indext.append(i+j)
print(min(indext))          
