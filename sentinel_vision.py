import time
import json
import hashlib

class SovereignLogger:
    def __init__(self, officer_id):
        self.officer_id = officer_id
        # We hash the officer ID so it's pseudonymous in the raw text file
        self.officer_hash = hashlib.sha256(officer_id.encode()).hexdigest()

    def log_scan(self, result, location_code):
        """
        Logs the ACTION, not the PERSON.
        """
        entry = {
            "timestamp": time.time(),
            "officer_signature": self.officer_hash,
            "location": location_code,
            "scan_result": result, # "MATCH" or "NO_MATCH"
            "software_version": "v1.0.1-SOVEREIGN"
        }
        
        # Append to the JSON log (simulating a WORM drive write)
        with open("daily_audit.json", "a") as f:
            f.write(json.dumps(entry) + "\n")
            
        print(f"[AUDIT] Scan logged. Result: {result}")
