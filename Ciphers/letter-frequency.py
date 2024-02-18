import pandas as pd
import math

def letter_Frequency(ciphertext):
    english_frequency = {"a": 8.2, "b": 1.5, "c": 2.8, "d": 4.3, "e": 12.7, "f": 2.2, "g": 2.0, "h": 6.1, "i": 7.0, "j": 0.2, "k": 0.8, "l": 4.0, "m" : 2.4, "n" : 6.7, "o" : 7.5, "p" : 1.9, "q" : 0.1, "r" : 6.0, "s" : 6.3, "t" : 9.1, "u" : 2.8, "v" : 1.0, "w" : 2.4, "x" : 0.2, "y" : 2.0, "z" : 0.1}
    total_elements = len(ciphertext)
    counts = pd.Series(ciphertext).value_counts()
    print(counts.iloc[0])
    translation = []
    for i in counts:
        freq = (i / total_elements) * 100
        num1_freq = math.floor(freq)
        num2_freq = math.ceil(freq)

        for key, value in english_frequency.items():
            num1 = math.floor(value)
            num2 = math.ceil(value)
            if num1_freq | num2_freq == num1 | num2:
                translation.append(key)
    print(''.join(translation))
cipher = list('UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ')
letter_Frequency(ciphertext=cipher)