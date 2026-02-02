from sentinel_vision import SentinelVision
import time
import numpy as np

# Import the Sovereign Modules
from security import SovereignSecurity
from audit_log import SovereignLogger
from sentinel_vision import SentinelVision  # <-- Now imports the Vision module

def run_sentinel_simulation():
    print("--- INITIALIZING PHYLAX SENTINEL PROTOCOL ---")
    
    # 1. Initialize Modules
    sec_shield = SovereignSecurity()
    logger = SovereignLogger("Officer-442")
    vision = SentinelVision()  # <-- Initialize the Camera

    # 2. Watchlist Download (Simulated Air-Gapped Sync)
    print("\n[SYSTEM] Downloading Daily Watchlist...")
    # We create a fake "Target" to look for
    fake_terrorist_face = np.random.rand(128).astype(np.float32)
    watchlist_hash = sec_shield.generate_salted_hash(fake_terrorist_face)
    print(f"[SYSTEM] Watchlist Loaded. Target Hash: {watchlist_hash[:8]}...")

    # 3. Start The Camera
    if vision.start_camera():
        print("\n[FIELD] Camera Active. Scanning for subjects...")
        
        # Capture a single frame for the demo
        frame = vision.capture_frame()
        
        if frame is not None:
            # 4. Vectorize the Face
            vector, status = vision.get_biometric_vector(frame)
            
            if status == "NO_FACE_DETECTED":
                print(">> ERROR: No subject in frame.")
            else:
                print(f"[VISION] Biometric Vector Acquired. Liveness Check: {vision.liveness_check(frame)}")
                
                # 5. Salt & Hash (The Sovereign Security Step)
                scan_hash = sec_shield.generate_salted_hash(vector)
                
                # 6. Compare against Watchlist
                if scan_hash == watchlist_hash:
                    print(">> ALERT: MATCH FOUND!")
                    logger.log_scan("MATCH", "GPS-51.5N-0.1W")
                else:
                    print(">> CLEAR: No Match.")
                    logger.log_scan("NO_MATCH", "GPS-51.5N-0.1W")
                
                # 7. Secure Wipe (The Privacy Step)
                sec_shield.secure_wipe(vector)
        
        vision.stop_camera()
    else:
        print("[ERROR] Camera hardware not found. Aborting.")

    print("\n--- SESSION COMPLETE ---")

if __name__ == "__main__":
    run_sentinel_simulation()
# Initialize Eyes
    eyes = SentinelVision()

    # ... inside the scan loop ...
    print("\n[FIELD] Acquiring Biometric Target...")
    # capture a real frame (or simulated if no camera)
    frame = eyes.capture_secure_frame()
    # turn it into a vector
    subject_vector = eyes.vectorize_face(frame)
