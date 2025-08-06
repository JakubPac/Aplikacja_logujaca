# Aplikacja logowania i rejestracji w Pythonie

Prosta aplikacja desktopowa z GUI w Tkinter, obsługująca rejestrację i logowanie użytkowników z wykorzystaniem bazy danych SQLite.

## Opis projektu

Projekt umożliwia użytkownikom:

- rejestrację nowego konta (z podwójnym wpisywaniem hasła),
- logowanie się przy użyciu wcześniej założonego konta,
- bezpieczne przechowywanie haseł w bazie (haszowane za pomocą SHA-256),
- przełączanie się między ekranem logowania i rejestracji w tym samym oknie.

## Wymagania

- Python 3.x (testowane na Python 3.8+)
- Moduły standardowe: `tkinter`, `sqlite3`, `hashlib`

Nie jest potrzebna instalacja zewnętrznych bibliotek.

## Jak uruchomić?

1. Sklonuj lub pobierz repozytorium.
2. Uruchom skrypt:

python aplikacja_logujaca.py


3. Pojawi się okno aplikacji z możliwością logowania i rejestracji.

## Struktura projektu

- `aplikacja_logujaca.py` – główny skrypt zawierający klasę GUI (`AplikacjaLogujaca`) i klasę obsługi bazy danych (`BazaUzytkownikow`).
- `users_db` – plik bazy danych SQLite tworzony automatycznie po pierwszym uruchomieniu.

---

## Funkcjonalności

- Tworzenie kont użytkowników z unikalną nazwą.
- Sprawdzanie poprawności danych podczas rejestracji i logowania.
- Bezpieczne zarządzanie hasłami poprzez ich hash SHA-256.
- Przełączanie się między ekranem logowania i rejestracji bez zamykania okna aplikacji.
- Walidacja podstawowa: puste pola i potwierdzenie hasła.

## Możliwe rozszerzenia

- Dodanie walidacji mocy hasła.
- Implementacja zarządzania sesjami użytkownika.
- Rozbudowa interfejsu o dodatkowe funkcje (reset hasła, profil użytkownika).
- Ulepszenia stylistyczne GUI.

## Autor

Jakub
