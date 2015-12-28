#!/usr/bin/python2.7

import json
from pprint import pprint
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from common import *

# importing dataset
with open('dataset/dump02') as data_file:
    data = json.load(data_file)

samples = data['results'][0]['series'][0]['values']

# tailoring
samples = [[nano_to_epoch(sample[0]), sample[1]] for sample in samples \
            if (nano_to_epoch(sample[0]) > TIMESTAMP_LOWER_BOUND and \
            nano_to_epoch(sample[0]) < TIMESTAMP_UPPER_BOUND)]

samples_x = [datetime.fromtimestamp(sample[0]) for sample in samples]
samples_y = [sample[1] for sample in samples]
assert len(samples_x) == len(samples_y)

print 'dateset length: ', len(samples_x)

print "max connections: ", max(samples_y), "; timestamp: ", samples_x[samples_y.index(max(samples_y))]

plt.plot(samples_x, samples_y, color='r')
ref_points = perdelta(datetime(2015, 12, 20, 18, 0, 0), datetime(2015, 12, 21, 0, 0, 0), timedelta(minutes=30))
for point in ref_points:
    plt.axvline(point, color='k', linestyle='--')
plt.title('connections on gateway')
plt.show()

