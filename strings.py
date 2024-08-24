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
    print("dance")
for review in reviews:
        if keyword in keywords and keyword in review:
                print(review)
                quotes.append(reviews)
                print(quotes)
#Task2:Sentiment Tally
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
for positive_word in positive_words: 
        print(positive_word)
        for review in reviews:     
                print(review.count(positive_word))
       
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"] 
for negative_word in negative_words: 
        print(negative_word)
        for review in reviews:
                print(reviews.count(negative_word))
#Task 3: Review Summary
for review in reviews:     
        substring = review[0:31]
        print(substring)
#2. User Input Data Processor
#Task 1: Input Length Validator Write a script that asks for and checks the length of the 
#user's first name and last name. Both should be at least 2 characters long.
#If not, print an error message.

User_First_name = input("Input the First Name")
print(len(User_First_name))
User_Last_name = input("Input the Last Name")
print(len(User_Last_name))
