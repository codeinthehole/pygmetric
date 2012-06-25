import pygmetric.shell
import pygmetric 


def submit(user, password, debug):
    stats = fetch_stats(user, password)
    for metric in stats.values():
        pygmetric.shell.call_gmetric(name=metric['name'],
                                     value=metric['value'],
                                     type=metric['type'],
                                     units=metric['units'],
                                     debug=debug)


COUNT_METRICS = {
    'Threads_connected': {
        'name': 'mysql_threads_connected',
        'type': 'uint32',
        'units': 'Threads',
    },
    'Threads_running': {
        'name': 'mysql_threads_running',
        'type': 'uint32',
        'units': 'Threads',
    },
}

RATE_METRICS = {
    'Connections': {
        'name': 'mysql_connections_rate',
        'type': 'float',
        'units': 'Conns/second',
    },
    'Queries': {
        'name': 'mysql_query_rate',
        'type': 'float',
        'units': 'Queries/second',
    },
    'Com_select': {
        'name': 'mysql_query_select_rate',
        'type': 'float',
        'units': 'Queries/second',
    },
    'Com_update': {
        'name': 'mysql_query_update_rate',
        'type': 'float',
        'units': 'Queries/second',
    },
    'Com_insert': {
        'name': 'mysql_query_insert',
        'type': 'float',
        'units': 'Queries/second',
    },
    'Com_delete': {
        'name': 'mysql_query_delete_rate',
        'type': 'float',
        'units': 'Queries/second',
    },
    'Com_load': {
        'name': 'mysql_query_load_rate',
        'type': 'float',
        'units': 'Queries/second',
    },
    'Slow_queries': {
        'name': 'mysql_slow_queries',
        'type': 'float',
        'units': 'Queries/second',
    },
    'Created_tmp_tables': {
        'name': 'mysql_created_tmp_tables',
        'type': 'float',
        'units': 'Tables/second',
    },
    'Bytes_received': {
        'name': 'mysql_bytes_received',
        'type': 'float',
        'units': 'Bytes/second',
    },
    'Bytes_sent': {
        'name': 'mysql_bytes_sent',
        'type': 'float',
        'units': 'Bytes/second',
    },
}


def fetch_stats(user, password):
    cmd = 'mysqladmin extended --user=%s --password=%s' % (user, password)
    stdout = pygmetric.shell.run(cmd)

    metrics = {}
    for line in stdout.split("\n"):
        parts = line.split()
        if len(parts) != 5:
            continue
        mysql_name, value = parts[1], parts[3]
        if mysql_name in COUNT_METRICS:
            prototype = COUNT_METRICS[mysql_name]
            metrics[prototype['name']] = {
                'name': prototype['name'],
                'value': int(value),
                'type': prototype['type'],
                'units': prototype['units'],
            }
        elif mysql_name in RATE_METRICS:
            prototype = RATE_METRICS[mysql_name]
            current_value = int(value)
            value = pygmetric.get_rate(prototype['name'], current_value, 1)
            if value:
                metrics[prototype['name']] = {
                    'name': prototype['name'],
                    'value': value,
                    'type': prototype['type'],
                    'units': prototype['units'],
                }
    return metrics