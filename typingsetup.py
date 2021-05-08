import sys

from cx_Freeze import *
import pygame
from pygame import mixer

includefiles = ['typingicon.ico', 'A.ico', 'bg.jpg', 'bg.mp3', 'keyboard.jpg', 'last.jpg', 'mute.png', 'play.png']
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "Typing Speed",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]\TypingSpeed.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR",  # WkDir
     )
]
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}
setup(
    version="1.0",
    description="Typing Speed Increaser Game",
    author="ForCodeCoder",
    name="Typing Speed",
    options={'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables=[
        Executable(
            script="TypingSpeed.py",
            base=base,
            icon='A.ico',
        )
    ]
)
