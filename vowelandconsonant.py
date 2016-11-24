''''This will check the given Alphabet is
Vowel or consonant'''

print('Please, give me an Alphabet')
chracter = input()

if chracter >= 'a' and chracter <= 'z' or chracter >= 'A' and chracter <= 'z':
    if chracter in 'aAeEiIoOuU':
        print(chracter + ' is a vowel')
    else:
        print(chracter + ' is a consonant')
else:
    print('Put a single an Alphabet chracter')
