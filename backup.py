import os
import shutil
from datetime import datetime

# Configuration
backup_source_dir = "/path/to/backup/source"  # Directory to back up
backup_destination_dir = "/path/to/backup/destination"  # Backup storage location

def backup_directory(source, destination):
    """
    Backs up the specified directory to the destination.
    """
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    backup_name = datetime.now().strftime("%Y%m%d%H%M%S") + "_backup"
    backup_path = os.path.join(destination, backup_name)
    
    try:
        shutil.copytree(source, backup_path)
        print(f"Backup completed: {backup_path}")
    except Exception as e:
        print(f"Backup failed: {e}")

if __name__ == "__main__":
    backup_directory(backup_source_dir, backup_destination_dir)
