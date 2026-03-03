#!/bin/bash
# Download script for NeRF Synthetic dataset (Lego scene)

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Dataset configuration
DATASET_URL="http://cseweb.ucsd.edu/~viscomp/projects/LFVR/papers/NSCV19/nerf_example_data.zip"
DATASET_ZIP="nerf_example_data.zip"
TARGET_DIR="nerf_synthetic/lego"

echo "================================================================"
echo "  NeRF Synthetic Dataset Downloader"
echo "================================================================"
echo ""

# Check if already exists
if [ -d "$TARGET_DIR" ]; then
    echo -e "${YELLOW}Dataset already exists at: $TARGET_DIR${NC}"
    read -p "Do you want to re-download? [y/N]: " response
    if [[ ! "$response" =~ ^[Yy]$ ]]; then
        echo "Skipping download."
        exit 0
    fi
    rm -rf "$TARGET_DIR"
fi

# Download
echo "[Step 1/4] Downloading dataset..."
echo "  URL: $DATASET_URL"
echo "  Size: ~350 MB"
echo ""

if command -v wget &> /dev/null; then
    wget --progress=bar:force "$DATASET_URL" -O "$DATASET_ZIP" 2>&1 | tail -f -n +6 || {
        echo -e "${RED}Download failed!${NC}"
        exit 1
    }
elif command -v curl &> /dev/null; then
    curl -L "$DATASET_URL" -o "$DATASET_ZIP" --progress-bar || {
        echo -e "${RED}Download failed!${NC}"
        exit 1
    }
else
    echo -e "${RED}Error: Neither wget nor curl is installed.${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Download complete!${NC}"
echo ""

# Extract
echo "[Step 2/4] Extracting archive..."
if command -v unzip &> /dev/null; then
    unzip -q "$DATASET_ZIP" || {
        echo -e "${RED}Extraction failed!${NC}"
        exit 1
    }
else
    echo -e "${RED}Error: unzip is not installed.${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Extraction complete!${NC}"
echo ""

# Organize
echo "[Step 3/4] Organizing files..."
mkdir -p nerf_synthetic

if [ -d "nerf_example_data/lego" ]; then
    mv nerf_example_data/lego nerf_synthetic/
    rm -rf nerf_example_data
    echo -e "${GREEN}✓ Organization complete!${NC}"
else
    echo -e "${RED}Error: Expected directory not found!${NC}"
    exit 1
fi
echo ""

# Clean up
echo "[Step 4/4] Cleaning up..."
rm -f "$DATASET_ZIP"
echo -e "${GREEN}✓ Cleanup complete!${NC}"
echo ""

# Verify
echo "Verifying dataset structure..."
if [ -f "$TARGET_DIR/transforms_train.json" ] && \
   [ -f "$TARGET_DIR/transforms_test.json" ] && \
   [ -d "$TARGET_DIR/train" ] && \
   [ -d "$TARGET_DIR/test" ]; then
    
    TRAIN_COUNT=$(ls -1 "$TARGET_DIR/train"/*.png 2>/dev/null | wc -l)
    TEST_COUNT=$(ls -1 "$TARGET_DIR/test"/*.png 2>/dev/null | wc -l)
    
    echo -e "${GREEN}✓ Dataset verified!${NC}"
    echo "    - Train images: $TRAIN_COUNT"
    echo "    - Test images: $TEST_COUNT"
    echo ""
    echo "================================================================"
    echo -e "${GREEN}  Dataset ready!${NC}"
    echo "================================================================"
    echo ""
    echo "You can now run:"
    echo "  python src/train_3dgs.py"
    echo ""
else
    echo -e "${RED}✗ Dataset verification failed!${NC}"
    exit 1
fi
