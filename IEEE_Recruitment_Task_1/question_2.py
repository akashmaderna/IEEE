s=input("Enter a line, or enter 1 for test example : ")# asking for sentence or test sentence
if int(s)==1:#if test paragraph is called for, then a test paragraph is assigned to the variable s for analysing
    s="A gentle racecar zipped past the noon clock, as a mad cyclist noticed a mom waving. The racer thought, 'Mrs. Smith, I'm Adam,' and waved back, feeling a civic duty to be polite. Soon, a nearby dog saw a cat. 'Go, dog', the driver muttered, before seeing a sign that read, 'Step on no pets'. The driver smiled, noting the simple, level humor of the day. It was a funny and harmless moment in an otherwise ordinary day.."
print('The Test paragraph is : \n' + s)#test paragraph is printed for user to know what is being analysed
s = s.lower()#all letters are converted to small caps for easily finding out palindromes
number = 0#initial number of palindromes before analysis
w=s.split(' ' or ', ' or '. ')#words are split across punctuations for individual analysis
n=len(w)#no. of words are calculated to find out how many calculations are needed
print('The palindromes in the given statement are:\n ')
for i in range(n):#each word is take separately
    word = w[i]
    rev_word=word[::-1]#each word is reversed and given to variable 'rev_word'
        
    if word==rev_word:# if word matches the reversed self of the word, then it is a palindrome
        print(word )#palindrome is printed
        number=number + 1#counter increases by one everytime a palindrome is discovered
print('There are a total of ' + str(number) +' palindromes in the given paragraph.')
    
    
    
