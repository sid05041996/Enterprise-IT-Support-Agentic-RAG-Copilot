##in order to Add the audit logging so you can track questions, sources, being used, and the agent’s execution paths.
import json
import sqlite3
from datetime import datetime, timezone
from app.core.config import get_settings

settings = get_settings()

def init_db() -> None:
    con=sqlite3.connect(settings.audit_db_path)
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS query_audit01 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TEXT NOT NULL,
        question TEXT NOT NULL,
        source_used TEXT NOT NULL,
        trace_json TEXT NOT NULL)
"""
    )
    con.commit()
    con.close()

## main function which helps us save any of the traces..!!..,,;;
#@@## 
def write_audit(question:str, source_used:str, trace: list[str]) -> None:
    con = sqlite3.connect(settings.audit_db_path)
    # 1. Create the table if it doesn't exist (no data parameters needed)
    # """CREATE TABLE IF NOT EXISTS query_audit01 (
    # """ALTER TABLE query_audit01 (
    con.execute(
        """CREATE TABLE IF NOT EXISTS query_audit01 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            question TEXT NOT NULL,
            source_used TEXT NOT NULL,
            trace_json TEXT NOT NULL
        )"""
    ) 
    
    # 2. Insert the new log entry (pass the tuple of parameters here)
    con.execute(
        "INSERT INTO query_audit01(created_at, question, source_used, trace_json) VALUES (?, ?, ?, ?)",
        (datetime.now(timezone.utc).isoformat(), question, source_used, json.dumps(trace))
    )    
    con.commit()
    con.close()

