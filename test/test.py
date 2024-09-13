#Tests written by geminiAI

import sys
sys.path.append("..")
from task_manager.task_mannager_class import TaskManager
import unittest
class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    # Edge Case Testing
    def test_empty_lists(self):
        self.assertEqual(self.task_manager.to_do, [])
        self.assertEqual(self.task_manager.done, [])

        self.assertEqual(self.task_manager.clear_todo_list(), "It's already empty.")
        self.assertEqual(self.task_manager.clear_done_list(), "It's already empty.")
        self.assertEqual(self.task_manager.reset(), "The lists are already empty")

    def test_duplicate_tasks(self):
        self.task_manager.add_task("Task 1", "task 1")
        self.assertEqual(self.task_manager.to_do, ["Task 1"])

    def test_special_characters(self):
        self.task_manager.add_task("Task 1", "Task 2 with spaces", "Task 3\nNew line")
        self.assertEqual(self.task_manager.to_do, ["Task 1", "Task 2 with spaces", "Task 3\nNew line"])

    def test_task_length(self):
        long_task = "This is a very long task that exceeds the maximum length."
        self.task_manager.add_task(long_task)
        self.assertIn(long_task, self.task_manager.to_do)

    # Error Handling
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            self.task_manager.add_task(123)

        with self.assertRaises(TypeError):
            self.task_manager.remove_task(123)

        with self.assertRaises(ValueError):
            self.task_manager.current_state("invalid_option")

    def test_unexpected_conditions(self):
        self.task_manager.to_do = None
        with self.assertRaises(AttributeError):
            self.task_manager.add_task("Task")

    # Performance Testing
    def test_large_dataset(self):
        num_tasks = 10000
        tasks = [f"Task {i}" for i in range(num_tasks)]
        self.task_manager.add_task(*tasks)
        self.assertEqual(len(self.task_manager.to_do), num_tasks)

    # Integration Testing (assuming other components)
    # ... (replace with actual integration tests)

if __name__ == '__main__':
    unittest.main()

