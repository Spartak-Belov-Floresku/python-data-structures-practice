def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    list_str = list(s)
    str_vowels = list('aeioua')
    list_vowels = []

    for lt in list_str:
        if(str_vowels.count(lt.lower()) > 0):
            list_vowels.append(lt)


    for i in range(len(list_str)):
        if(str_vowels.count(list_str[i].lower()) > 0):
            list_str[i] = list_vowels.pop()

    return ''.join(list_str)


