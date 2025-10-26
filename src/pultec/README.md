# Pultec Three-Band EQ - Modular Design

## Overview

This directory contains the modular PCB designs for a Pultec-style three-band equalizer. The design has been broken down from a monolithic schematic into four independent passive modules that can be built, tested, and integrated separately.

## Design Philosophy

**Modularity**: Each frequency processing section is on its own PCB, making it easier to:
- Build incrementally
- Test individual sections
- Troubleshoot problems
- Replace or modify sections without rebuilding everything

**Screw Terminals**: All inter-module connections use screw terminals for:
- Easy assembly without soldering interconnects
- Simple reconfiguration and testing
- No special connectors or cables needed
- Robust mechanical connections

## Directory Structure

```
src/pultec/
├── README.md (this file)
├── docs/
│   └── 1.0/
│       ├── COMPONENT_VALUES.md     # Component list extracted from original schematic
│       └── SYSTEM_OVERVIEW.md      # Complete system integration guide
└── modules/
    ├── low-cut/
    │   ├── README.md               # Module documentation
    │   └── BOM.csv                 # Bill of materials
    ├── low-boost/
    │   ├── README.md
    │   └── BOM.csv
    ├── high-boost/
    │   ├── README.md
    │   └── BOM.csv
    └── high-cut/
        ├── README.md
        └── BOM.csv
```

## Modules

### 1. Low Cut Module
Passive RC network for low-frequency attenuation.
- **Path**: `modules/low-cut/`
- **Complexity**: Simple (2 capacitors)
- **Cost**: ~$10
- **Build Time**: 30 minutes

### 2. Low Boost Module
Passive LC network for low-frequency boost with inductor-based resonance.
- **Path**: `modules/low-boost/`
- **Complexity**: Moderate (11 capacitors, requires 4 hand-wound inductors)
- **Cost**: ~$24 (excluding inductors)
- **Build Time**: 1-2 hours

### 3. High Boost Module
Passive LC network for high-frequency boost with adjustable bandwidth (Q).
- **Path**: `modules/high-boost/`
- **Complexity**: High (8 capacitors, requires 7 hand-wound inductors)
- **Cost**: ~$29 (excluding inductors)
- **Build Time**: 2-3 hours

### 4. High Cut Module
Passive RC network for high-frequency attenuation.
- **Path**: `modules/high-cut/`
- **Complexity**: Moderate (11 capacitors, 1 resistor)
- **Cost**: ~$22
- **Build Time**: 1-2 hours

## Getting Started

### 1. Review the Documentation
- Read `docs/1.0/SYSTEM_OVERVIEW.md` for the complete system architecture
- Review individual module README files for detailed specifications

### 2. Order Components
- Each module directory contains a `BOM.csv` with complete parts list
- All capacitors are standard film types available from Mouser
- Screw terminals are Phoenix Contact 1757 series (5.08mm pitch)

### 3. Design Inductors
The boost sections require hand-wound inductors:
- **Low Boost**: 4 inductors (20Hz, 30Hz, 60Hz, 100Hz)
- **High Boost**: 7 inductors (3kHz, 4kHz, 5kHz, 8kHz, 10kHz, 12kHz, 16kHz)

Refer to the original Ian Thompson-Bell documentation in `reference/` for inductor design guidance.

### 4. PCB Fabrication
**Note**: KiCAD schematic and PCB layout files are not yet created. The current documentation provides:
- Complete component values
- Connection requirements
- Board size estimates
- Terminal placement requirements

To create the PCB files, you will need to:
1. Create KiCAD schematics for each module based on the README
2. Design PCB layouts optimizing for component placement
3. Export Gerbers for fabrication

### 5. Build Order (Recommended)
1. **Low Cut** - Simplest module, good for testing workflow
2. **High Cut** - Similar to Low Cut but more components
3. **Low Boost** - More complex, requires inductors
4. **High Boost** - Most complex, requires many inductors

### 6. Integration
Follow the integration procedure in `docs/1.0/SYSTEM_OVERVIEW.md`:
- Phase 1: Build and test each module individually
- Phase 2: Integrate modules one at a time into signal chain
- Phase 3: Perform frequency response testing
- Phase 4: Final integration with front panel controls

## External Components Required

### Front Panel Controls
- 4× Potentiometers (2× boost level, 2× cut level)
- 1× Potentiometer (high boost Q/bandwidth)
- 4× Rotary switches (frequency selection)
- Knobs, panel hardware

### Inductors (Hand-Wound)
- 4× Low frequency inductors (for Low Boost)
- 7× High frequency inductors (for High Boost)

### Interconnects
- Wire for module-to-module connections
- Wire for control panel connections

### Input/Output Stages
The passive modules connect between:
- **Input Stage** (already built) → provides impedance matching, buffering
- **Output Stage** (already built) → provides makeup gain, buffering

## Cost Estimate

| Item | Cost |
|------|------|
| Module PCBs (4× boards) | $31 |
| Module components | $54 |
| Front panel controls | $50-100 |
| Enclosure | $30-80 |
| Wire, hardware | $20 |
| **Total** | **$185-285** |

*Excludes tools, test equipment, and inductor materials*

## Testing Equipment Needed

### Essential
- Multimeter (continuity, resistance, capacitance)
- LCR meter (for inductor measurement)
- Audio interface or signal generator

### Recommended
- Oscilloscope
- Audio analyzer software (REW - free)
- THD+N analyzer

## Reference Design

This modular design is based on:
- Original monolithic schematic: `src/schematics/pultec-three-band-eq/`
- Ian Thompson-Bell's Pultec documentation (see `reference/`)

## Current Status

✅ Component values extracted from original schematic
✅ Module documentation created
✅ Bills of materials generated
✅ System integration guide written
⬜ KiCAD schematics for individual modules
⬜ PCB layouts for individual modules
⬜ Gerber files for PCB fabrication
⬜ Inductor design calculations
⬜ Test procedures and fixtures

## Contributing

This is an open design. Contributions welcome:
- KiCAD schematic and PCB layout files
- Inductor winding specifications
- Test procedures and results
- Build photos and documentation
- Front panel designs

## License

See main repository README for license information.

## Questions?

Refer to:
- `docs/1.0/SYSTEM_OVERVIEW.md` for architecture and integration
- Individual module README files for component details
- Original documentation in `reference/` for circuit theory
