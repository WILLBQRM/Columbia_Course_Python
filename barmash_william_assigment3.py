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


# %%
#Rectangle class
class Rectangle:
   
var=Rectangle()
print(var)
print('sup')
    
   
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
