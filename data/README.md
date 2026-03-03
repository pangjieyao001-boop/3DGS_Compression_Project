# Dataset Directory

This directory is for storing the NeRF Synthetic dataset. Due to file size constraints, the actual data files are not included in this repository.

## 📥 Download Instructions

### NeRF Synthetic Dataset (Lego Scene)

**Official Source:**
```bash
# Download from the official NeRF repository
wget http://cseweb.ucsd.edu/~viscomp/projects/LFVR/papers/NSCV19/nerf_example_data.zip
```

**Alternative (Google Drive mirror):**
- URL: https://drive.google.com/drive/folders/1JDdLGDruGNXWnM1eqY1FNL9PlStjaKWi
- Download `nerf_synthetic.zip` and extract

**Expected Directory Structure:**
```
data/
└── nerf_synthetic/
    └── lego/
        ├── transforms_train.json    # Training camera parameters
        ├── transforms_test.json     # Test camera parameters
        ├── train/                   # 100 training images (800x800)
        │   ├── r_0.png
        │   ├── r_1.png
        │   └── ...
        └── test/                    # 200 test images (800x800)
            ├── r_0.png
            ├── r_1.png
            └── ...
```

## 🚀 Quick Setup

### Option 1: Manual Download
1. Download the dataset using links above
2. Extract to `data/nerf_synthetic/lego/`
3. Verify structure matches expected layout

### Option 2: Automated Download (Linux/Mac)
```bash
cd data
bash download_data.sh
```

### Option 3: Python Script
```bash
cd data
python download_data.py
```

## 📊 Dataset Statistics

| Property | Value |
|----------|-------|
| Training Images | 100 |
| Test Images | 200 |
| Resolution | 800 × 800 |
| Camera Views | 360° around object |
| Scene Type | Synthetic (Lego bulldozer) |

## 🔗 References

- **NeRF Paper**: Mildenhall et al., "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis", ECCV 2020
- **Dataset Source**: https://github.com/bmild/nerf

## ⚠️ License

The NeRF Synthetic dataset is provided for research purposes. Please refer to the original repository for licensing terms.
