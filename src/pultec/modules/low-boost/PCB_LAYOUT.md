# Low Boost Module - PCB Layout Specification

## Board Overview
- **Module**: Low Boost (Frequency-selective boost, 20Hz-100Hz with inductors)
- **Complexity**: Complex (11 capacitors, 1 resistor, 9 screw terminals, 4 inductor connections)
- **Estimated Size**: 100mm × 120mm (large, to accommodate all terminals)
- **Layer Count**: 2-layer through-hole PCB
- **Board Thickness**: 1.6mm

## Board Dimensions and Mounting
- **Board Size**: 100mm × 120mm
- **Mounting Holes**: 4× M3 holes at corners
  - Position: 3mm from edges (94mm × 114mm spacing)
  - Hole diameter: 3.2mm
  - Pad diameter: 6mm
  - Keep-out zone: 8mm diameter around each hole

## Component Count Summary
- **Capacitors**: 11 (C1, C2, C3, C4, C5, C4a2, C5a2, C6, C7, C34, C35)
- **Resistors**: 1 (R2, 56kΩ)
- **Screw Terminals**: 9 total
  - 5× 2-position (J_IN, J_OUT, J_GND, 4× inductor connections)
  - 2× 3-position (J_CUT_SEL_SND, J_BOOST_LVL)
  - 2× 6-position (J_BOOST_SEL_SND, J_BOOST_SEL_RET)

## Terminal Placement (All on Board Edges)

### Left Edge (Signal I/O)
- **J_IN** (2-pos): Input signal
  - Position: 15mm from top edge
  - Labels: "IN+", "IN-"
  - Trace width from pad: 0.8mm

### Right Edge (Signal I/O)
- **J_OUT** (2-pos): Output signal
  - Position: 15mm from top edge
  - Labels: "OUT+", "OUT-"
  - Trace width from pad: 0.8mm

### Top Edge (Controls)
- **J_BOOST_SEL_SND** (6-pos): Frequency selector send
  - Position: 20mm from left edge
  - Labels: "SEL_SND1" through "SEL_SND6"
  - Phoenix 1757025 footprint (30.48mm width)

- **J_BOOST_SEL_RET** (6-pos): Frequency selector return
  - Position: 55mm from left edge
  - Labels: "SEL_RET1" through "SEL_RET6"

### Bottom Edge (Controls & Inductor Connections)
- **J_CUT_SEL_SND** (3-pos): Cut selector send (interface)
  - Position: 10mm from left edge
  - Labels: "CUT_SND1", "CUT_SND2", "CUT_SND3"

- **J_BOOST_LVL** (3-pos): Boost level control
  - Position: 30mm from left edge
  - Labels: "LVL1", "LVL2", "LVL3"

- **J_GND** (2-pos): Ground connection
  - Position: 50mm from left edge
  - Labels: "GND", "GND"

### Right Edge (Inductor Connections)
All 2-position terminals, stacked vertically with 15mm spacing:

- **J_IND_20HZ** (2-pos): 20Hz inductor
  - Position: 30mm from top
  - Labels: "20Hz_L1", "20Hz_L2"

- **J_IND_30HZ** (2-pos): 30Hz inductor
  - Position: 50mm from top
  - Labels: "30Hz_L1", "30Hz_L2"

- **J_IND_60HZ** (2-pos): 60Hz inductor
  - Position: 70mm from top
  - Labels: "60Hz_L1", "60Hz_L2"

- **J_IND_100HZ** (2-pos): 100Hz inductor
  - Position: 90mm from top
  - Labels: "100Hz_L1", "100Hz_L2"

## Component Placement Strategy

### Capacitor Placement (Center Area)
Group capacitors by function and value:

#### Selector Network Capacitors (Upper Center)
- **C1** (18nF): 30mm, 30mm
- **C2** (10nF): 40mm, 30mm
- **C3** (4.7nF): 50mm, 30mm
- **C4** (3.3nF): 60mm, 30mm
- **C5** (2.2nF): 70mm, 30mm

#### Alternate Position Capacitors (Middle Center)
- **C4a2** (1nF): 60mm, 50mm
- **C5a2** (1.5nF): 70mm, 50mm

#### Additional Selector Capacitors (Lower Center)
- **C6** (1.8nF): 30mm, 70mm
- **C7** (1nF): 40mm, 70mm

#### Coupling Capacitors (Near Terminals)
- **C34** (1nF): 20mm, 90mm (near J_IN)
- **C35** (1nF): 80mm, 90mm (near J_OUT)

### Resistor Placement
- **R2** (56kΩ): 50mm, 90mm (center bottom, near coupling caps)
- **Orientation**: Horizontal, parallel to bottom edge
- **Footprint**: Through-hole, 0.4" spacing (10.16mm)

### Layout Rationale
1. **Signal flow**: Left to right (IN → network → OUT)
2. **Frequency progression**: Capacitors arranged by frequency (left to right, high to low)
3. **Inductor grouping**: All inductor terminals on right edge for easy external connection
4. **Symmetric placement**: Balanced component distribution
5. **Short traces**: Critical signal paths minimized
6. **Test access**: Space between components for probing

## Grounding Strategy

### Ground Plane Approach
- **Top layer**: Signal routing, component pads, minimal ground traces
- **Bottom layer**: Solid ground plane with strategic cutouts for signal vias
- **Ground connections**: Star ground point at board center (50mm, 60mm)
- **Via placement**: Via arrays at each ground terminal (4× vias minimum)
- **Ground plane splits**: None (continuous plane for low impedance)

### Star Ground Implementation
1. **Star point location**: Center of board, equidistant from all terminals
2. **Ground routing**:
   - J_IN ground → star point via heavy trace (2mm width)
   - J_OUT ground → star point via heavy trace (2mm width)
   - J_GND terminals → star point via multiple vias (direct)
   - Capacitor grounds → local vias to ground plane
   - Inductor terminals → via stitching to ground plane (4× vias per terminal)

### Ground Plane Stitching
- **Via stitching**: Every 20mm around perimeter
- **Via size**: 0.8mm drill, 1.3mm pad
- **Purpose**: Minimize ground plane impedance, improve shielding

## Trace Routing

### Signal Traces (Top Layer)
- **Width**: 0.8mm for audio signals
- **Clearance**: 0.5mm minimum (use 0.8mm where possible)
- **Via size**: 0.8mm drill, 1.3mm pad
- **Routing style**: 45° angles or smooth curves (no 90° corners)

### Critical Signal Paths
1. **Input path**: J_IN+ → C34 → frequency selector network
2. **Selector network**: C1-C7 interconnections via J_BOOST_SEL_SND/RET
3. **Inductor connections**: Selector network → J_IND_20HZ/30HZ/60HZ/100HZ → return to network
4. **Level control**: Network → J_BOOST_LVL → R2
5. **Output path**: R2 → C35 → J_OUT+

### Trace Width Guidelines
- **Audio signals**: 0.8mm
- **Control lines**: 0.6mm
- **Ground traces** (top layer): 2.0mm minimum
- **Power/high current**: 1.5mm (not applicable for this passive circuit)

### Via Strategy
- Minimize vias in signal path (keep routing on top layer)
- Use vias only for ground connections to bottom plane
- Via arrays (4× vias) for low-impedance ground connections
- Avoid vias under capacitor pads (use thermal relief if necessary)

## Layer Stackup

### Top Layer (Component Side)
- All component footprints
- Signal routing traces
- Control routing traces
- Screw terminal pads
- Silkscreen labels and component designators
- Test points at critical nodes

### Bottom Layer (Solder Side)
- Solid ground plane (maximum copper pour)
- Strategic cutouts for signal vias (if needed)
- Via stitching around perimeter
- Silkscreen: Board ID, revision, inductor connection diagram
- Mounting hole keep-outs

## Silkscreen Labels

### Component Labels (White on Green)
- **Capacitors**: Designators (C1-C7, C4a2, C5a2, C34, C35) above components
- **Values**: Actual values below designators (e.g., "18nF", "10nF")
- **R2**: "R2" above, "56K" below
- **Polarity**: Not applicable (non-polarized components)

### Terminal Labels (Large, Bold Font, 1.2mm height)
- **J_IN**: "INPUT", with "+" and "-" at each position
- **J_OUT**: "OUTPUT", with "+" and "-" at each position
- **J_BOOST_SEL_SND**: "BOOST SEL SEND", positions "1" through "6"
- **J_BOOST_SEL_RET**: "BOOST SEL RETURN", positions "1" through "6"
- **J_CUT_SEL_SND**: "CUT SEL SEND", positions "1" through "3"
- **J_BOOST_LVL**: "BOOST LEVEL", positions "1", "2", "3"
- **J_GND**: "GROUND"
- **J_IND_20HZ**: "20Hz INDUCTOR", "L1", "L2"
- **J_IND_30HZ**: "30Hz INDUCTOR", "L1", "L2"
- **J_IND_60HZ**: "60Hz INDUCTOR", "L1", "L2"
- **J_IND_100HZ**: "100Hz INDUCTOR", "L1", "L2"

### Board Information (Bottom Silkscreen)
- "PULTEC LOW BOOST MODULE"
- "Rev 1.0"
- Date code: "2025"
- "Requires 4× hand-wound inductors"
- Inductor connection diagram showing frequency assignments

### Functional Diagram (Bottom Silkscreen)
Simple block diagram showing:
- Signal flow: IN → Selector → Inductors → Level → OUT
- Inductor frequency assignments
- Control connections to front panel

## Test Point Locations

### Critical Test Points (1.2mm diameter pads, via-in-pad)
- **TP1**: J_IN+ (input signal)
  - Position: 15mm, 20mm
  - Label: "TP1_IN"

- **TP2**: After C34 (post-coupling)
  - Position: 25mm, 90mm
  - Label: "TP2_COUP"

- **TP3**: Selector network node
  - Position: 50mm, 40mm
  - Label: "TP3_SEL"

- **TP4**: After R2 (pre-output coupling)
  - Position: 60mm, 90mm
  - Label: "TP4_R2"

- **TP5**: J_OUT+ (output signal)
  - Position: 85mm, 20mm
  - Label: "TP5_OUT"

- **TP_GND**: Ground reference
  - Position: 50mm, 60mm (star point)
  - Label: "TP_GND"

## Design Rules

### Electrical
- **Minimum trace width**: 0.25mm (use 0.6mm minimum for signals)
- **Minimum clearance**: 0.25mm (use 0.5mm for safety)
- **Via drill**: 0.8mm
- **Via pad**: 1.3mm diameter
- **Via clearance**: 0.3mm
- **Ground plane clearance**: 0.3mm (thermal relief for pads)

### Mechanical
- **Board edge to component**: 8mm minimum
- **Board edge to mounting hole**: 3mm
- **Terminal to board edge**: 2mm (aligned flush)
- **Component spacing**: 8mm minimum (10mm preferred)
- **Capacitor spacing**: 10mm center-to-center (allows test probe access)

### Thermal
- **Thermal relief**: 4 spokes, 0.5mm width for ground pads
- **Heat dissipation**: Minimal (no power components, passive circuit)
- **Copper weight**: 1 oz sufficient

## Manufacturing Specifications

### PCB Fabrication
- **Base material**: FR-4, Tg 140°C minimum
- **Copper weight**: 1 oz (35μm) both layers
- **Surface finish**: ENIG preferred for long-term reliability (HASL acceptable)
- **Solder mask**: Green LPI, both sides
- **Silkscreen**: White epoxy ink, both sides
- **Board outline**: Routed with 2mm radius corners
- **E-test**: Required (100% continuity and isolation)

### Tolerances
- **Board dimensions**: ±0.2mm
- **Hole positions**: ±0.1mm
- **Hole diameter**: +0.1mm / -0.0mm
- **Trace width**: ±10%
- **Registration** (layer to layer): ±0.15mm

## Assembly Notes

### Assembly Sequence
1. **Install screw terminals first** (9 total)
   - Orientation: Wire entry facing outward
   - Sequence: J_IN, J_OUT, J_GND, inductor terminals, control terminals
   - Soldering: Reflow all pins, inspect for cold joints and bridges

2. **Install resistor R2**
   - Orientation: Value marking readable from top
   - Lead forming: Straight through-hole, trim leads after soldering
   - Inspection: Verify 56kΩ value with DMM

3. **Install capacitors** (11 total)
   - Sequence: Large values first (C1-C7), then smaller (C4a2, C5a2), then coupling (C34, C35)
   - Orientation: Value markings facing top of board
   - Lead spacing: 5.08mm per MKT1813 footprint
   - Height: Seated flush against PCB
   - Inspection: Visual check for proper seating and solder joints

4. **Final inspection**
   - Visual: All solder joints, no bridges
   - Continuity: Verify signal paths with DMM
   - Isolation: Verify no shorts to ground
   - Capacitance: Spot-check critical capacitor values

### Component Orientation Notes
- **Screw terminals**: All wire entries face outward (away from board center)
- **Capacitors**: Value markings face up for easy identification
- **Resistor**: Color bands or value marking readable from top
- **Inductor terminals**: Clearly labeled with frequency on silkscreen

## Critical Routing Notes

### Audio Signal Integrity
1. **Minimize trace lengths**: Especially in high-impedance nodes
2. **Star grounding**: All grounds meet at single point (50mm, 60mm)
3. **Ground plane integrity**: Solid plane, no splits, minimal cutouts
4. **Shielding**: Ground plane provides shielding between layers
5. **Symmetry**: Balanced routing to maintain phase coherence

### Inductor Connections
1. **Low DCR traces**: Wide traces (1.0mm) to inductor terminals to minimize series resistance
2. **Via stitching**: Multiple vias at inductor ground terminals for low impedance
3. **Electromagnetic compatibility**: Inductors are external; PCB provides connection only
4. **Clear labeling**: Each inductor terminal clearly marked with frequency

### Noise Minimization
1. **Ground plane**: Maximum copper pour on bottom layer
2. **Via stitching**: Perimeter vias every 20mm to lower ground impedance
3. **No loops**: Avoid creating ground loops in routing
4. **Separation**: Adequate spacing between signal traces (0.8mm minimum)

## Recommended Clearances

### Terminal Clearances (for Wiring Access)
- **Side clearance**: 20mm around terminals for screwdriver access
- **Top clearance**: 50mm above board for wire routing, bending, and stripping
- **Between terminals**: 15mm minimum for wire separation and strain relief
- **Inductor terminal access**: 25mm clearance for larger inductor leads

### Mounting Clearances
- **Standoff height**: 12mm recommended (accommodate solder joints and wire routing)
- **Bottom clearance**: 10mm for component leads and traces
- **Enclosure clearance**: 25mm minimum all sides for ventilation and wiring
- **Adjacent boards**: 30mm spacing if stacking or mounting side-by-side

## Inductor Integration Notes

### External Inductor Specifications
This module requires **4 hand-wound inductors**:
- **20Hz**: ~100-200mH (large, laminated or powdered iron core)
- **30Hz**: ~60-100mH
- **60Hz**: ~20-40mH
- **100Hz**: ~10-20mH

### PCB Terminal Design for Inductors
- **Terminal type**: Phoenix Contact 1757019 (2-position, 5.08mm pitch)
- **Wire gauge capacity**: 12-24 AWG (inductor lead wire)
- **Connection**: Screw terminals allow easy inductor swapping for tuning
- **Labeling**: Large, clear frequency labels on both silkscreen layers

### Inductor Connection Guidelines
1. Each inductor connects between:
   - Terminal position 1: To selector network
   - Terminal position 2: Return to network
2. Inductor polarity: Not critical for these applications
3. Secure mounting: Inductors should be mechanically secured (not hanging on wires)
4. Lead dress: Keep inductor leads short to minimize parasitic inductance

## Design Validation Checklist

- [ ] All mounting holes placed correctly (3mm from edges)
- [ ] All terminals on board edges for accessibility
- [ ] Signal flow is logical (left to right: IN → OUT)
- [ ] Ground plane is solid and continuous on bottom layer
- [ ] Star ground point implemented at board center
- [ ] All components have correct footprints (5.08mm pitch for capacitors)
- [ ] Inductor terminals clearly labeled with frequencies
- [ ] Silkscreen labels are clear and readable (1.2mm minimum height)
- [ ] Test points placed at critical signal nodes
- [ ] No acute angle traces (all 45° or curves)
- [ ] Via stitching around perimeter (every 20mm)
- [ ] DRC passes with no errors (clearance, width, annular ring)
- [ ] Board dimensions optimized (100mm × 120mm)
- [ ] Capacitor spacing allows test probe access (10mm minimum)

## Output Files Required

### Gerber Files (RS-274X format)
- **GTL**: Top copper layer
- **GBL**: Bottom copper layer (ground plane)
- **GTO**: Top silkscreen overlay
- **GBO**: Bottom silkscreen overlay
- **GTS**: Top solder mask
- **GBS**: Bottom solder mask
- **GM1**: Board outline / mechanical layer
- **GKO**: Keep-out layer

### Drill Files
- **Excellon format**: Plated through-holes
- **Tool list**: With sizes and quantities
- **Drill map**: PDF showing hole locations and sizes

### Additional Files
- **Assembly drawing** (PDF): Top view with component positions and values
- **Component placement file** (CSV): Ref, X, Y, Rotation, Layer, Value
- **BOM correlation**: Match PCB designators to BOM line items
- **Fabrication drawing**: Board dimensions, tolerances, stackup, notes
- **IPC-D-356 netlist**: For automated testing (optional but recommended)

## Special Considerations

### Inductor Design Dependencies
- PCB layout is complete and independent of inductor values
- Inductor terminals provide flexible connection for any inductor design
- Inductors must be designed by inductor-design-specialist based on capacitor values
- Test points allow verification of LC resonance frequencies

### Modular Integration
- This module receives signal from Low Cut module
- This module sends signal to High Boost module
- Control terminals connect to front panel rotary switch and potentiometer
- Ground terminal connects to system ground bus

### Testability
- Multiple test points for signal tracing
- Component spacing allows in-circuit testing
- Screw terminals allow easy disconnection for module-level testing
- Clear labeling facilitates troubleshooting

## Revision History
- **v1.0** (2025-10-26): Initial PCB layout specification

## Notes
- This is the most complex module due to 11 capacitors and 4 inductor connections
- Board size (100mm × 120mm) optimized for component density and terminal access
- Ground plane critical for low-noise operation with inductors
- All terminals on edges allow easy modular interconnection
- Inductor terminals enable flexible testing and tuning of hand-wound components
- Test points essential for verifying frequency response with external inductors
