# Using LLMs for CAD

[All resources](../README.md)

## A worked example

- [alex-3d-skills](https://github.com/alexchunlin/alex-3d-skills): how I get an LLM to design 3D printable assemblies, and check them before printing
- [Findings](https://github.com/alexchunlin/alex-3d-skills/blob/main/docs/FINDINGS.md): the mistakes agents actually made, and the rules each one led to
- [M&M Launcher](https://github.com/Every-Flavor-Robotics/mm-launcher): a machine designed this way
- [M&M Launcher build package](https://github.com/Every-Flavor-Robotics/mm-launcher/tree/main/mm-launch-hw/v2/BUILD): build instructions, including the interactive assembly guide

## CAD that an LLM can write

These tools describe parts as text, which LLMs can read, edit and rerun.

- [CadQuery](https://cadquery.readthedocs.io/): build parts from Python
- [build123d](https://build123d.readthedocs.io/): another Python CAD library
- [OpenSCAD](https://openscad.org/): a language for describing solid models
- [FeatureScript](https://cad.onshape.com/FsDoc/): Onshape's language for custom features
