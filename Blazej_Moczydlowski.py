import copy
import tkinter as tk
from tkinter import messagebox

# Wzorzec Prototypu
class ZadaniePrototyp:
    def klonuj(self):
        return copy.deepcopy(self)

class Zadanie(ZadaniePrototyp):
    def __init__(self, tytul, opis, stan):
        self.tytul = tytul
        self.opis = opis
        self.stan = stan

    def __str__(self):
        return f"Zadanie: {self.tytul}, Opis: {self.opis}, Stan: {self.stan.nazwa_stanu()}"

# Wzorzec Mostu
class PowiadomienieImplementacja:
    def wyslij_powiadomienie(self, zadanie):
        pass

class EmailPowiadomienie(PowiadomienieImplementacja):
    def wyslij_powiadomienie(self, zadanie):
        print(f"Wysłano email z powiadomieniem o zadaniu: {zadanie.tytul}")

class SMSPowiadomienie(PowiadomienieImplementacja):
    def wyslij_powiadomienie(self, zadanie):
        print(f"Wysłano SMS z powiadomieniem o zadaniu: {zadanie.tytul}")

class Powiadomienie:
    def __init__(self, implementacja):
        self.implementacja = implementacja

    def wyslij(self, zadanie):
        self.implementacja.wyslij_powiadomienie(zadanie)

# Wzorzec Polecenia
class Polecenie:
    def wykonaj(self):
        pass

class DodajZadaniePolecenie(Polecenie):
    def __init__(self, menedzer_zadan, zadanie):
        self.menedzer_zadan = menedzer_zadan
        self.zadanie = zadanie

    def wykonaj(self):
        self.menedzer_zadan.dodaj_zadanie(self.zadanie)

class UsunZadaniePolecenie(Polecenie):
    def __init__(self, menedzer_zadan, zadanie):
        self.menedzer_zadan = menedzer_zadan
        self.zadanie = zadanie

    def wykonaj(self):
        self.menedzer_zadan.usun_zadanie(self.zadanie)

# Wzorzec Stanu
class Stan:
    def nazwa_stanu(self):
        pass

    def obsluz(self, zadanie):
        pass

class NoweZadanie(Stan):
    def nazwa_stanu(self):
        return "Nowe"

    def obsluz(self, zadanie):
        print(f"Zadanie {zadanie.tytul} jest teraz nowe.")

class WTrakcieZadanie(Stan):
    def nazwa_stanu(self):
        return "W Trakcie"

    def obsluz(self, zadanie):
        print(f"Zadanie {zadanie.tytul} jest teraz w trakcie realizacji.")

class UkończoneZadanie(Stan):
    def nazwa_stanu(self):
        return "Ukończone"

    def obsluz(self, zadanie):
        print(f"Zadanie {zadanie.tytul} jest teraz ukończone.")

# Menedżer zadań
class MenedzerZadan:
    def __init__(self):
        self.zadania = []

    def dodaj_zadanie(self, zadanie):
        self.zadania.append(zadanie)
        print(f"Dodano zadanie: {zadanie.tytul}")

    def usun_zadanie(self, zadanie):
        self.zadania.remove(zadanie)
        print(f"Usunięto zadanie: {zadanie.tytul}")

# Modyfikuj Zadanie
class ModyfikujZadaniePolecenie(Polecenie):
    def __init__(self, menedzer_zadan, zadanie, nowy_opis, nowy_stan):
        self.menedzer_zadan = menedzer_zadan
        self.zadanie = zadanie
        self.nowy_opis = nowy_opis
        self.nowy_stan = nowy_stan

    def wykonaj(self):
        self.zadanie.opis = self.nowy_opis
        if self.nowy_stan == "Nowe":
            stan = NoweZadanie()
        elif self.nowy_stan == "W Trakcie":
            stan = WTrakcieZadanie()
        elif self.nowy_stan == "Ukończone":
            stan = UkończoneZadanie()
        self.zadanie.stan = stan
        print(f"Zmodyfikowano zadanie: {self.zadanie.tytul}")

# Interfejs graficzny
class Aplikacja:
    def __init__(self, root):
        self.menedzer_zadan = MenedzerZadan()
        
        self.root = root
        self.root.title("Zarządzanie Zadaniami")
        
        self.tytul_label = tk.Label(root, text="Tytuł")
        self.tytul_label.pack()
        self.tytul_entry = tk.Entry(root)
        self.tytul_entry.pack()
        
        self.opis_label = tk.Label(root, text="Opis")
        self.opis_label.pack()
        self.opis_entry = tk.Entry(root)
        self.opis_entry.pack()

        self.stan_label = tk.Label(root, text="Stan")
        self.stan_label.pack()
        self.stan_var = tk.StringVar(value="Nowe")
        self.stan_menu = tk.OptionMenu(root, self.stan_var, "Nowe", "W Trakcie", "Ukończone")
        self.stan_menu.pack()

        self.add_button = tk.Button(root, text="Dodaj Zadanie", command=self.dodaj_zadanie)
        self.add_button.pack()

        self.usun_button = tk.Button(root, text="Usuń Wybrane Zadanie", command=self.usun_zadanie)
        self.usun_button.pack()

        self.mod_button = tk.Button(root, text="Modyfikuj Zadanie", command=self.modyfikuj_zadanie)
        self.mod_button.pack()


        self.zadania_listbox = tk.Listbox(root)
        self.zadania_listbox.pack(fill=tk.BOTH, expand=True)

    def dodaj_zadanie(self):
        tytul = self.tytul_entry.get()
        opis = self.opis_entry.get()
        stan_nazwa = self.stan_var.get()
        
        if not tytul or not opis:
            messagebox.showwarning("Błąd", "Tytuł i opis nie mogą być puste!")
            return
        
        if stan_nazwa == "Nowe":
            stan = NoweZadanie()
        elif stan_nazwa == "W Trakcie":
            stan = WTrakcieZadanie()
        elif stan_nazwa == "Ukończone":
            stan = UkończoneZadanie()
        
        nowe_zadanie = Zadanie(tytul, opis, stan)
        dodaj_polecenie = DodajZadaniePolecenie(self.menedzer_zadan, nowe_zadanie)
        dodaj_polecenie.wykonaj()
        
        self.zadania_listbox.insert(tk.END, str(nowe_zadanie))

    def usun_zadanie(self):
        selected_index = self.zadania_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Błąd", "Wybierz zadanie do usunięcia!")
            return
        
        zadanie_str = self.zadania_listbox.get(selected_index)
        for zadanie in self.menedzer_zadan.zadania:
            if str(zadanie) == zadanie_str:
                usun_polecenie = UsunZadaniePolecenie(self.menedzer_zadan, zadanie)
                usun_polecenie.wykonaj()
                self.zadania_listbox.delete(selected_index)
                break
    
    def modyfikuj_zadanie(self):
        selected_index = self.zadania_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Błąd", "Wybierz zadanie do modyfikacji!")
            return
        
        zadanie_str = self.zadania_listbox.get(selected_index)
        for zadanie in self.menedzer_zadan.zadania:
            if str(zadanie) == zadanie_str:
                nowy_opis = self.opis_entry.get()
                nowy_stan = self.stan_var.get()
                mod_polecenie = ModyfikujZadaniePolecenie(self.menedzer_zadan, zadanie, nowy_opis, nowy_stan)
                mod_polecenie.wykonaj()
                self.zadania_listbox.delete(selected_index)
                self.zadania_listbox.insert(selected_index, str(zadanie))  # Aktualizacja wyświetlanego opisu zadania
                break

def main():
    root = tk.Tk()
    app = Aplikacja(root)
    root.mainloop()

if __name__ == "__main__":
    main()