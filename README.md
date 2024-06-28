# TaskbarHider

TaskbarHider is a Python utility for hiding system icons on the taskbar in Windows environments.

## Installation

### Requirements
- Python 3.x
- pip (Python package installer)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tuonome/taskbar-hider.git
   cd taskbar-hider
Install dependencies:
bash
Copy code
```pip install i```
Creating an executable (.exe)
You can convert the Python script into a standalone executable file (.exe) for easier distribution. We recommend using tools like PyInstaller for this purpose.

### Install PyInstaller:

bash
```Copy code pip install pyinstaller Generate the .exe:```

bash
### Copy code
```pyinstaller --onefile taskbar_hider.py```
This will create a dist folder containing the executable file taskbar_hider.exe.

### Download precompiled executable
Alternatively, you can download the precompiled executable from the releases page. Choose the appropriate version for your system (e.g., Windows 64-bit).

### Usage
To run the script or executable, simply execute taskbar_hider.py or taskbar_hider.exe. Follow the on-screen instructions to hide or show taskbar icons as needed.
