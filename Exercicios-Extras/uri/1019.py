sec = int(input())
hour = sec // 3600
sec %= 3600
minut = sec // 60
sec %= 60 
print("{0}:{1}:{2}".format(hour, minut, sec))