import os
import csv
import matplotlib.pyplot as plt

from linreg_simple import linear_regression, predict, create_line

if __name__ == '__main__':
    x = []
    y = []

    with open(os.path.join(os.path.dirname(__file__), '../data/data1.csv'), ) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            x.append(float(row['drug']))
            y.append(float(row['score']))

    slope, intercept = linear_regression(x, y)

    line_y = create_line(x, slope, intercept)

    predicted_y = predict(5.5, slope, intercept)
    print('Student sa kolicinom narkotika u krvi 5.5 je ostvario rezultat {0}.'.format(predicted_y))

    plt.plot(x, y, '.')
    plt.plot(x, line_y, 'b')
    plt.title('Slope: {0}, intercept: {1}'.format(slope, intercept))
    plt.xlabel('drug')
    plt.ylabel('score')
    plt.show()
