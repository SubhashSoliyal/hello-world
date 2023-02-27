import re

mystr = '''This is perhaps the best known database to be found in the pattern recognition literature. Fisher's paper is a classic in the field and is referenced frequently to this day. (See Duda & Hart, for example.) The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other.

Predicted attribute: class of iris plant.

This is an exceedingly simple domain.

This data differs from the data presented in Fishers article (identified by Steve Chadwick, spchadwick '@' espeedaz.net ). The 35th sample should be: 4.9,3.1,1.5,0.2,"Iris-setosa" where the error is in the fourth feature. The 38th sample: 4.9,3.6,1.4,0.1,"Iris-setosa" where the errors are in the second and third features.

'''

# findall, search, split, sub, finditer
 
# patt = re.compile(r'class')
# patt = re.compile(r'.')
# patt = re.compile(r'.cl')
# patt = re.compile(r'^This')
# patt = re.compile(r'.cl')
# patt = re.compile(r'es.$')
# patt = re.compile(r'a*i*')
# patt = re.compile(r'ai+')
# patt = re.compile(r'da{1}')
# patt = re.compile(r'(da){1}')
# patt = re.compile(r'(da){1}|t')


# special Sequence
# patt = re.compile(r'\aTa')
# patt = re.compile(r'Ta\b')
# patt = re.compile(r'\bTa')
patt = re.compile(r'\d{2}-\d{4}')


matches = patt.finditer(mystr)
for match in matches:
    print(match)
    # print(mystr[111:116])

