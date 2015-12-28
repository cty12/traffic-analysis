from datetime import datetime
from pytz import timezone

# unix epoch timestamp
# from 1800 dec. 20 to 0000 dec. 21, utc+8
TIMESTAMP_LOWER_BOUND = 1450605600
TIMESTAMP_UPPER_BOUND = 1450627200
TIMEZONE = 'Asia/Shanghai'

DATETIME_LOWER_BOUND = datetime.fromtimestamp(TIMESTAMP_LOWER_BOUND, timezone(TIMEZONE))
DATETIME_UPPER_BOUND = datetime.fromtimestamp(TIMESTAMP_UPPER_BOUND, timezone(TIMEZONE))

INTERFACE_LIST = ['em1', 'em1.2', 'em1.3', 'em1.8', 'br0', 'lo']
DIRECTION_LIST = ['rx', 'tx']

# nanosecond to unix epoch timestamp converter
def nano_to_epoch(nano): return nano / 1000000 / 1000.0

# generate datetime obj with a delta time interval
def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

