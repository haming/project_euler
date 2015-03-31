import string

fh = open('59 cipher.txt','r')

ciphertext = fh.read().split(',')
fh.close()
ciphertext = [chr(int(i)) for i in ciphertext]

fh = open('englishWords.txt', 'r')
words = fh.read().split(' ')
fh.close()

def decrypt(ciphertext, key):
    message = ''
    keyLen = len(key)
    for i in xrange(len(ciphertext)):
        message += chr(ord(ciphertext[i]) ^ ord(key[i%keyLen]))
    return message
    
def countWords(message, words):
    count = 0
    for word in message.split(' '):
        if word in words:
            count += 1
    return count
       
maxWordNum = 0
maxCipher = ''
for a in string.ascii_lowercase:
    for b in string.ascii_lowercase:
        for c in string.ascii_lowercase:
            message = decrypt(ciphertext,a+b+c)
            wordNum = countWords(message, words)
            print a+b+c,wordNum
            if wordNum > maxWordNum:
                maxWordNum = wordNum
                maxCipher = a+b+c
                print 'Yes'