from __future__ import division
import os
import pickle
import time

__version__ = '0.2'


def get_rate(name, current_value, period=60):
    """
    Fetch the rate of change of the given metric
    """
    # Try and fetch historical value - we use one file per metric
    current_ts = int(time.time())
    filepath = '/tmp/_pygmetric_%s' % name
    rate = None
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            old_stats = pickle.load(f)
            old_ts = old_stats['timestamp']
            old_value = old_stats['value']
            if old_ts != current_ts:
                rate = (current_value - old_value) / (current_ts - old_ts) * period

    # Save current metric for next time
    stats = {
        'timestamp': current_ts,
        'value': current_value
    }
    with open(filepath, 'w') as f:
        pickle.dump(stats, f)
    return rate
