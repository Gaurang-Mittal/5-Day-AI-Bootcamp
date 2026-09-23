
import numpy as np
from statistics import mode
languages=np.array(['java','pyhton','c','cpp','rust'])
values=np.array([10,20,30,40,50])

np.random.seed(5)
final=np.random.randint(10,101,size=5)


print("languages:",languages)
print("values",values)
print("final",final)


print("sum",np.sum(final))
print("mean",np.mean(final))
print("median",np.median(final))
print("mode",mode(final))
