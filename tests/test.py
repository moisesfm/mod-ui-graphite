import unittest
import urlparse
import sys
import os
import time
from datetime import datetime


FILE_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH = os.path.abspath(os.path.join(FILE_PATH, '../'))
sys.path.append(ROOT_PATH)

from module.util import JSONTemplate
from module.graphite_utils import GraphStyle, graphite_time


class TestGraphiteTarget(unittest.TestCase):
    pass


class TestGraphiteURL(unittest.TestCase):
    pass


class TestGraphiteMetric(unittest.TestCase):
    pass


class TestGraphiteTime(unittest.TestCase):
    def test_unixtime_0(self):
        self.assertEqual(graphite_time(0), '17:00_19691231')

    def test_unixtime_now(self):
        self.assertEqual(graphite_time(time.time()), datetime.now().strftime('%H:%M_%Y%m%d'))

    def test_string(self):
        self.assertEqual(graphite_time('test'), 'test')


class TestGraphiteStyle(unittest.TestCase):
    def test_base(self):
        style = GraphStyle()
        style = urlparse.parse_qs(str(style))
        self.assertEqual(style, {'width': ['586'], 'height': ['308'], 'fontSize': ['8']})

    def test_width(self):
        style = GraphStyle(width=10)
        style = urlparse.parse_qs(str(style))
        self.assertEqual(style, {'width': ['10'], 'height': ['308'], 'fontSize': ['8']})
        with self.assertRaises(ValueError):
            GraphStyle(width='test')

    def test_height(self):
        style = GraphStyle(height=7)
        style = urlparse.parse_qs(str(style))
        self.assertEqual(style, {'width': ['586'], 'height': ['7'], 'fontSize': ['8']})
        with self.assertRaises(ValueError):
            GraphStyle(height='test')

    def test_font(self):
        style = GraphStyle(font_size=16)
        style = urlparse.parse_qs(str(style))
        self.assertEqual(style, {'width': ['586'], 'height': ['308'], 'fontSize': ['16']})
        with self.assertRaises(ValueError):
            GraphStyle(font_size='test')

    def test_line_style(self):
        style = GraphStyle(line_style='connected')
        style = urlparse.parse_qs(str(style))
        self.assertEqual(style, {'width': ['586'], 'height': ['308'], 'fontSize': ['8'], 'lineMode': ['connected']})


class TestJSONTemplate(unittest.TestCase):
    data = [
        {
            "width": 586,
            "height": 308,
            "title": "Response Time on {{host}}",
            "min": 0,
            "targets": [
                {
                    "target": "legendValue(alias({{host}}.{{service}}.rta,\"Response Time\"),\"last\")"
                }
            ]
        },
        {
            "width": 586,
            "height": 308,
            "title": "Packet Loss Percentage on {{host}}",
            "min": 0,
            "max": 100,
            "targets": [
                {
                    "target": "legendValue(alias({{host}}.{{service}}.pl,\"Packet loss percentage\"),\"last\")"
                }
            ]
        }
    ]
    def test_load_file_path(self):
        file_path = os.path.join(ROOT_PATH, 'tempaltes', 'graphite', 'check-host-alive.graph')
        template = JSONTemplate(file_path)
        self.assertEqual(template.data, self.data)


class TestGraphFactory(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()