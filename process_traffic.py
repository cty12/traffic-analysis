#!/usr/bin/python2.7

# Analysis script of the traffic of the Gateway server

import json
from datetime import datetime
from pytz import timezone
import matplotlib.pyplot as plt
from common import *

LOG_FILENAME = 'dataset/dump01'

# importing dateset
with open(LOG_FILENAME) as log_file:
    data = json.load(log_file)

samples = data['results'][0]['series'][0]['values']

# tailoring
traffic = dict()
for interface in INTERFACE_LIST:
    traffic[interface] = dict()
    for direction in DIRECTION_LIST:
        traffic[interface][direction] = [[nano_to_epoch(sample[0]), sample[3]] for sample in samples \
        if (sample[1] == direction and sample[2] == interface \
        and nano_to_epoch(sample[0]) > TIMESTAMP_LOWER_BOUND \
        and nano_to_epoch(sample[0]) < TIMESTAMP_UPPER_BOUND)]

# for debug
for interface in INTERFACE_LIST:
    for direction in DIRECTION_LIST:
        print 'interface: ', interface, '; direction: ', direction, '; number: ', len(traffic[interface][direction])

# plotting
graph_index = 1
for interface in INTERFACE_LIST:
    plt.figure(graph_index)
    plt.subplot(211)
    sample_x = [datetime.fromtimestamp(sample[0]) for sample in traffic[interface]['rx']]
    sample_y = [sample[1] for sample in traffic[interface]['rx']]
    print 'interface: ', interface, '; max receive bandwidth: ', max(sample_y), '; timestamp: ', sample_x[sample_y.index(max(sample_y))]
    plt.plot(sample_x, sample_y, color='k')
    plt.title('Bandwidth on ' + interface + ', rx\n 18:00 - 24:00, Dec. 20, 2015')
    plt.subplot(212)
    sample_x = [datetime.fromtimestamp(sample[0]) for sample in traffic[interface]['tx']]
    sample_y = [sample[1] for sample in traffic[interface]['tx']]
    print 'interface: ', interface, '; max send bandwidth: ', max(sample_y), '; timestamp: ', sample_x[sample_y.index(max(sample_y))]
    plt.plot(sample_x, sample_y, color='r')
    plt.title('Bandwidth on ' + interface + ', tx')
    graph_index += 1

plt.show()

