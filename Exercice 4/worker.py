# workers.py  ← À COMPLÉTER
 
from abc import ABC, abstractmethod
from job import Job
 
class Worker(ABC):
    @abstractmethod
    def traiter(self, job: Job) -> str:
        pass
 
class WorkerConsole(Worker):
    def traiter(self, job: Job) -> str:
        # TODO : afficher et retourner le message
        # Format : "[WorkerConsole] Traitement du job #<id> : <format_entree> → <format_sortie>"
        mesg = f"[WorkerConsole] Traitement du job {job.id} : {job.format_entree} → {job.format_sortie}"
        print(mesg)
        return mesg