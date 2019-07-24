#This program first splits any song lyrics into different strings of words, then stores the words as keys in the dictionary, and then 
#stores their frequency of occurence as values

#function to separate words from a lyrics
def words_separator(sentences):
    words = []
    for line in sentences.split("\n"):
        words.extend(line.split())
    return words
    
#function to store the values in the dictionary
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict
    
    
#DEMO LYRICS
demo_lyrics = """She loves you, yeah, yeah, yeah
She loves you, yeah, yeah, yeah
She loves you, yeah, yeah, yeah, yeah
You think you've lost your love
Well, I saw her yesterday-ay
It's you she's thinking of
And she told me what to say-ay
She says she loves you
And you know that can't be bad
Yes, she loves you
And you know you should be glad
She said you hurt her so
She almost lost her mind
But now she says she knows
You're not the hurtin' kind
She says she loves you
And you know that can't be bad
Yes, she loves you
And you know you should be glad, ooh
She loves you, yeah, yeah, yeah
She loves you, yeah, yeah, yeah
With a love like that
You know you should be glad
You know it's up to you
I think it's only fair
Pride can hurt you, too
Apologize to her
Because she loves you
And you…"""

#printing frequencies of words in DEMO LYRICS
print(lyrics_to_frequencies(words_separators(demo_lyrics)))
