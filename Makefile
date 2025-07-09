# =============================================================================
# BlueFort ACM 2025 LaTeX Document - Enhanced Makefile
# =============================================================================
# Compiles the ACM 2025 sigconf format document into a PDF in the build directory
# Features: Dependency tracking, error handling, multiple targets, and user-friendly interface

# =============================================================================
# CONFIGURATION VARIABLES
# =============================================================================

# Document configuration
MAIN_DOC = paper
BUILD_DIR = build
LATEX_CMD = pdflatex -interaction=nonstopmode -output-directory="$(BUILD_DIR)"
BIBTEX_CMD = bibtex
PDF_FILE = $(BUILD_DIR)/$(MAIN_DOC).pdf

# Source files (for dependency tracking)
TEX_SOURCES = $(MAIN_DOC).tex abstract.tex acks.tex
SECTION_SOURCES = $(wildcard section-*.tex)
BIB_SOURCES = references.bib
CLS_SOURCES = acmart.cls
ALL_SOURCES = $(TEX_SOURCES) $(SECTION_SOURCES) $(BIB_SOURCES) $(CLS_SOURCES)

# Compilation flags
LATEX_FLAGS = -interaction=nonstopmode -output-directory="$(BUILD_DIR)"
BIBTEX_FLAGS = 

# =============================================================================
# DEFAULT TARGET
# =============================================================================

.PHONY: all
all: checklatex $(PDF_FILE)
	@echo "✅ Build completed successfully!"
	@echo "📄 PDF generated: $(PDF_FILE)"

# =============================================================================
# DEPENDENCY CHECKS
# =============================================================================

.PHONY: checklatex checkbibtex checkdeps
checklatex:
	@echo "🔍 Checking LaTeX installation..."
	@command -v pdflatex >/dev/null 2>&1 || { echo >&2 "❌ pdflatex not found. Please install TeX Live or MikTeX."; exit 1; }
	@echo "✅ pdflatex found: $(shell which pdflatex)"

checkbibtex:
	@echo "🔍 Checking BibTeX installation..."
	@command -v bibtex >/dev/null 2>&1 || { echo >&2 "❌ bibtex not found. Please install TeX Live or MikTeX."; exit 1; }
	@echo "✅ bibtex found: $(shell which bibtex)"

checkdeps: checklatex checkbibtex
	@echo "🔍 Checking source files..."
	@for file in $(ALL_SOURCES); do \
		if [ ! -f "$$file" ]; then \
			echo "❌ Missing source file: $$file"; \
			exit 1; \
		fi; \
	done
	@echo "✅ All source files present"

# =============================================================================
# DIRECTORY MANAGEMENT
# =============================================================================

$(BUILD_DIR):
	@echo "📁 Creating build directory..."
	@mkdir -p "$(BUILD_DIR)"
	@echo "✅ Build directory ready"

# =============================================================================
# COMPILATION TARGETS
# =============================================================================

# Main compilation target with dependency tracking
$(PDF_FILE): $(BUILD_DIR) $(ALL_SOURCES)
	@echo "🔄 Starting LaTeX compilation..."
	@echo "📝 First pass: Initial compilation"
	$(LATEX_CMD) $(LATEX_FLAGS) $(MAIN_DOC).tex
	@echo "📚 Second pass: Bibliography processing"
	-$(BIBTEX_CMD) $(BIBTEX_FLAGS) $(BUILD_DIR)/$(MAIN_DOC)
	@echo "🔄 Third pass: Resolving references"
	$(LATEX_CMD) $(LATEX_FLAGS) $(MAIN_DOC).tex
	@echo "🔄 Fourth pass: Final compilation"
	$(LATEX_CMD) $(LATEX_FLAGS) $(MAIN_DOC).tex
	@echo "✅ Compilation completed"

# Quick compilation (no bibliography)
.PHONY: quick
quick: checklatex $(BUILD_DIR) $(TEX_SOURCES) $(SECTION_SOURCES) $(CLS_SOURCES)
	@echo "⚡ Quick compilation (no bibliography)..."
	$(LATEX_CMD) $(LATEX_FLAGS) $(MAIN_DOC).tex
	$(LATEX_CMD) $(LATEX_FLAGS) $(MAIN_DOC).tex
	@echo "✅ Quick compilation completed"

# Bibliography-only compilation
.PHONY: bib
bib: checkbibtex $(BUILD_DIR) $(BIB_SOURCES)
	@echo "📚 Processing bibliography..."
	-$(BIBTEX_CMD) $(BIBTEX_FLAGS) $(BUILD_DIR)/$(MAIN_DOC)
	@echo "✅ Bibliography processed"

# =============================================================================
# CLEANING TARGETS
# =============================================================================

.PHONY: clean distclean spotless
clean:
	@echo "🧹 Cleaning build artifacts..."
	$(RM) -rf $(BUILD_DIR)/*
	@echo "✅ Build directory cleaned"

distclean: clean
	@echo "🗑️  Removing PDF file..."
	$(RM) -f $(PDF_FILE)
	@echo "✅ All files removed"

spotclean:
	@echo "🧽 Spot cleaning auxiliary files..."
	$(RM) -f $(BUILD_DIR)/*.aux $(BUILD_DIR)/*.log $(BUILD_DIR)/*.out $(BUILD_DIR)/*.toc
	$(RM) -f $(BUILD_DIR)/*.fls $(BUILD_DIR)/*.fdb_latexmk $(BUILD_DIR)/*.bbl $(BUILD_DIR)/*.blg
	$(RM) -f $(BUILD_DIR)/*.bcf $(BUILD_DIR)/*.run.xml $(BUILD_DIR)/*.synctex.gz
	@echo "✅ Auxiliary files cleaned"

# =============================================================================
# UTILITY TARGETS
# =============================================================================

.PHONY: view open
view: $(PDF_FILE)
	@echo "📖 Opening PDF viewer..."
	@xdg-open $(PDF_FILE) 2>/dev/null || \
	open $(PDF_FILE) 2>/dev/null || \
	start $(PDF_FILE) 2>/dev/null || \
	echo "❌ Could not open PDF automatically. Please open $(PDF_FILE) manually."

open: view

.PHONY: status info
status:
	@echo "📊 Build Status:"
	@echo "  📄 Main document: $(MAIN_DOC).tex"
	@echo "  📁 Build directory: $(BUILD_DIR)"
	@echo "  📋 Source files: $(words $(ALL_SOURCES)) files"
	@if [ -f "$(PDF_FILE)" ]; then \
		echo "  ✅ PDF exists: $(PDF_FILE)"; \
		echo "  📏 PDF size: $(shell ls -lh $(PDF_FILE) | awk '{print $$5}')"; \
		echo "  📅 Last modified: $(shell ls -l $(PDF_FILE) | awk '{print $$6, $$7, $$8}')"; \
	else \
		echo "  ❌ PDF not found"; \
	fi

info: status

.PHONY: debug
debug: checkdeps
	@echo "🐛 Debug Information:"
	@echo "  📝 LaTeX command: $(LATEX_CMD)"
	@echo "  📚 BibTeX command: $(BIBTEX_CMD)"
	@echo "  📁 Build directory: $(BUILD_DIR)"
	@echo "  📄 PDF target: $(PDF_FILE)"
	@echo "  📋 Source files:"
	@for file in $(ALL_SOURCES); do \
		echo "    - $$file"; \
	done

# =============================================================================
# PYTHON ENVIRONMENT TARGETS
# =============================================================================

.PHONY: python-env python-check python-install python-clean python-figures
python-env:
	@echo "🐍 Setting up Python virtual environment..."
	@if [ ! -d "venv" ]; then \
		echo "📁 Creating virtual environment..."; \
		python3 -m venv venv; \
		echo "✅ Virtual environment created"; \
	else \
		echo "✅ Virtual environment already exists"; \
	fi

python-check:
	@echo "🔍 Checking Python environment..."
	@command -v python3 >/dev/null 2>&1 || { echo >&2 "❌ python3 not found. Please install Python 3.8+."; exit 1; }
	@echo "✅ python3 found: $(shell which python3)"
	@if [ -d "venv" ]; then \
		echo "✅ Virtual environment exists"; \
		echo "📦 Python packages:"; \
		venv/bin/pip list --format=columns | head -10; \
	else \
		echo "⚠️  Virtual environment not found. Run 'make python-env' to create it."; \
	fi

python-install: python-env
	@echo "📦 Installing Python packages..."
	@venv/bin/pip install --upgrade pip
	@venv/bin/pip install -r requirements.txt
	@echo "✅ Python packages installed"

python-clean:
	@echo "🧹 Cleaning Python environment..."
	@if [ -d "venv" ]; then \
		rm -rf venv; \
		echo "✅ Virtual environment removed"; \
	else \
		echo "✅ No virtual environment to clean"; \
	fi

python-figures: python-check
	@echo "📊 Generating figures from Python scripts..."
	@if [ -d "scripts" ]; then \
		cd scripts && \
		for script in *.py; do \
			if [ -f "$$script" ]; then \
				echo "🔄 Running $$script..."; \
				../venv/bin/python "$$script"; \
			fi; \
		done; \
		echo "✅ Figures generated in figures/ directory"; \
	else \
		echo "⚠️  No scripts directory found"; \
	fi

# =============================================================================
# HELP AND DOCUMENTATION
# =============================================================================

.PHONY: help
help:
	@echo "=============================================================================="
	@echo "BlueFort ACM 2025 LaTeX Document - Makefile Help"
	@echo "=============================================================================="
	@echo ""
	@echo "📋 AVAILABLE TARGETS:"
	@echo ""
	@echo "🔨 BUILD TARGETS:"
	@echo "  all        - Build complete PDF with bibliography (default)"
	@echo "  quick      - Quick build without bibliography"
	@echo "  bib        - Process bibliography only"
	@echo ""
	@echo "🧹 CLEANING TARGETS:"
	@echo "  clean      - Remove all build artifacts"
	@echo "  distclean  - Remove everything including PDF"
	@echo "  spotclean  - Remove only auxiliary files"
	@echo ""
	@echo "🔍 UTILITY TARGETS:"
	@echo "  view/open  - Open PDF with default viewer"
	@echo "  status     - Show build status and file info"
	@echo "  debug      - Show debug information"
	@echo "  help       - Show this help message"
	@echo ""
	@echo "🐍 PYTHON TARGETS:"
	@echo "  python-env     - Create Python virtual environment"
	@echo "  python-check   - Check Python environment status"
	@echo "  python-install - Install Python packages"
	@echo "  python-clean   - Remove Python virtual environment"
	@echo "  python-figures - Generate figures from Python scripts"
	@echo ""
	@echo "🔧 CONFIGURATION:"
	@echo "  Main document: $(MAIN_DOC).tex"
	@echo "  Build directory: $(BUILD_DIR)"
	@echo "  Output PDF: $(PDF_FILE)"
	@echo ""
	@echo "💡 USAGE EXAMPLES:"
	@echo "  make              # Build complete document"
	@echo "  make quick        # Quick build without bibliography"
	@echo "  make clean        # Clean build artifacts"
	@echo "  make view         # Open PDF"
	@echo "  make status       # Check build status"
	@echo "  make python-env   # Set up Python environment"
	@echo "  make python-figures # Generate figures"
	@echo ""

# =============================================================================
# DEVELOPMENT TARGETS
# =============================================================================

.PHONY: watch
watch:
	@echo "👀 Watching for changes (requires inotify-tools)..."
	@command -v inotifywait >/dev/null 2>&1 || { echo >&2 "❌ inotifywait not found. Install inotify-tools for auto-rebuild."; exit 1; }
	@while inotifywait -e modify $(ALL_SOURCES) 2>/dev/null; do \
		echo "🔄 File changed, rebuilding..."; \
		make quick; \
	done

.PHONY: install-deps
install-deps:
	@echo "📦 Installing dependencies..."
	@echo "🔍 Detecting system..."
	@if command -v apt-get >/dev/null 2>&1; then \
		echo "📦 Ubuntu/Debian detected"; \
		sudo apt-get update && sudo apt-get install -y texlive-full make; \
	elif command -v yum >/dev/null 2>&1; then \
		echo "📦 RHEL/CentOS detected"; \
		sudo yum install -y texlive-scheme-full make; \
	elif command -v brew >/dev/null 2>&1; then \
		echo "📦 macOS detected"; \
		brew install --cask mactex; \
	else \
		echo "❌ Unsupported system. Please install TeX Live manually."; \
	fi

# =============================================================================
# PHONY TARGETS DECLARATION
# =============================================================================

.PHONY: all clean distclean spotclean quick bib view open status info debug help watch install-deps checklatex checkbibtex checkdeps python-env python-check python-install python-clean python-figures 