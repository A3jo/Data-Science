print("SJC23MCA-2008 : AJO JOJO")
print("Batch : MCA 2023-25")
import numpy as np;
X = np.array([[1, 2],
[3, 4],[5,6]])
Y = np.random.rand(*X.shape)
result = X * 2 + 2 * Y
print(result)