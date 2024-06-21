import pytest
import tkinter as tk
from tkinter import Tk
from Blazej_Moczydlowski import Aplikacja

@pytest.fixture
def app():
    """Fixture tworzy instancję aplikacji i zwraca ją do testów"""
    root = Tk()
    application = Aplikacja(root)
    yield application
    root.destroy()

def test_dodaj_zadanie(app):
    """Test sprawdza dodawanie zadania poprzez interfejs użytkownika"""
    app.tytul_entry.insert(0, "Test")
    app.opis_entry.insert(0, "Opis testowy")
    app.stan_var.set("Nowe")
    
    app.dodaj_zadanie()
    
    assert app.zadania_listbox.size() == 1, "Zadanie nie zostało poprawnie dodane"
    assert "Zadanie: Test, Opis: Opis testowy, Stan: Nowe" in app.zadania_listbox.get(0, tk.END), "Zadanie nie zostało poprawnie dodane do listy"
    
    print("Test dodawania zadania zakończony pomyślnie")

def test_usun_zadanie(app):
    """Test sprawdza usuwanie zadania poprzez interfejs użytkownika"""
    app.tytul_entry.insert(0, "Test")
    app.opis_entry.insert(0, "Opis testowy")
    app.stan_var.set("Nowe")
    
    app.dodaj_zadanie()
    app.zadania_listbox.select_set(0)
    app.usun_zadanie()
    
    assert app.zadania_listbox.size() == 0, "Zadanie nie zostało poprawnie usunięte"
    
    print("Test usuwania zadania zakończony pomyślnie")

def test_modyfikuj_zadanie(app):
    """Test sprawdza modyfikowanie zadania poprzez interfejs użytkownika"""
    app.tytul_entry.insert(0, "Test")
    app.opis_entry.insert(0, "Opis testowy")
    app.stan_var.set("Nowe")
    
    app.dodaj_zadanie()
    app.zadania_listbox.select_set(0)
    
    app.opis_entry.delete(0, tk.END)
    app.opis_entry.insert(0, "Nowy opis")
    app.stan_var.set("Ukończone")
    
    app.modyfikuj_zadanie()
    
    assert "Zadanie: Test, Opis: Nowy opis, Stan: Ukończone" in app.zadania_listbox.get(0, tk.END), "Zadanie nie zostało poprawnie zmodyfikowane"
    
    print("Test modyfikowania zadania zakończony pomyślnie")
