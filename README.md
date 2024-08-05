## Code Explanation

### **1. Backup Script (`backup_script.py`)**

This script automates the process of backing up a directory.

```python
import os
import shutil
from datetime import datetime
```
- `os`: This module provides a way of interacting with the operating system, like creating directories.
- `shutil`: Used to perform high-level file operations, such as copying files and directories.
- `datetime`: Used to work with dates and times, in this case, to timestamp the backup.

```python
backup_source_dir = "/path/to/backup/source"  # Directory to back up
backup_destination_dir = "/path/to/backup/destination"  # Backup storage location
```
- `backup_source_dir`: This variable holds the path to the directory you want to back up.
- `backup_destination_dir`: This is where the backup will be stored.

```python
def backup_directory(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    backup_name = datetime.now().strftime("%Y%m%d%H%M%S") + "_backup"
    backup_path = os.path.join(destination, backup_name)
    
    try:
        shutil.copytree(source, backup_path)
        print(f"Backup completed: {backup_path}")
    except Exception as e:
        print(f"Backup failed: {e}")
```
- `backup_directory(source, destination)`: A function that handles the backup process.
  - `os.path.exists(destination)`: Checks if the destination directory exists.
  - `os.makedirs(destination)`: Creates the destination directory if it doesn't exist.
  - `datetime.now().strftime("%Y%m%d%H%M%S")`: Generates a timestamp to uniquely name each backup.
  - `shutil.copytree(source, backup_path)`: Copies the entire directory tree from the source to the destination.
  - If the backup succeeds, it prints a success message; otherwise, it prints an error.

```python
if __name__ == "__main__":
    backup_directory(backup_source_dir, backup_destination_dir)
```
- This block ensures that the script runs the `backup_directory` function when executed directly.

### **2. System Update Script (`update_script.py`)**

This script automates the process of updating the system with security patches.

```python
import subprocess
```
- `subprocess`: This module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

```python
def update_system():
    try:
        print("Updating the system...")
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "upgrade", "-y"], check=True)
        print("System update completed.")
    except subprocess.CalledProcessError as e:
        print(f"System update failed: {e}")
```
- `update_system()`: A function that updates the system.
  - `subprocess.run(["sudo", "apt-get", "update"], check=True)`: Runs the command to update the package lists.
  - `subprocess.run(["sudo", "apt-get", "upgrade", "-y"], check=True)`: Runs the command to install available updates.
  - `check=True`: Raises an exception if the command fails.
  - If the update succeeds, it prints a success message; otherwise, it prints an error.

```python
if __name__ == "__main__":
    update_system()
```
- This block ensures that the script runs the `update_system` function when executed directly.

### **3. Log Rotation Script (`log_rotation_script.py`)**

This script manages log files by deleting old logs to prevent them from consuming too much disk space.

```python
import os
from datetime import datetime
```
- `os`: Used to interact with the file system.
- `datetime`: Used to work with dates and times, particularly to check the age of log files.

```python
log_dir = "/var/log/myapp"  # Directory containing log files
log_retention_days = 30  # Number of days to retain logs
log_file_extension = ".log"  # Log file extension
```
- `log_dir`: Specifies the directory where log files are stored.
- `log_retention_days`: Specifies how many days old a log file can be before it gets deleted.
- `log_file_extension`: Specifies the file extension of log files to be managed.

```python
def rotate_logs(log_directory, retention_days, file_extension):
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
```
- `rotate_logs(log_directory, retention_days, file_extension)`: A function that handles log rotation.
  - `os.listdir(log_directory)`: Lists all files in the log directory.
  - `os.path.getmtime(file_path)`: Gets the last modified time of a file.
  - `datetime.fromtimestamp(os.path.getmtime(file_path))`: Converts the last modified time to a `datetime` object.
  - If the file's age exceeds the retention period, it deletes the file and prints a success message; otherwise, it prints an error.

```python
if __name__ == "__main__":
    rotate_logs(log_dir, log_retention_days, log_file_extension)
```
- This block ensures that the script runs the `rotate_logs` function when executed directly.

These scripts are meant to be run on a schedule (e.g., via cron jobs) or manually when needed to maintain your system and manage resources efficiently.
