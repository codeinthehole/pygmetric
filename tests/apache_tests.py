import unittest

import mock


STDOUT = """Total Accesses: 5985679
Total kBytes: 27920506
CPULoad: .00514138
Uptime: 4238554
ReqPerSec: 1.4122
BytesPerSec: 6745.37
BytesPerReq: 4776.5
BusyWorkers: 1
IdleWorkers: 9
Scoreboard: _______..W.__.......................................................
................................................................................
................................................................................
............................
"""


class ApacheTests(unittest.TestCase):

    def test_keys_present(self):
        with mock.patch('pygmetric.shell.run') as run:
            run.return_value = STDOUT
            from pygmetric import apache
            stats = apache.fetch_stats()
        self.assertEqual(6, len(stats))

    def test_submit(self):
        with mock.patch('pygmetric.shell.run') as run:
            run.return_value = STDOUT
            from pygmetric import apache
            apache.submit()


