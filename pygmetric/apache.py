from pygmetric.shell import run, call_gmetric


def submit(host, port):
    stats = fetch_stats(host, port)
    for metric in stats:
        call_gmetric(name=metric['name'],
                     value=metric['value'],
                     type=metric['type'])

types = {
    'IdleWorkers': {
        'name': 'apache_idle_workers',
        'type': 'uint32',
    },
    'CPULoad': {
        'name': 'apache_cpu_load',
        'type': 'float',
    },
    'BytesPerSec': {
        'name': 'apache_bytes_per_second',
        'type': 'float',
    },
    'BytesPerReq': {
        'name': 'apache_bytes_per_request',
        'type': 'float',
    },
    'BusyWorkers': {
        'name': 'apache_busy_workers',
        'type': 'uint32',
    },
    'ReqPerSec': {
        'name': 'apache_request_per_second',
        'type': 'float',
    },
}

def fetch_stats(host, port):
    cmd = 'www-browser -dump http://%s:%s/server-status?auto' % (host, port)
    stdout = run(cmd)
    stats = []
    for line in stdout.split("\n"):
        if ':' not in line:
            continue
        key, value = line.split(': ')
        if key in types:
            prototype = types[key]
            stats.append({
                'name': prototype['name'],
                'type': prototype['type'],
                'value': value,
            })
    return stats
