import subprocess

def update_system():
    """
    Updates the system by installing security patches.
    """
    try:
        print("Updating the system...")
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "upgrade", "-y"], check=True)
        print("System update completed.")
    except subprocess.CalledProcessError as e:
        print(f"System update failed: {e}")

if __name__ == "__main__":
    update_system()
