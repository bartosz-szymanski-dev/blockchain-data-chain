# Prosty łańcuch danych w wybranym języku programowania

Prosty łańcuch danych w wybranym języku programowania to projekt edukacyjny demonstrujący podstawowe mechanizmy działania blockchaina, w tym system transakcji i algorytm proof-of-work (PoW).

## Funkcjonalności

- Tworzenie łańcucha bloków z danymi transakcyjnymi.
- Dodawanie transakcji do kolejki.
- Wydobywanie nowych bloków z wykorzystaniem mechanizmu proof-of-work.
- Weryfikacja integralności łańcucha przy każdym dodaniu bloku.

## Technologie

Projekt został napisany w Pythonie i używa biblioteki `hashlib` do obliczeń kryptograficznych.

## Struktura Projektu

- `block.py` - Definicja klasy `Block`, która reprezentuje pojedynczy blok w łańcuchu.
- `transaction.py` - Definicja klasy `Transaction`, która reprezentuje pojedynczą transakcję.
- `blockchain.py` - Główna klasa `Blockchain` zarządzająca łańcuchem bloków.

## Uruchamianie Projektu

Aby uruchomić projekt, upewnij się, że masz zainstalowanego Pythona3, a następnie wykonaj plik `main.py` w swoim środowisku.

```bash
python3 main.py
