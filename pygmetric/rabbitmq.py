from pygmetric.shell import run, call_gmetric


def submit(vhost, queue, debug):
    stats = fetch_stats(vhost, queue)
    for metric in stats.values():
        call_gmetric(name=metric['name'],
                     value=metric['value'],
                     type=metric['type'],
                     units=metric['units'],
                     debug=debug)


def fetch_stats(vhost, queue):
    """
    Fetch the count of a given queue
    """
    cmd = 'rabbitmqctl list_queues -p %s' % vhost
    stdout = run(cmd)
    lines = stdout.split("\n")

    metrics = {}
    for line in lines:
        if "\t" not in line:
            continue
        queue_name, count = line.split("\t")
        if queue_name == queue:
            name = 'rabbitmq_queue_%s' % queue
            metrics[name] = {
                'name': name,
                'value': int(count),
                'type': 'uint32',
                'units': 'Queue size',
            }
    return metrics
