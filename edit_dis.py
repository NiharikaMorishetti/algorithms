#Spelling Correction

#Double Gold Star

#For this question, your goal is to build a step towards a spelling corrector,
#similarly to the way Google used to respond,

#    "Did you mean: audacity"


#when you searched for "udacity" (but now considers "udacity" a real word!).

#One way to do spelling correction is to measure the edit distance between the
#entered word and other words in the dictionary.  Edit distance is a measure of
#the number of edits required to transform one word into another word.  An edit
#is either: (a) replacing one letter with a different letter, (b) removing a
#letter, or (c) inserting a letter.  The edit distance between two strings s and
#t, is the minimum number of edits needed to transform s into t.

#Define a procedure, edit_distance(s, t), that takes two strings as its inputs,
#and returns a number giving the edit distance between those strings.

#Note: it is okay if your edit_distance procedure is very expensive, and does
#not work on strings longer than the ones shown here.

#The built-in python function min() returns the mininum of all its arguments.

#print min(1,2,3)
#>>> 1

def edit_distance(s,t):
    l1 = len(s)
    l2 = len(t)
    i = 0
    matrix = []
    while i <= l1 :
        matrix.append([])
        i = i + 1
    i = 0    
    while i <= l2 :
        matrix[0].append(i)
        i = i + 1
    i = 1    
    while i <= l1 :
        matrix[i].append(i)
        i = i + 1
    
    i = 1 
    j = 1
    c = 0
    while i <= l1 :
        while j <= l2 :
            if s[i-1] == t[j-1] :
                c = 0
            else :
                c = 1
            matrix[i].append(min( matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+c))
            j = j + 1
            
        j = 1    
        i = i + 1
    return matrix[l1][l2]



#For example:

# Delete the 'a'
#print edit_distance('audacity', 'udacity')
#>>> 1

# Delete the 'a', replace the 'u' with 'U'
#print edit_distance('audacity', 'Udacity')
#>>> 2

# Five replacements
#print edit_distance('peter', 'sarah')
#>>> 5

# One deletion
#print edit_distance('pete', 'peter')
#>>> 1
