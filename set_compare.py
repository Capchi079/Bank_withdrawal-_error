'''s={1,2,3,4,5,7,8,9}
#sum=10
l=list(s)
l2=[ {l[i],l[j]} for i in range(len(l)) for j in range(i+1,len(l)) if l[i]+l[j]==10]
print(l2)
for i in l2:
    if i.issubset(s):
        print('yes')
        '''
import re
# s='hello ths is 123_ long join 321_'
# pattern=re.compile(r'[lo]')
# #print(pattern.findall(s))
# print(pattern.match(s))
# #print(pattern.search(s).group())
# #print(pattern.finditer(s))
'''
test_string='hello HELLO 23_ saty.j9@gmail.com'
pattern=re.compile(r'[a-zA-Z0-9]+[.]?\w+\d+[@]+[gmail,in][.][com]')
matches=pattern.finditer(test_string)
#print(matches) it will give object
for match in matches:
    print(match.group())


date="""
2022-03-23
2022/04/23
"""
# pattern=re.compile(r'\d\d\d\d.\d\d.\d\d')
pattern=re.compile(r'\d\d\d\d[-/]\d\d[-/]\d\d')

matches=pattern.finditer(date)
for match in matches:
    print(match)
  
s="""
satyajit 
mr sai
mr. son
mrs sona
mr bir
"""
pattern=re.compile(r'(mr|mrs)\.?\s\w+')
matches=pattern.finditer(s)
for match in matches:
    print(match)
  '''
'''
#email pattern
email="""
    saty-ajit@gmail.com
    satyajit@gmail.com
    satyajit65@gmail.com
    saty.cho@gmail.com
    """
pattern=re.compile(r'[a-zA-Z0-9]\w*[.]?\w+@[a-zA-Z-]+\.(com|in|org)')
matches=pattern.finditer(email)
for match in matches:
    print(match.group())

'''
#split method use
text='abc123ABCD123abcdABCD123'
pattern=re.compile(r'123')
splited=pattern.split(text)
print(splited)
#sub method use
tst='hellow world welcome, to this wonder fullworld'
pattern=re.compile(r'world')
sub_st=pattern.sub('plant', tst)
print(sub_st)