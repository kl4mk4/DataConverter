# DataConverter

## Opis projektu
**DataConverter** to program do konwersji danych pomiędzy formatami .xml, .json i .yml (.yaml). Program umożliwia przekonwertowanie danych z jednego formatu na inny, zapewniając poprawność składni i formatowania.

## Sposób użycia
Program jest uruchamiany z linii poleceń w następujący sposób:

```sh
data_converter.exe input_file output_file
```

gdzie `input_file` to ścieżka do pliku wejściowego, a `output_file` to ścieżka do pliku wyjściowego. Program automatycznie rozpozna format pliku wejściowego i przekonwertuje go do formatu pliku wyjściowego.

## Instalacja
Aby zainstalować wymagane zależności, uruchom poniższy skrypt:

```sh
./installResources.ps1
```

Skrypt ten zainstaluje wszystkie niezbędne komponenty Python, w tym:

- pyinstaller
- pyqt5
- pyyaml

## Budowanie pliku .exe
Aby zbudować plik wykonywalny .exe, użyj PyInstaller z flagą `--onefile` oraz `--noconsole`, aby uniknąć wyświetlania konsoli:
```sh
pyinstaller --onefile --noconsole converter.py
```
## Konfiguracja GitHub Actions
Projekt zawiera konfigurację GitHub Actions do automatycznego budowania i przesyłania pliku .exe na GitHub. Plik workflow znajduje się w `.github/workflows/build.yaml.`

### Zawartość pliku build.yaml:
```yaml
name: Build and Upload

on:
  push:
    branches:
      - main
  schedule:
    - cron: '0 0 * * 0'  # Automatyczne uruchomienie raz w tygodniu
  workflow_dispatch:  # Ręczne uruchomienie przez użytkownika

jobs:
  build:
    runs-on: windows-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        ./installResources.ps1

    - name: Build with PyInstaller
      run: |
        pyinstaller --onefile --noconsole converter.py

    - name: Upload artifact
      uses: actions/upload-artifact@v2
      with:
        name: converter-exe
        path: dist/converter.exe
```

## Zadania do wykonania
- Task0: Utwórz skrypt `installResources.ps1` do instalacji wymaganych komponentów.
- Task1: Parsowanie argumentów przekazywanych przy uruchomieniu programu.
- Task2: Wczytywanie do obiektu z pliku .json i weryfikacja poprawności składni pliku.
- Task3: Zapis danych z obiektu do pliku w formacie i zgodnie ze składnią .json.

## Dokumentacja
Więcej informacji na temat GitHub Actions można znaleźć w oficjalnej dokumentacji: [GitHub Actions Documentation](https://docs.github.com/en/actions)

## Licencja
Ten projekt jest licencjonowany na podstawie licencji MIT.

## Autor
- Szymon Klamka
