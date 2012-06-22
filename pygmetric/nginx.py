import re
import time
import pickle
import os

from pygmetric.shell import run, call_gmetric


def submit(host, port, debug):
    stats = fetch_stats(host, port)
    for metric in stats:
        call_gmetric(name=metric['name'],
                     value=metric['value'],
                     type=metric['type'],
                     debug=debug)


def fetch_stats(host, port):
    cmd = 'www-browser -dump http://%s:%s/nginx_status' % (host, port)
    stdout = run(cmd)
    lines = stdout.split("\n")
    if len(lines) < 4:
        raise RuntimeError("Invalid output: %s" % stdout)
    metrics = {}
    metrics['nginx_active_connections'] = {
        'name': 'nginx_active_connections',
        'type': 'uint32',
        'value': int(lines[0].split(': ')[1])
    }

    # Global stats - need to use these with previous values
    accepts, handled, requests = map(int, lines[2].split())
    metrics['nginx_server_accepts'] = {
        'name': 'nginx_server_accepts',
        'type': 'uint32',
        'value': accepts
    }
    metrics['nginx_server_handled'] = {
        'name': 'nginx_server_handled',
        'type': 'uint32',
        'value': handled
    }
    metrics['nginx_server_requests'] = {
        'name': 'nginx_server_requests',
        'type': 'uint32',
        'value': requests
    }

    # Attempt to load stats
    ts = int(time.time())
    filepath = '/tmp/nginx_stats'
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            old_data = pickle.load(f)
            delta = ts - old_data['timestamp']
            metrics['nginx_server_accepts_rate'] = {
                'name': 'nginx_server_accepts_rate',
                'type': 'float',
                'value': (accepts - old_data['accepts']) / delta
            }
            metrics['nginx_server_handled_rate'] = {
                'name': 'nginx_server_handled_rate',
                'type': 'float',
                'value': (handled - old_data['handled']) / delta
            }
            metrics['nginx_server_requests_rate'] = {
                'name': 'nginx_server_requests_rate',
                'type': 'float',
                'value': (requests - old_data['requests']) / delta
            }
    data = {
        'timestamp': ts,
        'accepts': accepts,
        'handled': handled,
        'requests': requests
    }
    with open(filepath, 'w') as f:
        pickle.dump(data, f)

    # Active stats
    match = re.match(r'^Reading: (\d+) Writing: (\d+) Waiting: (\d+)', lines[3])
    reading, writing, waiting = map(int, match.groups())
    metrics['nginx_reading'] = {
        'name': 'nginx_reading',
        'type': 'uint32',
        'value': reading
    }
    metrics['nginx_writing'] = {
        'name': 'nginx_writing',
        'type': 'uint32',
        'value': writing
    }
    metrics['nginx_waiting'] = {
        'name': 'nginx_waiting',
        'type': 'uint32',
        'value': waiting
    }

    return metrics
