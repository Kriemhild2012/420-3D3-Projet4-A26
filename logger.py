import sqlite3, datetime
import threading

class Logger:
    _instance = None
    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance._initialiser()
        return cls._instance

    def _initialiser(self):
        self._verrrou = threading.Lock()
        self.connexion = sqlite3.connect("logs.db")
        self.connexion.execute(
            "CREATE TABLE IF NOT EXISTS logs (ts TEXT, message TEXT)"
        )
        self.connexion.commit()

    def log(self, message: str) -> None:
        with self._verrrou:
            ts = datetime.datetime.now().isoformat()
            self.connexion.execute("INSERT INTO logs VALUES (?, ?)", (ts, message))
            self.connexion.commit()
            print(f"[{ts}] {message}")

    def tous_les_logs(self) -> list[tuple]:
        return self.connexion.execute("SELECT * FROM logs").fetchall()

l1 = Logger()
l1.log("démarrage")

l2 = Logger()
l2.log("conversion terminée")

print(l1 is l2)              # True
print(len(l1.tous_les_logs()))  # 2 — les deux logs dans la même BD