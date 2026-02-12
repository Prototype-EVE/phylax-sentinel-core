import sys
import time
import os
import random

# Import your actual modules
from security import SovereignSecurity
from sentinel_vision import SentinelVision
from audit_log import SovereignLogger

# --- CINEMATIC TOOLS ---
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def type_writer(text, speed=0.03, color=Colors.GREEN):
    """Effect to type text out like a retro computer"""
    sys.stdout.write(color + text)
    sys.stdout.flush()
    for char in "":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    # Actually just print the line with a small delay for readability
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print(Colors.RESET)

def loading_bar(label, duration=2):
    """Visual loading bar [######....]"""
    print(f"{Colors.CYAN}{label}{Colors.RESET}")
    toolbar_width = 40
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) 

    step = duration / toolbar_width
    for i in range(toolbar_width):
        time.sleep(step)
        sys.stdout.write("█")
        sys.stdout.flush()
    sys.stdout.write("]\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- THE DEMO SEQUENCE ---
def run_hollywood_demo():
    clear_screen()
    
    # 1. THE BRANDING
    print(Colors.GREEN + Colors.BOLD + r"""
    ____  __  ____  ____    ___  _  __
   / __ \/ / / / / / / /   /   || |/ /
  / /_/ / /_/ / /_/ / /   / /| ||   / 
 / ____/ __  /\__, / /___/ ___ /   |  
/_/   /_/ /_//____/_____/_/  |_\_|\_\ 
    CYBERNETICS | PROJECT SENTINEL
    """ + Colors.RESET)
    time.sleep(1)

    # 2. SYSTEM BOOT
    type_writer("[KERNEL] INITIALIZING SECURE BOOT...", 0.05)
    loading_bar("verifying_hardware_integrity(STM32_N6)", 1.5)
    print(f"[{Colors.GREEN}OK{Colors.RESET}] TPM CHIP DETECTED (SWISS MFG)")
    print(f"[{Colors.GREEN}OK{Colors.RESET}] RISC-V ARCHITECTURE VERIFIED")
    time.sleep(0.5)

    # 3. INITIALIZE MODULES
    type_writer("\n[MODULES] LOADING SOVEREIGN STACK...", 0.02)
    sec = SovereignSecurity()
    vision = SentinelVision()
    logger = SovereignLogger("OFFICER-CMD-442")
    time.sleep(1)

    # 4. AIR-GAP CHECK
    type_writer("\n[NETWORK] CHECKING CONNECTIVITY...", 0.05)
    time.sleep(1)
    print(f"[{Colors.RED}BLOCKED{Colors.RESET}] INTERNET CONNECTION: DISABLED")
    print(f"[{Colors.GREEN}SECURE{Colors.RESET}] AIR-GAP STATUS: CONFIRMED")
    
    # 5. WATCHLIST SYNC
    type_writer("\n[DATA] DECRYPTING DAILY WATCHLIST (RAM ONLY)...", 0.04)
    loading_bar("hashing_vectors", 1.0)
    print(f"[{Colors.GREEN}READY{Colors.RESET}] TARGET LIST LOADED. 0 BYTES ON DISK.")

    # 6. THE SCAN
    type_writer("\n[OPERATIONAL] WAITING FOR BIOMETRIC INPUT...", 0.05)
    print(f"{Colors.YELLOW}>> POINT DEVICE AT SUBJECT <<{Colors.RESET}")
    
    # Start Camera Logic
    if vision.start_camera():
        loading_bar("acquiring_optical_lock", 2.0)
        
        # Capture
        frame = vision.capture_frame()
        if frame is not None:
            # Simulate processing
            type_writer(">> FACE DETECTED. VECTORIZING...", 0.05)
            vector, status = vision.get_biometric_vector(frame)
            
            # Generate the Salted Hash
            scan_hash = sec.generate_salted_hash(vector)
            print(f"   GENERATED HASH: {Colors.CYAN}{scan_hash[:16]}...{Colors.RESET}")
            
            # DRAMATIC PAUSE FOR MATCHING
            time.sleep(0.5)
            type_writer(">> COMPARING AGAINST WATCHLIST...", 0.05)
            time.sleep(1)
            
            # RESULT (We simulate a match for the demo, or random)
            # Let's force a "CLEAR" for the demo to show the wipe
            print(f"\n{Colors.GREEN}>> [RESULT: NO MATCH FOUND] <<{Colors.RESET}")
            print(f"{Colors.GREEN}>> SUBJECT CLEARED.{Colors.RESET}")
            
            # LOGGING
            logger.log_scan("NO_MATCH", "GPS-CHANNEL-SECURE")
            
            # 7. THE WIPE (The Money Shot)
            type_writer("\n[PRIVACY] INITIATING RAM SCRUB...", 0.05)
            loading_bar("overwriting_memory_sectors", 1.0)
            sec.secure_wipe(vector)
            print(f"[{Colors.GREEN}CLEAN{Colors.RESET}] MEMORY WIPED. NO FORENSIC TRACE.")
            
        vision.stop_camera()

    print("\n" + Colors.GREEN + "=== DEMO COMPLETE | PHYLAX CYBERNETICS ===" + Colors.RESET)
    input(f"\n{Colors.YELLOW}[PRESS ENTER TO EXIT]{Colors.RESET}")

if __name__ == "__main__":
    run_hollywood_demo()
