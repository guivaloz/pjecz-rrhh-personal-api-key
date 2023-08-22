"""
Unit tests for personal category
"""
import unittest

import requests

from tests.load_env import config


class TestPersonal(unittest.TestCase):
    """Tests for personal category"""

    def test_get_personas(self):
        """Test GET method for personas"""
        response = requests.get(
            f"{config['host']}/v4/personas",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
