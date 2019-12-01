import matplotlib.pyplot as plt
import numpy as np

objects = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
x_pos = np.arange(len(objects))
performance = [8, 6, 4, 3, 2, 1]

plt.barh(x_pos, performance, align='center')
plt.yticks(x_pos, objects)
plt.xlabel('Usage')
plt.title('Programming Language Usage')

plt.show()