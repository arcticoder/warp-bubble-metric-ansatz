# warp-bubble-metric-ansatz

A small toolkit to fetch warp-bubble profile definitions from the `warp-bubble-coordinate-spec` repo and generate both:

1. A Python script (`metric_ansatz.py`) that:
   - Downloads the JSON shape definitions for the Alcubierre and Natário profiles.
   - Constructs the Sympy metric matrix \(g_{\mu\nu}\) for each profile.
   - Emits a standalone LaTeX document with the corresponding line elements.

2. A LaTeX file (`metric_ansatz.tex`) that compiles to show the metric ansatz for both profiles in a human-readable form.

## Prerequisites

- Python 3.7+
- Python packages:
```bash
  pip install requests sympy
```

-   LaTeX distribution with `amsmath` package
    

## Usage

1.  Clone the repo:
    
```bash
git clone https://github.com/your-org/warp-bubble-metric-ansatz.git
cd warp-bubble-metric-ansatz
```
    
2.  Run the generator script:
    
```bash
python scripts/metric_ansatz.py
```
    
    This will produce/update `metric_ansatz.tex`.
    
3.  Compile the LaTeX file:
    
```bash
pdflatex metric_ansatz.tex
```
    

You’ll end up with `metric_ansatz.pdf` showing the line elements for both warp-bubble profiles.

## Repository Structure

```bash
.
├── README.md
├── metric_ansatz.py       # Python generator script
└── metric_ansatz.tex      # Example/templated LaTeX output
```
