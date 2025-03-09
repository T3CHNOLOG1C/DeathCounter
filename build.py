import os
import sys
import shutil
import subprocess
import argparse
import zipfile

def build_executable():
    command = [
        'pyinstaller',
        '--onefile',
        '--icon=deathcounter.ico',         
        '--version-file', 'version.txt',  
        'deathcounter.py'
    ]
    print("Building executable with PyInstaller...")
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print("---Build failed!---")
        sys.exit(1)
    print("---Build complete!---")

def copy_executable():
    exe_name = "deathcounter.exe" if sys.platform == "win32" else "deathcounter"
    dist_dir = os.path.join(os.getcwd(), "dist")
    source_exe_path = os.path.join(dist_dir, exe_name)
    destination_exe_path = os.path.join(os.getcwd(), exe_name)
    
    if os.path.exists(source_exe_path):
        shutil.copy(source_exe_path, destination_exe_path)
        print(f"Copied executable to: {destination_exe_path}")
    else:
        print(f"Executable not found at: {source_exe_path}")

def create_distribution_zip():
    exe_name = "deathcounter.exe" if sys.platform == "win32" else "deathcounter"
    base_exe = os.path.splitext(exe_name)[0]
    zip_name = f"{base_exe}_{sys.platform}.zip"
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(exe_name, arcname=exe_name)
    print(f"Created distribution zip: {zip_name}")

def cleanup_build_environment():
    print("---Cleaning build environment---")
    folders_to_remove = ['build', 'dist']
    for folder in folders_to_remove:
        if os.path.exists(folder) and os.path.isdir(folder):
            shutil.rmtree(folder)
            print(f"Deleted folder: {folder}")
        else:
            print(f"Folder not found or not a directory: {folder}")
    spec_file = "deathcounter.spec"
    if os.path.exists(spec_file) and os.path.isfile(spec_file):
        os.remove(spec_file)
        print(f"Deleted spec file: {spec_file}")
    else:
        print(f"Spec file not found: {spec_file}")

def main():
    parser = argparse.ArgumentParser(description="Build DeathCounter executable.")
    parser.add_argument('--clean', action='store_true', help="Clean build environment.")
    parser.add_argument('--dist', action='store_true', help="Create zip distribution of the executable.")
    args = parser.parse_args()

    # If only --clean is provided, clean and exit.
    if args.clean and not args.dist:
        cleanup_build_environment()
        print("---Build environment cleaned.---")
        return 0

    build_executable()
    copy_executable()

    if args.dist:
        create_distribution_zip()

    if args.clean:
        cleanup_build_environment()

if __name__ == '__main__':
    main()
