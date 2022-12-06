'''
#############
Lab 5.02
#############
In this lab we will implement a word frequency algorithm. 
It will tell you how many of each word you had in an essay.

At the top of the document save a variable with a long paragraph (example below). 
In order to turn this paragraph into a list of lower case words we will use the split(" "), 
replace(), and lower() functions. There is code at the bottom of this page that will do this 
for you. Feel free to read more about split() in the Python documentation, but it's not critical 
to this lab.

For each word in the document, count the number of times it occurs. Consider the following phrase: 
'Cats are cool. Baby cats are called kittens. Cats make great pets.' The word 'cats' appears 3 times. 
The word 'are' appears 2 times.

The program will first create a dictionary with the words as keys and the number of times they occur 
as values. Then it will prompt the user which word they are curious about. If the word was in the 
paragraph it will print the number of times it occurred.

Example
------------
>>> python3 word_frequency_lab.py
What word would you like to know the frequency of? cats
'cats' occurs 3 times
>>> python3 word_frequency_lab.py
What word would you like to know the frequency of? dogs
'dogs' does not occur

split, replace, and lower
--------------------------
This is the code to lower case the letters in the paragraph, remove the periods, and split them into 
individual words.

example_paragraph = "It was a beautiful day in New York City. Our hero Ariana Grande was on a walk 
from the Standard to Duane Reade. Ariana Grande was walking rather quickly because she had lived in 
New York for a few months. All of a sudden a slimy donut appeared out of nowhere. Ariana Grande decided 
to prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana Grande 
decides to go to Times Square instead. What a beautiful day in New York."
​
#make all letters lowercase
example_paragraph_lower = example_paragraph.lower()
​
#remove all periods
example_paragraph_lower_no_punctuation = example_paragraph_lower.replace(".", "")
​
#convert paragraph into a list of individual strings
example_word_list = example_paragraph_lower_no_punctuation.split(" ")
'''

paragraph = '''
In many cases for the majority of students, finals can be a very stressful time of their schoolyear. Regardless, if it is midterms or 
end of the year final exams, most students cram as much studying as they can in before finals come. However, many kids procrastinate and do 
all their studying the nights before each exam, which is a terrible habit to have. So, instead of trying to fit all of this into a single night 
right before one's exams, one should study ahead of time, that way they are more confident, well prepared, and less stressed for their exams.
'''
word_list = []

print(paragraph)
counter_dict = {

}

# All Lowercase
paragraph_lower = paragraph.lower()


# Lowercase And No Punc
paragraph_lower_no_punctuation = paragraph_lower.replace(".","")

# Remove \n Character
paragraph_lower_no_punctuation_no_new = paragraph_lower_no_punctuation.replace("\n","")

# Dictionary For Seperate Words
word_list = paragraph_lower_no_punctuation_no_new.split(" ")
# print(word_list)

# Add Each Word To Dictionary and Count How Many Times It Appears
for word in word_list:
    if word in counter_dict:
        counter_dict[word] += 1
    else:
        counter_dict[word] = 1
# print(counter_dict)

running = True

while running:
    print()
    word_input = input("What word would you like to know the frequency of? ")
    if word_input in counter_dict:
        print(f"{word_input} appears {counter_dict[word_input]} times.")
    else:
        print(f"{word_input} appears 0 times")
    
    while True:
        again = input("Would you like to know the frequency of another word? (y/n) ")
        if again == "y":
            break
        elif again == "n":
            print("Bye Bye ")
            running = False
            break
        else:
            print("I didn't understand you...")
