import unittest

import mock


STDOUT = """Active connections: 1
server accepts handled requests
 5117421 5117421 5117345
Reading: 0 Writing: 1 Waiting: 0

"""


class NginxTests(unittest.TestCase):

    def test_keys_present(self):
        with mock.patch('pygmetric.shell.run') as run:
            run.return_value = STDOUT
            from pygmetric import nginx
            stats = nginx.fetch_stats(host='localhost', port='80')
        self.assertEqual(stats['nginx_active_connections']['value'], 1)
        self.assertEqual(stats['nginx_server_accepts']['value'], 5117421)
        self.assertEqual(stats['nginx_server_handled']['value'], 5117421)
        self.assertEqual(stats['nginx_server_requests']['value'], 5117345)
