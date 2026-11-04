# Tolerancing

[All resources](../README.md)

Vendor numbers disagree, so treat every value here as a starting point. Print a test coupon for your own printer and material.

## What I recommend

Gap is hole diameter minus shaft diameter in CAD, for a 0.4 mm nozzle.

| Fit | Gap | Use it for |
|---|---|---|
| Press | 0.1 mm | Bearings, magnets, dowel pins |
| Snug | 0.2 mm | Locating parts |
| Slide | 0.3 to 0.4 mm | Parts that need to move |
| Free | 0.5 mm or more | Screw clearance, hinges |

For holes under 5 mm, add another 0.1 mm.

## Holes and fits

- [Nophead: Polyholes](https://hydraraptor.blogspot.com/2011/02/polyholes.html): the classic explanation of why printed holes come out small
- [UAL CCI: Design the clearance and tolerance](https://wiki.cci.arts.ac.uk/books/digital-fabrication-lab/page/design-the-clearance-and-tolerance-readme): a fabrication lab's introduction to fits
- [Sovol: FDM tolerances and clearances](https://www.sovol3d.com/blogs/news/fdm-3d-printing-tolerances-clearances-how-to-design-parts-that-fit): a table of fits by application

## Calibrating your printer

- [OrcaSlicer: Filament tolerance calibration](https://www.orcaslicer.com/wiki/calibration/tolerance_calib): the built-in tolerance test
- [OrcaSlicer: Precision settings](https://www.orcaslicer.com/wiki/print_settings/quality/quality_settings_precision): X-Y hole and contour compensation
- [Teaching Tech: Calibration](https://teachingtechyt.github.io/calibration.html): a full printer calibration walkthrough
