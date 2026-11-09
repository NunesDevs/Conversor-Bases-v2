import unittest
import subprocess
import sys
from pathlib import Path
from conversor import to_decimal


class ConversionTests(unittest.TestCase):
    def test_cli_retries_invalid_digit_and_exits(self):
        script = str(Path(__file__).resolve().parents[1] / 'conversor.py')
        process = subprocess.run([sys.executable, '-X', 'utf8', script], input='1\n2\n3\nff\nn\n', text=True, encoding='utf-8', capture_output=True, timeout=5)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertIn('Dígito inválido para base 2', process.stdout)
        self.assertIn('Resultado da conversão: 255', process.stdout)
        eof = subprocess.run([sys.executable, '-X', 'utf8', script], input='', text=True, encoding='utf-8', capture_output=True, timeout=5)
        self.assertEqual(eof.returncode, 0, eof.stderr)
        self.assertIn('Encerrando', eof.stdout)

    def test_digits_zero_and_sign(self):
        for value, base, expected in [("10101", 2, 21), ("77", 8, 63), ("ff", 16, 255), ("j", 20, 19), ("-J", 20, -19), (" +0010 ", 2, 2), ("0", 4, 0)]:
            self.assertEqual(to_decimal(value, base), expected)

    def test_reject_invalid_digits_and_empty_input(self):
        for value, base in [("2", 2), ("8", 8), ("G", 16), ("K", 20), ("", 2), ("-", 2), ("1 0", 2), ("0xFF", 16), ("1_0", 2), ("1.0", 2)]:
            with self.assertRaises(ValueError):
                to_decimal(value, base)
        with self.assertRaises(ValueError):
            to_decimal("10", 3)
        with self.assertRaises(TypeError):
            to_decimal(10, 2)

    def test_positional_evaluation_against_python(self):
        for base in (2, 4, 8, 16, 20):
            for digits in ("10", "101", "1111111111111111111111111"):
                self.assertEqual(to_decimal(digits, base), int(digits, base))


if __name__ == "__main__":
    unittest.main()
