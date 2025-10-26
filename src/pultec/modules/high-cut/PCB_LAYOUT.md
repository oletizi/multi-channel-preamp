# High Cut Module - PCB Layout Specification

## Board Overview
- **Module**: High Cut (Frequency-selective attenuation, 5kHz-20kHz)
- **Complexity**: Moderate (11 capacitors, 1 resistor, 6 screw terminals)
- **Estimated Size**: 90mm × 100mm (medium size)
- **Layer Count**: 2-layer through-hole PCB
- **Board Thickness**: 1.6mm

## Board Dimensions and Mounting
- **Board Size**: 90mm × 100mm
- **Mounting Holes**: 4× M3 holes at corners
  - Position: 3mm from edges (84mm × 94mm spacing)
  - Hole diameter: 3.2mm
  - Pad diameter: 6mm
  - Keep-out zone: 8mm diameter around each hole

## Component Count Summary
- **Capacitors**: 11 (C18, C19, C20, C21, C22, C25, C26, C27, C28, C30, C31)
  - Range: 10nF to 330nF
  - Three duplicate values (C22, C25, C26 all 47nF; C27, C28 both 22nF)
- **Resistors**: 1 (R1, 430Ω)
- **Screw Terminals**: 6 total
  - 3× 2-position (J_IN, J_OUT, J_GND)
  - 2× 6-position (J_CUT_SEL_SND, J_CUT_SEL_RET)
  - 1× 3-position (J_CUT_LVL)

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

### Top Edge (Frequency Selector)
- **J_CUT_SEL_SND** (6-pos): Frequency selector send
  - Position: 15mm from left edge
  - Labels: "SEL_SND1" through "SEL_SND6"
  - Phoenix 1757025 footprint (30.48mm width)

- **J_CUT_SEL_RET** (6-pos): Frequency selector return
  - Position: 50mm from left edge
  - Labels: "SEL_RET1" through "SEL_RET6"

### Bottom Edge (Controls and Ground)
- **J_CUT_LVL** (3-pos): Cut level control
  - Position: 20mm from left edge
  - Labels: "LVL1", "LVL2", "LVL3"

- **J_GND** (2-pos): Ground connection
  - Position: 50mm from left edge
  - Labels: "GND", "GND"

## Component Placement Strategy

### Capacitor Placement (Center Area)
Organize capacitors by value and function:

#### Large Value Capacitors (Upper Left)
- **C18** (330nF): 20mm, 30mm (largest value)
- **C19** (220nF): 30mm, 30mm
- **C20** (120nF): 40mm, 30mm

#### Medium Value Capacitors (Upper Right)
- **C21** (68nF): 50mm, 30mm
- **C22** (47nF): 60mm, 30mm
- **C25** (47nF): 70mm, 30mm

#### Duplicate Value Group (Middle)
- **C26** (47nF): 30mm, 50mm
- **C27** (22nF): 40mm, 50mm
- **C28** (22nF): 50mm, 50mm

#### Smaller Value Capacitors (Lower)
- **C30** (33nF): 30mm, 70mm
- **C31** (10nF): 40mm, 70mm (smallest value)

### Resistor Placement
- **R1** (430Ω): 60mm, 70mm (attenuation pad resistor)
- **Orientation**: Horizontal, parallel to bottom edge
- **Footprint**: Through-hole, 0.4" spacing (10.16mm)
- **Critical component**: Provides loading for frequency-selective network

### Layout Rationale
1. **Signal flow**: Left to right (IN → capacitor network → R1 → OUT)
2. **Value progression**: Capacitors arranged by descending value (visual organization)
3. **Functional grouping**: Duplicate values (47nF, 22nF) grouped together
4. **Selector access**: All capacitors routed to top edge selector terminals
5. **Short traces**: Minimize signal path lengths, especially to R1
6. **Symmetric placement**: Balanced component distribution
7. **Test access**: Adequate spacing (10mm) between components for probing

## Grounding Strategy

### Ground Plane Approach
- **Top layer**: Signal routing, component pads, minimal ground traces
- **Bottom layer**: Solid ground plane (maximum copper pour)
- **Ground connections**: Star ground point at board center (45mm, 50mm)
- **Via placement**: Via arrays (4× vias minimum) at each ground terminal
- **Ground plane integrity**: Continuous plane, no splits

### Star Ground Implementation
1. **Star point location**: Board center (45mm, 50mm)
2. **Ground routing**:
   - J_IN ground → star point via 2.0mm trace
   - J_OUT ground → star point via 2.0mm trace
   - J_GND terminals → star point via via array
   - All capacitor grounds → local vias to ground plane
   - R1 ground connection → via to ground plane

### Ground Plane Stitching
- **Via stitching frequency**: Every 20mm around perimeter
- **Interior stitching**: 30mm × 30mm grid in open areas
- **Via size**: 0.8mm drill, 1.3mm pad
- **Purpose**: Low ground impedance, effective shielding

## Trace Routing

### Signal Traces (Top Layer)
- **Width**: 0.8mm for audio signals
- **Clearance**: 0.5mm minimum (use 0.8mm where space permits)
- **Via size**: 0.8mm drill, 1.3mm pad
- **Routing style**: 45° angles or smooth curves (no 90° corners)

### Critical Signal Paths
1. **Input path**: J_IN+ → capacitor selector network
2. **Selector network**: C18-C31 interconnections via J_CUT_SEL_SND/RET
3. **Attenuation path**: Selector network → R1 (critical low-resistance path)
4. **Output path**: R1 → J_OUT+

### Trace Width Guidelines
- **Audio signals**: 0.8mm
- **Control lines**: 0.6mm
- **Ground traces** (top layer): 2.0mm minimum
- **R1 connections**: 1.0mm (minimize series resistance)

### Via Strategy
- Minimize vias in signal path (route on top layer)
- Use vias only for ground connections to bottom plane
- Via arrays (4× vias) for low-impedance ground connections
- Thermal relief for ground vias (4 spokes, 0.5mm width)
- No vias under component pads

## Layer Stackup

### Top Layer (Component Side)
- All component footprints
- Signal routing traces (primary routing layer)
- Control routing traces
- Screw terminal pads
- Silkscreen labels and component designators
- Test points at critical nodes

### Bottom Layer (Solder Side)
- Solid ground plane (maximum copper pour, 95%+ coverage)
- Strategic cutouts only for non-plated holes
- Via stitching grid (20mm perimeter, 30mm interior)
- Silkscreen: Board ID, revision, frequency response curve
- Mounting hole keep-outs

## Silkscreen Labels

### Component Labels (White on Green, 0.8mm height)
- **Capacitors**: Designators (C18-C31) above components
- **Values**: Actual values below designators (e.g., "330nF", "220nF", "47nF")
- **R1**: "R1" above, "430R" below
- **Polarity**: Not applicable (all non-polarized)

### Terminal Labels (Large, Bold Font, 1.2mm height)
- **J_IN**: "INPUT", with "+" and "-" at positions
- **J_OUT**: "OUTPUT", with "+" and "-" at positions
- **J_CUT_SEL_SND**: "CUT SEL SEND", positions "1" through "6"
- **J_CUT_SEL_RET**: "CUT SEL RETURN", positions "1" through "6"
- **J_CUT_LVL**: "CUT LEVEL", positions "1", "2", "3"
- **J_GND**: "GROUND"

### Board Information (Bottom Silkscreen)
- "PULTEC HIGH CUT MODULE"
- "Rev 1.0"
- Date code: "2025"
- "Frequency-selective HF attenuation: 5kHz, 10kHz, 20kHz"

### Functional Diagram (Bottom Silkscreen)
Simple block diagram showing:
- Signal flow: IN → Selector → R1 Pad → OUT
- Frequency selector positions
- Typical frequency response curves

## Test Point Locations

### Critical Test Points (1.2mm diameter pads)
- **TP1**: J_IN+ (input signal monitoring)
  - Position: 20mm, 20mm
  - Label: "TP1_IN"

- **TP2**: Selector network node (after frequency selection)
  - Position: 45mm, 40mm
  - Label: "TP2_SEL"

- **TP3**: Before R1 (pre-attenuation pad)
  - Position: 55mm, 65mm
  - Label: "TP3_R1_IN"

- **TP4**: After R1 (post-attenuation pad)
  - Position: 65mm, 65mm
  - Label: "TP4_R1_OUT"

- **TP5**: J_OUT+ (output signal monitoring)
  - Position: 70mm, 20mm
  - Label: "TP5_OUT"

- **TP_GND**: Ground reference (star point)
  - Position: 45mm, 50mm
  - Label: "TP_GND"

## Design Rules

### Electrical
- **Minimum trace width**: 0.25mm (use 0.6mm minimum for signals)
- **Minimum clearance**: 0.25mm (use 0.5mm for reliability)
- **Via drill**: 0.8mm
- **Via pad**: 1.3mm diameter
- **Via annular ring**: 0.25mm minimum
- **Via clearance**: 0.3mm
- **Ground plane clearance**: 0.3mm (with thermal relief)

### Mechanical
- **Board edge to component**: 8mm minimum
- **Board edge to mounting hole**: 3mm
- **Terminal to board edge**: 2mm (flush mounted)
- **Component spacing**: 10mm minimum
- **Capacitor spacing**: 10mm center-to-center (test probe access)

### Thermal
- **Thermal relief**: 4 spokes, 0.5mm width for ground pads
- **Heat dissipation**: Minimal (passive circuit, no power dissipation)
- **Copper weight**: 1 oz adequate

## Manufacturing Specifications

### PCB Fabrication
- **Base material**: FR-4, Tg 140°C minimum
- **Copper weight**: 1 oz (35μm) both layers
- **Surface finish**: HASL (lead-free) or ENIG
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
1. **Install screw terminals first** (6 total)
   - Sequence: J_IN, J_OUT, J_GND, J_CUT_SEL_SND, J_CUT_SEL_RET, J_CUT_LVL
   - Orientation: All wire entries face outward
   - Soldering: Reflow all pins, inspect for cold joints
   - Verification: Gently tug to ensure mechanical integrity

2. **Install resistor R1** (430Ω, critical component)
   - Orientation: Value marking readable from top
   - Lead forming: 0.4" (10.16mm) spacing
   - Insertion: Fully seated against PCB
   - Soldering: Both leads, good fillets
   - Verification: Measure resistance (425-435Ω expected for 1% tolerance)

3. **Install capacitors** (11 total)
   - Sequence: Largest first (C18 330nF), then descending by value
   - Orientation: Value markings facing top of board
   - Lead spacing: 5.08mm per Vishay MKT1813 footprint
   - Lead forming: Straight insertion, no bending
   - Seating: Flush against PCB
   - Soldering: Both leads, inspect fillets
   - Trimming: Trim excess leads flush

4. **Final inspection and testing**
   - Visual: All solder joints under 10× magnification
   - Continuity: Verify signal paths with DMM
   - Isolation: Verify no shorts (>10MΩ)
   - Component values: Spot-check with LCR meter
   - R1 verification: Critical component, verify 430Ω ±1%

### Component Orientation Notes
- **Screw terminals**: Wire entries face outward
- **Capacitors**: Value markings face up for easy identification
- **R1**: Value marking readable from top (critical for troubleshooting)
- **Polarity**: Not applicable (all non-polarized)

## Critical Routing Notes

### Audio Signal Integrity
1. **Minimize trace lengths**: Especially in high-impedance nodes before R1
2. **Star grounding**: Single-point ground at board center
3. **Ground plane integrity**: Solid plane on bottom layer
4. **No ground loops**: All returns via ground plane
5. **Shielding**: Ground plane provides inter-layer shielding

### R1 Attenuation Pad (Critical Component)
1. **Low-resistance connections**: Wide traces (1.0mm) to R1 minimize added series resistance
2. **Short connections**: Direct routing from selector network to R1
3. **Thermal considerations**: R1 dissipates minimal power, but use thermal relief on ground pad
4. **Value criticality**: 430Ω value is critical for proper network operation
5. **Test points**: TP3 and TP4 allow verification of attenuation

### Capacitor Network
1. **Parallel connections**: Some capacitors may be used in parallel (C22/C25/C26 all 47nF)
2. **Series connections**: Some capacitors may be used in series (C27/C28 both 22nF)
3. **Selector routing**: All capacitors route to top edge selector terminals
4. **Low loss**: Film capacitors (Vishay MKT1813) ensure low ESR and high Q

### Noise Minimization
1. **Ground plane**: Maximum copper pour on bottom layer (95%+ coverage)
2. **Via stitching**: 20mm perimeter, 30mm interior for low ground impedance
3. **No ground loops**: All ground returns via ground plane
4. **Trace separation**: 0.8mm minimum between signal traces

## Recommended Clearances

### Terminal Clearances (for Wiring Access)
- **Side clearance**: 20mm around terminals for screwdriver access
- **Top clearance**: 50mm above board for wire routing and stripping
- **Between terminals**: 15mm minimum for wire separation
- **Control terminal access**: 25mm for level control wiring

### Mounting Clearances
- **Standoff height**: 12mm recommended (accommodate solder joints and wiring)
- **Bottom clearance**: 10mm for component leads and bottom vias
- **Enclosure clearance**: 25mm minimum all sides for ventilation and wiring
- **Adjacent boards**: 30mm spacing if stacking or side-by-side mounting

## Design Validation Checklist

- [ ] All mounting holes placed correctly (3mm from edges)
- [ ] All terminals on board edges for accessibility
- [ ] Signal flow is logical (left to right: IN → network → R1 → OUT)
- [ ] Ground plane is solid and continuous (95%+ coverage)
- [ ] Star ground point implemented at board center (45mm, 50mm)
- [ ] All components have correct footprints (5.08mm pitch for capacitors)
- [ ] R1 (430Ω) placement optimized for low series resistance
- [ ] Silkscreen labels are clear and readable (1.2mm minimum height)
- [ ] Test points placed at critical signal nodes (6 test points total)
- [ ] No acute angle traces (all 45° or smooth curves)
- [ ] Via stitching implemented (20mm perimeter, 30mm interior)
- [ ] DRC passes with no errors (clearance, width, annular ring)
- [ ] Board dimensions optimized (90mm × 100mm)
- [ ] Capacitor spacing allows test probe access (10mm minimum)
- [ ] Duplicate value capacitors properly identified (C22/C25/C26, C27/C28)

## Output Files Required

### Gerber Files (RS-274X format)
- **GTL**: Top copper layer
- **GBL**: Bottom copper layer (solid ground plane)
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
- **BOM correlation**: Cross-reference PCB designators to BOM line items
- **Fabrication drawing**: Board dimensions, layer stackup, tolerances, notes
- **IPC-D-356 netlist**: For automated testing (optional)

## Special Considerations

### R1 Attenuation Pad Resistor
- **Critical value**: 430Ω ±1% is essential for proper frequency-selective attenuation
- **Power rating**: 1/4W sufficient (passive network, minimal power)
- **Tolerance**: 1% metal film required (not 5% carbon film)
- **Verification**: Test in-circuit after assembly
- **Replacement**: Use exact replacement (Vishay MRS25 or equivalent)

### Multiple Capacitors with Same Value
This design uses multiple capacitors with identical values:
- **Three 47nF capacitors** (C22, C25, C26): May be in parallel or series network
- **Two 22nF capacitors** (C27, C28): May be in parallel or series network

This is intentional for the frequency-selective network. The schematic determines the exact configuration.

### Modular Integration
- This module receives signal from High Boost module (via J_IN)
- This module sends signal to Output Stage (via J_OUT)
- Control terminals connect to front panel:
  - Rotary switch (frequency selector, 6+ positions)
  - Cut level potentiometer (J_CUT_LVL)
- Ground terminal connects to system ground bus

### Testability
- 6 test points cover all critical signal nodes
- Test points TP3 and TP4 bracket R1 for attenuation verification
- Component spacing allows in-circuit testing
- Screw terminals allow easy disconnection for module-level testing
- Clear labeling facilitates troubleshooting

### High-Frequency Attenuation
- This module operates at audio frequencies (5-20kHz)
- Capacitor network provides frequency-selective attenuation
- R1 provides resistive loading for the network
- Ground plane ensures low-noise operation
- Film capacitors (MKT1813) provide low ESR and high Q

## Revision History
- **v1.0** (2025-10-26): Initial PCB layout specification

## Notes
- This is a moderately complex module (11 capacitors, 1 critical resistor)
- Board size (90mm × 100mm) optimized for component count and terminal access
- Ground plane critical for low-noise operation
- All terminals on edges enable easy modular interconnection
- R1 (430Ω) is the most critical component for proper attenuation
- Multiple test points essential for verifying frequency-selective attenuation
- Capacitor network uses some duplicate values (intentional for circuit topology)
- Passive RC network provides high-frequency attenuation complementary to High Boost module
