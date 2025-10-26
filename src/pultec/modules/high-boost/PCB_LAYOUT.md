# High Boost Module - PCB Layout Specification

## Board Overview
- **Module**: High Boost (Frequency-selective boost, 3kHz-16kHz with inductors and Q control)
- **Complexity**: Very Complex (8 capacitors, 1 resistor, 10 screw terminals, 7 inductor connections)
- **Estimated Size**: 120mm × 140mm (largest module due to 7 inductors)
- **Layer Count**: 2-layer through-hole PCB
- **Board Thickness**: 1.6mm

## Board Dimensions and Mounting
- **Board Size**: 120mm × 140mm
- **Mounting Holes**: 4× M3 holes at corners
  - Position: 3mm from edges (114mm × 134mm spacing)
  - Hole diameter: 3.2mm
  - Pad diameter: 6mm
  - Keep-out zone: 8mm diameter around each hole

## Component Count Summary
- **Capacitors**: 8 (C14, C15, C16, C17, C2a2, C29, C32, C33)
- **Resistors**: 1 (R3, 4.7kΩ)
- **Screw Terminals**: 10 total
  - 9× 2-position (J_IN, J_OUT, J_GND, 7× inductor connections)
  - 3× 3-position (J_BOOST_LVL, J_BOOST_L_SND, J_BOOST_Q)
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

### Top Edge (Frequency Selector)
- **J_BOOST_SEL_SND** (6-pos): Frequency selector send
  - Position: 15mm from left edge
  - Labels: "SEL_SND1" through "SEL_SND6"
  - Phoenix 1757025 footprint (30.48mm width)

- **J_BOOST_SEL_RET** (6-pos): Frequency selector return
  - Position: 55mm from left edge
  - Labels: "SEL_RET1" through "SEL_RET6"

### Bottom Edge (Controls and Ground)
- **J_BOOST_LVL** (3-pos): Boost level control
  - Position: 15mm from left edge
  - Labels: "LVL1", "LVL2", "LVL3"

- **J_BOOST_L_SND** (3-pos): Boost level send
  - Position: 35mm from left edge
  - Labels: "L_SND1", "L_SND2", "L_SND3"

- **J_BOOST_Q** (3-pos): Bandwidth (Q) control
  - Position: 55mm from left edge
  - Labels: "Q1", "Q2", "Q3"

- **J_GND** (2-pos): Ground connection
  - Position: 75mm from left edge
  - Labels: "GND", "GND"

### Right Edge (Inductor Connections - 7 terminals)
All 2-position terminals, vertically stacked with 18mm spacing:

- **J_IND_3KHZ** (2-pos): 3kHz inductor
  - Position: 20mm from top
  - Labels: "3kHz_L1", "3kHz_L2"

- **J_IND_4KHZ** (2-pos): 4kHz inductor
  - Position: 38mm from top
  - Labels: "4kHz_L1", "4kHz_L2"

- **J_IND_5KHZ** (2-pos): 5kHz inductor
  - Position: 56mm from top
  - Labels: "5kHz_L1", "5kHz_L2"

- **J_IND_8KHZ** (2-pos): 8kHz inductor
  - Position: 74mm from top
  - Labels: "8kHz_L1", "8kHz_L2"

- **J_IND_10KHZ** (2-pos): 10kHz inductor
  - Position: 92mm from top
  - Labels: "10kHz_L1", "10kHz_L2"

- **J_IND_12KHZ** (2-pos): 12kHz inductor
  - Position: 110mm from top
  - Labels: "12kHz_L1", "12kHz_L2"

- **J_IND_16KHZ** (2-pos): 16kHz inductor
  - Position: 128mm from top
  - Labels: "16kHz_L1", "16kHz_L2"

## Component Placement Strategy

### Capacitor Placement (Center Area)
Arrange capacitors in logical groups:

#### Selector Network Capacitors (Upper Center)
- **C14** (4.7nF): 35mm, 35mm
- **C15** (4.7nF): 45mm, 35mm
- **C16** (3.3nF): 55mm, 35mm
- **C17** (1nF): 65mm, 35mm
- **C2a2** (470pF): 75mm, 35mm

#### Q Network Capacitors (Middle Center)
- **C29** (15nF): 35mm, 60mm
- **C32** (10nF): 50mm, 60mm
- **C33** (2.2nF): 65mm, 60mm

### Resistor Placement
- **R3** (4.7kΩ): 60mm, 85mm (central position)
- **Orientation**: Horizontal, parallel to bottom edge
- **Footprint**: Through-hole, 0.4" spacing (10.16mm)

### Layout Rationale
1. **Signal flow**: Left to right (IN → selector network → inductors → Q network → OUT)
2. **Frequency progression**: Capacitors arranged by descending frequency
3. **Inductor grouping**: All 7 inductor terminals on right edge (vertical stack)
4. **Q network separation**: Q control capacitors grouped separately from selector network
5. **Short critical paths**: Minimize trace lengths in high-impedance nodes
6. **Symmetric layout**: Balanced component distribution for aesthetic and electrical balance
7. **Test access**: Adequate spacing between components for probing

## Grounding Strategy

### Ground Plane Approach
- **Top layer**: Signal routing, component pads, minimal ground traces
- **Bottom layer**: Solid ground plane with strategic cutouts only where necessary
- **Ground connections**: Star ground point at board geometric center (60mm, 70mm)
- **Via placement**: Via arrays (6× vias minimum) at each ground terminal
- **Ground plane integrity**: Continuous plane, no splits, minimal cutouts

### Star Ground Implementation
1. **Star point location**: Center of board (60mm, 70mm)
2. **Ground routing**:
   - J_IN ground → star point via 2.5mm trace
   - J_OUT ground → star point via 2.5mm trace
   - J_GND terminals → star point via via array (direct connection)
   - All capacitor grounds → local vias to ground plane
   - All inductor terminal grounds → via arrays (6× vias per terminal)
   - Control terminal grounds → star point

### Ground Plane Stitching
- **Via stitching frequency**: Every 15mm around perimeter
- **Additional stitching**: Grid pattern in open areas (30mm × 30mm grid)
- **Via size**: 0.8mm drill, 1.3mm pad
- **Purpose**: Minimize ground impedance, maximize shielding effectiveness

## Trace Routing

### Signal Traces (Top Layer)
- **Width**: 0.8mm for audio signals (high impedance nodes)
- **Clearance**: 0.5mm minimum (use 0.8mm where space permits)
- **Via size**: 0.8mm drill, 1.3mm pad
- **Routing style**: 45° angles or smooth curves (no 90° corners)
- **Differential routing**: Not required (single-ended audio)

### Critical Signal Paths
1. **Input path**: J_IN+ → selector network → frequency-dependent capacitors
2. **Selector network**: C14-C17, C2a2 interconnections via J_BOOST_SEL_SND/RET
3. **Inductor connections**: Selector network → 7× inductor terminals → return to network
4. **Q control path**: Network → C29/C32/C33 → J_BOOST_Q
5. **Level control**: Network → J_BOOST_LVL, J_BOOST_L_SND → R3
6. **Output path**: R3 → J_OUT+

### Trace Width Guidelines
- **Audio signals** (high impedance): 0.8mm
- **Control lines**: 0.6mm
- **Ground traces** (top layer): 2.5mm minimum
- **Inductor connections**: 1.0mm (low series resistance critical for Q)

### Via Strategy
- Minimize vias in signal path (route entirely on top layer if possible)
- Use vias only for ground connections to bottom plane
- Via arrays (6× vias) for ultra-low-impedance ground at inductor terminals
- Avoid vias under capacitor or resistor pads
- Thermal relief for ground vias (4 spokes, 0.5mm width)

## Layer Stackup

### Top Layer (Component Side)
- All component footprints
- Signal routing traces (primary layer)
- Control routing traces
- Screw terminal pads
- Silkscreen labels and component designators
- Test points at all critical nodes
- Ground traces where necessary (heavy width)

### Bottom Layer (Solder Side)
- Solid ground plane (maximum copper pour, 98%+ coverage)
- Strategic cutouts only for non-plated holes
- Via stitching grid (15mm perimeter, 30mm interior)
- Silkscreen: Board ID, revision, inductor frequency map
- Mounting hole keep-outs

## Silkscreen Labels

### Component Labels (White on Green, 0.8mm height minimum)
- **Capacitors**: Designators (C14-C17, C2a2, C29, C32, C33) above components
- **Values**: Actual values below designators (e.g., "4.7nF", "470pF", "15nF")
- **R3**: "R3" above, "4K7" below
- **Polarity**: Not applicable (all non-polarized)

### Terminal Labels (Large, Bold Font, 1.5mm height)
- **J_IN**: "INPUT" (header), "+" and "-" at positions
- **J_OUT**: "OUTPUT" (header), "+" and "-" at positions
- **J_BOOST_SEL_SND**: "BOOST SEL SEND", positions "1" through "6"
- **J_BOOST_SEL_RET**: "BOOST SEL RETURN", positions "1" through "6"
- **J_BOOST_LVL**: "BOOST LEVEL", positions "1", "2", "3"
- **J_BOOST_L_SND**: "BOOST L SEND", positions "1", "2", "3"
- **J_BOOST_Q**: "BANDWIDTH Q", positions "1", "2", "3"
- **J_GND**: "GROUND"

### Inductor Terminal Labels (Extra Large, 2.0mm height)
Each inductor terminal clearly marked:
- **J_IND_3KHZ**: "3kHz INDUCTOR", "L1", "L2"
- **J_IND_4KHZ**: "4kHz INDUCTOR", "L1", "L2"
- **J_IND_5KHZ**: "5kHz INDUCTOR", "L1", "L2"
- **J_IND_8KHZ**: "8kHz INDUCTOR", "L1", "L2"
- **J_IND_10KHZ**: "10kHz INDUCTOR", "L1", "L2"
- **J_IND_12KHZ**: "12kHz INDUCTOR", "L1", "L2"
- **J_IND_16KHZ**: "16kHz INDUCTOR", "L1", "L2"

### Board Information (Bottom Silkscreen)
- "PULTEC HIGH BOOST MODULE"
- "Rev 1.0"
- Date code: "2025"
- "Requires 7× hand-wound inductors (3kHz-16kHz)"
- Inductor frequency map showing terminal assignments

### Functional Diagram (Bottom Silkscreen)
Block diagram showing:
- Signal flow: IN → Selector → Inductors → Q Control → Level → OUT
- 7 inductor frequency assignments with visual indicators
- Control connections to front panel (frequency, level, Q)

## Test Point Locations

### Critical Test Points (1.5mm diameter pads, gold plated)
- **TP1**: J_IN+ (input signal monitoring)
  - Position: 20mm, 20mm
  - Label: "TP1_IN"

- **TP2**: Selector network node (after frequency selection)
  - Position: 50mm, 45mm
  - Label: "TP2_SEL"

- **TP3**: After inductor network (inductor output)
  - Position: 100mm, 70mm
  - Label: "TP3_IND"

- **TP4**: Q control network node
  - Position: 50mm, 70mm
  - Label: "TP4_Q"

- **TP5**: After R3 (pre-output)
  - Position: 70mm, 85mm
  - Label: "TP5_R3"

- **TP6**: J_OUT+ (output signal monitoring)
  - Position: 100mm, 20mm
  - Label: "TP6_OUT"

- **TP_GND**: Ground reference (star point)
  - Position: 60mm, 70mm
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
- **Board edge to component**: 10mm minimum
- **Board edge to mounting hole**: 3mm
- **Terminal to board edge**: 2mm (flush mounted)
- **Component spacing**: 10mm minimum (12mm preferred)
- **Capacitor spacing**: 10mm center-to-center
- **Inductor terminal spacing**: 18mm center-to-center (vertical stack)

### Thermal
- **Thermal relief**: 4 spokes, 0.5mm width for all ground pads
- **Heat dissipation**: Minimal (passive circuit, low power)
- **Copper weight**: 1 oz adequate (2 oz optional for lower ground impedance)

## Manufacturing Specifications

### PCB Fabrication
- **Base material**: FR-4, Tg 150°C minimum (high-quality substrate)
- **Copper weight**: 1 oz (35μm) both layers (2 oz optional for ground plane)
- **Surface finish**: ENIG (gold) preferred for test points and long-term reliability
- **Solder mask**: Green LPI, both sides, 0.025mm thickness
- **Silkscreen**: White epoxy ink, both sides, high contrast
- **Board outline**: Routed with 3mm radius corners (smooth edges)
- **E-test**: Required (100% continuity, isolation, and impedance testing)
- **Impedance control**: Not critical (low frequency audio, <100kHz)

### Tolerances
- **Board dimensions**: ±0.2mm
- **Hole positions**: ±0.1mm
- **Hole diameter**: +0.1mm / -0.0mm
- **Trace width**: ±10%
- **Trace spacing**: ±0.05mm
- **Registration** (layer to layer): ±0.1mm

## Assembly Notes

### Assembly Sequence
1. **Install screw terminals first** (10 total, largest components)
   - Sequence: J_IN, J_OUT, J_GND first (structural)
   - Then: 7× inductor terminals (J_IND_3KHZ through J_IND_16KHZ)
   - Finally: Control terminals (J_BOOST_SEL_SND, J_BOOST_SEL_RET, J_BOOST_LVL, J_BOOST_L_SND, J_BOOST_Q)
   - Orientation: All wire entries face outward from board
   - Soldering: Reflow all pins, inspect carefully for cold joints and bridges
   - Verification: Gently tug each terminal to ensure mechanical integrity

2. **Install resistor R3** (4.7kΩ)
   - Orientation: Value marking readable from top of board
   - Lead forming: Bend to 0.4" (10.16mm) spacing
   - Insertion: Fully seated against PCB
   - Soldering: Both leads, trim excess
   - Verification: Measure resistance (4.6-4.8kΩ expected)

3. **Install capacitors** (8 total)
   - Sequence: Largest first (C29 15nF), then by value descending
   - Orientation: Value markings facing top of board for easy identification
   - Lead spacing: 5.08mm per Vishay MKT1813 footprint
   - Lead forming: Straight insertion, no bending
   - Seating: Flush against PCB surface
   - Soldering: Both leads, inspect fillet quality
   - Trimming: Trim excess leads flush with solder joint

4. **Final inspection and testing**
   - Visual: Inspect all solder joints under magnification (10×)
   - Continuity: Verify signal paths end-to-end with DMM
   - Isolation: Verify no shorts between traces or to ground (>10MΩ)
   - Capacitance: Spot-check critical capacitor values with LCR meter
   - Resistance: Verify R3 value in-circuit

### Component Orientation Notes
- **Screw terminals**: All wire entries face outward (away from board center)
- **Capacitors**: Value markings face up (readable when board is horizontal)
- **Resistor**: Color bands or value marking readable from top edge
- **Inductor terminals**: Frequency labels clearly visible from right edge
- **Polarity**: Not applicable (all components non-polarized)

## Critical Routing Notes

### Audio Signal Integrity
1. **Minimize trace lengths**: Especially critical in high-impedance, high-frequency nodes
2. **Star grounding**: Single-point ground at board center (60mm, 70mm)
3. **Ground plane integrity**: Solid, continuous plane on bottom layer
4. **No ground loops**: All returns via ground plane, not traces
5. **Shielding**: Ground plane provides inter-layer shielding
6. **Symmetry**: Balanced routing for phase coherence across frequency bands

### Inductor Connections (Critical for Q)
1. **Low DCR traces**: Wide traces (1.0mm) to inductor terminals minimize series resistance
2. **Short connections**: Route directly from selector network to inductor terminals
3. **Via arrays**: Multiple vias (6×) at ground terminals for ultra-low impedance
4. **No vias in signal path**: Route inductor signals on top layer only
5. **Electromagnetic isolation**: Inductors are external; PCB provides connections only
6. **Q preservation**: Low-resistance connections critical for high Q operation

### Q Control Network
1. **Dedicated routing**: Q control capacitors (C29, C32, C33) have separate routing
2. **J_BOOST_Q connection**: Low-resistance path to Q control potentiometer
3. **Minimal loading**: Avoid adding capacitance or resistance in Q path
4. **Test point**: TP4_Q allows verification of Q control operation

### Noise Minimization
1. **Ground plane**: Maximum copper pour on bottom layer (98%+ coverage)
2. **Via stitching**: Dense grid (15mm perimeter, 30mm interior) lowers ground impedance
3. **No ground loops**: All ground returns via ground plane vias
4. **Trace separation**: Minimum 0.8mm between signal traces
5. **Guard traces**: Not required (ground plane provides adequate shielding)

## Recommended Clearances

### Terminal Clearances (for Wiring Access)
- **Side clearance**: 25mm around all terminals for screwdriver access
- **Top clearance**: 60mm above board for wire routing, bending, stripping
- **Between terminals**: 20mm minimum for wire separation and strain relief
- **Inductor terminal access**: 30mm clearance for inductor lead dress

### Mounting Clearances
- **Standoff height**: 15mm recommended (accommodate component leads and wire routing)
- **Bottom clearance**: 12mm for component leads and bottom-layer vias
- **Enclosure clearance**: 30mm minimum all sides for ventilation and wiring
- **Adjacent boards**: 40mm spacing if stacking or mounting side-by-side

## Inductor Integration Notes

### External Inductor Specifications
This module requires **7 hand-wound inductors**:
- **3kHz**: ~3-5mH (powdered iron toroid, Type 26)
- **4kHz**: ~2-3mH
- **5kHz**: ~1.5-2.5mH
- **8kHz**: ~0.8-1.2mH
- **10kHz**: ~0.5-0.8mH
- **12kHz**: ~0.3-0.5mH
- **16kHz**: ~0.2-0.3mH

### PCB Terminal Design for Inductors
- **Terminal type**: Phoenix Contact 1757019 (2-position, 5.08mm pitch)
- **Wire gauge capacity**: 18-24 AWG (typical for hand-wound inductors)
- **Connection method**: Screw terminals allow easy swapping for tuning
- **Labeling**: Large, clear frequency labels (2.0mm height) on both silkscreen layers
- **Mechanical notes**: Inductors should be externally mounted (not hanging on terminals)

### Inductor Connection Guidelines
1. Each inductor connects between two terminals:
   - Terminal position 1: To selector network (signal)
   - Terminal position 2: Return to network (ground or signal return)
2. Inductor polarity: Generally not critical, but maintain consistent winding direction
3. Lead dress: Keep inductor leads as short as possible
4. Secure mounting: Inductors must be mechanically secured (epoxy, mounting brackets, or encapsulated)
5. Testing: Use TP3_IND to verify inductor operation and resonance

## Q Control Operation

### Q Control Implementation
The Q (bandwidth) control adjusts the sharpness of the boost curve:
- **High Q**: Narrow, peaked boost (more selective)
- **Low Q**: Broad, gentle boost (less selective)
- **Control**: Front-panel potentiometer via J_BOOST_Q
- **Capacitors**: C29, C32, C33 form Q control network

### Q Control Routing Requirements
1. **Low-resistance path**: Minimize trace resistance in Q network
2. **Short connections**: J_BOOST_Q close to C29/C32/C33
3. **No loading**: Avoid adding stray capacitance in Q path
4. **Test point**: TP4_Q for Q network verification

## Design Validation Checklist

- [ ] All mounting holes placed correctly (3mm from edges)
- [ ] All terminals on board edges for accessibility
- [ ] Signal flow is logical (left to right: IN → network → OUT)
- [ ] Ground plane is solid and continuous (98%+ coverage)
- [ ] Star ground point implemented at board center (60mm, 70mm)
- [ ] All components have correct footprints (5.08mm pitch for capacitors)
- [ ] 7× inductor terminals clearly labeled with frequencies (large font)
- [ ] Q control network properly routed (C29, C32, C33, J_BOOST_Q)
- [ ] Silkscreen labels are clear and readable (1.5mm minimum height)
- [ ] Test points placed at all critical signal nodes (7 test points total)
- [ ] No acute angle traces (all 45° or smooth curves)
- [ ] Via stitching implemented (15mm perimeter, 30mm interior grid)
- [ ] DRC passes with no errors (clearance, width, annular ring, isolation)
- [ ] Board dimensions optimized (120mm × 140mm)
- [ ] Capacitor spacing allows test probe access (10mm minimum)
- [ ] Inductor terminal spacing allows wire routing (18mm vertical)

## Output Files Required

### Gerber Files (RS-274X format)
- **GTL**: Top copper layer
- **GBL**: Bottom copper layer (solid ground plane)
- **GTO**: Top silkscreen overlay
- **GBO**: Bottom silkscreen overlay (with inductor frequency map)
- **GTS**: Top solder mask
- **GBS**: Bottom solder mask
- **GM1**: Board outline / mechanical layer
- **GKO**: Keep-out layer

### Drill Files
- **Excellon format**: Plated through-holes
- **Tool list**: With sizes, quantities, and hole types
- **Drill map**: PDF showing hole locations, sizes, and types

### Additional Files
- **Assembly drawing** (PDF): Top view with component positions, values, and orientations
- **Component placement file** (CSV): Ref, X, Y, Rotation, Layer, Value, Package
- **BOM correlation**: Cross-reference PCB designators to BOM line items
- **Fabrication drawing**: Board dimensions, layer stackup, materials, tolerances, notes
- **IPC-D-356 netlist**: For automated optical and electrical testing
- **Inductor connection diagram**: Showing frequency assignments and wiring

## Special Considerations

### Inductor Design Dependencies
- PCB layout is complete and independent of final inductor values
- Inductor terminals provide flexible connection for any inductor design
- Inductors must be designed by inductor-design-specialist based on actual capacitor values
- Test points (especially TP3_IND) allow verification of LC resonance frequencies
- Q control allows fine-tuning of bandwidth after inductor installation

### Modular Integration
- This module receives signal from Low Boost module (via J_IN)
- This module sends signal to High Cut module (via J_OUT)
- Control terminals connect to front panel:
  - Rotary switch (frequency selector, 7+ positions)
  - Boost level potentiometer (J_BOOST_LVL, J_BOOST_L_SND)
  - Q control potentiometer (J_BOOST_Q)
- Ground terminal connects to system ground bus (star ground architecture)

### Testability
- 7 test points cover all critical signal nodes
- Component spacing allows in-circuit testing and probing
- Screw terminals allow easy disconnection for module-level testing
- Clear labeling facilitates troubleshooting and frequency response measurement
- Gold-plated test points ensure reliable long-term contact

### High-Frequency Considerations
- This module operates at audio frequencies (3-16kHz), but uses high-Q inductors
- Low-resistance connections critical for maintaining inductor Q
- Ground plane provides excellent HF shielding
- Via stitching further reduces ground impedance at higher frequencies
- Trace routing minimizes parasitic capacitance and inductance

## Revision History
- **v1.0** (2025-10-26): Initial PCB layout specification

## Notes
- This is the largest and most complex module (7 inductors, Q control, 8 capacitors)
- Board size (120mm × 140mm) optimized for component density and inductor terminal access
- Ground plane and via stitching critical for low-noise, high-Q operation
- All terminals on edges enable easy modular interconnection
- 7 inductor terminals enable flexible testing and tuning of hand-wound components
- Q control adds additional complexity but provides classic Pultec high-frequency shaping
- Test points essential for verifying frequency response, Q operation, and inductor tuning
- ENIG surface finish recommended for long-term reliability of test points and terminals
