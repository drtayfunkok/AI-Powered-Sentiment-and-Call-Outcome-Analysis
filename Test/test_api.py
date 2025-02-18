import unittest
import requests

class TestAPI(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"

    def test_upload_file(self):
        files = {'file': open("sample_transcript.txt", 'rb')}
        response = requests.post(f"{self.API_URL}/", files=files)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

