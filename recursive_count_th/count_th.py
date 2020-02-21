'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):
    # need to define this here since we aren't passing it in the function
    substr = "th"

    #there can't be any more instances if there are less than 2 letters in the word
    if len(word) < len(substr):
        return count

    if word[0 : len(substr)] == substr:
        count += 1
        # if we get a match, loop again with the new word being all of the characters we haven't tested yet (word[len(substr) - 1:])
        return count_th(word[len(substr) - 1:], count)
    else:
        # else, we do the same thing except we don't increment the count var
        return count_th(word[len(substr) - 1:], count)

    return count

# just testing here
# print(count_th("abcthxyz"))