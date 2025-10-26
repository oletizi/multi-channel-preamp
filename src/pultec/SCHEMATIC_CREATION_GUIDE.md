# KiCAD Schematic Creation Guide
## Pultec Three-Band EQ Modular Design

**Date**: 2025-10-26
**Revision**: 1.0
**Author**: KiCAD Expert Agent

---

## Overview

This document provides complete specifications for creating KiCAD schematics for all four Pultec EQ modules. Due to the complexity of KiCAD's file format, schematics should be created using KiCAD GUI (version 7.x or 8.x) following these detailed specifications.

## Prerequisites

- KiCAD 7.x or 8.x installed
- Standard libraries: Device, Connector
- Phoenix Contact footprint library (for screw terminals)

---

## Module 1: Low-Cut

### Overview
- **Function**: Low frequency attenuation (20Hz, 30Hz, 60Hz, 100Hz)
- **Topology**: Passive RC network
- **Complexity**: Simple (2 capacitors, 4 connectors)

### Schematic Components

#### Capacitors
| Reference | Value | Description | Footprint | MPN |
|-----------|-------|-------------|-----------|-----|
| C23 | 33nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813333104 |
| C24 | 47nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813447104 |

#### Connectors (Phoenix Contact 1757 Series)
| Reference | Type | Label | Description | MPN |
|-----------|------|-------|-------------|-----|
| J1 | 2-pos | IN | Input from previous stage | 1757019 |
| J2 | 2-pos | OUT | Output to Low Boost | 1757019 |
| J3 | 3-pos | CUT_SEL_RET | Frequency selector return | 1757022 |
| J4 | 2-pos | CUT_LVL | Cut level control | 1757019 |

#### Power
| Reference | Type | Net Name |
|-----------|------|----------|
| #PWR01 | GND | GND |
| #PWR02 | GND | GND |

### Circuit Description

The Low Cut module uses two capacitors (C23, C24) that are switched via an external rotary selector. The selector return connection (J3) allows different capacitor values to create frequency-selective attenuation. The level control (J4) connects to an external potentiometer that adjusts the amount of cut.

**Signal Flow**:
```
J1 (IN) → C23/C24 (selected via J3) → J4 (level control) → J2 (OUT)
                                     ↓
                                    GND
```

### Net Labels
- `SIG_IN`: Input signal from J1
- `SIG_OUT`: Output signal to J2
- `CUT_SEL_RET`: Selector return signals
- `GND`: Ground plane

### Layout Suggestions
- Place J1 (input) on left side of board
- Place J2 (output) on right side of board
- Center capacitors between input/output
- Place J3 (selector) and J4 (level) at bottom edge
- Use clear silkscreen labels for all terminals

---

## Module 2: Low-Boost

### Overview
- **Function**: Low frequency boost (20Hz, 30Hz, 60Hz, 100Hz)
- **Topology**: Passive LC network with external inductors
- **Complexity**: High (11 capacitors, 1 resistor, 4 inductor connections, 9 connectors)

### Schematic Components

#### Capacitors
| Reference | Value | Description | Footprint | MPN |
|-----------|-------|-------------|-----------|-----|
| C1 | 18nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813183104 |
| C2 | 10nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813103104 |
| C3 | 4.7nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813472104 |
| C4 | 3.3nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813332104 |
| C5 | 2.2nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813222104 |
| C4a2 | 1nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813102104 |
| C5a2 | 1.5nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813152104 |
| C6 | 1.8nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813182104 |
| C7 | 1nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813102104 |
| C34 | 1nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813102104 |
| C35 | 1nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813102104 |

#### Resistors
| Reference | Value | Description | Footprint | MPN |
|-----------|-------|-------------|-----------|-----|
| R2 | 56kΩ | Metal film, 1/4W, 1% | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm | Vishay MRS25 |

#### Inductors (External, Hand-Wound)
| Reference | Value | Frequency | Description | Connection |
|-----------|-------|-----------|-------------|------------|
| L1 | TBD | 20Hz | Hand-wound, powdered iron | J6 (IND_20HZ) |
| L2 | TBD | 30Hz | Hand-wound, powdered iron | J7 (IND_30HZ) |
| L3 | TBD | 60Hz | Hand-wound, powdered iron | J8 (IND_60HZ) |
| L4 | TBD | 100Hz | Hand-wound, powdered iron | J9 (IND_100HZ) |

#### Connectors (Phoenix Contact 1757 Series)
| Reference | Type | Label | Description | MPN |
|-----------|------|-------|-------------|-----|
| J1 | 2-pos | IN | Input from Low Cut | 1757019 |
| J2 | 2-pos | OUT | Output to High Boost | 1757019 |
| J3 | 6-pos | BOOST_SEL_SND | Frequency selector send | 1757025 |
| J4 | 6-pos | BOOST_SEL_RET | Frequency selector return | 1757025 |
| J5 | 3-pos | BOOST_LVL | Boost level control | 1757022 |
| J6 | 2-pos | IND_20HZ | 20Hz inductor connection | 1757019 |
| J7 | 2-pos | IND_30HZ | 30Hz inductor connection | 1757019 |
| J8 | 2-pos | IND_60HZ | 60Hz inductor connection | 1757019 |
| J9 | 2-pos | IND_100HZ | 100Hz inductor connection | 1757019 |

#### Power
| Reference | Type | Net Name |
|-----------|------|----------|
| #PWR01 | GND | GND |
| #PWR02 | GND | GND |

### Circuit Description

The Low Boost module uses a complex capacitor network (C1-C7, C34-C35, C4a2, C5a2) that works with external inductors (L1-L4) to create resonant boost at selected frequencies. The rotary frequency selector (connected via J3/J4) switches between different capacitor/inductor combinations. R2 provides network loading.

**Signal Flow**:
```
J1 (IN) → R2 → Capacitor Network → Inductor (external via J6-J9) →
                                  ↓
                            J5 (level control) → J2 (OUT)
                                  ↓
                                 GND
```

### Important Notes

1. **Inductors are external**: L1-L4 must be hand-wound and connected via J6-J9
2. **Selector complexity**: 6-position rotary selector required for frequency selection
3. **Capacitor arrangement**: Multiple capacitors may be switched in series/parallel depending on frequency
4. **See inductor design docs**: Refer to LOW_BOOST_INDUCTOR_SPECIFICATIONS.md for winding details

### Net Labels
- `SIG_IN`: Input signal
- `SIG_OUT`: Output signal
- `BOOST_SEL_SND`: Selector send signals (6 positions)
- `BOOST_SEL_RET`: Selector return signals (6 positions)
- `IND_20HZ`, `IND_30HZ`, `IND_60HZ`, `IND_100HZ`: Inductor connections
- `GND`: Ground plane

### Layout Suggestions
- Place J1 (input) on left edge
- Place J2 (output) on right edge
- Group capacitors by value in center area
- Place inductor connectors (J6-J9) along one edge for easy access
- Place selector connectors (J3, J4) along opposite edge
- Use silkscreen to clearly label all inductor terminals with frequency

---

## Module 3: High-Boost

### Overview
- **Function**: High frequency boost (3kHz, 4kHz, 5kHz, 8kHz, 10kHz, 12kHz, 16kHz)
- **Topology**: Passive LC network with external inductors and Q control
- **Complexity**: Very high (8 capacitors, 1 resistor, 7 inductor connections, 13 connectors)

### Schematic Components

#### Capacitors
| Reference | Value | Description | Footprint | MPN |
|-----------|-------|-------------|-----------|-----|
| C14 | 4.7nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813472104 |
| C15 | 4.7nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813472104 |
| C16 | 3.3nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813332104 |
| C17 | 1nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813102104 |
| C2a2 | 470pF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813471104 |
| C29 | 15nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813153104 |
| C32 | 10nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813103104 |
| C33 | 2.2nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813222104 |

#### Resistors
| Reference | Value | Description | Footprint | MPN |
|-----------|-------|-------------|-----------|-----|
| R3 | 4.7kΩ | Metal film, 1/4W, 1% | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm | Vishay MRS25 |

#### Inductors (External, Hand-Wound)
| Reference | Value | Frequency | Description | Connection |
|-----------|-------|-----------|-------------|------------|
| L5 | TBD | 3kHz | Hand-wound, powdered iron toroid | J7 (IND_3KHZ) |
| L6 | TBD | 4kHz | Hand-wound, powdered iron toroid | J8 (IND_4KHZ) |
| L7 | TBD | 5kHz | Hand-wound, powdered iron toroid | J9 (IND_5KHZ) |
| L8 | TBD | 8kHz | Hand-wound, powdered iron toroid | J10 (IND_8KHZ) |
| L9 | TBD | 10kHz | Hand-wound, powdered iron toroid | J11 (IND_10KHZ) |
| L10 | TBD | 12kHz | Hand-wound, powdered iron toroid | J12 (IND_12KHZ) |
| L11 | TBD | 16kHz | Hand-wound, powdered iron toroid | J13 (IND_16KHZ) |

#### Connectors (Phoenix Contact 1757 Series)
| Reference | Type | Label | Description | MPN |
|-----------|------|-------|-------------|-----|
| J1 | 2-pos | IN | Input from Low Boost | 1757019 |
| J2 | 2-pos | OUT | Output to High Cut | 1757019 |
| J3 | 6-pos | BOOST_SEL_SND | Frequency selector send | 1757025 |
| J4 | 6-pos | BOOST_SEL_RET | Frequency selector return | 1757025 |
| J5 | 3-pos | BOOST_LVL | Boost level control | 1757022 |
| J6 | 3-pos | BOOST_Q | Bandwidth (Q) control | 1757022 |
| J7 | 2-pos | IND_3KHZ | 3kHz inductor connection | 1757019 |
| J8 | 2-pos | IND_4KHZ | 4kHz inductor connection | 1757019 |
| J9 | 2-pos | IND_5KHZ | 5kHz inductor connection | 1757019 |
| J10 | 2-pos | IND_8KHZ | 8kHz inductor connection | 1757019 |
| J11 | 2-pos | IND_10KHZ | 10kHz inductor connection | 1757019 |
| J12 | 2-pos | IND_12KHZ | 12kHz inductor connection | 1757019 |
| J13 | 2-pos | IND_16KHZ | 16kHz inductor connection | 1757019 |

#### Power
| Reference | Type | Net Name |
|-----------|------|----------|
| #PWR01 | GND | GND |
| #PWR02 | GND | GND |

### Circuit Description

Similar to Low Boost but for higher frequencies (3kHz-16kHz). The Q control (J6) allows adjustment of boost bandwidth - a unique Pultec feature. Seven frequency positions require seven hand-wound inductors with smaller inductance values than low-frequency section.

**Signal Flow**:
```
J1 (IN) → R3 → Capacitor Network → Inductor (external via J7-J13) →
                                  ↓
                            J5 (level) & J6 (Q control) → J2 (OUT)
                                  ↓
                                 GND
```

### Important Notes

1. **Seven inductors required**: L5-L11 cover 3kHz to 16kHz range
2. **Q control**: J6 allows bandwidth adjustment (narrow/wide boost)
3. **Smaller inductors**: High-frequency inductors are smaller than low-frequency
4. **Toroid cores recommended**: Powdered iron toroids (Type 26) work well at these frequencies

### Net Labels
- `SIG_IN`: Input signal
- `SIG_OUT`: Output signal
- `BOOST_SEL_SND`: Selector send signals (6 positions)
- `BOOST_SEL_RET`: Selector return signals (6 positions)
- `IND_3KHZ` through `IND_16KHZ`: Inductor connections (7 total)
- `GND`: Ground plane

### Layout Suggestions
- Larger board required due to component count
- Group inductor terminals along bottom edge
- Place selector and control terminals along top edge
- Clear frequency labeling on silkscreen is critical
- Consider two rows of inductor terminals for easier wiring

---

## Module 4: High-Cut

### Overview
- **Function**: High frequency attenuation (5kHz, 10kHz, 20kHz)
- **Topology**: Passive RC network
- **Complexity**: Moderate (11 capacitors, 1 resistor, 5 connectors)

### Schematic Components

#### Capacitors
| Reference | Value | Description | Footprint | MPN |
|-----------|-------|-------------|-----------|-----|
| C18 | 330nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813334104 |
| C19 | 220nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813224104 |
| C20 | 120nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813124104 |
| C21 | 68nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813683104 |
| C22 | 47nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813473104 |
| C25 | 47nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813473104 |
| C26 | 47nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813473104 |
| C27 | 22nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813223104 |
| C28 | 22nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813223104 |
| C30 | 33nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813333104 |
| C31 | 10nF | Film capacitor, 5%, 100V | Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm | MKT1813103104 |

#### Resistors
| Reference | Value | Description | Footprint | MPN |
|-----------|-------|-------------|-----------|-----|
| R1 | 430Ω | Metal film, 1/4W, 1% | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm | Vishay MRS25 |

#### Connectors (Phoenix Contact 1757 Series)
| Reference | Type | Label | Description | MPN |
|-----------|------|-------|-------------|-----|
| J1 | 2-pos | IN | Input from High Boost | 1757019 |
| J2 | 2-pos | OUT | Output to output stage | 1757019 |
| J3 | 6-pos | CUT_SEL_SND | Frequency selector send | 1757025 |
| J4 | 6-pos | CUT_SEL_RET | Frequency selector return | 1757025 |
| J5 | 3-pos | CUT_LVL | Cut level control | 1757022 |

#### Power
| Reference | Type | Net Name |
|-----------|------|----------|
| #PWR01 | GND | GND |
| #PWR02 | GND | GND |

### Circuit Description

The High Cut module uses a resistor-capacitor network to create frequency-selective attenuation at high frequencies. R1 (430Ω) provides the attenuation pad loading. Multiple capacitors with similar values (e.g., three 47nF capacitors) may be used in series or parallel configurations depending on the selected frequency.

**Signal Flow**:
```
J1 (IN) → R1 → Capacitor Network (C18-C31, selected via J3/J4) →
                                  ↓
                            J5 (level control) → J2 (OUT)
                                  ↓
                                 GND
```

### Important Notes

1. **No inductors**: Pure RC network for high-frequency cut
2. **Critical resistor**: R1 (430Ω) is essential for proper network loading
3. **Multiple 47nF caps**: C22, C25, C26 may be switched together for certain frequencies
4. **Large capacitor values**: Uses larger capacitance values than boost sections

### Net Labels
- `SIG_IN`: Input signal
- `SIG_OUT`: Output signal
- `CUT_SEL_SND`: Selector send signals (6 positions)
- `CUT_SEL_RET`: Selector return signals (6 positions)
- `GND`: Ground plane

### Layout Suggestions
- Moderate board size
- Group capacitors by value
- Place R1 near input for proper loading
- Selector terminals (J3, J4) along one edge
- Clear frequency markings on silkscreen

---

## General KiCAD Workflow

### Creating Each Module Schematic

1. **Create New Project**
   - File → New Project
   - Save as `[module-name].kicad_pro` in appropriate directory
   - Example: `src/pultec/modules/low-cut/low-cut.kicad_pro`

2. **Configure Title Block**
   - Open schematic editor
   - Page Setup → Title Block
   - Fill in: Title, Date, Revision, Company, Comments

3. **Add Components**
   - Press 'A' to add symbol
   - Search for component type (Device:C, Device:R, Device:L, Connector:Screw_Terminal_01x02, etc.)
   - Place all components per specifications above

4. **Set Component Properties**
   - Select component → 'E' for properties
   - Set Reference (C1, R2, J3, etc.)
   - Set Value (10nF, 56k, etc.)
   - Set Footprint (from table above)
   - Add custom field "MPN" with manufacturer part number
   - Add Description field

5. **Wire Components**
   - Press 'W' to start wire
   - Connect components according to circuit topology
   - Add junctions where needed (right-click → Place Junction)

6. **Add Net Labels**
   - Press 'L' to add label
   - Label critical nets (SIG_IN, SIG_OUT, etc.)
   - Use hierarchical labels for inter-module connections

7. **Add Power Symbols**
   - Add GND symbols where needed
   - Connect to terminal grounds and component grounds

8. **Add Text Annotations**
   - Add notes about external components (inductors)
   - Add frequency labels near selector terminals
   - Document any special requirements

9. **Run ERC (Electrical Rules Check)**
   - Tools → Electrical Rules Checker
   - Resolve all errors
   - Address warnings (some may be acceptable)

10. **Annotate Schematic**
    - Tools → Annotate Schematic
    - Use automatic annotation
    - Verify all references are unique

11. **Generate Netlist**
    - Tools → Generate Netlist
    - Save for PCB layout import

12. **Export PDF**
    - File → Plot
    - Select PDF format
    - Save to module directory for documentation

### Common ERC Issues and Solutions

**"Pin not connected"**
- Solution: Connect all component pins or mark as "No Connect" (X)

**"Power input pin not driven"**
- Solution: Ensure GND symbols are properly connected

**"Pin to pin warning"**
- Solution: Normal for screw terminals, can be ignored

**"Different unit footprints"**
- Solution: Ensure all instances of multi-unit symbols use same footprint

### Symbol Selection

Use standard KiCAD libraries:

- **Capacitors**: Device:C (unpolarized)
- **Resistors**: Device:R
- **Inductors**: Device:L
- **Screw Terminals 2-pos**: Connector:Screw_Terminal_01x02
- **Screw Terminals 3-pos**: Connector:Screw_Terminal_01x03
- **Screw Terminals 6-pos**: Connector:Screw_Terminal_01x06
- **Ground**: power:GND

### Footprint Assignments

**Phoenix Contact Screw Terminals** (use Phoenix footprint library):
- 2-position: `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.00mm_Horizontal`
- 3-position: `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-3_1x03_P5.00mm_Horizontal`
- 6-position: `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-6_1x06_P5.00mm_Horizontal`

**Film Capacitors**:
- `Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm`

**Resistors**:
- `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm`

**Inductors** (placeholder, external components):
- `Inductor_THT:L_Axial_L5.0mm_D3.6mm_P10.00mm` (or similar)

---

## Quality Checklist

Before finalizing each schematic:

- [ ] All components have unique references
- [ ] All components have correct values
- [ ] All components have footprint assignments
- [ ] All components have MPN in custom field
- [ ] All pins are connected or marked No Connect
- [ ] Net labels are clear and descriptive
- [ ] Title block is complete
- [ ] ERC runs with zero errors
- [ ] Warnings are reviewed and acceptable
- [ ] PDF schematic exported to module directory
- [ ] Netlist generated for PCB layout

---

## Next Steps

After completing schematics:

1. **Create PCB Layouts**: Import netlists into PCB editor
2. **Component Placement**: Follow layout suggestions above
3. **Routing**: Route traces with appropriate widths
4. **Design Rules Check**: Run DRC and resolve all issues
5. **Generate Gerbers**: Create manufacturing files
6. **Create Assembly Drawings**: For board assembly

---

## References

- Original schematic: `src/schematics/pultec-three-band-eq/pultec-three-band-eq.kicad_sch`
- Component values: `src/pultec/docs/1.0/COMPONENT_VALUES.md`
- Module READMEs: `src/pultec/modules/*/README.md`
- Inductor specs: `src/pultec/docs/1.0/LOW_BOOST_INDUCTOR_SPECIFICATIONS.md`
- KiCAD documentation: https://docs.kicad.org/

---

**End of Schematic Creation Guide**
