## Problem description

Given a `words.txt` file containing a newline-delimited list of dictionary words, please implement the Anagrams class so that the `get_anagrams()` method.
returns all anagrams from `words.txt` for a given word.

## Bonus requirements:

- Optimise the code for fast retrieval
- Write more tests
- Thread safe implementation

# Problem Solution

Given the following `words.txt` file containing a list of words, I solve this problem by focusing on how to optimize the code. And also, how can I retrieve the list of words quickly and efficiently? Before implementing the `get_anagrams()` function, first
I preprocess the list of words and make a dictionary that contains the anagrams of the words. This step involves a few steps.

- First, process each word and transform the word into a lower-case word.
- Sort the word's characters.
- Then it will act as a dictionary key.
- Push similar words into the dictionary.

After preprocessing, we can implement the `get_anagrams()` function. First, we will check if the word is valid or not. if valid, then check in the dictionary and retrieve the list; otherwise, return a not-found list.
