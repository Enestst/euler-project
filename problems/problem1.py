main_list = []
for i in range(1,1000):
    if i % 3 == 0 or i  % 5 == 0:
        main_list.append(i)
print(sum(main_list))        
