import heapq

n = input()

number_result = 0
heap_list= []
character_result =""

for i in n :
    if ord(i) < 65 :
        number_result += int(i)
    else:
        heapq.heappush(heap_list, ord(i))

for _ in range(len(heap_list)) :
    character_result += chr(heapq.heappop(heap_list))

print(character_result + str(number_result))