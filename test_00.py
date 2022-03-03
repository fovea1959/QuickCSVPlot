import matplotlib.pyplot as plt
import csv
import numpy as np
data = {}

with open('fixed_shooter_m_20220302-174807.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    labels = reader.fieldnames
    for label in labels:
        data[label] = []
    for row in reader:
        if row['time'] is not None and row['time'] != '':
            for label in labels:
                v = row[label]
                if v is not None:
                    try:
                        v = float(v)
                    except:
                        pass
                data[label].append(v)

x = data['time']
print(x)
y0 = data['main.rpm.actual']
y1 = data['main.rpm.requested']

#x = [ 0, 1, 2]
#y = [0, 1, 2]

min_x = int(min(x) - 1)
max_x = int(max(x) + 1)
print(min_x, max_x)
plt.xticks(np.arange(min_x, max_x + 1, 1.0))
xx = plt.plot(x, y0, y1)
print(type(xx), xx)

if False:
    ax = plt.gca()

    for idx, label in enumerate(ax.xaxis.get_ticklabels()):
        label.set_visible(False)
elif False:
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom=False,  # ticks along the bottom edge are off
        top=False,  # ticks along the top edge are off
        labelbottom=False)  # labels along the bottom edge are off
else:
    #plt.xticks([0., 2., 12.])
    min_x = int(min(x)-1)
    max_x = int(max(x)+1)
    print(min_x, max_x)
    plt.xticks(np.arange(min_x, max_x+1, 1.0))

plt.legend(loc='lower right')
plt.show()