import re
import random
#Module 2 Lesson 6: Assignments | Python Strings
#1.Product Review Analysis
#Task 1:Keyword Highlighter
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]
quotes = []
keywords = ["good", "excellent", "bad", "poor","average"]
for keyword in keywords:
    words = keyword.upper()
    print(words)
for review in reviews:
        if keyword in keywords and keyword in review:
                quotes.append(reviews)
                print(quotes)
#Task2:Sentiment Tally
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
for positive_word in positive_words: 
    print(positive_word)
    print(reviews.count(positive_word))
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"] 
for negative_word in negative_words: 
    print(negative_word)
    print(reviews.count(negative_word))
#Task 3: Review Summary
for review in reviews:     
        substring = review[0:31]
        print(substring + "...")
#2. User Input Data Processor
#Task 1: Input Length Validator Write a script that asks for and checks the length of the 
#user's first name and last name. Both should be at least 2 characters long.
#If not, print an error message.
User_First_name = input("Input the First Name")
y =len(User_First_name)
if y >= 2:
      print(y)
else:
      print("First name must be more than two Characters")
User_Last_name = input("Input the Last Name")
z = len(User_Last_name)
if z >= 2:
      print(z)
else:
      print("Last name must be more than two Characters")
