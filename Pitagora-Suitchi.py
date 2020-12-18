characters = ['t', 'a','c','o']

output = ''

length = len(characters)
i=0
while (i < length):
    output = output + characters[i]
    i = i + 1
length = length * -1
i = -2

while(i >= length):
    output =output + characters[i]
    i= i - 1
print(output) 


#'t', 'a','c','o'
#'a','m','a','n','a','p','i','a','n','a','e'
#'w','a','s','i','t','a','r'