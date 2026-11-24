# journal.py
import threading

class Journal:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            new = super().__new__(cls)
            new._initialisation()
            cls._instance = new
        return cls._instance

    def _initialisation(self):
        self._verrou = threading.Lock()
        self._messages = []

    def enregistrer(self, message: str) -> None:
        with self._verrou:
            self._messages.append(message)

    def vider(self):
        with self._verrou:
            self._messages.clear()

    def afficher(self) -> None:
        for msg in self._messages:
            print(msg)

    def nb_messages(self) -> int:
        return len(self._messages)