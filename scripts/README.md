# Scripts Directory

This directory contains Python scripts for generating figures and performing analysis for the BlueFort ACM 2025 research paper.

## 📁 Contents

### Python Scripts

- **`lsc.py`** - Generates LSC (Link Security Control) protocol sequence diagram
  - Output: `../figures/lsc.png`
  - Purpose: Visualizes the Bluetooth LSC protocol flow

- **`example_analysis.py`** - Comprehensive example script demonstrating various visualizations
  - Outputs: Multiple figures in `../figures/` directory
  - Purpose: Shows how to create publication-quality figures for research papers

## 🚀 Usage

### From Project Root
```bash
# Generate all figures
make python-figures

# Run individual scripts
cd scripts
python lsc.py
python example_analysis.py
```

### From Scripts Directory
```bash
# Activate virtual environment first
source ../venv/bin/activate

# Run scripts
python lsc.py
python example_analysis.py
```

## 📊 Generated Figures

All scripts output high-quality PNG files (600 DPI) to the `../figures/` directory:

- `lsc.png` - LSC protocol sequence diagram
- `performance_comparison.png` - Algorithm performance comparison
- `timing_analysis.png` - Execution time analysis
- `network_topology.png` - Network visualization
- `statistical_analysis.png` - Statistical plots

## 💡 Best Practices

1. **Always run from scripts directory** - Scripts are designed to output to `../figures/`
2. **Use virtual environment** - Ensure `(venv)` is active
3. **High DPI output** - All figures generated at 600 DPI for publication quality
4. **Consistent styling** - All scripts use the same matplotlib/seaborn style
5. **Error handling** - Scripts include proper error handling and status messages

## 🔧 Adding New Scripts

1. **Create new Python file** in this directory
2. **Set output path** to `../figures/filename.png`
3. **Use consistent imports** and styling
4. **Add error handling** and status messages
5. **Update this README** with script description

## 📝 LaTeX Integration

To include generated figures in your LaTeX document:

```latex
\includegraphics[width=0.8\columnwidth]{figures/filename.png}
``` 