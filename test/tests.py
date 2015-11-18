import unittest
import os
from datetime import datetime

import icsliberator.liberatorlib

class TestLiberator(unittest.TestCase):

    def setUp(self):
        pass

    def test_basic_item(self):

        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "data/sub_file.txt"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path) as f:
            lines = f.readlines()
            response = icsliberator.liberatorlib.handle_whole_record(lines)
            response.list = "Books to read"
            todo = icsliberator.liberatorlib.TodoEntry()
            todo.createdDate = datetime.strptime("2015-06-26 00:00:00", "%Y-%m-%d %H:%M:%S")
            todo.list = "Books to read"
            todo.summary = "Funky Restaurant"
            self.assertEqual(response, todo)
            return

        self.assertEqual(False, True)

    def test_basic_item_str(self):
        todo = icsliberator.liberatorlib.TodoEntry()
        todo.createdDate = datetime.strptime("2015-06-26 00:00:00", "%Y-%m-%d %H:%M:%S")
        todo.list = "Books to read"
        todo.summary = "Funky Restaurant"
        self.assertEqual(str(todo), "2015-06-26 Funky Restaurant @Books_to_read")

    def test_basic_item_str_completed(self):
        todo = icsliberator.liberatorlib.TodoEntry()
        todo.createdDate = datetime.strptime("2015-06-26 00:00:00", "%Y-%m-%d %H:%M:%S")
        todo.completedDate = datetime.strptime("2015-06-26 00:00:00", "%Y-%m-%d %H:%M:%S")
        todo.list = "Books to read"
        todo.summary = "Funky Restaurant"
        self.assertEqual(str(todo), "x 2015-06-26 Funky Restaurant @Books_to_read")
