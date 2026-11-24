# file_attente.py  ← À COMPLÉTER
 
import threading
from job import Job
from worker import Worker
 
class FileAttente:
    _instance = None
    _verrou_classe = threading.Lock()
 
    def __new__(cls):
        # TODO : implémenter le Singleton
        if cls._instance is None:
            new = super().__new__(cls)
            new._initialiser()
            cls._instance = new
        return cls._instance
 
    def _initialiser(self):
        # TODO : initialiser la liste de jobs
        self._jobs = []
 
    def soumettre(self, job: Job) -> None:
        # TODO : ajouter le job à la file
        with FileAttente._verrou_classe:
            self._jobs.append(job)
 
    def traiter_prochain(self, worker: Worker) -> str | None:
        # TODO : retirer le premier job et le faire traiter par le worker
        # Retourner None si la file est vide
        with FileAttente._verrou_classe:
            if self._jobs is None:
                return None
            else:
                job = self._jobs[0]
                worker.traiter(job)
                self._jobs.pop(0)
 
    def nb_en_attente(self) -> int:
        # TODO : retourner le nombre de jobs dans la file
        return len(self._jobs)