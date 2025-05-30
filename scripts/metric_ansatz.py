#!/usr/bin/env python3
import json
import requests
from sympy import symbols, Matrix, sin, Function, sympify

# URLs for the shape definitions
SHAPES = {
    "Alcubierre": "https://raw.githubusercontent.com/arcticoder/warp-bubble-coordinate-spec/refs/heads/main/scripts/shapes/alcubierre.json",
    "Natário":    "https://raw.githubusercontent.com/arcticoder/warp-bubble-coordinate-spec/refs/heads/main/scripts/shapes/natario.json",
}

def load_shape(url: str) -> dict:
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def build_metric(f_expr, r, theta):
    """Construct the 4×4 metric matrix g for a profile f(r,t)."""
    # Coordinates: [t, r, θ, φ]
    g = Matrix([[0]*4 for _ in range(4)])
    g[0,0] = -1
    g[1,1] = 1 - f_expr
    g[2,2] = r**2
    g[3,3] = r**2 * sin(theta)**2
    return g

def main():
    # Declare symbols
    t, r, theta, phi = symbols('t r theta phi')
    # Declare profile functions
    interp_alc = Function('interpolated_alcubierre')
    interp_nat = Function('interpolated_natario')

    sections = []

    for name, url in SHAPES.items():
        data = load_shape(url)
        f_str = data['f']  # e.g. "interpolated_alcubierre(r)"
        # Map the function name to the Sympy Function
        local_map = {
            'interpolated_alcubierre': interp_alc,
            'interpolated_natario':    interp_nat,
            'r': r, 't': t
        }
        f_expr = sympify(f_str, locals=local_map)
        # Build metric matrix (not directly used in .tex but exercise)
        g = build_metric(f_expr, r, theta)

        # Prepare LaTeX block
        line_element = (
            r"ds^2 = -\,dt^2 + \bigl(1 - f(r,t)\bigr)\,dr^2 "
            r"+ r^2\,d\theta^2 + r^2\sin^2\theta\,d\phi^2"
        )
        profile_desc = data.get('description', '')
        sections.append((name, f_str, profile_desc, line_element))    # Write the LaTeX document
    with open("metric_ansatz.tex", "w", encoding="utf-8") as tex:
        tex.write(r"""\documentclass{article}
\usepackage{amsmath}
\begin{document}

Coordinates: (t, r, θ, φ) with axial symmetry about the z-axis; functions have compact support in r.

""")
        for name, f_str, desc, elem in sections:
            tex.write(f"\\section*{{{name}}}\n")
            tex.write(f"Profile: $f(r,t) = {f_str}$\\quad ({desc})\n\n")
            tex.write(r"\[")
            tex.write(elem)
            tex.write(r"\]" + "\n\n")
        tex.write(r"\end{document}" + "\n")

    print("Generated metric_ansatz.tex")

if __name__ == "__main__":
    main()