txt = input()
count_simbol = 0 
find_simbol = txt[0]
result = ""
for i in txt:
    if i == find_simbol: 
        count_simbol = count_simbol + 1  
    else:
        result = result + str(count_simbol) + find_simbol  
        count_simbol = 1 
        find_simbol = i 
result = result + str(count_simbol) + find_simbol    
print(result) 