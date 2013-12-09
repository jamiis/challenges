from math import pow
r = range(1,101)
print int(pow(sum(r),2) - sum([pow(i,2) for i in r]))
