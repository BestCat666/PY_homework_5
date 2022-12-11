#1 Напишите программу, удаляющую из файла все слова, содержащие "абв".
file = open('ex1.txt','r',encoding = 'utf-8')

substring = 'абв'
s = file.readline()
print(s)
lst_txt = s.split(" ")
print(lst_txt)
output_txt = filter(lambda x: x.lower().find(substring) == -1, lst_txt)
print(type(output_txt))
a = list(output_txt)
b =' '.join(a)
print(b)
file = open('ex1.txt','w',encoding = 'utf-8')
file.write(b)
file.close()

#В Зимбабве нет сабвея ---- В нет