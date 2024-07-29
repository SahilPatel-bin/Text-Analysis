class TextAnalyzer():
    def __init__(self,text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
         # make text lowercase
        self.text = formattedText.lower()

    def freqAll(self):
         # split text into words
        wordList = self.text.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)

        return freqMap
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        
text = '''I’m very disappointed with my recent purchase. The product arrived late and was poorly packaged, 
        resulting in visible damage. The quality was far from what was advertised—several parts were defective 
        and didn’t function as promised. Customer service was unhelpful and slow to respond to my concerns, 
        leaving me frustrated. I had to jump through hoops just to arrange a return, and the refund process was 
        equally cumbersome. This experience was not only inconvenient but also frustrating. I expected much better 
        from this company and will be hesitant to make future purchases. Definitely not worth the hassle.'''

analyzed = TextAnalyzer(text)
print("Formatted Text:", analyzed.text)
freqMap = analyzed.freqAll()
print(freqMap)

word = "service"
frequency = analyzed.freqOf(word)
print("The word",word,"appears",frequency,"times.")