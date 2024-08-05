import os
from datetime import datetime

# Configuration
log_dir = "/var/log/myapp"  # Directory containing log files
log_retention_days = 30  # Number of days to retain logs
log_file_extension = ".log"  # Log file extension

def rotate_logs(log_directory, retention_days, file_extension):
    """
    Rotates logs by deleting logs older than the specified retention period.
    """
    now = datetime.now()
    
    for filename in os.listdir(log_directory):
        if filename.endswith(file_extension):
            file_path = os.path.join(log_directory, filename)
            file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            age_in_days = (now - file_modified_time).days
            
            if age_in_days > retention_days:
                try:
                    os.remove(file_path)
                    print(f"Deleted log: {file_path}")
                except Exception as e:
                    print(f"Failed to delete log {file_path}: {e}")

if __name__ == "__main__":
    rotate_logs(log_dir, log_retention_days, log_file_extension)
