def encrypt(text, key):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = text.lower()
    text_indexes = []
    key_indexes = []

    for x in text:
        for a in alphabet:
            if x == a:
                index_letter_text = alphabet.index(a)
                text_indexes.append(index_letter_text)
                break
    
    for k in key:
        for a in alphabet:
            if k == a:
                index_letter_text = alphabet.index(a)
                key_indexes.append(index_letter_text)
                break

    # calculation matrix
    a = alphabet[text_indexes[0] * key_indexes[0] + text_indexes[1] * key_indexes[2] % 26]
    b = alphabet[text_indexes[0] * key_indexes[1] + text_indexes[1] * key_indexes[3] % 26]
    c = alphabet[text_indexes[2] * key_indexes[0] + text_indexes[3] * key_indexes[2] % 26]
    d = alphabet[text_indexes[2] * key_indexes[1] + text_indexes[3] * key_indexes[3] % 26]

    final = a + b + c + d
    print(final)

encrypt('cake', 'bake')