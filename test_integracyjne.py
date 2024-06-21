import unittest
from Blazej_Moczydlowski import Zadanie, NoweZadanie, MenedzerZadan

class TestMenedzerZadan(unittest.TestCase):
    def test_dodaj_usun_zadanie(self):
        """Test sprawdza dodawanie i usuwanie zadania z menedżera zadań"""
        menedzer = MenedzerZadan()
        stan = NoweZadanie()
        zadanie = Zadanie("Test", "Opis testowy", stan)
        
        menedzer.dodaj_zadanie(zadanie)
        self.assertIn(zadanie, menedzer.zadania)
        
        menedzer.usun_zadanie(zadanie)
        self.assertNotIn(zadanie, menedzer.zadania)

if __name__ == "__main__":
    unittest.main()
