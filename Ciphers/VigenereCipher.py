def encrypt(text, key):
    text = text.lower()
    key = key.lower()
    text = list(text)
   
    key = list(key)
    converted_letters = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if len(text) != len(key):
        print('key must be of same size as text')
    else:
        for x in range(len(text)):
                # print(text[x])
                for a in alphabet:
                    if text[x] == a:
                        index_letter_text = alphabet.index(a)
                        print(index_letter_text)
                        for k in alphabet:
                            if key[x] == k:
                                index_letter_key_text = alphabet.index(k)
                                converted_letter_index = index_letter_text + index_letter_key_text % 26
                                converted_letters.append(alphabet[converted_letter_index])
                                break
                        break         
    print(converted_letters)

# 2.
# same answer as in the notes
encrypt('wearediscoveredsaveyourself', 'deceptivedeceptivedeceptive')

