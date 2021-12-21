# unittest
from unittest import TestCase

from session_01_02.general_python.file import read_data_to_json


class TestUtils(TestCase):

    def setUp(self) -> None:
        print("preparar ambiente de pruebas")

    def tearDown(self) -> None:
        print("una vez ejecutado los tests")

    def test_given_valid_input_read_file(self):
        # Given
        fake_path = "nada.json"

        # When
        result = read_data_to_json(file_path=fake_path)

        # Then
        self.assertIsNone(result)
