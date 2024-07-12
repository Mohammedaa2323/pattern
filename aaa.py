
word = "AABCAAADA"
k = 3

for i in range(0,len(word),k):
    words=word[i:i+k]   #A : A+k >> AAB
#     print(words)
    
    seen=set()

    result=""

    for char in words:

        if char not in seen:
            seen.add(char)
            result+=char
    print(result)    
# print(count)



# string="abracadabra"

# position=5

# charcter="k"

# word=list(string)

# word[position] = charcter

# print(word)

# mutad_string= ''.join(word)

# print(mutad_string)


# string="hello world there"
# cap_word=[]

# word=string.split(' ')

# for i in word:

#     cap_word.append(''.join(i.capitalize()))

# result=' '.join(cap_word)

# print(result)

# text=' '.join(c.capitalize() for c in string.split(' '))


# print(text)

# string="BANANA"

# vowels = 'AEIOU'
# stuart_score = 0
# kevin_score = 0
# length = len(string)

# for i in range(length):
        
#         if string[i] in vowels:
#             kevin_score += length - i

#             # print(i)
#         else:
#             stuart_score += length -i

#             # print(i)

# if kevin_score > stuart_score:
#         print("Kevin", kevin_score)
# elif kevin_score < stuart_score:
#         print("Stuart", stuart_score)
# else:
#         print("Draw")


class Bird:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} is chirping"

class Parrot(Bird):
    def speak(self):
        return f"{self.name} is talking"

class Sparrow(Bird):
    def speak(self):
        return f"{self.name} is singing"

# Function that takes any bird and calls the speak method
def bird_sound(bird):
    print(bird.speak())

# Create objects of Parrot and Sparrow
polly = Parrot("Polly")
jack = Sparrow("Jack")

print(polly.speak())

bird_sound(polly)  # Polly is talking
bird_sound(jack)  # Jack is singing
