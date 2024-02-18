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

text = 'ClarRusWay'
print(text.upper())
print(text.lower())
print(text.swapcase())
print(text)

text = 'ClaRusWay'
print(text.replace('W','***'))
print(text.replace('W','***').lower())
print(text.replace('W','***').lower().upper())

print(text.count('a'))
print(text.title())
text ='the better the family, the better the society'
print(text.title())


text = 'S0d0me and G0m0re'
print(text.replace('0','o'))

isim = '             ali            '
print(isim.strip())
meslek=' \n codder   \t' 
print(meslek.strip())
print(meslek.rstrip())

text = 'abcdabcd'
print(text.strip('a'))
print(text.strip('ab'))
print(text.strip('ba'))
print(text.strip('bad'))
print(text.strip('badc'))

print(None or 1)
print(True or False)
print(True or not False)

a= ' '
b= 'False'
c= True
d= ''
print(a or b or c and not d)


text = 'tyou can learn almost everything in pre-classz '
print(text.strip('tz'))
print(text.strip('tz').upper())
print(text.rstrip('z').lstrip('t'))
print(text.rstrip('z').lstrip('t').upper())

text = 'In God wee Trust'
print(text.replace('wee','we'))