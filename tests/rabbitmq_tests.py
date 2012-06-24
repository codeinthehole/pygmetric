import unittest

import mock


STDOUT = """Listing queues ...
solr	25578
csv.landmark-pe-proc1.celeryd.pidbox	0
celerydlery.landmark-pe-proc1.celeryd.pidbox	0
default	0
solr.landmark-pe-proc11.celeryd.pidbox	0
csv_imports	0
...done.
"""


class RabbitmqTests(unittest.TestCase):

    def test_queue_count_captured(self):
        with mock.patch('pygmetric.shell.run') as run:
            run.return_value = STDOUT
            from pygmetric import rabbitmq
            stats = rabbitmq.fetch_stats(vhost='/', queue='solr')
        self.assertEqual(stats['rabbitmq_queue_solr']['value'], 25578)
