"""Basic tests for the Student Management System."""
import unittest
from unittest.mock import patch
import student_management as sms


class StudentManagementTests(unittest.TestCase):
    def setUp(self):
        sms.students.clear()

    def test_add_student(self):
        with patch("builtins.input", side_effect=["101", "Rahul", "CSE"]):
            sms.add_student()
        self.assertEqual(sms.students, [{"roll": 101, "name": "Rahul", "branch": "CSE"}])

    def test_duplicate_roll_is_rejected(self):
        sms.students.append({"roll": 101, "name": "Rahul", "branch": "CSE"})
        with patch("builtins.input", side_effect=["101", "Madhu", "CSE"]):
            sms.add_student()
        self.assertEqual(len(sms.students), 1)

    def test_find_student(self):
        sms.students.append({"roll": 101, "name": "Rahul", "branch": "CSE"})
        self.assertEqual(sms.find_student(101)["name"], "Rahul")
        self.assertIsNone(sms.find_student(999))

    def test_delete_student(self):
        sms.students.append({"roll": 101, "name": "Rahul", "branch": "CSE"})
        with patch("builtins.input", return_value="101"):
            sms.delete_student()
        self.assertEqual(sms.students, [])


if __name__ == "__main__":
    unittest.main()
