# BlueFort ACM 2025 Research Paper

Modular LaTeX template for ACM SIGCONF 2025 research papers with Python figure generation.

## Quick Start

```bash
# Build document
make

# Generate figures
make python-figures

# View PDF
make view
```

## Project Structure

```
BlueFortACM2025/
├── paper.tex                 # Main document
├── section-*.tex             # Modular sections
├── acmart.cls                # ACM 2025 class file
├── references.bib            # Bibliography
├── utils/                    # Utilities (utils.tex, activate_venv.sh)
├── scripts/                  # Python scripts for figures
├── figures/                  # Generated figures
├── sources/                  # Diagram sources (PlantUML)
├── requirements.txt          # Python dependencies
├── .vscode/                  # VS Code workspace configuration
└── Makefile                  # Build automation
```

## Setup

### Prerequisites
- TeX Live or MikTeX
- Python 3.8+
- make

### Installation

1. **Clone repository**
   ```bash
   git clone <repository-url>
   cd BlueFortACM2025
   ```

2. **Setup Python environment**
   ```bash
   make python-install
   ```

3. **VS Code (optional)**
   - Open project in VS Code
   - Virtual environment activates automatically in terminals
   - Install LaTeX Workshop extension

4. **Build document**
   ```bash
   make
   ```

## Usage

### LaTeX Commands
```latex
% Available in all .tex files
\haining{Comment from Haining}
\upg{Comment from UPG}
\randy{Comment from Randy}
```

### Python Scripts
```bash
# Generate all figures
make python-figures

# Run individual scripts
cd scripts
python lsc.py
python example_analysis.py
```

### Makefile Targets
```bash
make              # Build complete document
make quick        # Quick build without bibliography
make clean        # Clean build artifacts
make view         # Open PDF
make help         # Show all commands
```

## Customization

### Add New Section
1. Create `section-new.tex`
2. Add `\input{section-new}` to `paper.tex`

### Update Metadata
Edit `paper.tex`:
```latex
\title{Your Title}
\author{Your Name}
\acmConference[Conference '25]{Conference Name}{Date}{Location}
```

## Troubleshooting

```bash
# Reinstall Python packages
make python-install

# Clean and rebuild
make distclean && make

# Check LaTeX installation
pdflatex --version
``` 