data = open("text.txt", encoding='utf-8')
rows = data.readline()
data.close()

print(rows)

