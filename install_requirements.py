#!/usr/bin/env python3
"""
Requirements installer for the missionary word cloud project
"""

import subprocess
import sys

def install_requirements():
    """Install required Python packages"""
    
    packages = [
        'matplotlib',
        'wordcloud',
        'numpy',
        'collections-extended'  # For enhanced Counter functionality
    ]
    
    print("Installing required packages...")
    print("=" * 40)
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"✅ {package} installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {package}: {e}")
            return False
    
    print("\n🎉 All packages installed successfully!")
    print("\nYou can now run:")
    print("  python word_cloud_analysis.py")
    print("  python japanese_teaching_tool.py")
    
    return True

if __name__ == "__main__":
    install_requirements()
