def solution(l):
    l.sort(key=lambda s: [int(u) for u in s.split('.')])
    return l

# Dear Google,

# The answer popped up right away with a search. I wish I could take credit, but why reinvent the wheel? Instead, I'll show in the comments below how I came to understand what's happening, and try to extrapolate what the problem-solving process might have been if I were on my own.

# https://stackoverflow.com/questions/2574080/sorting-a-list-of-dot-separated-numbers-like-software-versions

# To fully understand how the solution works, I rewrote the lambda function and tested it as the 'key' value for our sort.

# The function turns each string passed into lists of integers. Sort() is now sorting a list of lists containing ints rather than a list of strings.

# Here, I use print() scaffolding to figure out how the lambda function is working.


def test_lamb(s):
    print(s.split('.'))
    sol_list = []
    for u in s.split('.'):
        print(u)
        sol_list.append(int(u))
    print(sol_list)
    return sol_list

def solution(l):
    l.sort(key=test_lamb)
    return l



"""
Hypothetical Problem Solving Process:

After working the problem for a while, I would have arrived at something similar to test_lambs() above but would have named it differently, not being aware that it would eventually get consolidated into a lambda function using a list comprehension. It's possible that without researching the matter, I might have overlooked the utility of lambda here.

In the end, what I submitted would likely have looked different, but the same reasoning would have applied. The steps are: go through the list, split each string into three distinct integers, and compare them with priority applied to the earliest ints, somehow.

This exercise deepened my understanding of lambda functions, a concept that I only had a passing familiarity with previously. In future challenges, it is likely I will remember this, look up how to implement lambda functions again, and over time it will become second nature.
"""

# I would also like to note, it is too late to change my submission, but I did go back to the challenge that immediately preceded this one and combined calc_stingy() and calc_generous() into the same function, calc_solution(). The need for this change stood out unmistakeably as soon as I loaded up the code again.

# Another improvement to my previous submission that I considered was the possibility of making the generator functions nested within my solution function to make it more evident that those exist to complement calc_solution(). 

# As I become a better programmer, I anticipate learning and forming the habit of applying many more such techniques to improve my style, readability, and concision.

# Moving forward, I will attempt to treat this as less of a fun game, and more of a job application.