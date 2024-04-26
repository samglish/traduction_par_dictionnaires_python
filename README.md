# traduction par dictionnaire en python
Nous allons utiliser un dictionnaire pour traduire des phrases en bon français en langage sms.

sms_dictionnary = {' ': ' ', 'bonjour': 'bjr', 'salut': 'slt'}

```python
phrase = input("Entrez une phrase :")

sms_dictionnary = {' ': ' ', 'bonjour': 'bjr', 'salut': 'slt'}  # completer le dictionnaire
 
 
def sms_translator():
 
    sms_message = ""
    for x in phrase:
        try: # on éssait de traduire
            sms_message += sms_dictionnary[x]
            sms_message += " "
        except KeyError:# sinon on restitue le mot tel qu'il est.
            sms_message += phrase[phrase.index(x)]
            sms_message += " "
    print(sms_message)
 
 
phrase += ""
 
phrase = [mot for mot in phrase.split(" ")]
 
 
sms_translator()
```
