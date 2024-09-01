#Tests written by geminiAI

import unittest
from main import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        self.task_manager.add_task("Task 1", "Task 2")
        self.assertEqual(self.task_manager.to_do, ["Task 1", "Task 2"])

        result = self.task_manager.add_task("Task 1")
        self.assertEqual(result, "Task 1 already in the to-do list:\n ['Task 1', 'Task 2']")

    def test_remove_task(self):
        self.task_manager.add_task("Task 1", "Task 2", "Task 3")
        self.task_manager.remove_task("Task 2", "Task 4")
        self.assertEqual(self.task_manager.to_do, ["Task 1", "Task 3"])

    def test_task_done(self):
        self.task_manager.add_task("Task 1", "Task 2")
        self.task_manager.task_done("Task 1")
        self.assertEqual(self.task_manager.to_do, ["Task 2"])
        self.assertEqual(self.task_manager.done, ["Task 1"])

    def test_current_state(self):
        self.task_manager.add_task("Task 1", "Task 2")
        self.task_manager.task_done("Task 1")

        expected_both = "Your tasks to do are:\n['Task 2']\nYour done tasks are:\n ['Task 1']"
        self.assertEqual(self.task_manager.current_state('both'), expected_both)

        expected_to_do = "Your current to do list is:\n['Task 2']"
        self.assertEqual(self.task_manager.current_state('to-do'), expected_to_do)

        expected_done = "Your done tasks are:\n['Task 1']"
        self.assertEqual(self.task_manager.current_state('done'), expected_done)

    def test_clear_lists(self):
        self.task_manager.add_task("Task 1", "Task 2")
        self.task_manager.task_done("Task 1")

        self.task_manager.clear_todo_list()
        self.assertEqual(self.task_manager.to_do, [])
        self.assertEqual(self.task_manager.done, ["Task 1"])

        self.task_manager.clear_done_list()
        self.assertEqual(self.task_manager.to_do, [])
        self.assertEqual(self.task_manager.done, [])

    def test_reset(self):
        self.task_manager.add_task("Task 1", "Task 2")
        self.task_manager.task_done("Task 1")

        self.task_manager.reset()
        self.assertEqual(self.task_manager.to_do, [])
        self.assertEqual(self.task_manager.done, [])

if __name__ == '__main__':
    unittest.main()
