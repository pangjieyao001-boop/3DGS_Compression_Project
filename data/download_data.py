#!/usr/bin/env python3
"""
Download script for NeRF Synthetic dataset.
Downloads and extracts the Lego scene data automatically.
"""

import os
import urllib.request
import zipfile
import sys
from pathlib import Path

# Dataset configuration
DATASET_URL = "http://cseweb.ucsd.edu/~viscomp/projects/LFVR/papers/NSCV19/nerf_example_data.zip"
DATASET_ZIP = "nerf_example_data.zip"
EXTRACT_DIR = "."
TARGET_SCENE = "lego"

def print_header(text):
    """Print formatted header."""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def print_step(step_num, text):
    """Print step indicator."""
    print(f"\n[Step {step_num}] {text}")

def download_file(url, output_path):
    """Download file with progress bar."""
    def progress_hook(count, block_size, total_size):
        percent = int(count * block_size * 100 / total_size)
        percent = min(100, percent)
        sys.stdout.write(f"\r  Downloading... {percent}%")
        sys.stdout.flush()
    
    print(f"  From: {url}")
    print(f"  To: {output_path}")
    print("  Starting download...")
    
    try:
        urllib.request.urlretrieve(url, output_path, progress_hook)
        print("\n  ✓ Download complete!")
        return True
    except Exception as e:
        print(f"\n  ✗ Download failed: {e}")
        return False

def extract_zip(zip_path, extract_to):
    """Extract zip file."""
    print(f"  Extracting: {zip_path}")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print("  ✓ Extraction complete!")
        return True
    except Exception as e:
        print(f"  ✗ Extraction failed: {e}")
        return False

def organize_files():
    """Organize extracted files into expected structure."""
    print_step(3, "Organizing files")
    
    # Check if extracted data exists
    extracted_path = Path("nerf_example_data/lego")
    target_path = Path("nerf_synthetic/lego")
    
    if not extracted_path.exists():
        print(f"  ! Expected path not found: {extracted_path}")
        print("  ! Please check the extracted contents manually")
        return False
    
    # Create target directory
    target_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Move files
    print(f"  Moving: {extracted_path} -> {target_path}")
    extracted_path.rename(target_path)
    
    # Clean up
    print("  Cleaning up temporary files...")
    if Path("nerf_example_data").exists():
        import shutil
        shutil.rmtree("nerf_example_data")
    
    print("  ✓ Organization complete!")
    return True

def verify_dataset():
    """Verify dataset structure."""
    print_step(4, "Verifying dataset")
    
    base_path = Path("nerf_synthetic/lego")
    required_files = [
        base_path / "transforms_train.json",
        base_path / "transforms_test.json",
        base_path / "train",
        base_path / "test"
    ]
    
    all_exist = True
    for file_path in required_files:
        exists = file_path.exists()
        status = "✓" if exists else "✗"
        print(f"  {status} {file_path}")
        if not exists:
            all_exist = False
    
    if all_exist:
        # Count images
        train_images = len(list((base_path / "train").glob("*.png")))
        test_images = len(list((base_path / "test").glob("*.png")))
        print(f"\n  Dataset verified!")
        print(f"    - Train images: {train_images}")
        print(f"    - Test images: {test_images}")
        return True
    else:
        print("\n  ✗ Dataset verification failed!")
        return False

def main():
    """Main download workflow."""
    print_header("NeRF Synthetic Dataset Downloader")
    
    # Check if already exists
    if Path("nerf_synthetic/lego").exists():
        print("\n  ℹ Dataset already exists at: nerf_synthetic/lego/")
        response = input("  Do you want to re-download? [y/N]: ").lower()
        if response != 'y':
            print("  Skipping download.")
            verify_dataset()
            return
        import shutil
        shutil.rmtree("nerf_synthetic/lego")
    
    # Step 1: Download
    print_step(1, "Downloading dataset")
    print(f"  URL: {DATASET_URL}")
    print(f"  Size: ~350 MB")
    print()
    
    if not download_file(DATASET_URL, DATASET_ZIP):
        print("\n  ✗ Download failed!")
        print("  Alternative: Download manually from:")
        print("  https://drive.google.com/drive/folders/1JDdLGDruGNXWnM1eqY1FNL9PlStjaKWi")
        return
    
    # Step 2: Extract
    print_step(2, "Extracting archive")
    if not extract_zip(DATASET_ZIP, EXTRACT_DIR):
        print("\n  ✗ Extraction failed!")
        return
    
    # Step 3: Organize
    if not organize_files():
        print("\n  ✗ Organization failed!")
        return
    
    # Step 4: Clean up zip
    if Path(DATASET_ZIP).exists():
        print("\n  Removing zip file...")
        Path(DATASET_ZIP).unlink()
    
    # Step 5: Verify
    if verify_dataset():
        print_header("Dataset ready!")
        print("\n  You can now run:")
        print("    python src/train_3dgs.py")
        print("\n  Or evaluate with existing model:")
        print("    python src/run_high_score_experiments.py")
    else:
        print_header("Setup incomplete")
        print("\n  Please check the error messages above.")

if __name__ == "__main__":
    main()
