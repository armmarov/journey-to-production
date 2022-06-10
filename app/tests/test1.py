import app
import unittest

class Test1(unittest.TestCase):

  def test_index(self):
    tester = app.test_client(self)
    response = tester.get("/health")
    status_code = response.status_code

    self.assertEqual(status_code, 200)

if __name__ == "__main__":
  unittest.main()