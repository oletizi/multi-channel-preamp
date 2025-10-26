# Multi-Channel Preamp Project - Project-Specific Instructions

This is a Pultec-style three-band equalizer project with modular PCB design for professional audio applications.

## Project Overview

**Type**: Analog audio equalizer (passive LC/RC networks)
**Architecture**: Modular design with four separate PCB modules
**Reference**: Based on classic Pultec EQP-1A topology
**Status**: Input/output stages built and tested; passive modules need PCB design

## Project Structure

```
src/
├── pultec/
│   ├── modules/          # Four modular PCB designs
│   │   ├── low-cut/      # Low frequency attenuation
│   │   ├── low-boost/    # Low frequency boost (requires inductors)
│   │   ├── high-boost/   # High frequency boost with Q control (requires inductors)
│   │   └── high-cut/     # High frequency attenuation
│   └── docs/1.0/         # Component values and system documentation
├── schematics/
│   └── pultec-three-band-eq/  # Original monolithic schematic (KiCAD)
└── reference/            # Ian Thompson-Bell's documentation
```

## Design Requirements

### Inter-Module Connections
- **All connections use screw terminals**: Phoenix Contact 1757 series, 5.08mm (0.2") pitch
- **No soldered interconnects**: Modular approach for easy testing and reconfiguration
- **Standard terminal sizes**:
  - 2-position: Phoenix 1757019 (signal I/O, power)
  - 3-position: Phoenix 1757022 (controls, selectors)
  - 6-position: Phoenix 1757025 (frequency selectors)

### Component Standards

#### Signal Path Capacitors
- **Type**: Film capacitors only (no electrolytics in signal path)
- **Preferred**: Vishay MKT1813 series
- **Alternative**: WIMA MKS/MKP (premium audio grade)
- **Specifications**: 5%, 100V minimum, 5.08mm lead spacing
- **Values**: Range from 470pF to 330nF (see component values doc)

#### Resistors
- **Type**: Metal film for low noise
- **Preferred**: Vishay MRS25 (1/4W, 1%)
- **Specifications**: ±1% tolerance, <100ppm/°C TCR
- **Power rating**: Derate to 50% maximum

#### Inductors
- **Hand-wound required**: Not available off-the-shelf for these frequencies
- **Low boost**: 4 inductors (20Hz, 30Hz, 60Hz, 100Hz) - larger values, laminated or powdered iron cores
- **High boost**: 7 inductors (3kHz, 4kHz, 5kHz, 8kHz, 10kHz, 12kHz, 16kHz) - smaller values, powdered iron toroids
- **Core materials**: Powdered iron (Type 26 preferred), laminated steel for low frequencies
- **Wire**: Magnet wire, gauge selected for low DCR and high Q
- **Reference**: Ian Thompson-Bell documentation in `reference/` directory

### PCB Design Standards
- **Board type**: 2-layer through-hole
- **Mounting**: 4× M3 mounting holes at corners
- **Grounding**: Star grounding or ground plane appropriate for audio
- **Trace widths**: 0.5mm signals, 1.0mm+ power
- **Clearances**: 0.25mm minimum
- **Silkscreen**: Clear labeling of all terminals with function

## Module Signal Chain

```
Input Stage (built) → Low Cut → Low Boost → High Boost → High Cut → Output Stage (built)
```

Each module is independent and testable. All modules connect via screw terminals.

## Specialized Agents Available

This project has five specialized Claude agents for circuit design tasks:

1. **circuit-design-specialist**: Circuit analysis, component calculations, frequency response
2. **pcb-layout-engineer**: PCB layout, component placement, grounding strategies
3. **inductor-design-specialist**: Inductor design, core selection, winding specifications
4. **kicad-expert**: KiCAD schematics, PCB layouts, Gerber generation
5. **bom-and-sourcing**: Component sourcing, part numbers, pricing from Mouser/Digikey

See `.claude/agents/README.md` for detailed usage instructions.

## Key Reference Documents

- **Component values**: `src/pultec/docs/1.0/COMPONENT_VALUES.md`
- **System overview**: `src/pultec/docs/1.0/SYSTEM_OVERVIEW.md`
- **Module specs**: `src/pultec/modules/*/README.md` (each module)
- **Original schematic**: `src/schematics/pultec-three-band-eq/pultec-three-band-eq.kicad_sch`
- **Ian Thompson-Bell docs**: `reference/` directory

## Current Status and Next Steps

### Completed ✓
- Input and output stages built and tested
- Component values extracted from monolithic schematic
- Module documentation created (4 modules)
- Bills of materials generated
- System integration documentation
- Specialized agents created

### In Progress
- KiCAD schematics for individual modules
- PCB layouts for individual modules
- Inductor design calculations and specifications

### Not Started
- Gerber file generation for PCB fabrication
- Front panel design and control layout
- Complete inductor winding specifications
- Testing procedures and fixtures

## Working Conventions

### When Creating Schematics
- Use KiCAD 7.x or 8.x
- One project per module in `src/pultec/modules/[module-name]/`
- Include complete title block with revision, date, author
- Run ERC and resolve all errors before finalizing
- Export PDF for documentation

### When Creating PCB Layouts
- Place screw terminals along board edges for accessibility
- Group related components (capacitors by frequency, etc.)
- Provide test points for key signal nodes
- Include clear silkscreen labels (terminal functions, component values)
- Generate complete Gerber set in module's `gerbers/` subdirectory

### When Designing Inductors
- Always calculate from actual capacitor values in schematic
- Document core type, size, material, supplier part number
- Specify exact wire gauge and length needed
- Include winding instructions (turns, layers, direction)
- Provide test criteria (expected L, DCR, Q at target frequency)
- Reference Ian Thompson-Bell's inductor documentation

### When Creating BOMs
- Use CSV format with standard columns (Ref, Qty, Value, Desc, Mfr, P/N, etc.)
- Include Mouser part numbers as primary source
- Note alternatives for expensive or hard-to-find parts
- Separate hand-wound inductors and custom parts
- Calculate total cost with quantity breaks
- Update pricing periodically (component prices fluctuate)

## Quality Standards

- **Audio grade**: This is professional audio equipment; use appropriate components
- **Noise minimization**: Proper grounding, layout, component selection critical
- **Reliability**: Derate components, use quality parts, robust connections
- **Testability**: Include test points, clear documentation, modular architecture
- **Reproducibility**: Complete documentation allows others to build identical units

## Invoking Specialized Agents

Use the Task tool or direct invocation:

```
"Use the inductor-design-specialist to calculate specs for all low-boost inductors"

"Ask the circuit-design-specialist to validate the frequency response of the high-cut section"

"Have the kicad-expert create a schematic for the low-cut module"
```

Agents can work in parallel on independent tasks:

```
"Run in parallel:
- inductor-design-specialist: Design low-boost inductors
- bom-and-sourcing: Update pricing for all modules
- circuit-design-specialist: Verify impedance matching"
```

## Notes

- This is a passive EQ design (no active components in boost/cut sections)
- Inductor quality directly affects Q and frequency response
- Modular approach allows incremental building and testing
- Screw terminals make prototyping and modifications easy
- Reference classic Pultec designs when making design decisions
