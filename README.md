![Unreal Engine](https://img.shields.io/badge/unrealengine-%23313131.svg?style=for-the-badge&logo=unrealengine&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
# Unreal Engine Delete Empty Folders Script
## ue-empty-folder-deleter

This script allows you to delete empty folders within a specified directory and its subfolders in Unreal Engine. It uses Unreal Engine's EditorAssetLibrary to list all assets and folders within the specified directory and its subfolders, and then deletes any empty folders it finds.

# Requirements 
* Unreal Engine 4.26 or later installed
* Python 3.7 or later installed
* unreal Python module installed

# Installation
1. Clone this repository or download the ZIP archive and extract its contents.
2. Copy and paste it into your Unreal Engine project script file.

# Usage
To use this script:

1. Modify the ```source_dir variable``` (in the script) to specify the directory path where you want to delete empty folders. For example, if you want to delete empty folders within the /Game/Test directory, set source_dir to "/Game/Test".
2. Open Unreal Engine.
3. In the main menu, Select **File > Execute Python Script** and look for the Python Script location. 

# Notes
* This script will delete any empty folders it finds within the specified directory and its subfolders. Be sure to double-check the specified directory before running the script and be sure to save the project before executing the script.
* This script uses the does_directory_have_assets method to determine if a folder contains any assets. If a folder contains any assets, it will not be deleted even if it does not contain any subfolders.
