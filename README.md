# BlueFort ACM 2025 Research Paper Template

A modular LaTeX template for ACM SIGCONF 2025 research papers with improved organization, collaboration, and maintainability.

## 📋 Table of Contents

- [Overview](#-overview)
- [ACM SIGCONF 2025 Format](#-acm-sigconf-2025-format)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Makefile Usage](#-makefile-usage)
- [File Organization](#-file-organization)
- [Customization](#-customization)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [References](#-references)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

## 🎯 Overview

This project demonstrates **BlueFort**, a novel approach to organizing ACM research papers using modular LaTeX files. The template separates content into individual files for better maintainability, collaboration, and version control while maintaining full ACM compliance.

### Key Features

- ✅ **ACM SIGCONF 2025 Compliant**: Uses official `acmart.cls` class
- ✅ **Modular Structure**: Each section in separate `.tex` files
- ✅ **Automated Build**: Makefile with dependency checking
- ✅ **Clean Organization**: Clear separation of concerns
- ✅ **Collaboration Ready**: Reduces merge conflicts in version control

## 📄 ACM SIGCONF 2025 Format

### What is ACM SIGCONF?

ACM SIGCONF is the **Association for Computing Machinery's conference proceedings format** for research papers. It features:

- **Two-column layout** for optimal readability
- **Specific typography** using Libertine fonts
- **Mandatory metadata** including CCS concepts and keywords
- **Structured author information** with affiliations
- **Professional formatting** for academic publication

### Format Requirements

```latex
\documentclass[sigconf]{acmart}  % Two-column conference format
```

**Required Elements:**
- Abstract (before `\maketitle`)
- CCS Concepts (`\ccsdesc`)
- Keywords (`\keywords`)
- Author affiliations with institution, city, country
- ACM conference metadata (`\acmConference`, `\acmYear`, etc.)

## 📁 Project Structure

```
BlueFortACM2025/
├── paper.tex                 # Main document with ACM metadata
├── abstract.tex              # Abstract section
├── acks.tex                  # Acknowledgments section
├── section-introduction.tex  # Introduction section
├── section-background.tex    # Background and related work
├── section-methodology.tex   # Methodology and approach
├── section-results.tex       # Results and analysis
├── section-conclusion.tex    # Conclusion and future work
├── acmart.cls                # ACM 2025 class file
├── references.bib            # Bibliography file with citations
├── Makefile                  # Build automation
├── .gitignore               # Git ignore rules
├── build/                   # Output directory (generated)
├── images/                  # Images, figures, and graphics
│   └── README.md            # Image usage guidelines
└── acmart-primary/          # Official ACM 2025 template files (reference)
```

## 🚀 Getting Started

### Prerequisites

- **TeX Live** (Linux/macOS) or **MikTeX** (Windows)
- **pdflatex** compiler
- **make** utility

### Installation

1. **Clone or download** this repository
2. **Verify LaTeX installation**:
   ```bash
   pdflatex --version
   ```
3. **Build the document**:
   ```bash
   make
   ```

## 🔧 Makefile Usage

The Makefile provides several targets for building and managing your document:

### Build Commands

```bash
# Build the complete PDF (default)
make

# Build with verbose output
make all

# Clean auxiliary files only
make clean

# Clean everything including PDF
make distclean

# Open PDF in default viewer
make view

# Show available commands
make help
```

### Makefile Features

- **Dependency Checking**: Verifies `pdflatex` is installed
- **Automatic Directory Creation**: Creates `build/` if needed
- **Double Compilation**: Runs LaTeX twice for cross-references
- **Cross-Platform**: Works on Linux, macOS, and Windows
- **Error Handling**: Graceful handling of missing files

### Build Process

1. **Check Dependencies**: Verifies `pdflatex` availability
2. **Create Build Directory**: Ensures `build/` exists
3. **First Compilation**: Generates initial PDF and auxiliary files
4. **Second Compilation**: Resolves cross-references and citations
5. **Output**: Final PDF in `build/main-acm2025.pdf`

## 📝 File Organization

### Main Document (`paper.tex`)

The main document handles:
- Document class and package declarations
- ACM metadata (conference info, DOI, copyright)
- Author information and affiliations
- CCS concepts and keywords
- Section inclusion via `\input{}` commands

### Modular Sections

Each section file contains:
- **Clear section heading** with appropriate labels
- **Well-structured subsections**
- **Professional academic content**
- **No preamble or document-level commands**

#### Section Files

| File | Purpose | Content |
|------|---------|---------|
| `abstract.tex` | Paper abstract | Research summary and contributions |
| `section-introduction.tex` | Introduction | Problem, motivation, contributions |
| `section-background.tex` | Background | Related work and context |
| `section-methodology.tex` | Methodology | Research approach and methods |
| `section-results.tex` | Results | Experimental results and analysis |
| `section-conclusion.tex` | Conclusion | Summary, limitations, future work |
| `acks.tex` | Acknowledgments | Credits and thanks |
| `references.bib` | Bibliography | All citations and references |

### ACM Class File (`acmart.cls`)

The `acmart.cls` file provides:
- ACM 2025 formatting requirements
- Two-column layout for sigconf
- Required metadata fields
- Professional typography and spacing

### Official ACM Template (`acmart-primary/`)

The `acmart-primary/` directory contains the **official ACM 2025 template files** that serve as a reference for:
- **Original template structure**: See how ACM intended the template to be used
- **Example implementations**: Reference implementations for different ACM formats
- **Documentation**: Official documentation and examples
- **Best practices**: ACM's recommended usage patterns

**When to refer to acmart-primary/:**
- Understanding the original template structure
- Comparing with official examples
- Troubleshooting formatting issues
- Learning ACM-specific LaTeX commands
- Verifying compliance with official standards

> **Note**: Our modular approach in the root directory is an improvement over the original single-file template, but `acmart-primary/` remains the authoritative source for ACM formatting requirements.

### Bibliography File (`references.bib`)

The `references.bib` file contains all citations and references used in the paper:

- **ACM Reference Format**: Uses official ACM citation style
- **Comprehensive Coverage**: Includes conference papers, journal articles, books, and online resources
- **Proper Metadata**: Complete DOI, URL, and publication information
- **Organized Structure**: Categorized by reference type for easy management

**Reference Types Included:**
- Conference proceedings (`@inproceedings`)
- Journal articles (`@article`)
- Technical reports (`@techreport`)
- Books and book chapters (`@book`, `@inbook`)
- Websites and online resources (`@misc`)
- Software and tools (`@software`)

### Images Directory (`images/`)

The `images/` directory organizes all visual content for the research paper:

- **Structured Organization**: Separate folders for figures, screenshots, and logos
- **Usage Guidelines**: Comprehensive documentation in `images/README.md`
- **Format Support**: PNG, JPG, PDF, and vector graphics
- **ACM Compliance**: Size and quality requirements for publication

**Directory Structure:**
```
images/
├── figures/          # Main figures, diagrams, and charts
├── screenshots/      # Application and interface screenshots
└── logos/           # Logos and branding elements
```

**Key Features:**
- **Size Guidelines**: Optimized for ACM two-column format
- **Quality Standards**: 300 DPI minimum for print quality
- **LaTeX Integration**: Ready-to-use code examples for inclusion
- **Version Control**: Properly tracked in Git with documentation

## 🎨 Customization

### Adding New Sections

1. **Create section file**:
   ```bash
   # Create new section
   touch section-new-section.tex
   ```

2. **Add content** to `section-new-section.tex`:
   ```latex
   % =============================================================================
   % NEW SECTION
   % =============================================================================
   
   \section{New Section}\label{sec:new-section}
   
   Your content here...
   ```

3. **Include in main document** (`paper.tex`):
   ```latex
   \input{section-new-section}
   ```

### Modifying ACM Metadata

Update these fields in `paper.tex`:

```latex
% Conference information
\acmConference[Conference '25]{Conference Name}{Month Day--Day, 2025}{Location, Country}

% Author information
\author{Your Name}
\affiliation{
  \institution{Your Institution}
  \city{Your City}
  \country{Your Country}
}

% CCS concepts (required)
\ccsdesc[500]{Computer systems organization~Embedded and cyber-physical systems}
\ccsdesc[300]{Software and its engineering~Software organization and properties}

% Keywords
\keywords{ACM, LaTeX, research paper, template, organization}
```

### Adding Bibliography

1. **Create bibliography file** (`references.bib`)
2. **Add to main document**:
   ```latex
   \bibliographystyle{ACM-Reference-Format}
   \bibliography{references}
   ```
3. **Update Makefile** to include BibTeX compilation

## 🔍 Troubleshooting

### Common Issues

#### LaTeX Not Found
```bash
# Install TeX Live (Ubuntu/Debian)
sudo apt-get install texlive-full

# Install TeX Live (macOS)
brew install --cask mactex

# Install MikTeX (Windows)
# Download from https://miktex.org/
```

#### Build Errors
```bash
# Clean and rebuild
make distclean
make

# Check for syntax errors
pdflatex paper.tex
```

#### Missing Dependencies
```bash
# Install additional LaTeX packages
sudo apt-get install texlive-latex-extra
```

### Debug Mode

For detailed compilation information:
```bash
# Verbose compilation
pdflatex -interaction=nonstopmode paper.tex
```

## 🤝 Contributing

### Development Workflow

1. **Fork** the repository
2. **Create feature branch**:
   ```bash
   git checkout -b feature/new-section
   ```
3. **Make changes** to section files
4. **Test build**:
   ```bash
   make clean && make
   ```
5. **Commit changes**:
   ```bash
   git commit -m "Add new methodology section"
   ```
6. **Push and create pull request**

### Code Style

- **Consistent formatting** in all `.tex` files
- **Clear comments** explaining complex LaTeX
- **Modular structure** with single responsibility
- **ACM compliance** maintained throughout

## 📚 References

- [ACM Author Guidelines](https://www.acm.org/publications/authors/submissions)
- [ACM LaTeX Template](https://github.com/borisveytsman/acmart)
- [LaTeX Documentation](https://www.latex-project.org/help/documentation/)
- [Make Documentation](https://www.gnu.org/software/make/manual/)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- ACM for providing excellent LaTeX templates
- Open-source community for continuous improvements
- Contributors to the academic publishing workflow

---

**Happy Writing! 📝✨** 