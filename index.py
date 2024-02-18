text = 'Clarusway'
print(text[0])

print(text[:5] + 'k' + text[-3:])

text = 'AaBbCc'
print(text.lower())
print(text)
text = text.lower()
print(text)

cumle = 'In God We Trust'
print(cumle.lower())
print(cumle)
yeni_cumle = cumle.lower()
print(yeni_cumle)

print('t' in cumle)
print('R' in cumle)
print('Trust' in cumle)
print('R' not in cumle)

text = 'www.clarusway.com'
print(text.endswith('.com'))
print(text.startswith('https:'))

text = 'aabbcc'

print(text.startswith('a'))
print(text.startswith('aa'))
print(text.startswith('b',2))

print('abcdeabcde'.startswith('c',2,8))

email = 'clarusway@clarusway.com is my e-mail address'
print(email.startswith('@', 9))
print(email.endswith('-', 10,32))

text = 'a b c d'
print(len(text))

print(email[10:32])

text='www.clarusway.com'
print(text.endswith('.co'))
print(text.startswith('w.'))

text = 'abcdef'
print(text.startswith('b',-5))


text ='abcabcabc'

print(text.find('ca'))
print(text.find('klm'))
print(text.rfind('a'))
print(text.index('ca'))
print(text.index('ca'))
# eger yoksa index hata verir


text='www.clarusway.com'
print(text.index('com'))
print(text.find('com'))

sentence = 'I live and work in Virginia'
print(sentence.upper())
print(sentence.lower())
print(sentence.swapcase())
print(sentence)