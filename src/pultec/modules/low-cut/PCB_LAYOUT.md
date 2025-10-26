# Low Cut Module - PCB Layout Specification

## Board Overview
- **Module**: Low Cut (Frequency-selective attenuation, 20Hz-100Hz)
- **Complexity**: Simple (2 capacitors, 5 screw terminals)
- **Estimated Size**: 60mm × 60mm (small, optimized)
- **Layer Count**: 2-layer through-hole PCB
- **Board Thickness**: 1.6mm

## Board Dimensions and Mounting
- **Board Size**: 60mm × 60mm
- **Mounting Holes**: 4× M3 holes at corners
  - Position: 3mm from edges (54mm × 54mm spacing)
  - Hole diameter: 3.2mm
  - Pad diameter: 6mm
  - Keep-out zone: 8mm diameter around each hole

## Component Count Summary
- **Capacitors**: 2 (C23, C24)
- **Screw Terminals**: 5 total
  - 2× 2-position (J_IN, J_OUT, J_GND)
  - 1× 3-position (J_CUT_SEL_RET)
  - 1× 2-position (J_CUT_LVL)

## Terminal Placement (All on Board Edges)

### Left Edge (Signal Flow)
- **J_IN** (2-pos): Input signal
  - Position: 10mm from top edge, left edge
  - Labels: "IN+", "IN-"

### Right Edge (Signal Flow)
- **J_OUT** (2-pos): Output signal
  - Position: 10mm from top edge, right edge
  - Labels: "OUT+", "OUT-"

### Top Edge (Controls)
- **J_CUT_SEL_RET** (3-pos): Frequency selector return
  - Position: Center of top edge (30mm from left)
  - Labels: "SEL_RET1", "SEL_RET2", "SEL_RET3"

- **J_CUT_LVL** (2-pos): Level control
  - Position: 45mm from left edge, top edge
  - Labels: "LVL_CCW", "LVL_CW"

### Bottom Edge (Ground)
- **J_GND** (2-pos): Ground connection
  - Position: Center of bottom edge
  - Labels: "GND", "GND"

## Component Placement Strategy

### Capacitor Placement (Center Area)
- **C23** (33nF): Position at 30mm, 30mm (board center)
- **C24** (47nF): Position at 40mm, 30mm (adjacent to C23)
- **Orientation**: Both vertical, aligned for neat appearance
- **Spacing**: 10mm between components for easy access
- **Lead spacing**: 5.08mm per Vishay MKT1813 footprint

### Layout Rationale
1. **Signal flow**: Left to right (IN → OUT)
2. **Symmetric placement**: Capacitors centered for balanced appearance
3. **Short traces**: Minimize signal path lengths
4. **Accessibility**: All terminals on edges for easy wiring
5. **Test points**: Available at capacitor pads for troubleshooting

## Grounding Strategy

### Ground Plane Approach
- **Top layer**: Signal routing and component pads
- **Bottom layer**: Solid ground plane (maximum copper pour)
- **Ground connections**: All ground terminals connect to bottom plane via multiple vias
- **Star ground point**: Center of board, near capacitors
- **Via placement**: 2× vias per ground connection, minimum 0.8mm drill

### Ground Routing
1. J_IN ground terminal → star point (via array)
2. J_OUT ground terminal → star point (via array)
3. J_GND terminals → star point (direct, heavy traces)
4. Capacitor ground pads → local vias to ground plane
5. **All ground traces**: 1.5mm minimum width on top layer

## Trace Routing

### Signal Traces (Top Layer)
- **Width**: 0.8mm for audio signals
- **Clearance**: 0.5mm minimum (use 0.8mm for safety)
- **Via size**: 0.8mm drill, 1.3mm pad

### Signal Path Routing
1. **J_IN+ → C23/C24 network → J_CUT_SEL_RET → J_CUT_LVL → J_OUT+**
   - Keep traces short and direct
   - Avoid sharp angles (use 45° or curves)
   - Route on top layer only if possible

2. **Ground returns**: Via to bottom ground plane at each terminal

### Power/Ground Traces
- **Width**: 1.5mm minimum
- **Ground plane clearance**: 0.3mm
- **Thermal relief**: 4 spokes, 0.4mm width

## Layer Stackup

### Top Layer (Component Side)
- Component footprints
- Signal routing traces
- Terminal pads
- Silkscreen labels
- Test points

### Bottom Layer (Solder Side)
- Solid ground plane (maximum copper fill)
- Minimal signal routing (via connections only)
- Silkscreen: Board ID, revision, mounting info

## Silkscreen Labels

### Component Labels (White on Green)
- **C23, C24**: Component designators above components
- **Value labels**: "33nF", "47nF" below component designators
- **Polarity**: Not applicable (non-polarized capacitors)

### Terminal Labels (Large, Bold Font)
- **J_IN**: "INPUT", with "+" and "-" at each position
- **J_OUT**: "OUTPUT", with "+" and "-" at each position
- **J_CUT_SEL_RET**: "CUT SEL RETURN", with "1", "2", "3" at each position
- **J_CUT_LVL**: "CUT LEVEL", with "CCW" and "CW"
- **J_GND**: "GROUND", with "GND" at both positions

### Board Information (Bottom Silkscreen)
- "PULTEC LOW CUT MODULE"
- "Rev 1.0"
- Date code: "2025"
- Mounting hole markers

## Test Point Locations

### Critical Test Points (1mm diameter pads)
- **TP1**: J_IN+ (input signal monitoring)
  - Position: Near J_IN terminal
  - Label: "TP1_IN"

- **TP2**: J_OUT+ (output signal monitoring)
  - Position: Near J_OUT terminal
  - Label: "TP2_OUT"

- **TP3**: Ground reference
  - Position: Near board center
  - Label: "TP_GND"

## Design Rules

### Electrical
- **Minimum trace width**: 0.25mm (use 0.8mm for signals)
- **Minimum clearance**: 0.25mm (use 0.5mm for safety)
- **Via drill**: 0.8mm
- **Via pad**: 1.3mm diameter
- **Via clearance**: 0.3mm

### Mechanical
- **Board edge to component**: 5mm minimum
- **Board edge to mounting hole**: 3mm
- **Terminal to board edge**: 2mm (aligned with edge)
- **Component spacing**: 5mm minimum

### Thermal
- **Thermal relief**: 4 spokes, 0.4mm width for ground connections
- **Heat dissipation**: Not critical (no power components)

## Manufacturing Specifications

### PCB Fabrication
- **Base material**: FR-4
- **Copper weight**: 1 oz (35μm) both layers
- **Surface finish**: HASL (lead-free) or ENIG
- **Solder mask**: Green, both sides
- **Silkscreen**: White, both sides
- **Board outline**: Routed, not v-scored
- **E-test**: Required

### Tolerances
- **Board dimensions**: ±0.2mm
- **Hole positions**: ±0.1mm
- **Hole diameter**: +0.1mm / -0.0mm
- **Trace width**: ±10%

## Assembly Notes

### Assembly Sequence
1. Install screw terminals (J_IN, J_OUT, J_CUT_SEL_RET, J_CUT_LVL, J_GND)
   - Orientation: Wire entry from board edge (outward)
   - Soldering: All pins, inspect for cold joints

2. Install capacitors (C23, C24)
   - Orientation: Value label visible from top
   - Lead forming: Straight down, 5.08mm spacing
   - Height: Seated flush against PCB

3. Inspection
   - Visual: Check all solder joints
   - Continuity: Verify signal path
   - Isolation: Verify no shorts to ground plane

### Component Orientation Notes
- **Screw terminals**: Wire entry facing outward (away from board center)
- **Capacitors**: Value markings facing top of board for readability
- **Test points**: Accessible from top layer

## Critical Routing Notes

### Audio Signal Integrity
1. **Keep signal traces short**: Minimize capacitance and noise pickup
2. **Avoid ground loops**: Single star ground point
3. **Separate signal and ground**: Use ground plane for return, not traces
4. **No split ground planes**: Solid plane on bottom layer only

### Noise Minimization
1. **Ground plane**: Maximize copper pour on bottom layer
2. **Shielding**: Ground plane acts as shield between layers
3. **Bypass capacitors**: Not required (no active components)
4. **EMI considerations**: Low-frequency circuit, minimal EMI concerns

## Recommended Clearances

### Terminal Clearances (for Wiring Access)
- **Side clearance**: 15mm around terminals for screwdriver access
- **Top clearance**: 40mm above board for wire routing and stripping
- **Between terminals**: 10mm minimum for wire separation

### Mounting Clearances
- **Standoff height**: 10mm recommended
- **Bottom clearance**: 8mm for solder joints and wire routing
- **Enclosure clearance**: 20mm minimum all sides for ventilation

## Design Validation Checklist

- [ ] All mounting holes placed correctly (3mm from edges)
- [ ] All terminals on board edges for accessibility
- [ ] Signal flow is left to right (IN → OUT)
- [ ] Ground plane is solid and continuous on bottom layer
- [ ] All components have correct footprints (5.08mm pitch)
- [ ] Silkscreen labels are clear and readable
- [ ] Test points placed at critical signal nodes
- [ ] No acute angle traces (all 45° or curves)
- [ ] DRC passes with no errors
- [ ] Board dimensions are optimized (60mm × 60mm)

## Output Files Required

### Gerber Files
- GTL: Top copper layer
- GBL: Bottom copper layer (ground plane)
- GTO: Top silkscreen overlay
- GBO: Bottom silkscreen overlay
- GTS: Top solder mask
- GBS: Bottom solder mask
- GM1: Board outline / mechanical layer
- GKO: Keep-out layer (optional)

### Drill Files
- TXT or Excellon format
- Separate plated and non-plated if needed
- Drill map (PDF or image)

### Additional Files
- Assembly drawing (PDF): Top view with component positions
- Component placement file (CSV): Ref, X, Y, Rotation, Layer
- BOM correlation: Match designators to BOM
- Fabrication drawing: Dimensions, tolerances, notes

## Revision History
- **v1.0** (2025-10-26): Initial PCB layout specification

## Notes
- This is a simple module with minimal components
- Focus on clean layout and easy assembly
- Ground plane provides excellent shielding for this passive circuit
- All terminals accessible from board edges for modular wiring
- Board size optimized for component count while maintaining manufacturability
