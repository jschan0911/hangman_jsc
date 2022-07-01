point = 0
max_try = 9
try_count = 0
tried_chars = ''

word = input('Type the answer : ')
print('=' * 30)
hidden = '_' * len(word)

while True:
    print('word : ' + hidden)
    print('tried_chars : ' + str(tried_chars))
    print('try_count : ' + str(try_count))
    print('max_try : ' + str(max_try))
    
    ans = input('Type the alphabet : ')

     # If ans exists in hidden or tried_chars
    if hidden.find(ans) != -1 or tried_chars.find(ans) != -1:   
        print('Please type another alphabet.') 

    # If ans exists in word
    elif word.find(ans) != -1:
        for i in range(0, len(word), 1):
            if word[i] == ans:
                l = list(hidden)
                l[i] = ans
                hidden = ''.join(l)
                point += 1
    
    else:
        tried_chars += ans + ' '
        try_count += 1
    
    print('=' * 30)

    if point == len(word):
        print(hidden)
        print('Congratulation!')
        break
    
    if ans == word:
        print(word)
        print('Congratulation!')
        break

    if try_count == max_try:
        print('Game Over')
        break

    print('try count : ' + str(try_count))