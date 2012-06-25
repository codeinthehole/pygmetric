import pygmetric.shell
import pygmetric


def submit(vhost, queue, debug):
    stats = fetch_stats(vhost, queue)
    for metric in stats.values():
        pygmetric.shell.call_gmetric(name=metric['name'],
                                     value=metric['value'],
                                     type=metric['type'],
                                     units=metric['units'],
                                     debug=debug)


def fetch_stats(vhost, queue):
    """
    Fetch stats of a given queue
    """
    cmd = '/usr/sbin/rabbitmqctl list_queues -p %s' % vhost
    stdout = pygmetric.shell.run(cmd)
    lines = stdout.split("\n")

    metrics = {}
    for line in lines:
        if "\t" not in line:
            continue
        queue_name, count = line.split("\t")
        if queue_name == queue:
            value = int(count)
            name = 'rabbitmq_queue_%s' % queue
            metrics[name] = {
                'name': name,
                'value': value,
                'type': 'uint32',
                'units': 'Queue size',
            }
            rate_name = "%s_rate" % name
            rate = pygmetric.get_rate(rate_name, value, period=60)
            
            if rate:
                metrics[rate_name] = {
                    'name': rate_name,
                    'value': rate,
                    'type': 'float',
                    'units': 'Items per minute',
                }
    return metrics
    

