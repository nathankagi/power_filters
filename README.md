# power_filters

Package for designing passive power filters based on the paper published by CERN.
https://cds.cern.ch/record/2038629/files/265-289-Kunzi.pdf

This only includes parallel RC damped filters as they are suitable for high-power designs.

# Design Note

This tool does not include component parasitic properties in its calculations. This should be considered when applying this to a design as it will impact the ideal performance of a filter.
