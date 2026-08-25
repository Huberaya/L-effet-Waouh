"""
Agent Base - L'Effet Waouh V3 - 9 agents IA
"""
from abc import ABC, abstractmethod
import sqlite3
from pathlib import Path
from datetime import datetime

class BaseAgent(ABC):
    def __init__(self, db_path="/tmp/waouh_v3_test2.db"):
        self.db_path = db_path
        self.name = self.__class__.__name__
        self.last_run = None
        self.logs = []

    def log(self, msg):
        entry = f"[{datetime.now().isoformat()}] {self.name}: {msg}"
        self.logs.append(entry)
        print(entry)

    def get_conn(self):
        # try multiple paths
        for p in [self.db_path, "/tmp/waouh_v2.db", "/tmp/waouh_v3_test.db"]:
            try:
                conn = sqlite3.connect(p)
                conn.row_factory = sqlite3.Row
                # test
                conn.execute("SELECT 1")
                return conn
            except:
                continue
        # fallback memory
        return sqlite3.connect(":memory:")

    @abstractmethod
    def analyze(self):
        pass

    @abstractmethod
    def recommend(self):
        pass

    def run_daily(self):
        self.log("Début run_daily")
        try:
            analysis = self.analyze()
            recos = self.recommend()
            self.last_run = datetime.now()
            self.log(f"Analyse: {analysis}")
            self.log(f"Recos: {recos}")
            return {"analysis": analysis, "recommendations": recos, "logs": self.logs}
        except Exception as e:
            self.log(f"ERREUR: {e}")
            return {"error": str(e), "logs": self.logs}
