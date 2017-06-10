# -*- coding: utf-8 -*-
"""
Created on Fri May 26 12:00:17 2017

@author: Ian
"""

f = open('C:\Users\Ian\Desktop\ExperimentData.txt', 'r')
a = f.read()
f.close()

g = open('C:/Users/Ian/Desktop/template.py')
apple = g.read()
g.close()

f = open('C:\Users\Ian\Desktop\ExperimentData.txt', 'r')
for line in f: 
    art = line.rstrip('	') + '    '
    a = a.replace(line,art)
f.close()



           
pear = apple.replace('STRING', a)

h = open('C:\Users\Ian\Desktop\PressedExpData.py', 'w')
h.write(pear)
h.close()

expno = {}
with open('C:\Users\Ian\Desktop\ExperimentData.txt') as e:
    for line in e:
        splitLine = line.split()
        expno[int(splitLine[0])] = ','.join(splitLine[1:])
e.close()

print ' '
print ' '
print ' '
print expno[252]
print ' '
print ' '
print ' '
#print pear
