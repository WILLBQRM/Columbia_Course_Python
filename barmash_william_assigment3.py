# %%
#palindrome checker
def is_palindrome(word): 
    reverse = "" 
    for i in word: 
     revstr= i + reverse 
    if(word== reverse): 
       return 'true'
    elif(word!=reverse): 
        return 'false'

is_palindrome('racecar')
is_palindrome('palindrome')


# %%
#Rectangle class
class Rectangle:

    def __init__ (self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2*(self.length + self.width)
    def area(self):
        return self.length*self.width

r = Rectangle(3,4)
r.perimeter()
r.area()
#%%
#Word Counter
def count_words(str_list):
    dict={}
    for element in str_list:
        if element in dict:
            dict[element]+=1

        else:
            dict.update({element: 1})
    return dict
count_words(["hello", "world", "hello", "python"])


# %%
