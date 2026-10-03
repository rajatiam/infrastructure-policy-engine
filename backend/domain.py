import csv, hashlib, io, json, math, re
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from .validation import validate_input, http_url, unique

def now(): return datetime.now(timezone.utc).isoformat()
def validate(data,records): return initialize(validate_input(data,CONFIG['example']),records)

def initialize(row,records): return row
def violations(row): return [label for key,label in [('public','Public access'),('encrypted','Encryption disabled'),('backup','Backups disabled')] if (row[key] if key=='public' else not row[key])]
def summary(rows):
    findings=[{'id':row['id'],'name':row['name'],'violations':violations(row)} for row in rows]
    return {'checked':len(rows),'failing':sum(bool(finding['violations']) for finding in findings),'findings':findings}
def transition(row,action): raise ValueError('Policy assessments are immutable')
