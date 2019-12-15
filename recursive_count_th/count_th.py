'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC

   #Need to figure out how to remove only the first occurence of th for the recuresive call
   
    if "th" in word:
        # print("yes", count)
        return 1 + count_th(word.replace("th", " ", 1))
    else:
        # print("no")
        return 0
    # return count 