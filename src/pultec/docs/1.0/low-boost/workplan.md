# LOW BOOST MODULE - COMPREHENSIVE IMPLEMENTATION WORKPLAN

**Project:** Pultec Three-Band EQ - Modular Design
**Module:** Low Boost (Passive LC Network)
**Revision:** 1.0
**Date:** 2025-10-26
**Status:** Ready for Implementation

---

## EXECUTIVE SUMMARY

This workplan provides step-by-step implementation guidance for the Low Boost module, synthesizing input from specialized design agents across circuit design, inductor engineering, PCB layout, KiCAD workflow, and procurement.

**Total Project Duration:** 6-8 weeks
**Estimated Cost:** $80-102 (single prototype), $56-69 per unit (3-unit build)
**Complexity:** Moderate-High (requires hand-wound inductors)
**Critical Path:** Inductor design and fabrication

---

## TABLE OF CONTENTS

1. [Circuit Overview](#1-circuit-overview)
2. [Component Specifications](#2-component-specifications)
3. [Inductor Design and Fabrication](#3-inductor-design-and-fabrication)
4. [PCB Design Requirements](#4-pcb-design-requirements)
5. [KiCAD Implementation Workflow](#5-kicad-implementation-workflow)
6. [Procurement Plan](#6-procurement-plan)
7. [Assembly Instructions](#7-assembly-instructions)
8. [Testing and Validation](#8-testing-and-validation)
9. [Timeline and Milestones](#9-timeline-and-milestones)
10. [Risk Management](#10-risk-management)

---

## 1. CIRCUIT OVERVIEW

### 1.1 Circuit Topology

The low-boost section implements a **passive LC resonant shunt circuit** based on the classic Pultec EQP-1A design:

- **Primary voltage divider:** 47kΩ (high-frequency side) + 4.7kΩ (low-frequency side)
- **Nominal insertion loss:** 20.8dB (0.091 ratio)
- **Boost mechanism:** Variable resistor (0-22kΩ) sits in parallel with 4.7kΩ section, reducing attenuation at low frequencies
- **Frequency selection:** LC resonant circuit creates low-impedance shunt at selected frequency

### 1.2 Signal Flow

```
INPUT → Voltage Divider → Frequency Selector → LC Network → Inductor Connections → Boost Level Control → OUTPUT
```

**Key Circuit Elements:**
- 11 film capacitors (1nF to 18nF)
- 1 resistor (56kΩ)
- 4 hand-wound inductors (7.68H to 35.16H)
- 13 screw terminal connections
- External frequency selector (6-position rotary switch)
- External boost level control (variable resistor ladder)

### 1.3 Frequency Response

**Target Frequencies:**
- 20Hz: C1 (18nF) + L20 (35.16H)
- 30Hz: C2 (10nF) + L30 (28.15H)
- 60Hz: C3 (4.7nF) + L60 (14.98H)
- 100Hz: C4 (3.3nF) + L100 (7.68H)

**Boost Range:** 0-11dB at selected frequency
**Bandwidth:** Depends on inductor Q (higher Q = narrower boost)
**Insertion Loss:** ~20.8dB (compensated by makeup gain in output stage)

### 1.4 Critical Design Parameters

- **Inductor Q Factor:** Must exceed 20 for good performance
  - Q = 88+ for 20Hz with DCR <50Ω (excellent)
  - Q = 44+ for 20Hz with DCR <100Ω (acceptable)
  - Q = 22+ for 20Hz with DCR <200Ω (marginal)

- **Impedances:**
  - Input: ~51.7kΩ (47kΩ + 4.7kΩ)
  - Output: 4-10kΩ (varies with settings)
  - Requires low-impedance source (<600Ω) and high-impedance load (>100kΩ)

---

## 2. COMPONENT SPECIFICATIONS

### 2.1 Passive Components

#### Capacitors (11 total - Film, Non-Polarized)

| Ref | Value | Description | Manufacturer | Part Number | Mouser P/N |
|-----|-------|-------------|--------------|-------------|------------|
| C1 | 18nF | Film cap, 5%, 100V, 5.08mm | Vishay | MKT1813183104 | 594-MKT1813183104 |
| C2 | 10nF | Film cap, 5%, 100V, 5.08mm | Vishay | MKT1813103104 | 594-MKT1813103104 |
| C3 | 4.7nF | Film cap, 5%, 100V, 5.08mm | Vishay | MKT1813472104 | 594-MKT1813472104 |
| C4 | 3.3nF | Film cap, 5%, 100V, 5.08mm | Vishay | MKT1813332104 | 594-MKT1813332104 |
| C5 | 2.2nF | Film cap, 5%, 100V, 5.08mm | Vishay | MKT1813222104 | 594-MKT1813222104 |
| C4a2 | 1nF | Film cap, 5%, 100V, 5.08mm | Vishay | MKT1813102104 | 594-MKT1813102104 |
| C5a2 | 1.5nF | Film cap, 5%, 100V, 5.08mm | Vishay | MKT1813152104 | 594-MKT1813152104 |
| C6 | 1.8nF | Film cap, 5%, 100V, 5.08mm | Vishay | MKT1813182104 | 594-MKT1813182104 |
| C7 | 1nF | Film cap, 5%, 100V, 5.08mm | Vishay | MKT1813102104 | 594-MKT1813102104 |
| C34 | 1nF | Film cap, 5%, 100V, 5.08mm | Vishay | MKT1813102104 | 594-MKT1813102104 |
| C35 | 1nF | Film cap, 5%, 100V, 5.08mm | Vishay | MKT1813102104 | 594-MKT1813102104 |

**Subtotal:** $5.50

**Alternatives:**
- WIMA MKS2 series (premium, ~$1-2 each)
- EPCOS B32529 series (good quality)
- ±10% tolerance acceptable if ±5% unavailable

#### Resistor

| Ref | Value | Description | Manufacturer | Part Number | Mouser P/N |
|-----|-------|-------------|--------------|-------------|------------|
| R2 | 56kΩ | Metal film, 1/4W, 1% | Vishay | MRS25000C5602FCT00 | 594-MRS25C5602FCT00 |

**Cost:** $0.20

### 2.2 Screw Terminals (Phoenix Contact 1757 Series)

| Ref | Positions | Qty | Manufacturer P/N | Mouser P/N | Unit Price |
|-----|-----------|-----|------------------|------------|------------|
| J_IN | 2 | 1 | 1757019 | 651-1757019 | $0.75 |
| J_OUT | 2 | 1 | 1757019 | 651-1757019 | $0.75 |
| J_BOOST_SEL_SND | 6 | 1 | 1757025 | 651-1757025 | $1.50 |
| J_BOOST_SEL_RET | 6 | 1 | 1757025 | 651-1757025 | $1.50 |
| J_CUT_SEL_SND | 3 | 1 | 1757022 | 651-1757022 | $1.00 |
| J_BOOST_LVL | 3 | 1 | 1757022 | 651-1757022 | $1.00 |
| J_IND_20HZ | 2 | 1 | 1757019 | 651-1757019 | $0.75 |
| J_IND_30HZ | 2 | 1 | 1757019 | 651-1757019 | $0.75 |
| J_IND_60HZ | 2 | 1 | 1757019 | 651-1757019 | $0.75 |
| J_IND_100HZ | 2 | 1 | 1757019 | 651-1757019 | $0.75 |
| J_GND | 2 | 1 | 1757019 | 651-1757019 | $0.75 |

**Subtotal:** $10.75

**Specifications:**
- Pitch: 5.08mm (0.2")
- Wire range: 26-16 AWG
- Current rating: 17.5A max
- Mounting: Through-hole (THT)

**Alternatives:**
- On Shore OSTTE series (-40% cost)
- Wurth 691137 series (comparable quality)

### 2.3 PCB Specifications

**Board Dimensions:** 60mm × 100mm (2.36" × 3.94")
**Layers:** 2 (Top copper + Bottom copper with ground plane)
**Thickness:** 1.6mm (standard FR-4)
**Copper Weight:** 1oz (35μm) both sides
**Surface Finish:** ENIG preferred (HASL acceptable)
**Mounting Holes:** 4× M3 (3.2mm diameter)

**Estimated Cost:** $4-8 per board (minimum order 5 boards)

---

## 3. INDUCTOR DESIGN AND FABRICATION

### 3.1 Calculated Inductance Values

Using series LC resonance formula: **f₀ = 1 / (2π√LC)**

| Frequency | Capacitor | Capacitance | Required Inductance |
|-----------|-----------|-------------|---------------------|
| 20Hz      | C1        | 18nF        | **35.16H**          |
| 30Hz      | C2        | 10nF        | **28.15H**          |
| 60Hz      | C3        | 4.7nF       | **14.98H**          |
| 100Hz     | C4        | 3.3nF       | **7.68H**           |

**Note:** These are very large inductance values (tens of Henries), requiring thousands of turns and large ferromagnetic cores.

### 3.2 Recommended Core Specifications

#### 20Hz Inductor
- **Inductance:** 35.16H ±5%
- **Core:** Laminated E-I steel, EI-100, 25mm stack (Hammond 166J00)
- **Wire:** 20 AWG magnet wire, 1675 turns
- **DCR:** ~2.8Ω
- **Q Factor:** 157 @ 20Hz
- **Air Gap:** 0.4mm

#### 30Hz Inductor
- **Inductance:** 28.15H ±5%
- **Core:** Laminated E-I steel, EI-100, 25mm stack
- **Wire:** 20 AWG magnet wire, 1500 turns
- **DCR:** ~2.5Ω
- **Q Factor:** 211 @ 30Hz
- **Air Gap:** 0.4mm

#### 60Hz Inductor
- **Inductance:** 14.98H ±5%
- **Core:** Laminated E-I steel, EI-87, 25mm stack (Hammond 166K00)
- **Wire:** 20 AWG magnet wire, 1400 turns
- **DCR:** ~2.2Ω
- **Q Factor:** 257 @ 60Hz
- **Air Gap:** 0.5mm

#### 100Hz Inductor
- **Inductance:** 7.68H ±5%
- **Core:** Laminated E-I steel, EI-87, 25mm stack
- **Wire:** 20 AWG magnet wire, 990 turns
- **DCR:** ~1.5Ω
- **Q Factor:** 314 @ 100Hz
- **Air Gap:** 0.5mm

### 3.3 Winding Instructions

**General Procedure:**

1. **Core Preparation**
   - Clean laminations, remove burrs
   - Stack to specified height
   - Insert air gap material (non-magnetic shim)
   - Secure with clamps or tape

2. **Bobbin Setup**
   - Install bobbin on core (if removable)
   - Or wind directly on core with insulation tape base layer

3. **Winding Technique**
   - Use hand drill or winding machine
   - Maintain consistent tension (not too tight)
   - Layer winding with insulation between layers
   - Count turns accurately (use counter or tally marks)
   - Leave 6" leads at start and end

4. **Termination**
   - Strip and tin wire ends
   - Attach to solder lugs or terminal strip
   - Secure with strain relief
   - Label inductor with frequency marking

5. **Testing**
   - Measure inductance with LCR meter @ 120Hz
   - Measure DCR with multimeter
   - Calculate Q = 2πfL/DCR
   - Verify within ±10% of target

**Estimated Winding Time:**
- 20Hz (1675 turns): 2-3 hours
- 30Hz (1500 turns): 1.5-2 hours
- 60Hz (1400 turns): 1-1.5 hours
- 100Hz (990 turns): 1 hour
- **Total:** 6-8 hours for complete set

### 3.4 Inductor Material Sourcing

#### Cores
- **Supplier:** Hammond Manufacturing, Amidon, or equivalent
- **Part Numbers:**
  - EI-100, 25mm stack: Hammond 166J00 or equivalent
  - EI-87, 25mm stack: Hammond 166K00 or equivalent
- **Quantity:** 4 cores (plus 1 spare recommended)
- **Cost:** $10-15 each (total $40-60)
- **Lead Time:** 2-3 weeks

#### Wire
- **Type:** Magnet wire, enameled copper
- **Gauge:** 20 AWG (0.812mm diameter)
- **Quantity:** 1 lb spool (~405 feet) - sufficient for all 4 inductors
- **Supplier:** BNTECHGO, Remee Wire, or DigiKey
- **Cost:** $15-20
- **Lead Time:** 1 week

---

## 4. PCB DESIGN REQUIREMENTS

### 4.1 Board Layout Strategy

**Signal Flow:** Left to Right
```
INPUT (Left) → FREQUENCY SELECTION (Center) → INDUCTORS (Right) → OUTPUT (Right)
```

**Component Placement:**
- **Input Section (Left edge):** J_IN terminal
- **Capacitor Array (Center):** 11 capacitors in organized grid, 2-3 rows
- **Inductor Connections (Right edge):** 4× 2-position terminals vertically stacked
- **Output Section (Right edge):** J_OUT terminal, R2 resistor
- **Control Terminals (Top/Bottom edges):** Selector and level control connections
- **Ground Terminal (Bottom edge):** J_GND

### 4.2 Grounding Strategy

**Modified Star Grounding with Ground Plane:**

- **Bottom layer:** Solid copper pour (90%+ coverage)
- **Star point:** Located near input terminal
- **Signal grounds:** All converge at star point before connecting to plane
- **Ground vias:** Minimum 4 vias at star point, 2 vias at each component ground
- **J_GND connection:** 4-6 vias to plane for low impedance

### 4.3 Routing Guidelines

**Trace Widths:**
- Primary audio paths: 0.5-0.8mm (20-30mil)
- Secondary audio paths: 0.4-0.5mm (16-20mil)
- Control signals: 0.3-0.4mm (12-16mil)
- Ground connections: 1.0-1.5mm (40-60mil)

**Design Rules:**
- Avoid 90° corners (use 45° or arcs)
- Keep signal traces short and direct
- Minimize via usage in audio signal paths
- Use bottom layer for crossovers only when necessary
- Maintain 0.3mm minimum trace spacing

### 4.4 Mechanical Considerations

**Mounting Holes:**
- 4× M3 holes at corners
- 3.5-5mm from board edges
- 6mm keepout zone (no copper)

**Terminal Clearances:**
- 10mm screwdriver access radius around each screw
- 2mm minimum between adjacent terminal blocks
- 5mm clearance from terminals to nearest component

**Silkscreen Requirements:**
- Clear terminal labels (2.0mm height text)
- Frequency markings for inductor connections (3.0mm height)
- Component designators (1.0-1.2mm height)
- Pin 1 indicators on all connectors
- Board title, revision, date

### 4.5 Test Points

**Recommended Test Points:**
- TP_IN: Input signal
- TP_OUT: Output signal
- TP_GND: Ground reference
- TP_20Hz, TP_30Hz, TP_60Hz, TP_100Hz: Frequency branch signals
- TP_LVL: Boost level control

---

## 5. KICAD IMPLEMENTATION WORKFLOW

### 5.1 Project Setup

**Step 1: Create New Project**
1. KiCAD → File → New Project
2. Location: `/Users/orion/work/multi-channel-preamp/src/schematics/pultec-boost-low/`
3. Name: `pultec-boost-low`

**Step 2: Configure Page Settings**
- Title: "Pultec Low Boost Module"
- Revision: "1.0"
- Date: Current date
- Comments: "Three-Band EQ - Low Boost Section", "Passive LC Network", "External Inductors Required"

### 5.2 Schematic Creation

**Step 3: Place Components**

**Connectors (11 total):**
- Symbol: `Connector:Screw_Terminal_01x02` (for 2-pos)
- Symbol: `Connector:Screw_Terminal_01x03` (for 3-pos)
- Symbol: `Connector:Screw_Terminal_01x06` (for 6-pos)
- Arrange logically: Input (left), Output (right), Controls (top), Inductors (right)

**Capacitors (11 total):**
- Symbol: `Device:C`
- Values: 18nF, 10nF, 4.7nF, 3.3nF, 2.2nF, 1.5nF, 1.8nF, 1nF (×5)
- Footprint: `Capacitor_THT:C_Rect_L7.0mm_W2.5mm_P5.00mm` or similar

**Resistor (1 total):**
- Symbol: `Device:R`
- Value: 56kΩ
- Footprint: `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`

**Step 4: Wire Circuit**
- Connect according to circuit topology
- Add net labels for all major nodes
- Use consistent naming: `SIG_IN`, `SIG_OUT`, `SEL_SND_20HZ`, etc.

**Step 5: Annotate**
- Tools → Annotate Schematic
- Use automatic annotation

**Step 6: Assign Footprints**
- Tools → Assign Footprints
- Verify all components have footprints
- Check Phoenix Contact terminals against OL Library or create custom

**Step 7: Run ERC**
- Inspect → Electrical Rules Checker
- Resolve all errors
- Target: Zero errors

### 5.3 PCB Layout

**Step 8: Update PCB from Schematic**
- Tools → Update PCB from Schematic (F8)
- Import all components

**Step 9: Board Setup**
- Define board outline: 60mm × 100mm
- Add 4× M3 mounting holes (3.2mm diameter)
- Set design rules:
  - Min track: 0.25mm
  - Min clearance: 0.20mm
  - Min via: 0.6mm / 0.3mm drill

**Step 10: Component Placement**
- Follow layout strategy from section 4.1
- Use 3D viewer to verify clearances
- Check screwdriver access around terminals

**Step 11: Routing**
- Add ground plane on bottom layer
- Route signal traces on top layer
- Follow routing guidelines from section 4.3
- Add ground vias at star point and component grounds

**Step 12: Run DRC**
- Inspect → Design Rules Checker
- Resolve all errors
- Target: Zero errors

**Step 13: Final Touches**
- Add silkscreen labels
- Verify pin 1 indicators
- Add frequency markings near inductor terminals
- Update title block

### 5.4 Manufacturing Output

**Step 14: Generate Gerber Files**
- File → Fabrication Outputs → Gerbers
- Select all required layers:
  - F.Cu, B.Cu (copper)
  - F.Mask, B.Mask (soldermask)
  - F.Silkscreen, B.Silkscreen (silkscreen)
  - Edge.Cuts (board outline)
- Output directory: `gerbers/`

**Step 15: Generate Drill Files**
- File → Fabrication Outputs → Drill Files
- Format: Excellon
- Generate separate PTH and NPTH files

**Step 16: Export BOM**
- Tools → Generate BOM
- Export as CSV
- Include: Ref, Qty, Value, Description, Footprint, MPN, Supplier P/N

**Step 17: Create Assembly Drawing**
- File → Print → Export to PDF
- Show top view with component outlines and designators

**Step 18: Verify Gerbers**
- Open in GerbView
- Inspect each layer for correctness
- Upload to manufacturer's preview tool (JLCPCB, OSH Park, etc.)

---

## 6. PROCUREMENT PLAN

### 6.1 Component Order

**Mouser Electronics Order (Standard Components):**

| Item | Quantity | Cost |
|------|----------|------|
| Capacitors (11 types) | 1 each (or 3× for spares) | $5.50 ($16.50) |
| Resistor R2 (56kΩ) | 1 (or 3×) | $0.20 ($0.60) |
| Screw Terminals (11 assorted) | 1 set (or 3×) | $10.75 ($32.25) |
| **Subtotal** | | **$16.45** (**$49.35**) |
| Shipping (Standard Ground) | | **$7.99** |
| **Total** | | **$24.44** (**$57.34**) |

**Recommendation:** Order components for 3 boards (provides spares, better unit cost)

### 6.2 PCB Fabrication

**Option A: JLCPCB (Cost-Optimized)**
- Quantity: 5 boards minimum
- Specifications: 2-layer, 60×100mm, 1.6mm, 1oz copper, ENIG finish
- Cost: $15-20 + $12-18 shipping
- Lead Time: 3-4 days production + 3-5 days shipping
- **Total: $30-38, 1-2 weeks**

**Option B: OSH Park (Quality-Optimized)**
- Quantity: 3 boards
- Specifications: 2-layer, 60×100mm, 1.6mm, 1oz copper
- Cost: $30-50 (includes shipping)
- Lead Time: 12 days
- **Total: $30-50, 2 weeks**

**Recommendation:** OSH Park for first build (better quality, US-based), JLCPCB for production runs

### 6.3 Inductor Materials

**Cores:**
- **Type:** Hammond 166J00 (EI-100), 166K00 (EI-87) or equivalent
- **Quantity:** 4 cores (2× EI-100, 2× EI-87) + 1 spare
- **Supplier:** Hammond direct, Allied Electronics, or eBay
- **Cost:** $10-15 each = $40-60 total
- **Lead Time:** 2-3 weeks

**Magnet Wire:**
- **Type:** 20 AWG enameled copper magnet wire
- **Quantity:** 1 lb spool (~405 feet)
- **Supplier:** BNTECHGO (Amazon), Remee Wire, or DigiKey
- **Cost:** $15-20
- **Lead Time:** 1 week

### 6.4 Total Cost Summary

**Single Prototype Unit:**
- Electronic Components: $16.45
- PCB (from min. order): $4-8
- Inductor Materials: $32-44
- Shipping: $28-38
- **Total: $80-102**

**Three-Unit Build (Recommended):**
- Electronic Components: $49.35 (×3 + spares)
- PCBs: $20-25 (5 boards)
- Inductor Materials: $72-96 (12 cores, wire)
- Shipping: $28-38
- **Total: $169-208 ($56-69 per unit)**

### 6.5 Procurement Timeline

| Week | Action | Item | Lead Time |
|------|--------|------|-----------|
| **0** | Design | Finalize inductor specs | - |
| **1** | Order | Inductor cores | 2-3 weeks |
| **1** | Order | Magnet wire | 1 week |
| **1-2** | Order | PCB fabrication | 1-2 weeks |
| **2** | Order | Standard components | 1 week |
| **2** | Receive | Magnet wire | - |
| **2-3** | Receive | PCBs | - |
| **3** | Receive | Standard components | - |
| **3-4** | Receive | Inductor cores | - |

**Critical Path:** Inductor cores (2-3 week lead time)

**Recommendation:** Order cores immediately once inductor design finalized

---

## 7. ASSEMBLY INSTRUCTIONS

### 7.1 Pre-Assembly Preparation

**Tools Required:**
- Soldering iron (adjustable temperature, 315-370°C)
- Solder (60/40 Sn/Pb or SAC305 lead-free)
- Wire cutters (flush cut)
- Long-nose pliers
- Multimeter
- Magnifier or microscope
- ESD wrist strap (recommended)

**Workspace Setup:**
- ESD-safe mat
- Good lighting
- Component organizer
- Solder fume extraction

### 7.2 Assembly Sequence

**Step 1: Screw Terminal Installation (30 minutes)**
1. Install J_IN, J_OUT, J_GND first (establish orientation)
2. Install control terminals (J_BOOST_SEL_SND, J_BOOST_SEL_RET, J_CUT_SEL_SND, J_BOOST_LVL)
3. Install inductor terminals (J_IND_20HZ, J_IND_30HZ, J_IND_60HZ, J_IND_100HZ)
4. Ensure terminals are flush against PCB
5. Solder from bottom side
6. Inspect: All pins soldered, no cold joints, no bridges

**Step 2: Resistor Installation (5 minutes)**
1. Bend R2 (56kΩ) leads to 10.16mm spacing
2. Insert through PCB
3. Bend leads on bottom to secure
4. Solder and trim excess leads
5. Verify with multimeter: 56kΩ ±1%

**Step 3: Capacitor Installation (30 minutes)**
1. Install in order of value (largest first for organization):
   - C1 (18nF), C2 (10nF), C3 (4.7nF), C4 (3.3nF), C5 (2.2nF)
   - C4a2 (1nF), C5a2 (1.5nF), C6 (1.8nF), C7 (1nF)
   - C34 (1nF), C35 (1nF)
2. Film capacitors are non-polarized (no polarity concern)
3. Insert, bend leads, solder, trim
4. Double-check values before soldering (difficult to desolder)

**Step 4: Post-Assembly Inspection (15 minutes)**
1. Visual inspection with magnifier:
   - All solder joints shiny and smooth (no cold joints)
   - No solder bridges between pads
   - All components properly seated
   - No lifted pads or damaged traces
2. Clean flux residue if necessary
3. Label inductor terminals with frequency markings (if not already on silkscreen)

### 7.3 Inductor Connection

**External Inductor Wiring:**
1. Hand-wound inductors mount separately (not on PCB)
2. Connect each inductor to corresponding terminal:
   - L_20Hz → J_IND_20HZ
   - L_30Hz → J_IND_30HZ
   - L_60Hz → J_IND_60HZ
   - L_100Hz → J_IND_100HZ
3. Use 18-22 AWG stranded wire, keep length <30cm
4. Twist pair for noise reduction (optional but recommended)
5. Label each inductor wire clearly

---

## 8. TESTING AND VALIDATION

### 8.1 Initial Electrical Testing

**Visual Inspection:**
- [ ] All components installed per BOM
- [ ] No solder bridges
- [ ] No cold solder joints
- [ ] All terminal screws accessible
- [ ] No physical damage

**Continuity Testing:**
- [ ] Input to output path (depends on selector position)
- [ ] Ground continuity (all grounds to J_GND)
- [ ] No shorts between adjacent traces

**Component Value Verification:**
- [ ] R2 = 56kΩ ±1% (multimeter)
- [ ] Spot-check capacitor values with LCR meter (if available)

**Inductor Testing (Critical):**
- [ ] Measure each inductor with LCR meter @ 120Hz:
  - L_20Hz: 35.16H ±10%
  - L_30Hz: 28.15H ±10%
  - L_60Hz: 14.98H ±10%
  - L_100Hz: 7.68H ±10%
- [ ] Measure DCR of each inductor:
  - Target: <5Ω for all inductors
  - Acceptable: <10Ω
  - Marginal: <20Ω
- [ ] Calculate Q = 2πfL/DCR:
  - Target: Q >20 at resonant frequency
  - Good: Q >50
  - Excellent: Q >100

### 8.2 Bench Testing (No System Integration)

**Test Equipment:**
- Audio signal generator (20Hz-20kHz sine wave)
- Oscilloscope or audio analyzer
- Multimeter
- Function generator (optional)

**Procedure:**
1. **Inject 1kHz sine wave at J_IN**
   - Expected: Signal passes through with ~20dB insertion loss
   - Verify at J_OUT with oscilloscope
   - Should be flat response at 1kHz (not a boost frequency)

2. **Test Each Frequency Position:**
   - Connect to external frequency selector switch
   - Set selector to 20Hz position
   - Inject 20Hz sine wave
   - Measure boost at J_OUT
   - Expected: +X dB boost (depends on J_BOOST_LVL setting)
   - Repeat for 30Hz, 60Hz, 100Hz

3. **Frequency Sweep:**
   - Sweep 10Hz-200Hz with signal generator
   - Plot frequency response
   - Verify peak at selected frequency
   - Measure Q (bandwidth at -3dB points)

### 8.3 Integration Testing

**System Integration:**
1. Connect module in signal chain:
   - Input Stage → Low Cut → **Low Boost** → High Boost → High Cut → Output Stage
2. Test with actual audio material (music, pink noise)
3. Verify selector switching (no pops or clicks)
4. Test boost level control (smooth adjustment, no noise)
5. Check for hum or noise (50/60Hz power line interference)

**Pass/Fail Criteria:**
- [ ] All four frequencies boost correctly
- [ ] Boost range 0-11dB (approximately)
- [ ] Selector switches cleanly
- [ ] No audible noise or distortion
- [ ] Inductor Q >20 for all frequencies
- [ ] No ground loops or hum

### 8.4 Performance Characterization

**Measurements to Document:**
- Frequency response plot (20Hz-20kHz, all selector positions)
- Insertion loss at 1kHz: ~20.8dB (expected)
- Peak boost frequency and amplitude (each position)
- Q factor (bandwidth) at each frequency
- THD+N at 1kHz, +4dBu input level
- Noise floor with no signal

---

## 9. TIMELINE AND MILESTONES

### 9.1 Overall Project Schedule

**Total Duration:** 6-8 weeks (optimistic), 10-13 weeks (conservative)

| Phase | Duration | Dependencies |
|-------|----------|--------------|
| Design Finalization | 1-2 weeks | None |
| Procurement | 2-4 weeks | Design complete |
| Inductor Winding | 1-2 weeks | Cores received |
| PCB Assembly | 1 week | PCBs and components received |
| Testing & Integration | 1-2 weeks | Assembly complete |

### 9.2 Detailed Milestone Timeline

#### Week 0-1: Design Finalization
- [ ] Review circuit topology and calculations
- [ ] Finalize inductor specifications
- [ ] Complete KiCAD schematic
- [ ] Complete PCB layout
- [ ] Run ERC and DRC (zero errors)
- [ ] Generate Gerber files
- [ ] Generate BOM
- **Deliverable:** Manufacturing-ready design files

#### Week 1-2: Procurement
- [ ] Order inductor cores (Amidon/Hammond)
- [ ] Order magnet wire (BNTECHGO/DigiKey)
- [ ] Submit PCBs to fabrication
- [ ] Order standard components (Mouser)
- [ ] Track all shipments
- **Deliverable:** All materials ordered

#### Week 2-3: Receiving
- [ ] Receive magnet wire (Week 2)
- [ ] Receive PCBs (Week 2-3)
- [ ] Receive standard components (Week 3)
- [ ] Inspect all received materials
- **Deliverable:** All materials on hand (except cores)

#### Week 3-4: Core Arrival
- [ ] Receive inductor cores
- [ ] Inspect cores (no damage, correct specifications)
- **Deliverable:** Ready to begin winding

#### Week 4-6: Inductor Winding
- [ ] Wind 20Hz inductor (2-3 hours)
- [ ] Test 20Hz inductor (measure L, DCR, Q)
- [ ] Wind 30Hz inductor (1.5-2 hours)
- [ ] Test 30Hz inductor
- [ ] Wind 60Hz inductor (1-1.5 hours)
- [ ] Test 60Hz inductor
- [ ] Wind 100Hz inductor (1 hour)
- [ ] Test 100Hz inductor
- [ ] Verify all inductors meet specifications
- [ ] Rework if needed (add/remove turns)
- **Deliverable:** 4 tested, working inductors

#### Week 6: PCB Assembly
- [ ] Install screw terminals
- [ ] Install resistor
- [ ] Install capacitors
- [ ] Visual inspection
- [ ] Continuity testing
- [ ] Component value verification
- **Deliverable:** Assembled PCB, ready for integration

#### Week 7-8: Integration and Testing
- [ ] Connect inductors to PCB
- [ ] Bench testing (frequency sweep, boost verification)
- [ ] Connect to input/output stages
- [ ] System integration testing
- [ ] Performance characterization
- [ ] Final adjustments
- **Deliverable:** Working, tested Low Boost module

### 9.3 Critical Path Items

**Critical Path** (longest sequence, determines overall timeline):
1. Inductor design (Week 0-1)
2. Core ordering and delivery (Week 1-4) ← **LONGEST LEAD TIME**
3. Inductor winding (Week 4-6)
4. Final assembly and testing (Week 6-8)

**Parallel Paths** (can happen simultaneously):
- PCB design and fabrication (Week 1-3)
- Component ordering and delivery (Week 2-3)
- Wire ordering and delivery (Week 1-2)

### 9.4 Buffer Time Allocation

**Built-In Buffers:**
- Component delays: +1 week
- PCB fabrication delays: +1 week
- Core sourcing delays: +2 weeks (already in 2-3 week estimate)
- Inductor winding learning curve: +1 week
- Testing iterations: +1 week
- **Total Buffer: 6 weeks**

**Risk-Adjusted Schedule:**
- Optimistic (everything perfect): 6-8 weeks
- Realistic (typical delays): 10-11 weeks
- Conservative (significant delays): 12-13 weeks

**Recommendation:** Plan for realistic timeline (10-11 weeks) to manage expectations.

---

## 10. RISK MANAGEMENT

### 10.1 High-Risk Items

#### Risk 1: Inductor Values Uncertain
- **Description:** Circuit topology requires analysis; calculated values may need adjustment
- **Impact:** Cannot order cores or begin winding
- **Probability:** Medium
- **Mitigation:**
  - Thorough schematic review before ordering
  - Consult reference documentation (Ian Thompson-Bell)
  - Order spare cores for experimentation
  - Design for adjustability (add/remove turns)
- **Contingency:** Order cores with adjustable AL value; use variable turns count

#### Risk 2: Inductor Core Availability
- **Description:** Specialty items, limited suppliers, long lead times
- **Impact:** 2-3 week delay if out of stock
- **Probability:** Medium
- **Mitigation:**
  - Check stock before finalizing design
  - Order immediately once values confirmed
  - Identify alternate core sizes/types
  - Consider eBay or surplus suppliers
- **Contingency:** Use different core size, recalculate turns; use multiple smaller cores in series

#### Risk 3: First-Time Inductor Winding
- **Description:** Learning curve, potential for errors, time-consuming
- **Impact:** Wasted time, potentially damaged cores
- **Probability:** High (first-time builders)
- **Mitigation:**
  - Order extra cores (1-2 spares)
  - Practice winding technique on scrap core
  - Follow winding instructions meticulously
  - Test frequently during winding process
  - Document actual turns count for repeatability
- **Contingency:** Unwind and re-wind if inductance incorrect; purchase pre-wound inductors if available

### 10.2 Medium-Risk Items

#### Risk 4: PCB Design Errors
- **Description:** First PCB layout for this module, potential mistakes
- **Impact:** Board unusable, requires re-spin (2-3 weeks)
- **Probability:** Medium
- **Mitigation:**
  - Thorough review before submission
  - Run ERC and DRC multiple times
  - 3D viewer check for mechanical fit
  - Order extra boards (5-10 vs. minimum)
  - Peer review if possible
- **Contingency:** Build prototype on perfboard; order PCB rev 2.0

#### Risk 5: Component Availability
- **Description:** Vishay capacitors or Phoenix terminals out of stock
- **Impact:** Minor delay, easy substitution
- **Probability:** Low-Medium
- **Mitigation:**
  - Check stock before ordering
  - Have alternative part numbers ready
  - Use multiple suppliers (Mouser, DigiKey)
  - Accept wider tolerances if needed (±10% vs ±5%)
- **Contingency:** Substitute WIMA, EPCOS, or Kemet capacitors; use On Shore or Wurth terminals

### 10.3 Low-Risk Items

#### Risk 6: Shipping Delays
- **Description:** Weather, holidays, customs issues
- **Impact:** 1-2 week delay
- **Probability:** Medium (but low impact)
- **Mitigation:**
  - Order early in project
  - Use expedited shipping for critical items
  - Track all packages
  - Have buffer time in schedule
- **Contingency:** Wait; no alternative

#### Risk 7: Testing Equipment Availability
- **Description:** Need LCR meter for inductor testing, signal generator for frequency response
- **Impact:** Cannot verify proper operation
- **Probability:** Low (can borrow or buy cheaply)
- **Mitigation:**
  - Arrange access to test equipment early
  - Purchase basic LCR meter (~$30-50)
  - Use PC sound card as signal generator (free)
  - Use multimeter for basic DC tests
- **Contingency:** Send to friend/lab for testing; use in-circuit testing

### 10.4 Risk Mitigation Summary

**Proactive Measures:**
1. Order spare cores and wire (add 20% to quantities)
2. Order extra PCBs (5 or 10 vs. minimum)
3. Have alternative component part numbers ready
4. Build in 6 weeks of buffer time
5. Document everything (turns count, measurements, issues)
6. Test frequently throughout build
7. Arrange test equipment access early

**Reactive Measures:**
1. If inductor wrong: Adjust turns, re-wind if needed
2. If PCB wrong: Build on perfboard, order rev 2.0
3. If component unavailable: Substitute from alternatives list
4. If cores unavailable: Use different size, recalculate
5. If behind schedule: Focus on critical path items, parallelize where possible

---

## 11. DOCUMENTATION AND DELIVERABLES

### 11.1 Design Documentation

**Schematic Files:**
- [ ] KiCAD schematic (.kicad_sch)
- [ ] Schematic PDF export
- [ ] Netlist for PCB

**PCB Files:**
- [ ] KiCAD PCB layout (.kicad_pcb)
- [ ] 3D render (PNG or STEP)
- [ ] Assembly drawing PDF

**Manufacturing Files:**
- [ ] Gerber files (all layers)
- [ ] Drill files (PTH, NPTH)
- [ ] BOM (CSV format)
- [ ] Pick-and-place file (optional)

### 11.2 Inductor Documentation

**Inductor Specifications:**
- [ ] Complete design calculations (L, DCR, Q for each frequency)
- [ ] Core specifications (manufacturer, part number, dimensions)
- [ ] Wire specifications (gauge, length, type)
- [ ] Winding instructions (turns count, layer arrangement)
- [ ] Test procedures (how to verify inductance and Q)

**As-Built Documentation:**
- [ ] Actual turns count for each inductor (may differ from calculated)
- [ ] Measured inductance (LCR meter readings)
- [ ] Measured DCR
- [ ] Calculated Q factor
- [ ] Photos of completed inductors

### 11.3 Test Results

**Bench Test Data:**
- [ ] Frequency response plots (all selector positions)
- [ ] Boost amplitude vs. frequency (each position)
- [ ] Insertion loss at 1kHz
- [ ] Q factor measurements
- [ ] THD+N measurements

**Integration Test Data:**
- [ ] Full signal chain frequency response
- [ ] Interaction with other modules
- [ ] Noise floor measurements
- [ ] Selector switching verification

### 11.4 Assembly Instructions

- [ ] Step-by-step assembly procedure (this document, section 7)
- [ ] Photos of each assembly stage
- [ ] Troubleshooting guide
- [ ] Common mistakes and solutions

### 11.5 Project Summary

**Final Report Contents:**
- Project overview and objectives
- Circuit design and analysis
- Inductor design and fabrication
- PCB layout and manufacturing
- Component sourcing and costs
- Assembly and testing procedures
- Test results and performance characterization
- Lessons learned and recommendations for rev 2.0

---

## 12. REFERENCES

### 12.1 Project Files

- **Module Documentation:** `/Users/orion/work/multi-channel-preamp/src/pultec/modules/low-boost/README.md`
- **Component Values:** `/Users/orion/work/multi-channel-preamp/src/pultec/docs/1.0/COMPONENT_VALUES.md`
- **System Overview:** `/Users/orion/work/multi-channel-preamp/src/pultec/docs/1.0/SYSTEM_OVERVIEW.md`
- **Original Schematic:** `/Users/orion/work/multi-channel-preamp/src/schematics/pultec-three-band-eq/pultec-three-band-eq.kicad_sch`
- **BOM:** `/Users/orion/work/multi-channel-preamp/src/pultec/modules/low-boost/BOM.csv`

### 12.2 Reference Documentation

**Ian Thompson-Bell Pultec Documentation:**
- Location: `/Users/orion/work/multi-channel-preamp/reference/pultec-style-eq/`
- Contains inductor design guidance, component calculations, and circuit analysis

**Similar Modules:**
- Low Cut: `/Users/orion/work/multi-channel-preamp/src/schematics/pultec-cut-low/`
- High Boost: `/Users/orion/work/multi-channel-preamp/src/schematics/pultec-boost-high/`
- High Cut: `/Users/orion/work/multi-channel-preamp/src/schematics/pultec-cut-high/`

### 12.3 Technical Resources

**Inductor Design:**
- Hammond Manufacturing core datasheets
- Amidon core selection guides
- Inductor winding calculators and formulas
- Q factor optimization techniques

**PCB Design:**
- KiCAD documentation and tutorials
- Audio PCB layout best practices
- Star grounding techniques
- Phoenix Contact terminal datasheets

**Component Datasheets:**
- Vishay MKT1813 film capacitors
- Phoenix Contact 1757 screw terminals
- Hammond E-I lamination cores
- Magnet wire specifications

---

## 13. CONCLUSION

This workplan provides comprehensive, step-by-step guidance for implementing the Low Boost module from design through testing. Success depends on:

1. **Careful inductor design** - The critical path item requiring the most attention
2. **Thorough PCB layout** - Audio-optimized grounding and routing
3. **Precise procurement** - Ordering long-lead items early
4. **Patient assembly** - Taking time to wind and test inductors properly
5. **Systematic testing** - Verifying each stage before proceeding

**Expected Outcome:** A working Low Boost module providing 0-11dB boost at 20Hz, 30Hz, 60Hz, and 100Hz with excellent audio quality (Q >20, low THD+N).

**Timeline:** 6-8 weeks (optimistic) to 10-13 weeks (realistic)

**Cost:** $80-102 per unit (single prototype) or $56-69 per unit (3-unit build)

**Next Action:** Begin inductor design work using the specifications in Section 3 of this document.

---

**Document prepared by:** Multi-agent team (circuit-design-specialist, inductor-design-specialist, kicad-expert, pcb-layout-engineer, bom-and-sourcing)
**Date:** 2025-10-26
**Revision:** 1.0
**Status:** Ready for Implementation
