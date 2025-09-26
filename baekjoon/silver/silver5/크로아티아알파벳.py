croatian = ['c=', 'c-', 'dz=','d-', 'lj','nj','s=','z=']
input = 'ljes=njak'
result = 0
other = 0
for i in croatian:
    result_croatian = input.count(i)
    result += result_croatian
    input = input.replace(i,"*")  #처음에 공백대체 후 앞뒤 문자열 합쳐지는 찐빠발생.
input = input.replace("*","") #그래서 *로 대체 후 다시 공백으로 바꿈.
other = len(input)
result += other
print(result)
