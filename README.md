# Zarządzanie Zadaniami

## Opis
Projekt implementuje system zarządzania zadaniami wykorzystujący różne wzorce projektowe i interfejs graficzny stworzony w tkinter.
Program do implementacji testów został wykorzystany z zająć wzorce projektowe od Błażeja Moczydłowskiego. W wykonaniu pracy zaliczeniowej brali udział Bartek Woźnica, Patryk Gawicki, Błażej Moczydłowski.

## Struktura Systemu
Projekt składa się z następujących komponentów:
- **Zadanie**: Klasa reprezentująca zadanie z jego tytułem, opisem i stanem.
- **Powiadomienie**: Implementacja mostu umożliwiająca wysyłanie powiadomień przez email lub SMS.
- **Polecenie**: Implementacja wzorca polecenia do dodawania, usuwania i modyfikowania zadań.
- **Stan**: Implementacja wzorca stanu dla różnych stanów zadania (Nowe, W Trakcie, Ukończone).
- **MenedzerZadan**: Klasa zarządzająca zbiorami zadań.

## Scenariusze Testów
### Testy Akceptacyjne
1. **Dodawanie Zadania**: Testuje dodawanie zadania przez interfejs użytkownika.
2. **Usuwanie Zadania**: Testuje usuwanie zadania przez interfejs użytkownika.
3. **Modyfikowanie Zadania**: Testuje modyfikowanie zadania przez interfejs użytkownika.
python -m pytest -v test_akceptacyjne.py

### Testy Integracyjne
- **TestMenedzerZadan**: Testuje dodawanie i usuwanie zadania z menedżera zadań.
python -m unittest test_integracyjne.py

### Testy Jednostkowe
- **TestZadanie**: Testuje poprawność reprezentacji tekstowej zadania.
python -m unittest -v test_jednostkowe.py

## Wykorzystane Narzędzia i Biblioteki
- Python 3
- tkinter - biblioteka do budowy interfejsu graficznego.
- pytest - framework do testowania w Pythonie.
- unittest - wbudowany framework do testów jednostkowych w Pythonie.

## Ewentualne Problemy i Ich Rozwiązania
- **Problem**: Brak obsługi błędów dla pustych tytułów lub opisów przy dodawaniu zadania.
  **Rozwiązanie**: Dodanie warunków sprawdzających przed dodaniem zadania, informowanie użytkownika o błędzie.

- **Problem**: Możliwość dodania wielu zadań o tym samym tytule.
  **Rozwiązanie**: Implementacja unikalnych identyfikatorów lub dodatkowej walidacji tytułów.

## Uruchomienie
Aby uruchomić aplikację, należy uruchomić plik `Blazej_Moczydlowski.py` w interpreterze Pythona.


```python
python Blazej_Moczydlowski.py
python -m pytest -v test_akceptacyjne.py
python -m unittest test_integracyjne.py
python -m unittest -v test_jednostkowe.py