import matplotlib.pyplot as plt
import numpy as np

no_students = 4
ads = [89, 78, 57, 41]
pdv = [72, 83, 65, 91]

#fig, ax = plt.subplots()
x_pts = np.arange(no_students)
b_width = 0.35


rects1 = plt.bar(x_pts, ads, b_width, color='b', label = 'ADS')
rects2 = plt.bar(x_pts + b_width, pdv, b_width, color='g', label = 'PDV')
plt.xlabel('Persons')
plt.ylabel('Scores')
plt.xticks(x_pts + b_width/2,['A', 'B', 'C', 'D'])
plt.title('Scores by Persons')
plt.legend()

plt.tight_layout()

plt.show()