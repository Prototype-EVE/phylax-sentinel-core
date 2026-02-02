import time
import numpy as np
import sys

# Import Phylax Core Modules
from security import SovereignSecurity
from audit_log import SovereignLogger

def run_phylax_simulation():
    print("\n==================================================")
    print("   PHYLAX CYBERNETICS | PROJECT SENTINEL v2.0")
    print("   Sovereign Identity Protocol | Status: ACTIVE")
    print("==================================================\n")
    
    # 1. Boot Sequence
    print("[SYSTEM] Initializing Secure Boot...")
    time.sleep(1)
    
    # Initialize Security Shield
    shield = SovereignSecurity()
    if not shield.verify_tpm_integrity():
        sys.exit("[CRITICAL] TAMPER DETECTED. SYSTEM HALT.")
        
    # Initialize Logger (Officer Login)
    # In reality, this comes from the officer's smart card
    logger = SovereignLogger("OFFICER-ID-9924")
    print("[SYSTEM] Officer Authenticated. Logging Active.\n")
    
    # 2. Watchlist Ingest (Simulation)
    print("[NET] Mode: AIR-GAPPED (Offline)")
    print("[DB] Loading Daily Watchlist Hash-Set...")
    
    # Create a fake "Target" (Terrorist) vector
    fake_target_vector = np.random.rand(128).astype(np.float32)
    # Hash it with today's salt (This is what the station does)
    watchlist_hash = shield.generate_salted_hash(fake_target_vector)
    print(f"[DB] Watchlist Loaded. Target Hash: {watchlist_hash[:12]}...\n")

    # 3. Field Scan Simulation
    print(">>> READY FOR SCAN. PRESS CAMERA BUTTON.")
    time.sleep(1)
    print("[CAM] Capturing Subject Biometrics...")
    
    # Simulate scanning an Innocent Person (Random Vector)
    subject_vector = np.random.rand(128).astype(np.float32)
    subject_hash = shield.generate_salted_hash(subject_vector)
    
    print(f"[PROCESS] Subject Hash Generated: {subject_hash[:12]}...")
    
    # 4. The Comparison
    if subject_hash == watchlist_hash:
        print("\n[ALERT] *** MATCH CONFIRMED ***")
        print("[ALERT] INITIATE DETAINMENT PROTOCOL")
        logger.log_scan("MATCH_CONFIRMED", "GRID-51N-01W")
    else:
        print("\n[RESULT] NO MATCH. Subject Cleared.")
        logger.log_scan("NO_MATCH", "GRID-51N-01W")
        
    # 5. The Secure Wipe
    print("\n[PRIVACY] Initiating Volatile Memory Wipe...")
    shield.secure_wipe(subject_vector)
    print("[SYSTEM] Cycle Complete. Ready for next scan.")

if __name__ == "__main__":
    run_phylax_simulation()
