import unittest
import mock

from pygmetric import rabbitmq


STDOUT = """Listing queues ...
solr	25578
csv.landmark-pe-proc1.celeryd.pidbox	0
celerydlery.landmark-pe-proc1.celeryd.pidbox	0
default	0
solr.landmark-pe-proc11.celeryd.pidbox	0
csv_imports	0
...done.
"""


@mock.patch('pygmetric.shell.run')
class RabbitmqTests(unittest.TestCase):

    def test_queue_count_captured(self, mock_run):
        mock_run.return_value = STDOUT
        stats = rabbitmq.fetch_stats(vhost='/', queue='solr')
        self.assertEqual(stats['rabbitmq_queue_solr']['value'], 25578)

    @mock.patch('pygmetric.get_rate')
    def test_queue_rate_captured(self, mock_rate, mock_run):
        mock_run.return_value = STDOUT
        mock_rate.return_value = 3
        stats = rabbitmq.fetch_stats(vhost='/', queue='solr')
        self.assertEqual(stats['rabbitmq_queue_solr_rate']['value'], 3)
