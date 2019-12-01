import matplotlib.pyplot as plt
import numpy as np

objects = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
x_pos = np.arange(len(objects))
performance = [8, 6, 4, 3, 2, 1]

plt.bar(x_pos, performance)
plt.xticks(x_pos, objects)
plt.xlabel('Language')
plt.ylabel('Usage')
plt.title('Programming Language Usage')

plt.show()