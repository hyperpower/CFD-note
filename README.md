# CFD-note

Personal notes for learning computational fluid dynamics.

The main documentation is a Sphinx project under `source/`. It includes notes on
basic numerical definitions, structured finite-volume meshes, the Poisson
equation, and appendices.

## Build

Generate figures and build the HTML documentation:

```powershell
python make.py
```

The generated site is written to `build/`.

## Structure

- `source/basic/`: basic numerical definitions.
- `source/mesh/`: mesh and finite-volume structure notes.
- `source/equations/`: equation-specific discretization notes.
- `source/appendix/`: reference material.
- `source/_scripts/`: shared helper scripts for figures.
- `source/_examples/`: reStructuredText examples.
