# team = 'New England Patriots'

#
# print(len(team))
#
# letter = team[1]
# print(letter)
#
# print(team[0])
#
# # print(team[1.0])
#
# print(team[len(team)-1])
#
# print(team[-1])
#
# print(team[-20])

# team = 'New England Patriots'
#
# for letter in team:
#     print(letter)
#
#
#
#
# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     # if letter == 'O' or letter == 'Q':
#     if letter in 'OQ':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix)


team = 'New England Patriots'

print(team[0:11])
print(team[:11])

print(team[12:20])
print(team[12:])

print(team[::-1])

name = 'anna'

def is_palindrome(word):
    return word == word[::-1]

# print(is_palindrome(name))






word = 'New England Patriots'
count = 0
for letter in word:
    if letter in 'aeoiuAEOIU':
        count = count + 1
print(count)



name = 'Anna'
new_name = name[:2]+name[-1]
print(new_name)


new_team = ""
for letter in team:
    if letter != 'a':
        new_team = new_team+letter

print(new_team)

print(team.upper())

print(team.find('w'))


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)


in_both('babe sone', 'colle ge')


