import unittest
from Blazej_Moczydlowski import Zadanie, NoweZadanie

class TestZadanie(unittest.TestCase):
    def test_zadanie_str(self):
        """Test sprawdza, czy reprezentacja tekstowa zadania jest poprawna"""
        stan = NoweZadanie()
        zadanie = Zadanie("Test", "Opis testowy", stan)
        self.assertEqual(str(zadanie), "Zadanie: Test, Opis: Opis testowy, Stan: Nowe")

if __name__ == "__main__":
    unittest.main()
