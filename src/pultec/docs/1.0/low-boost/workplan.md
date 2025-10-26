# LOW-BOOST MODULE - Complete Workplan
## From Schematic to PCBWay Manufacturing

**Project**: Pultec Three-Band EQ - Low Boost Module
**Date Created**: 2025-10-26
**Revision**: 1.0
**Status**: Ready for Execution

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Current Status Assessment](#2-current-status-assessment)
3. [Phase 1: Schematic Completion](#3-phase-1-schematic-completion)
4. [Phase 2: PCB Layout Creation](#4-phase-2-pcb-layout-creation)
5. [Phase 3: Manufacturing File Generation](#5-phase-3-manufacturing-file-generation)
6. [Phase 4: PCBWay Submission](#6-phase-4-pcbway-submission)
7. [Agent Responsibilities](#7-agent-responsibilities)
8. [Quality Checklist](#8-quality-checklist)
9. [Timeline and Milestones](#9-timeline-and-milestones)
10. [Risk Assessment](#10-risk-assessment)
11. [Success Criteria](#11-success-criteria)
12. [References](#12-references)

---

## 1. Project Overview

### Module Description

The **Low-Boost Module** is a passive LC resonant network that provides frequency-selective boost in the low-frequency range (20Hz, 30Hz, 60Hz, 100Hz). This is one of four modular PCBs in the Pultec Three-Band EQ system.

**Circuit Topology**: Passive LC network with hand-wound external inductors
**Frequency Range**: 20Hz - 100Hz (4 selectable positions)
**Complexity**: High (11 capacitors, 1 resistor, 9 screw terminals, 4 inductor connections)

### Current Status

- ✅ **Component values extracted** from monolithic schematic
- ✅ **Documentation created**: README, BOM, PCB_LAYOUT spec, INDUCTOR_SPECS
- ✅ **Template schematic** exists at `src/pultec/modules/low-boost/low-boost.kicad_sch`
- ⚠️ **KiCAD MCP server** now connected and operational
- ❌ **Schematic not finalized** (needs component population and ERC)
- ❌ **PCB layout not created**
- ❌ **Manufacturing files not generated**

### Goals and Deliverables

**Primary Goal**: Complete Low-Boost module and submit to PCBWay for fabrication

**Key Deliverables**:
1. Finalized KiCAD schematic (with ERC clean)
2. Complete PCB layout (100mm × 120mm, 2-layer)
3. Manufacturing file package (Gerbers, drill files, assembly drawings)
4. PCBWay order placed with correct specifications
5. Documentation package ready for assembly

**Success Metric**: Manufacturable PCB design submitted to PCBWay, ready for fabrication

---

## 2. Current Status Assessment

### Existing Assets

| Asset | Location | Status | Notes |
|-------|----------|--------|-------|
| Module README | `src/pultec/modules/low-boost/README.md` | ✅ Complete | Comprehensive specs |
| PCB Layout Spec | `src/pultec/modules/low-boost/PCB_LAYOUT.md` | ✅ Complete | Detailed layout guide |
| Bill of Materials | `src/pultec/modules/low-boost/BOM.csv` | ✅ Complete | All parts sourced |
| Inductor Specs | `src/pultec/modules/low-boost/INDUCTOR_SPECS.md` | ✅ Complete | Winding instructions |
| Template Schematic | `src/pultec/modules/low-boost/low-boost.kicad_sch` | ⚠️ Partial | Needs population |
| Schematic Guide | `src/pultec/SCHEMATIC_CREATION_GUIDE.md` | ✅ Complete | Step-by-step guide |
| Component Values | `src/pultec/docs/1.0/COMPONENT_VALUES.md` | ✅ Complete | Reference values |

### Known Challenges

1. **Capacitor Value Ambiguity**: INDUCTOR_SPECS.md notes potential error in capacitor values (nF vs µF)
   - **Action Required**: Verify in original schematic before finalizing
   - **Impact**: Critical for inductor design

2. **Complex Connectivity**: 11 capacitors + 4 inductor connections + multiple selectors
   - **Mitigation**: Use clear net labels and functional grouping

3. **Star Grounding Critical**: Audio quality depends on proper ground implementation
   - **Mitigation**: Follow PCB_LAYOUT.md star ground specifications exactly

4. **External Inductor Integration**: 4 hand-wound inductors not on PCB
   - **Mitigation**: Clear terminal labeling and connection diagrams

### Prerequisites Checklist

- [x] KiCAD 7.x or 8.x installed
- [x] KiCAD MCP server connected
- [x] Phoenix Contact footprint library available
- [x] Component specifications finalized
- [x] PCB layout specifications documented
- [x] Inductor design specifications complete
- [ ] Capacitor values verified (nF vs µF) - **CRITICAL**

---

## 3. Phase 1: Schematic Completion

**Objective**: Create production-ready KiCAD schematic with all components, wiring, and ERC clean

**Estimated Time**: 4-6 hours
**Dependencies**: None
**Deliverable**: `low-boost.kicad_sch` with exported PDF

### 3.1 Critical Pre-Work: Verify Capacitor Values

**Priority**: CRITICAL - Must complete before proceeding

- [ ] Open original monolithic schematic: `src/schematics/pultec-three-band-eq/pultec-three-band-eq.kicad_sch`
- [ ] Locate low-boost section (components C1-C7, C34, C35, C4a2, C5a2)
- [ ] Verify capacitor values and units (nF or µF)
- [ ] Cross-reference with Ian Thompson-Bell documentation in `reference/` directory
- [ ] Document findings in this workplan
- [ ] Update COMPONENT_VALUES.md if corrections needed
- [ ] Update INDUCTOR_SPECS.md if corrections needed

**Decision Point**: If capacitors are µF (not nF), inductor values in INDUCTOR_SPECS.md are correct. If nF, frequencies or design may need revision.

### 3.2 Component Addition (All 23 Components)

**Using KiCAD GUI or MCP Commands**

#### Capacitors (11 total)

**Film capacitors, all 5.08mm pitch, Vishay MKT1813 series**

- [ ] **C1**: 18nF (or 18µF - verify first!)
  - Symbol: `Device:C`
  - Footprint: `Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm`
  - MPN: `MKT1813183104` (or electrolytic if µF)

- [ ] **C2**: 10nF (or 10µF)
  - Symbol: `Device:C`
  - Footprint: `Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm`
  - MPN: `MKT1813103104`

- [ ] **C3**: 4.7nF (or 4.7µF)
  - Symbol: `Device:C`
  - Footprint: `Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm`
  - MPN: `MKT1813472104`

- [ ] **C4**: 3.3nF (or 3.3µF)
  - Symbol: `Device:C`
  - Footprint: `Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm`
  - MPN: `MKT1813332104`

- [ ] **C5**: 2.2nF (or 2.2µF)
  - Symbol: `Device:C`
  - Footprint: `Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm`
  - MPN: `MKT1813222104`

- [ ] **C4a2**: 1nF (or 1µF)
  - Symbol: `Device:C`
  - Footprint: `Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm`
  - MPN: `MKT1813102104`

- [ ] **C5a2**: 1.5nF (or 1.5µF)
  - Symbol: `Device:C`
  - Footprint: `Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm`
  - MPN: `MKT1813152104`

- [ ] **C6**: 1.8nF
  - Symbol: `Device:C`
  - Footprint: `Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm`
  - MPN: `MKT1813182104`

- [ ] **C7**: 1nF
  - Symbol: `Device:C`
  - Footprint: `Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm`
  - MPN: `MKT1813102104`

- [ ] **C34**: 1nF (input coupling)
  - Symbol: `Device:C`
  - Footprint: `Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm`
  - MPN: `MKT1813102104`

- [ ] **C35**: 1nF (output coupling)
  - Symbol: `Device:C`
  - Footprint: `Capacitor_THT:C_Rect_L7.0mm_W3.5mm_P5.00mm`
  - MPN: `MKT1813102104`

#### Resistor (1 total)

- [ ] **R2**: 56kΩ, 1/4W, 1%
  - Symbol: `Device:R`
  - Footprint: `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm`
  - MPN: `MRS25000C5602FCT00` (Vishay MRS25)

#### Screw Terminals (9 total - Phoenix Contact 1757 series)

**2-position terminals (5 total)**

- [ ] **J_IN**: Signal input from Low-Cut module
  - Symbol: `Connector:Screw_Terminal_01x02`
  - Footprint: `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.08mm_Horizontal`
  - MPN: `1757019`
  - Labels: "IN+", "IN-"

- [ ] **J_OUT**: Signal output to High-Boost module
  - Symbol: `Connector:Screw_Terminal_01x02`
  - Footprint: `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.08mm_Horizontal`
  - MPN: `1757019`
  - Labels: "OUT+", "OUT-"

- [ ] **J_GND**: Ground connection
  - Symbol: `Connector:Screw_Terminal_01x02`
  - Footprint: `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.08mm_Horizontal`
  - MPN: `1757019`
  - Labels: "GND", "GND"

**Inductor connection terminals (4 × 2-position)**

- [ ] **J_IND_20HZ**: 20Hz inductor connection
  - Symbol: `Connector:Screw_Terminal_01x02`
  - Footprint: `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.08mm_Horizontal`
  - MPN: `1757019`
  - Labels: "20Hz_L1", "20Hz_L2"

- [ ] **J_IND_30HZ**: 30Hz inductor connection
  - Symbol: `Connector:Screw_Terminal_01x02`
  - Footprint: `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.08mm_Horizontal`
  - MPN: `1757019`
  - Labels: "30Hz_L1", "30Hz_L2"

- [ ] **J_IND_60HZ**: 60Hz inductor connection
  - Symbol: `Connector:Screw_Terminal_01x02`
  - Footprint: `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.08mm_Horizontal`
  - MPN: `1757019`
  - Labels: "60Hz_L1", "60Hz_L2"

- [ ] **J_IND_100HZ**: 100Hz inductor connection
  - Symbol: `Connector:Screw_Terminal_01x02`
  - Footprint: `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.08mm_Horizontal`
  - MPN: `1757019`
  - Labels: "100Hz_L1", "100Hz_L2"

**3-position terminals (2 total)**

- [ ] **J_CUT_SEL_SND**: Low-cut selector send (interface to other module)
  - Symbol: `Connector:Screw_Terminal_01x03`
  - Footprint: `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-3_1x03_P5.08mm_Horizontal`
  - MPN: `1757022`
  - Labels: "CUT_SND1", "CUT_SND2", "CUT_SND3"

- [ ] **J_BOOST_LVL**: Boost level control (to external potentiometer)
  - Symbol: `Connector:Screw_Terminal_01x03`
  - Footprint: `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-3_1x03_P5.08mm_Horizontal`
  - MPN: `1757022`
  - Labels: "LVL1", "LVL2", "LVL3"

**6-position terminals (2 total)**

- [ ] **J_BOOST_SEL_SND**: Frequency selector send (to rotary switch)
  - Symbol: `Connector:Screw_Terminal_01x06`
  - Footprint: `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-6_1x06_P5.08mm_Horizontal`
  - MPN: `1757025`
  - Labels: "SEL_SND1" through "SEL_SND6"

- [ ] **J_BOOST_SEL_RET**: Frequency selector return (from rotary switch)
  - Symbol: `Connector:Screw_Terminal_01x06`
  - Footprint: `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-6_1x06_P5.08mm_Horizontal`
  - MPN: `1757025`
  - Labels: "SEL_RET1" through "SEL_RET6"

#### Power Symbols (2 total)

- [ ] **#PWR01**: GND at input
- [ ] **#PWR02**: GND at output

### 3.3 LC Resonant Circuit Wiring Strategy

**Circuit Topology** (from original Pultec design):

```
            ┌─────────────────────────────────────────┐
            │                                         │
J_IN+ ──►─ C34 ─┬─ C1,C2,C3,C4,C5... ─┬─► J_BOOST_SEL_SND ─► Rotary Switch
               │   (selector network)  │
               │                       │
               └────────► R2 ──────────┘
                          │
                          │
           Rotary Switch ◄─ J_BOOST_SEL_RET
                          │
                          ├─► J_IND_20HZ ─► L1 (20Hz) ──┐
                          ├─► J_IND_30HZ ─► L2 (30Hz) ──┤
                          ├─► J_IND_60HZ ─► L3 (60Hz) ──┼─► Back to network
                          └─► J_IND_100HZ ► L4 (100Hz) ─┘
                                  │
                          J_BOOST_LVL ──► Level Pot ──► C35 ──► J_OUT+
                                  │
                                 GND
```

**Wiring Steps**:

1. [ ] **Input Stage**
   - Wire J_IN+ to C34 (input coupling capacitor)
   - Wire C34 to capacitor selector network junction
   - Wire J_IN- to GND (#PWR01)

2. [ ] **Capacitor Selector Network**
   - Connect C1-C7, C4a2, C5a2 to J_BOOST_SEL_SND positions
   - Each capacitor gets one position on 6-position terminal
   - Common node connects to R2 and inductor return path

3. [ ] **Frequency Selector Interface**
   - Wire capacitor nodes to J_BOOST_SEL_SND (send to external rotary switch)
   - Wire J_BOOST_SEL_RET (return from rotary switch) to inductor terminal selector

4. [ ] **Inductor Connections**
   - Each inductor terminal (J_IND_20HZ through J_IND_100HZ) connects:
     - Pin 1: To frequency selector return circuit
     - Pin 2: Return to resonant network common node

5. [ ] **Level Control**
   - Wire resonant network output to J_BOOST_LVL (external potentiometer)
   - Wire potentiometer wiper (via J_BOOST_LVL) through R2 to network

6. [ ] **Output Stage**
   - Wire level control output to C35 (output coupling capacitor)
   - Wire C35 to J_OUT+
   - Wire J_OUT- to GND (#PWR02)

7. [ ] **Ground Connections**
   - Connect all ground points (J_IN-, J_OUT-, capacitor grounds) to GND symbols
   - Add J_GND terminal connected to GND for star ground connection

**Net Labels to Add**:
- [ ] `SIG_IN` at J_IN+ connection
- [ ] `SIG_OUT` at J_OUT+ connection
- [ ] `BOOST_SEL_SND_1` through `BOOST_SEL_SND_6` at selector send
- [ ] `BOOST_SEL_RET_1` through `BOOST_SEL_RET_6` at selector return
- [ ] `IND_20HZ_L1`, `IND_20HZ_L2` at 20Hz inductor terminal
- [ ] `IND_30HZ_L1`, `IND_30HZ_L2` at 30Hz inductor terminal
- [ ] `IND_60HZ_L1`, `IND_60HZ_L2` at 60Hz inductor terminal
- [ ] `IND_100HZ_L1`, `IND_100HZ_L2` at 100Hz inductor terminal
- [ ] `BOOST_LVL_1`, `BOOST_LVL_2`, `BOOST_LVL_3` at level control
- [ ] `GND` at all ground points

### 3.4 Title Block Configuration

- [ ] **Title**: "PULTEC THREE-BAND EQ - LOW BOOST MODULE"
- [ ] **Revision**: "1.0"
- [ ] **Date**: Current date (YYYY-MM-DD format)
- [ ] **Company**: Your company or "Open Hardware"
- [ ] **Sheet**: "1 of 1"
- [ ] **Comment 1**: "Low Frequency Boost Circuit (20Hz, 30Hz, 60Hz, 100Hz)"
- [ ] **Comment 2**: "Requires 4 external hand-wound inductors"
- [ ] **Comment 3**: "All capacitors: Vishay MKT1813 film, 5%, 100V"
- [ ] **Comment 4**: "Terminals: Phoenix Contact 1757 series, 5.08mm pitch"

### 3.5 Annotation and Cross-References

- [ ] Use KiCAD annotation tool: Tools → Annotate Schematic
- [ ] Verify all references are unique and sequential
- [ ] Add text annotations:
  - [ ] "External Inductor: See INDUCTOR_SPECS.md" near each inductor terminal
  - [ ] "20Hz: 3.5H" annotation near J_IND_20HZ
  - [ ] "30Hz: 2.8H" annotation near J_IND_30HZ
  - [ ] "60Hz: 1.5H" annotation near J_IND_60HZ
  - [ ] "100Hz: 0.77H" annotation near J_IND_100HZ
  - [ ] "Star Ground Required" annotation near J_GND

### 3.6 Electrical Rules Check (ERC)

**Run ERC**: Tools → Electrical Rules Checker

**Expected Warnings** (acceptable):
- Pin-to-pin warnings on screw terminals (normal for multi-position connectors)
- "Power pin not driven" if GND symbols used (can be ignored if properly connected)

**Errors to Resolve** (must fix):
- Unconnected pins (all pins must connect or be marked "No Connect")
- Power input not driven (verify GND connections)
- Conflicting net names
- Duplicate references

**ERC Clean Criteria**:
- [ ] Zero errors
- [ ] All warnings reviewed and justified
- [ ] All nets properly labeled
- [ ] All power pins connected

### 3.7 Schematic Export

- [ ] Export PDF: File → Plot → Select PDF
  - Filename: `low-boost-schematic.pdf`
  - Location: `src/pultec/modules/low-boost/`
  - Options: Color, include title block, one page per sheet

- [ ] Export PNG (optional, for documentation):
  - Filename: `low-boost-schematic.png`
  - Resolution: 300 DPI minimum

- [ ] Generate Netlist: Tools → Generate Netlist
  - Format: KiCAD (for PCB import)
  - Filename: `low-boost.net`
  - Location: `src/pultec/modules/low-boost/`

### 3.8 Phase 1 Deliverables Checklist

- [ ] All 23 components added and annotated
- [ ] All components have correct values and footprints
- [ ] All components have MPN custom field populated
- [ ] Circuit wiring complete per topology
- [ ] Net labels applied to all critical signals
- [ ] Title block complete
- [ ] ERC clean (zero errors, warnings justified)
- [ ] PDF schematic exported
- [ ] Netlist generated
- [ ] Capacitor value ambiguity resolved (nF vs µF)

**Phase 1 Sign-Off**: Ready to proceed to PCB layout when all items checked

---

## 4. Phase 2: PCB Layout Creation

**Objective**: Create production-ready 2-layer PCB layout with proper component placement, routing, and grounding

**Estimated Time**: 8-12 hours
**Dependencies**: Phase 1 complete (schematic finalized, netlist generated)
**Deliverable**: `low-boost.kicad_pcb` ready for DRC and manufacturing file generation

### 4.1 Board Setup

**Open PCB Editor**: KiCAD → PCB Editor (pcbnew)

#### 4.1.1 Import Netlist

- [ ] File → Import → Netlist
- [ ] Select `low-boost.net` (generated in Phase 1)
- [ ] Review component list
- [ ] Import all components
- [ ] Verify footprint assignments

#### 4.1.2 Board Dimensions and Edge Cuts

**Board Size**: 100mm × 120mm (per PCB_LAYOUT.md specification)

- [ ] Select Edge.Cuts layer
- [ ] Draw rectangle: 100mm wide × 120mm tall
  - Use "Draw Rectangle" tool
  - Start point: (0, 0)
  - End point: (100, 120)
- [ ] Add corner radius: 2mm radius on all corners (optional, recommended for professional look)
- [ ] Verify board outline is closed polygon

#### 4.1.3 Mounting Holes (4× M3)

**Position**: 3mm from edges (per PCB_LAYOUT.md)

- [ ] **Hole 1** (top-left): X=3mm, Y=3mm
  - Hole diameter: 3.2mm
  - Pad diameter: 6mm
  - Layer: Through-hole, all layers

- [ ] **Hole 2** (top-right): X=97mm, Y=3mm

- [ ] **Hole 3** (bottom-right): X=97mm, Y=117mm

- [ ] **Hole 4** (bottom-left): X=3mm, Y=117mm

- [ ] Add keep-out zones around mounting holes:
  - Diameter: 8mm
  - No copper, no silkscreen within keep-out

#### 4.1.4 Design Rules Setup

**Navigate to**: File → Board Setup → Design Rules → Constraints

**Minimum Values** (per PCB_LAYOUT.md):

- [ ] **Minimum Trace Width**: 0.25mm (default minimum, use 0.6mm in practice)
- [ ] **Minimum Clearance**: 0.25mm (use 0.5mm for safety margin)
- [ ] **Minimum Via Diameter**: 0.8mm (drill), 1.3mm (pad)
- [ ] **Minimum Annular Ring**: 0.15mm

**Working Values** (actually use these):

- [ ] **Signal Traces**: 0.8mm width
- [ ] **Control Traces**: 0.6mm width
- [ ] **Ground Traces** (top layer): 2.0mm width
- [ ] **Via Drill**: 0.8mm
- [ ] **Via Pad**: 1.3mm
- [ ] **Trace-to-trace Clearance**: 0.5mm (0.8mm preferred)
- [ ] **Trace-to-edge Clearance**: 8mm minimum

#### 4.1.5 Layer Stackup Configuration

**2-layer board, FR-4, 1.6mm thickness**

- [ ] **Top Layer (F.Cu)**:
  - Signal routing
  - Component pads
  - Screw terminal pads
  - Ground traces (heavy, 2mm width)

- [ ] **Bottom Layer (B.Cu)**:
  - Solid ground plane (copper pour)
  - Strategic cutouts for signal vias (if needed)
  - Via stitching (every 20mm around perimeter)

- [ ] **Copper Weight**: 1 oz (35µm) both layers

- [ ] **Surface Finish** (configure in manufacturing notes):
  - Preferred: ENIG (Electroless Nickel Immersion Gold)
  - Acceptable: HASL (Hot Air Solder Leveling)

### 4.2 Component Placement Strategy

**Reference**: Follow PCB_LAYOUT.md specifications exactly

#### 4.2.1 Terminal Placement (All on Board Edges)

**Left Edge - Signal I/O**

- [ ] **J_IN** (2-pos): X=0mm (flush with edge), Y=15mm from top
  - Orientation: Wire entry facing outward (left)
  - Silkscreen: "INPUT" above, "IN+" and "IN-" at positions

**Right Edge - Signal I/O**

- [ ] **J_OUT** (2-pos): X=100mm (flush with edge), Y=15mm from top
  - Orientation: Wire entry facing outward (right)
  - Silkscreen: "OUTPUT" above, "OUT+" and "OUT-" at positions

**Top Edge - Control Selectors**

- [ ] **J_BOOST_SEL_SND** (6-pos): X=20mm from left, Y=0mm (flush with top)
  - Orientation: Wire entry facing outward (up)
  - Width: 30.48mm (6 × 5.08mm)
  - Silkscreen: "BOOST SEL SEND", positions "1" through "6"

- [ ] **J_BOOST_SEL_RET** (6-pos): X=55mm from left, Y=0mm (flush with top)
  - Orientation: Wire entry facing outward (up)
  - Silkscreen: "BOOST SEL RETURN", positions "1" through "6"

**Bottom Edge - Controls & Ground**

- [ ] **J_CUT_SEL_SND** (3-pos): X=10mm from left, Y=120mm (flush with bottom)
  - Orientation: Wire entry facing outward (down)
  - Silkscreen: "CUT SEL SEND", positions "1", "2", "3"

- [ ] **J_BOOST_LVL** (3-pos): X=30mm from left, Y=120mm (flush with bottom)
  - Orientation: Wire entry facing outward (down)
  - Silkscreen: "BOOST LEVEL", positions "1", "2", "3"

- [ ] **J_GND** (2-pos): X=50mm from left, Y=120mm (flush with bottom)
  - Orientation: Wire entry facing outward (down)
  - Silkscreen: "GROUND"

**Right Edge - Inductor Connections** (stacked vertically)

- [ ] **J_IND_20HZ** (2-pos): X=100mm (flush), Y=30mm from top
  - Orientation: Wire entry facing outward (right)
  - Silkscreen: "20Hz INDUCTOR", "L1", "L2"

- [ ] **J_IND_30HZ** (2-pos): X=100mm (flush), Y=50mm from top
  - Silkscreen: "30Hz INDUCTOR", "L1", "L2"

- [ ] **J_IND_60HZ** (2-pos): X=100mm (flush), Y=70mm from top
  - Silkscreen: "60Hz INDUCTOR", "L1", "L2"

- [ ] **J_IND_100HZ** (2-pos): X=100mm (flush), Y=90mm from top
  - Silkscreen: "100Hz INDUCTOR", "L1", "L2"

#### 4.2.2 Capacitor Placement (Center Area)

**Selector Network Capacitors** (upper center region, grouped by function)

- [ ] **C1** (18nF): X=30mm, Y=30mm
- [ ] **C2** (10nF): X=40mm, Y=30mm
- [ ] **C3** (4.7nF): X=50mm, Y=30mm
- [ ] **C4** (3.3nF): X=60mm, Y=30mm
- [ ] **C5** (2.2nF): X=70mm, Y=30mm

**Alternate Position Capacitors** (middle center)

- [ ] **C4a2** (1nF): X=60mm, Y=50mm
- [ ] **C5a2** (1.5nF): X=70mm, Y=50mm

**Additional Selector Capacitors** (lower center)

- [ ] **C6** (1.8nF): X=30mm, Y=70mm
- [ ] **C7** (1nF): X=40mm, Y=70mm

**Coupling Capacitors** (near I/O terminals)

- [ ] **C34** (1nF): X=20mm, Y=90mm (near J_IN)
- [ ] **C35** (1nF): X=80mm, Y=90mm (near J_OUT)

**Orientation**: All capacitors oriented horizontally (parallel to top/bottom edge), with value markings facing up

#### 4.2.3 Resistor Placement

- [ ] **R2** (56kΩ): X=50mm, Y=90mm (center bottom, near coupling capacitors)
  - Orientation: Horizontal (parallel to bottom edge)
  - Footprint: Through-hole, 0.4" (10.16mm) spacing
  - Value marking: Readable from top

### 4.3 Grounding Strategy (CRITICAL FOR AUDIO QUALITY)

**Star Ground Implementation** (per PCB_LAYOUT.md)

#### 4.3.1 Star Ground Point Definition

- [ ] **Star Point Location**: X=50mm, Y=60mm (center of board)
  - Mark with via array (4× vias minimum)
  - Via size: 0.8mm drill, 1.3mm pad
  - Pattern: Square, 2mm spacing
  - Connect to both top and bottom layers

#### 4.3.2 Ground Routing (Top Layer)

**Heavy traces (2.0mm width) from all ground points to star:**

- [ ] J_IN- → Star Point (2.0mm trace)
- [ ] J_OUT- → Star Point (2.0mm trace)
- [ ] J_GND → Star Point (direct connection, multiple vias)
- [ ] All capacitor ground pads → Local vias → Bottom ground plane
- [ ] All inductor terminal ground pins → Via stitching (4× vias per terminal) → Bottom plane

#### 4.3.3 Bottom Ground Plane (Copper Pour)

- [ ] Add copper pour to entire bottom layer (B.Cu)
  - Net: GND
  - Clearance: 0.3mm from all non-GND pads
  - Thermal relief: 4 spokes, 0.5mm spoke width
  - Minimum width: 0.5mm
  - Priority: 1 (highest)
  - Keep-out zones: Around mounting holes (8mm diameter)
  - Smoothing: None (sharp corners acceptable on ground plane)

- [ ] Verify ground plane is continuous (no unintended splits)

#### 4.3.4 Via Stitching (Ground Plane Integrity)

**Perimeter Stitching** (every 20mm around board edge):

- [ ] Add vias around perimeter at 20mm intervals
  - Total: Approximately 30 vias
  - Via size: 0.8mm drill, 1.3mm pad
  - Distance from edge: 5mm minimum
  - Net: GND
  - Purpose: Low-impedance ground, EMI shielding

**Component Ground Connections**:

- [ ] Via arrays at each screw terminal ground pin (4× vias minimum)
- [ ] Single via at each capacitor ground pad (connects to bottom plane)

### 4.4 Trace Routing

**Reference**: PCB_LAYOUT.md Section "Trace Routing"

#### 4.4.1 Routing Guidelines

**General Rules**:
- [ ] Use 45° angles or smooth curves (no 90° corners)
- [ ] Minimize vias in signal path (stay on top layer)
- [ ] Avoid routing under capacitors if possible
- [ ] Route critical signals first (input → output path)

**Trace Width Standards**:
- Audio signals: 0.8mm
- Control lines: 0.6mm
- Ground traces (top layer): 2.0mm

#### 4.4.2 Critical Signal Paths (Route in Order)

**Path 1: Input Stage**

- [ ] J_IN+ → C34 (input coupling)
  - Trace width: 0.8mm
  - Keep short, direct path

- [ ] C34 → Capacitor selector network junction
  - Trace width: 0.8mm
  - This is the "hot" input node

**Path 2: Frequency Selector Network**

- [ ] Capacitors (C1-C7, C4a2, C5a2) → J_BOOST_SEL_SND positions
  - Trace width: 0.6mm (control signals)
  - Each capacitor connects to one terminal position
  - Common node of capacitor network connects to R2

- [ ] J_BOOST_SEL_RET positions → Inductor terminal selector circuit
  - Trace width: 0.6mm
  - This routes the selected frequency back from external rotary switch

**Path 3: Inductor Connections**

- [ ] Inductor selector circuit → J_IND_20HZ, J_IND_30HZ, J_IND_60HZ, J_IND_100HZ
  - Trace width: 1.0mm (wide to minimize series resistance)
  - Each inductor terminal connects in parallel to selector return
  - Terminal L1: To selector circuit
  - Terminal L2: Return to resonant network

- [ ] Inductor returns → Common resonant network node
  - Trace width: 1.0mm

**Path 4: Level Control**

- [ ] Resonant network output → J_BOOST_LVL
  - Trace width: 0.8mm
  - Connects to external level potentiometer

- [ ] J_BOOST_LVL (wiper) → R2 → Network
  - Trace width: 0.8mm
  - R2 provides network loading

**Path 5: Output Stage**

- [ ] Level control output → C35 (output coupling)
  - Trace width: 0.8mm

- [ ] C35 → J_OUT+
  - Trace width: 0.8mm
  - Keep short, direct path

#### 4.4.3 Ground Routing

- [ ] J_IN- → Star point (2.0mm trace)
- [ ] J_OUT- → Star point (2.0mm trace)
- [ ] J_GND → Star point (direct via array)
- [ ] All component ground pads → Via → Bottom ground plane

#### 4.4.4 Via Usage Strategy

**Minimize signal vias**:
- [ ] Route all signal traces on top layer (F.Cu) when possible
- [ ] Use vias only for ground connections to bottom plane
- [ ] Via size: 0.8mm drill, 1.3mm pad (consistent throughout)

**Via arrays for low-impedance ground**:
- [ ] 4× via array at each terminal ground connection
- [ ] 1× via at each capacitor ground pad
- [ ] Via stitching around perimeter (every 20mm)

### 4.5 Silkscreen Labeling

**Reference**: PCB_LAYOUT.md Section "Silkscreen Labels"

#### 4.5.1 Component Labels (Top Silkscreen, White on Green)

**Capacitors**:
- [ ] Designators above components (C1, C2, C3, etc.)
- [ ] Values below designators (18nF, 10nF, 4.7nF, etc.)
- [ ] Font size: 1.0mm height minimum

**Resistor**:
- [ ] "R2" above component
- [ ] "56K" below component

**Non-polarized components**: No polarity marking needed

#### 4.5.2 Terminal Labels (Large, Bold, 1.2mm Height)

**Input/Output**:
- [ ] J_IN: "INPUT" (large), "+" and "-" at each position
- [ ] J_OUT: "OUTPUT" (large), "+" and "-" at each position

**Frequency Selectors**:
- [ ] J_BOOST_SEL_SND: "BOOST SEL SEND", positions "1" through "6"
- [ ] J_BOOST_SEL_RET: "BOOST SEL RETURN", positions "1" through "6"

**Controls**:
- [ ] J_CUT_SEL_SND: "CUT SEL SEND", positions "1", "2", "3"
- [ ] J_BOOST_LVL: "BOOST LEVEL", positions "1", "2", "3"

**Ground**:
- [ ] J_GND: "GROUND"

**Inductors** (CRITICAL - clear frequency labels):
- [ ] J_IND_20HZ: "20Hz INDUCTOR", "L1", "L2"
- [ ] J_IND_30HZ: "30Hz INDUCTOR", "L1", "L2"
- [ ] J_IND_60HZ: "60Hz INDUCTOR", "L1", "L2"
- [ ] J_IND_100HZ: "100Hz INDUCTOR", "L1", "L2"

#### 4.5.3 Board Information (Bottom Silkscreen)

- [ ] **Board Name**: "PULTEC LOW BOOST MODULE" (large, centered)
- [ ] **Revision**: "Rev 1.0"
- [ ] **Date**: "2025" (or current year)
- [ ] **Warning**: "Requires 4× hand-wound inductors"
- [ ] **Inductor Assignment Diagram**:
  ```
  20Hz → 3.5H
  30Hz → 2.8H
  60Hz → 1.5H
  100Hz → 0.77H
  ```

#### 4.5.4 Functional Diagram (Bottom Silkscreen)

Simple block diagram showing signal flow:

```
IN → Selector → Inductors → Level → OUT
      ↕           ↕           ↕
   Freq Sw    External   Pot
```

### 4.6 Test Points

**Add test points at critical nodes** (1.2mm diameter pads, via-in-pad)

- [ ] **TP1**: J_IN+ (input signal) - X=15mm, Y=20mm - Label: "TP1_IN"
- [ ] **TP2**: After C34 (post-coupling) - X=25mm, Y=90mm - Label: "TP2_COUP"
- [ ] **TP3**: Selector network node - X=50mm, Y=40mm - Label: "TP3_SEL"
- [ ] **TP4**: After R2 (pre-output coupling) - X=60mm, Y=90mm - Label: "TP4_R2"
- [ ] **TP5**: J_OUT+ (output signal) - X=85mm, Y=20mm - Label: "TP5_OUT"
- [ ] **TP_GND**: Ground reference (star point) - X=50mm, Y=60mm - Label: "TP_GND"

**Test point specifications**:
- Pad diameter: 1.2mm
- Via drill: 0.8mm (via-in-pad construction)
- Net: Connected to appropriate signal
- Silkscreen label: Clear, readable from top

### 4.7 Design Rule Check (DRC)

**Run DRC**: Tools → Design Rules Checker

#### 4.7.1 Pre-DRC Checklist

- [ ] All components placed (no components at origin)
- [ ] All footprints on correct layers (top components on F.Cu)
- [ ] Board outline closed (Edge.Cuts layer)
- [ ] Mounting holes placed with keep-outs
- [ ] Copper pour (ground plane) filled on bottom layer
- [ ] All ratsnest connections routed (no airwires remaining)

#### 4.7.2 DRC Error Categories to Resolve

**Clearance Violations**:
- [ ] No trace-to-trace clearance violations (<0.25mm)
- [ ] No trace-to-pad clearance violations
- [ ] No pad-to-pad clearance violations

**Track Width Violations**:
- [ ] No traces narrower than minimum (0.25mm)
- [ ] Verify all signal traces are 0.6-0.8mm
- [ ] Verify all ground traces are 2.0mm

**Via Violations**:
- [ ] Via drill size adequate (0.8mm minimum)
- [ ] Via annular ring adequate (0.15mm minimum)
- [ ] Vias not too close to board edge

**Copper Pour Issues**:
- [ ] Ground plane continuous (no unintended islands)
- [ ] Thermal relief pads correct (4 spokes, 0.5mm width)
- [ ] Clearances around non-GND pads adequate (0.3mm)

**Other Issues**:
- [ ] Silkscreen not on pads (automatic check)
- [ ] Mounting holes not violating clearances
- [ ] Board outline valid

#### 4.7.3 DRC Clean Criteria

- [ ] **Zero errors** (all errors must be resolved)
- [ ] Warnings reviewed and justified (some warnings are acceptable)
- [ ] Manual visual inspection complete

### 4.8 Final Layout Review

**Visual Inspection Checklist**:

- [ ] Component placement logical (signal flow left-to-right)
- [ ] All terminals accessible from board edges
- [ ] Adequate spacing for wiring and screwdriver access (20mm around terminals)
- [ ] Silkscreen labels clear and readable
- [ ] Inductor frequency labels prominent and correct
- [ ] Test points accessible for probing
- [ ] Ground plane solid and continuous
- [ ] Via stitching present around perimeter
- [ ] Star ground point clearly visible
- [ ] Mounting holes positioned correctly (3mm from edges)
- [ ] Board dimensions correct (100mm × 120mm)

**Functional Review**:

- [ ] Input and output on opposite sides (left/right)
- [ ] Control terminals grouped logically
- [ ] Inductor terminals clearly labeled with frequencies
- [ ] Signal path short and direct
- [ ] Ground routing follows star topology
- [ ] No ground loops created
- [ ] Capacitors grouped by function

### 4.9 Phase 2 Deliverables Checklist

- [ ] All components placed per specifications
- [ ] All traces routed (no airwires)
- [ ] Ground plane filled and verified
- [ ] Silkscreen labels complete and clear
- [ ] Test points added
- [ ] DRC clean (zero errors)
- [ ] Visual inspection complete
- [ ] Board dimensions verified (100mm × 120mm)
- [ ] Mounting holes placed correctly
- [ ] `low-boost.kicad_pcb` file saved

**Phase 2 Sign-Off**: Ready to generate manufacturing files when all items checked

---

## 5. Phase 3: Manufacturing File Generation

**Objective**: Generate complete manufacturing file package for PCB fabrication and assembly

**Estimated Time**: 2-3 hours
**Dependencies**: Phase 2 complete (PCB layout finalized, DRC clean)
**Deliverable**: Manufacturing file package in `src/pultec/modules/low-boost/gerbers/`

### 5.1 Gerber File Generation

**Navigate to**: File → Plot

#### 5.1.1 Gerber Plot Settings

**Output Directory**: Create `gerbers/` subdirectory
- [ ] Create directory: `src/pultec/modules/low-boost/gerbers/`

**Plot Format**: Gerber (RS-274X)

**Layers to Generate**:

- [ ] **F.Cu** (Front Copper) → Output: `low-boost-F_Cu.gbr` or `GTL`
  - Top copper layer with all signal traces

- [ ] **B.Cu** (Back Copper) → Output: `low-boost-B_Cu.gbr` or `GBL`
  - Bottom ground plane

- [ ] **F.Silkscreen** → Output: `low-boost-F_SilkS.gbr` or `GTO`
  - Top silkscreen with component labels

- [ ] **B.Silkscreen** → Output: `low-boost-B_SilkS.gbr` or `GBO`
  - Bottom silkscreen with board info and diagram

- [ ] **F.Mask** (Front Solder Mask) → Output: `low-boost-F_Mask.gbr` or `GTS`
  - Top solder mask (solder resist openings)

- [ ] **B.Mask** (Back Solder Mask) → Output: `low-boost-B_Mask.gbr` or `GBS`
  - Bottom solder mask

- [ ] **Edge.Cuts** → Output: `low-boost-Edge_Cuts.gbr` or `GM1`/`GKO`
  - Board outline and mounting holes

**Gerber Options**:
- [ ] Format: 4.6 unit mm (standard)
- [ ] Include Gerber job file: Yes
- [ ] Subtract soldermask from silkscreen: Yes (prevents silkscreen on pads)
- [ ] Use Protel filename extensions: Optional (some fabs prefer, others don't)
  - Standard: `.gbr` extension
  - Protel: `.GTL`, `.GBL`, `.GTO`, `.GBO`, `.GTS`, `.GBS`, `.GM1`

#### 5.1.2 Generate Gerber Files

- [ ] Click "Plot" button
- [ ] Verify all 7 files generated in `gerbers/` directory
- [ ] Check file sizes (all >0 bytes)

#### 5.1.3 Gerber File Verification

**Use Gerber Viewer** (built into KiCAD or external like gerbv):

- [ ] Open all Gerber files in viewer
- [ ] Verify layers align correctly
- [ ] Check for:
  - [ ] Complete board outline
  - [ ] All copper traces present
  - [ ] Ground plane continuous
  - [ ] Silkscreen readable and not on pads
  - [ ] Solder mask openings at all pads
  - [ ] Mounting holes visible

### 5.2 Drill File Generation

**Navigate to**: File → Plot → "Generate Drill Files" button

#### 5.2.1 Drill File Settings

**Output Directory**: Same as Gerbers (`gerbers/`)

**Drill File Format**: Excellon

**Drill Units**: Millimeters

**Zeros Format**: Decimal format (recommended)

**Drill Options**:
- [ ] Merge PTH and NPTH into one file: No (separate is better)
  - PTH (Plated Through-Hole): Component leads, vias
  - NPTH (Non-Plated Through-Hole): Mounting holes

- [ ] Minimal header: No (full header for compatibility)

**Drill Map**:
- [ ] Generate drill map: Yes
- [ ] Format: PDF (for reference)
- [ ] Type: Using drill symbols

#### 5.2.2 Generate Drill Files

- [ ] Click "Generate Drill File"
- [ ] Verify files created:
  - [ ] `low-boost-PTH.drl` (plated holes: vias, component pads)
  - [ ] `low-boost-NPTH.drl` (non-plated holes: mounting holes)
  - [ ] `low-boost-drl_map.pdf` (drill map reference drawing)

#### 5.2.3 Drill File Verification

**Check drill file contents**:

- [ ] Open PTH drill file in text editor
- [ ] Verify tool list (different drill sizes)
- [ ] Verify hole count matches expected:
  - Vias: ~35-40 (depends on design)
  - Component pads: ~90 (11 capacitors × 2 + 1 resistor × 2 + terminals)

- [ ] Open NPTH drill file
- [ ] Verify 4 mounting holes (3.2mm diameter)

- [ ] Open drill map PDF
- [ ] Verify hole positions match PCB layout
- [ ] Verify mounting holes at corners (3mm from edges)

### 5.3 Assembly Drawing (PDF)

**Objective**: Create clear assembly drawing showing component placement and values

#### 5.3.1 Generate Assembly Drawing

**Navigate to**: File → Plot

**Settings for Assembly Drawing**:

- [ ] Output format: PDF
- [ ] Layers to include:
  - [ ] F.Cu (front copper, for pad reference)
  - [ ] F.Silkscreen (component labels)
  - [ ] Dwgs.User (optional, for additional notes)
  - [ ] Edge.Cuts (board outline)

- [ ] Options:
  - [ ] Print in color: Yes
  - [ ] Include title block: Yes
  - [ ] Plot footprint values: Yes
  - [ ] Plot reference designators: Yes

- [ ] Output filename: `low-boost-assembly-top.pdf`

#### 5.3.2 Assembly Drawing Content Checklist

**Verify PDF includes**:

- [ ] All component positions visible
- [ ] All reference designators readable (C1, C2, R2, J1, etc.)
- [ ] All component values shown (18nF, 10nF, 56K, etc.)
- [ ] Board outline and mounting holes
- [ ] Silkscreen labels (terminal functions)
- [ ] Title block with board name and revision

**Optional but recommended**: Add assembly notes to Dwgs.User layer:
- [ ] "Install screw terminals first"
- [ ] "Install resistor R2"
- [ ] "Install capacitors C1-C7, C34, C35, C4a2, C5a2"
- [ ] "Verify all solder joints for cold joints and bridges"

### 5.4 Pick-and-Place File (CSV)

**For automated assembly** (optional for hand assembly, but useful for documentation)

**Navigate to**: File → Fabrication Outputs → Component Placement (.pos)

#### 5.4.1 Pick-and-Place Settings

- [ ] Output format: CSV (ASCII)
- [ ] Units: Millimeters
- [ ] Files: Separate files for front and back (only front needed for this board)
- [ ] Include only SMT parts: No (include all components)

#### 5.4.2 Generate Pick-and-Place

- [ ] Click "Generate Position File"
- [ ] Output: `low-boost-top-pos.csv`
- [ ] Verify CSV contains:
  - Ref (reference designator)
  - Val (component value)
  - Package (footprint)
  - PosX, PosY (position coordinates)
  - Rot (rotation angle)
  - Side (top or bottom)

### 5.5 Bill of Materials Export

**Generate BOM from schematic** (if not already created in Phase 1)

#### 5.5.1 BOM Generation (from Schematic Editor)

**Navigate to**: Schematic Editor → Tools → Generate BOM

**BOM Plugin**: Use built-in BOM plugin or third-party (KiCost, etc.)

**Format**: CSV

**Columns to include**:
- [ ] Reference Designator
- [ ] Quantity
- [ ] Value
- [ ] Description
- [ ] Footprint
- [ ] Manufacturer
- [ ] Part Number (MPN)
- [ ] Supplier
- [ ] Supplier P/N

**Output filename**: `low-boost-BOM.csv`

#### 5.5.2 BOM Cross-Reference

- [ ] Verify BOM matches PCB (all components in BOM are on PCB)
- [ ] Verify no missing components
- [ ] Verify quantities correct (e.g., 11 capacitors, 1 resistor, 9 terminals)
- [ ] Cross-reference with existing BOM.csv in module directory

### 5.6 Fabrication Drawing (PDF)

**Create fabrication drawing with board specifications**

#### 5.6.1 Fabrication Drawing Content

Create PDF document (can use text editor + export, or draw on Dwgs.User layer) with:

- [ ] **Board Dimensions**: 100mm × 120mm ±0.2mm
- [ ] **Layer Count**: 2-layer
- [ ] **Board Thickness**: 1.6mm ±0.15mm
- [ ] **Copper Weight**: 1 oz (35µm) both layers
- [ ] **Surface Finish**: ENIG preferred, HASL acceptable
- [ ] **Solder Mask**: Green LPI, both sides
- [ ] **Silkscreen**: White epoxy ink, both sides
- [ ] **Minimum Trace Width**: 0.25mm
- [ ] **Minimum Clearance**: 0.25mm
- [ ] **Minimum Hole Size**: 0.8mm
- [ ] **Board Outline**: Routed, 2mm radius corners
- [ ] **E-Test**: 100% continuity and isolation required
- [ ] **Mounting Holes**: 4× 3.2mm diameter, non-plated, 3mm from edges
- [ ] **Material**: FR-4, Tg 140°C minimum
- [ ] **IPC Class**: Class 2 (standard)

**Stackup Diagram**:
```
┌─────────────────────┐
│ Silkscreen (white)  │
├─────────────────────┤
│ Solder Mask (green) │
├─────────────────────┤
│ Copper (1 oz) F.Cu  │ ← Top layer: signals
├═════════════════════┤
│   FR-4 Core (1.6mm) │
├═════════════════════┤
│ Copper (1 oz) B.Cu  │ ← Bottom layer: ground plane
├─────────────────────┤
│ Solder Mask (green) │
├─────────────────────┤
│ Silkscreen (white)  │
└─────────────────────┘
```

**Save as**: `low-boost-fabrication-drawing.pdf`

### 5.7 Compressed Manufacturing Package

**Create ZIP archive for PCBWay submission**

#### 5.7.1 Package Contents Checklist

- [ ] All Gerber files (7 files):
  - [ ] `low-boost-F_Cu.gbr` (or `.GTL`)
  - [ ] `low-boost-B_Cu.gbr` (or `.GBL`)
  - [ ] `low-boost-F_SilkS.gbr` (or `.GTO`)
  - [ ] `low-boost-B_SilkS.gbr` (or `.GBO`)
  - [ ] `low-boost-F_Mask.gbr` (or `.GTS`)
  - [ ] `low-boost-B_Mask.gbr` (or `.GBS`)
  - [ ] `low-boost-Edge_Cuts.gbr` (or `.GM1`)

- [ ] Drill files (2-3 files):
  - [ ] `low-boost-PTH.drl`
  - [ ] `low-boost-NPTH.drl`
  - [ ] `low-boost-drl_map.pdf` (optional but helpful)

- [ ] Documentation (recommended):
  - [ ] `low-boost-assembly-top.pdf`
  - [ ] `low-boost-BOM.csv`
  - [ ] `low-boost-fabrication-drawing.pdf`
  - [ ] `README.txt` (brief description of board and specifications)

#### 5.7.2 Create ZIP Archive

**Command line** (macOS/Linux):
```bash
cd src/pultec/modules/low-boost/gerbers/
zip -r low-boost-gerbers-v1.0.zip *.gbr *.drl *.pdf
```

**Or use GUI** (Finder/Explorer):
- [ ] Select all files in `gerbers/` directory
- [ ] Right-click → Compress
- [ ] Rename to `low-boost-gerbers-v1.0.zip`

#### 5.7.3 Verify ZIP Archive

- [ ] Extract ZIP to temporary location
- [ ] Verify all files present and readable
- [ ] Check file sizes match originals
- [ ] Re-open Gerbers in viewer from extracted files

### 5.8 Phase 3 Deliverables Checklist

- [ ] Gerber files generated (7 layers)
- [ ] Drill files generated (PTH, NPTH)
- [ ] Drill map PDF created
- [ ] Assembly drawing PDF created
- [ ] Pick-and-place CSV generated (optional)
- [ ] BOM CSV verified/updated
- [ ] Fabrication drawing PDF created
- [ ] All files verified in Gerber viewer
- [ ] ZIP archive created and verified
- [ ] Manufacturing package complete

**Phase 3 Sign-Off**: Ready to submit to PCBWay when all items checked

---

## 6. Phase 4: PCBWay Submission

**Objective**: Submit manufacturing files to PCBWay and place order for PCB fabrication

**Estimated Time**: 1-2 hours
**Dependencies**: Phase 3 complete (manufacturing files generated and verified)
**Deliverable**: PCBWay order placed, confirmation received

### 6.1 PCBWay Account Setup

**If you don't have a PCBWay account**:

- [ ] Go to: https://www.pcbway.com/
- [ ] Click "Sign Up" (top right)
- [ ] Create account with email and password
- [ ] Verify email address
- [ ] Log in

### 6.2 PCBWay Specifications Checklist

**Before uploading, prepare specifications**:

#### 6.2.1 Basic Specifications

- [ ] **Board Type**: PCB
- [ ] **Layer Count**: 2 layers
- [ ] **Material**: FR-4 TG 140-150
- [ ] **Board Thickness**: 1.6mm
- [ ] **Board Dimensions**: 100mm × 120mm (will be auto-detected from Gerbers)
- [ ] **PCB Qty**: 5 or 10 (minimum order, select based on need)
- [ ] **Product Type**: Industrial/Professional control

#### 6.2.2 Copper Specifications

- [ ] **Outer Copper Weight**: 1 oz (35µm)
- [ ] **Copper Type**: Standard copper
- [ ] **Trace Width / Spacing**: 6/6 mil (0.15mm/0.15mm) - our design is 10/10 mil minimum

#### 6.2.3 Solder Mask and Silkscreen

- [ ] **Solder Mask**: Green (standard, or choose color)
- [ ] **Solder Mask Sides**: Both sides
- [ ] **Silkscreen**: White
- [ ] **Silkscreen Sides**: Both sides

#### 6.2.4 Surface Finish

**Preferred**: ENIG (Electroless Nickel Immersion Gold)
- [ ] **Advantages**: Best for long-term reliability, shelf life, solderability
- [ ] **Cost**: Higher (~$30-50 additional for this board size)
- [ ] **Recommended for**: Professional audio equipment

**Acceptable Alternative**: HASL (Hot Air Solder Leveling)
- [ ] **Advantages**: Lower cost, standard process
- [ ] **Acceptable for**: Prototypes, budget builds
- [ ] **Note**: Slightly rougher surface, shorter shelf life

**Selection**:
- [ ] Choose: ENIG (if budget allows) or HASL (for prototypes)

#### 6.2.5 Via Options

- [ ] **Via Process**: Tenting vias (standard)
- [ ] **Min Hole Size**: 0.3mm (our design uses 0.8mm, well within spec)

#### 6.2.6 Finished Copper

- [ ] **Finished Copper**: 1 oz (matches outer copper weight)

#### 6.2.7 Additional Options

- [ ] **Remove Order Number**: Yes (recommended for clean appearance)
  - Small additional cost (~$5)
  - Prevents PCBWay from adding serial number to silkscreen

- [ ] **Gold Fingers**: No
- [ ] **Castellated Holes**: No
- [ ] **Impedance Control**: No (not needed for audio frequencies)
- [ ] **Edge Connector**: No

#### 6.2.8 Testing

- [ ] **E-test** (Electrical Test): Yes (100% continuity and isolation)
  - **IMPORTANT**: Select "Fully Test" or "100% E-test"
  - Ensures all traces are connected and no shorts exist
  - Critical for multi-terminal boards like this one

### 6.3 File Upload and Review

#### 6.3.1 Upload Gerber Package

- [ ] Click "Quick Order PCB" or "Instant Quote"
- [ ] Click "Add Gerber File"
- [ ] Upload: `low-boost-gerbers-v1.0.zip`
- [ ] Wait for automatic file analysis
- [ ] Review auto-detected parameters:
  - [ ] Board dimensions: 100mm × 120mm
  - [ ] Layers: 2
  - [ ] Different nets: ~20-30 (varies by design)
  - [ ] Pads: ~90-100
  - [ ] Holes: ~40-50 (vias + component holes + mounting holes)

#### 6.3.2 PCBWay Online Gerber Viewer

**Review board in PCBWay's viewer**:

- [ ] Click "Gerber Viewer" button
- [ ] Check all layers:
  - [ ] Top copper: All traces visible, no missing connections
  - [ ] Bottom copper: Ground plane continuous
  - [ ] Top silkscreen: Labels readable, not on pads
  - [ ] Bottom silkscreen: Board info visible
  - [ ] Solder mask: Openings at all pads
  - [ ] Drill holes: All holes present, correct positions
  - [ ] Board outline: Correct dimensions, mounting holes visible

**Common Issues to Check**:
- [ ] No missing copper (isolated islands unintentionally)
- [ ] No silkscreen on pads (auto-check usually prevents this)
- [ ] No drill hits on board edge
- [ ] Mounting holes correct size (3.2mm)

#### 6.3.3 Specification Confirmation

**On PCBWay quote page, enter specifications**:

- [ ] Select all options from Section 6.2 checklist
- [ ] Review price quote
- [ ] Verify lead time (standard: 5-7 business days production + shipping)
- [ ] Select quantity (5 or 10 boards)

**Price Estimate** (as of 2025, subject to change):
- 5 boards, HASL, standard options: ~$25-40
- 5 boards, ENIG, remove serial#: ~$60-80
- 10 boards, HASL: ~$30-50
- Shipping (varies by location): $15-40

### 6.4 Design Rule Check (DRC) by PCBWay

**After upload, PCBWay runs automatic DRC**:

- [ ] Wait for DRC completion (usually 5-15 minutes)
- [ ] Review any DRC warnings or errors
- [ ] Address any critical issues:
  - Trace spacing violations (unlikely if our DRC passed)
  - Minimum hole size violations
  - Silkscreen on pads
  - Board outline issues

**If DRC errors occur**:
- [ ] Download PCBWay's detailed DRC report
- [ ] Fix issues in KiCAD PCB layout
- [ ] Regenerate Gerbers (repeat Phase 3)
- [ ] Re-upload corrected files

**Expected result**: DRC clean (no errors) if Phase 2 DRC was thorough

### 6.5 Submit Order

#### 6.5.1 Review Order Summary

- [ ] Board specifications correct
- [ ] Quantity correct
- [ ] Price acceptable
- [ ] Lead time acceptable
- [ ] Shipping method selected (standard or expedited)
- [ ] Shipping address correct

#### 6.5.2 Additional Services (Optional)

**PCB Assembly**:
- [ ] Not needed for this project (through-hole assembly is manual)
- [ ] Skip assembly services

**Stencil**:
- [ ] Not needed (no SMT components on this board)

**Additional Notes Field**:
- [ ] Add any special instructions:
  - "This is an audio circuit board. Please ensure clean fabrication with no flux residue."
  - "100% E-test critical. Verify all terminals and pads."
  - "Gold fingers: None. Edge connector: None."

#### 6.5.3 Place Order

- [ ] Review total cost (PCB + shipping + any options)
- [ ] Add to cart
- [ ] Proceed to checkout
- [ ] Select payment method (credit card, PayPal, etc.)
- [ ] Complete payment
- [ ] **Save order confirmation number**

#### 6.5.4 Post-Order Communication

**Expected timeline**:

- [ ] **Day 0**: Order placed, payment confirmed
- [ ] **Day 1-2**: PCBWay reviews order, may request clarification
- [ ] **Day 2-3**: Production begins
- [ ] **Day 5-7**: Production complete, PCBs shipped
- [ ] **Day 10-20**: Delivery (varies by shipping method and location)

**Monitor order status**:
- [ ] Check PCBWay account for status updates
- [ ] Respond promptly to any questions from PCBWay
- [ ] Review production photos (PCBWay often provides before shipping)

### 6.6 Receive and Inspect Boards

**Upon delivery**:

- [ ] Inspect packaging (no damage during shipping)
- [ ] Count boards (verify quantity ordered)
- [ ] Visual inspection:
  - [ ] Board dimensions correct (measure with caliper)
  - [ ] Silkscreen readable and correct
  - [ ] Solder mask uniform, no defects
  - [ ] Copper traces clean, no shorts visible
  - [ ] Mounting holes correct size and position
  - [ ] Surface finish uniform (ENIG gold color, or HASL silver)

- [ ] Electrical inspection (if possible):
  - [ ] Continuity test key traces
  - [ ] Verify no shorts between ground and signal pads
  - [ ] Mounting holes are non-plated (if specified)

**If issues found**:
- [ ] Document with photos
- [ ] Contact PCBWay support within 7 days
- [ ] Request replacement or refund per PCBWay quality guarantee

### 6.7 Phase 4 Deliverables Checklist

- [ ] PCBWay account created/verified
- [ ] Gerber package uploaded
- [ ] Board specifications confirmed
- [ ] PCBWay DRC passed
- [ ] Order placed and payment confirmed
- [ ] Order confirmation number saved
- [ ] Production completed
- [ ] Boards received and inspected
- [ ] Boards meet quality standards

**Phase 4 Sign-Off**: Manufacturing complete, boards ready for assembly

---

## 7. Agent Responsibilities

**This section defines which specialized agents handle which tasks and dependencies**

### 7.1 Agent Overview

**Available Specialized Agents**:

1. **kicad-expert** (this agent)
2. **circuit-design-specialist**
3. **pcb-layout-engineer**
4. **inductor-design-specialist**
5. **bom-and-sourcing**

### 7.2 Task Assignment Matrix

| Phase | Task | Primary Agent | Support Agent | Dependencies |
|-------|------|---------------|---------------|--------------|
| Phase 1 | Verify capacitor values | circuit-design-specialist | kicad-expert | Original schematic |
| Phase 1 | Add schematic components | kicad-expert | - | Capacitor verification |
| Phase 1 | Wire LC circuits | kicad-expert | circuit-design-specialist | Component values |
| Phase 1 | Run ERC | kicad-expert | - | Wiring complete |
| Phase 1 | Export schematic PDF | kicad-expert | - | ERC clean |
| Phase 2 | Import netlist to PCB | kicad-expert | - | Phase 1 complete |
| Phase 2 | Component placement | pcb-layout-engineer | kicad-expert | PCB_LAYOUT.md |
| Phase 2 | Grounding strategy | pcb-layout-engineer | circuit-design-specialist | Star ground spec |
| Phase 2 | Trace routing | pcb-layout-engineer | kicad-expert | Placement complete |
| Phase 2 | Run DRC | kicad-expert | pcb-layout-engineer | Routing complete |
| Phase 3 | Generate Gerbers | kicad-expert | - | Phase 2 complete |
| Phase 3 | Generate drill files | kicad-expert | - | Phase 2 complete |
| Phase 3 | Create assembly drawing | kicad-expert | - | Phase 2 complete |
| Phase 3 | Verify manufacturing files | kicad-expert | pcb-layout-engineer | Files generated |
| Phase 4 | Upload to PCBWay | kicad-expert | - | Phase 3 complete |
| Phase 4 | Specify board parameters | kicad-expert | - | PCB specs known |
| Phase 4 | Review and order | kicad-expert | - | DRC clean |
| Parallel | Update inductor specs | inductor-design-specialist | - | Capacitor values verified |
| Parallel | Verify BOM pricing | bom-and-sourcing | - | Component list final |

### 7.3 Parallel vs Sequential Execution

#### Can Run in Parallel (Independent Tasks)

**During Phase 1-2**:
- [ ] **inductor-design-specialist**: Update inductor calculations if capacitor values change
- [ ] **bom-and-sourcing**: Verify component availability and update pricing
- [ ] **circuit-design-specialist**: Calculate expected frequency response

**These tasks do not block PCB design progress**

#### Must Run Sequentially (Dependencies)

**Critical Path**:
1. Verify capacitor values → Update docs if needed
2. Create schematic → Run ERC → Export netlist
3. Import netlist → Place components → Route traces → Run DRC
4. Generate Gerbers → Verify → Submit to PCBWay

**Each step must complete before next begins**

### 7.4 Agent Coordination Points

**Decision Point 1: Capacitor Value Verification** (Phase 1 start)
- **Lead Agent**: circuit-design-specialist
- **Action**: Examine original schematic, verify nF vs µF
- **Outcome**: Update COMPONENT_VALUES.md and INDUCTOR_SPECS.md if needed
- **Blocking**: Phase 1 cannot proceed until resolved

**Decision Point 2: Grounding Strategy** (Phase 2)
- **Lead Agent**: pcb-layout-engineer
- **Action**: Implement star ground per PCB_LAYOUT.md
- **Outcome**: Ground plane and trace routing correct
- **Blocking**: DRC will fail if grounding incorrect

**Decision Point 3: Inductor Integration** (After PCB complete)
- **Lead Agent**: inductor-design-specialist
- **Action**: Design and wind 4 inductors based on final capacitor values
- **Outcome**: Hand-wound inductors ready for PCB connection
- **Blocking**: Module cannot be tested without inductors

### 7.5 Communication Protocol

**Status Updates**:
- [ ] kicad-expert reports progress at end of each phase
- [ ] circuit-design-specialist confirms capacitor values
- [ ] pcb-layout-engineer confirms grounding strategy implemented
- [ ] inductor-design-specialist confirms inductor specs updated (if needed)
- [ ] bom-and-sourcing confirms components available

**Issue Escalation**:
- Any blocking issue (e.g., capacitor value ambiguity) reported immediately
- User consulted for major decisions (e.g., ENIG vs HASL)
- All agents have access to shared documentation

---

## 8. Quality Checklist

**Final verification before submission**

### 8.1 Schematic Quality (Phase 1)

- [ ] All 23 components present and annotated
- [ ] All component values correct (verified against COMPONENT_VALUES.md)
- [ ] All footprints assigned and correct
- [ ] All MPN custom fields populated
- [ ] Circuit topology matches original Pultec design
- [ ] Net labels clear and descriptive
- [ ] Title block complete and accurate
- [ ] ERC zero errors
- [ ] ERC warnings justified
- [ ] PDF schematic exported and readable
- [ ] Netlist generated successfully

### 8.2 PCB Layout Quality (Phase 2)

#### Component Placement

- [ ] All components placed (none at origin)
- [ ] Terminals on board edges for accessibility
- [ ] Capacitors grouped logically by function
- [ ] Signal flow left-to-right (IN → OUT)
- [ ] Adequate spacing for wiring (20mm around terminals)
- [ ] Inductor terminals clearly labeled with frequencies
- [ ] Test points accessible
- [ ] Mounting holes correctly positioned (3mm from edges)

#### Routing

- [ ] All traces routed (no airwires)
- [ ] Signal traces 0.8mm width
- [ ] Control traces 0.6mm width
- [ ] Ground traces 2.0mm width
- [ ] No 90° angles (all 45° or curves)
- [ ] Via usage minimized in signal path
- [ ] Via size consistent (0.8mm drill, 1.3mm pad)

#### Grounding

- [ ] Star ground point at board center
- [ ] All grounds route to star point
- [ ] Bottom ground plane continuous
- [ ] Via stitching around perimeter (every 20mm)
- [ ] Via arrays at terminal grounds (4× vias)
- [ ] Thermal relief pads on ground plane (4 spokes, 0.5mm)
- [ ] No ground loops

#### Silkscreen

- [ ] Component designators readable (C1, R2, J3, etc.)
- [ ] Component values shown
- [ ] Terminal labels large and clear (1.2mm height)
- [ ] Inductor frequency labels prominent
- [ ] Board name and revision on bottom
- [ ] No silkscreen on pads (auto-checked)
- [ ] Polarity markings where needed

#### Dimensions

- [ ] Board size 100mm × 120mm (±0.2mm)
- [ ] Mounting holes 3mm from edges
- [ ] Components >8mm from board edge
- [ ] Terminals 2mm from board edge (aligned flush)

### 8.3 Design Rules (Phase 2)

- [ ] DRC zero errors
- [ ] All clearances >0.25mm (0.5mm preferred)
- [ ] All trace widths >0.25mm (actual: 0.6-2.0mm)
- [ ] Via drill >0.8mm minimum
- [ ] Via annular ring >0.15mm minimum
- [ ] No copper-to-edge violations
- [ ] Ground plane filled and continuous

### 8.4 Manufacturing Files (Phase 3)

#### Gerber Files

- [ ] All 7 Gerber layers generated
- [ ] File sizes >0 bytes (not empty)
- [ ] Gerber viewer shows all layers correctly
- [ ] Layers align properly
- [ ] Board outline closed
- [ ] Silkscreen readable
- [ ] Solder mask openings at all pads
- [ ] Ground plane visible and continuous

#### Drill Files

- [ ] PTH drill file generated
- [ ] NPTH drill file generated
- [ ] Drill map PDF generated
- [ ] Drill sizes match design (0.8mm, 3.2mm)
- [ ] Hole count matches expected (~90-100 holes)
- [ ] Mounting holes present (4× 3.2mm)

#### Documentation

- [ ] Assembly drawing PDF clear and readable
- [ ] BOM CSV accurate and complete
- [ ] Fabrication drawing includes all specs
- [ ] Pick-and-place CSV generated (optional)
- [ ] All files named consistently

#### ZIP Package

- [ ] All files included in ZIP
- [ ] ZIP extracts without errors
- [ ] Extracted files readable
- [ ] README.txt included (optional but helpful)

### 8.5 PCBWay Submission (Phase 4)

#### Pre-Submission

- [ ] Account created and verified
- [ ] All specifications documented
- [ ] Surface finish selected (ENIG or HASL)
- [ ] Quantity determined (5 or 10 boards)
- [ ] Budget approved

#### Upload and Review

- [ ] Gerber ZIP uploaded successfully
- [ ] Auto-detection correct (dimensions, layers)
- [ ] PCBWay Gerber viewer shows board correctly
- [ ] All specifications entered correctly
- [ ] E-test selected (100% testing)
- [ ] Remove order number option selected (optional)
- [ ] Price quote acceptable

#### Post-Upload

- [ ] PCBWay DRC passed (no errors)
- [ ] Any warnings addressed
- [ ] Order confirmation received
- [ ] Confirmation number saved
- [ ] Expected delivery date noted

### 8.6 Critical Measurements Verification

**Before finalizing design, verify these critical dimensions**:

- [ ] Board width: 100mm (±0.2mm acceptable)
- [ ] Board height: 120mm (±0.2mm acceptable)
- [ ] Mounting hole spacing: 94mm × 114mm (center-to-center)
- [ ] Mounting hole diameter: 3.2mm
- [ ] Mounting hole position from edges: 3mm
- [ ] Terminal positions match PCB_LAYOUT.md specifications
- [ ] Inductor terminal vertical spacing: 20mm (J_IND_20HZ to J_IND_30HZ, etc.)
- [ ] Star ground point: X=50mm, Y=60mm (center of board)

### 8.7 Documentation Completeness

**Ensure all documentation is updated and accessible**:

- [ ] README.md current and accurate
- [ ] BOM.csv matches actual components used
- [ ] PCB_LAYOUT.md reflects actual layout
- [ ] INDUCTOR_SPECS.md updated if capacitor values changed
- [ ] Schematic PDF in module directory
- [ ] Assembly drawing in module directory
- [ ] Manufacturing files in gerbers/ subdirectory
- [ ] This WORKPLAN.md updated with actual outcomes

---

## 9. Timeline and Milestones

**Estimated total time: 15-23 hours of work + manufacturing time**

### 9.1 Detailed Timeline

#### Week 1: Schematic and Layout

**Day 1-2: Phase 1 - Schematic Completion** (4-6 hours)
- [ ] Hour 1-2: Verify capacitor values (CRITICAL)
- [ ] Hour 2-4: Add all components to schematic
- [ ] Hour 4-5: Wire LC circuits and add net labels
- [ ] Hour 5-6: Run ERC, export PDF and netlist
- **Milestone 1**: Schematic complete, ERC clean, netlist ready

**Day 3-5: Phase 2 - PCB Layout** (8-12 hours)
- [ ] Hour 1-2: Board setup, import netlist, place mounting holes
- [ ] Hour 2-4: Place all screw terminals on edges
- [ ] Hour 4-6: Place capacitors and resistor in center area
- [ ] Hour 6-8: Route signal traces
- [ ] Hour 8-9: Implement star ground and ground plane
- [ ] Hour 9-10: Add silkscreen labels
- [ ] Hour 10-11: Add test points
- [ ] Hour 11-12: Run DRC, fix errors, final review
- **Milestone 2**: PCB layout complete, DRC clean

#### Week 2: Manufacturing Files and Submission

**Day 6: Phase 3 - Manufacturing Files** (2-3 hours)
- [ ] Hour 1: Generate Gerber files (7 layers)
- [ ] Hour 1.5: Generate drill files and drill map
- [ ] Hour 2: Create assembly drawing
- [ ] Hour 2.5: Generate pick-and-place and verify BOM
- [ ] Hour 3: Create fabrication drawing, ZIP package, verify all files
- **Milestone 3**: Manufacturing files ready for submission

**Day 7: Phase 4 - PCBWay Submission** (1-2 hours)
- [ ] Hour 1: Create PCBWay account, upload Gerbers
- [ ] Hour 1.5: Specify all board parameters
- [ ] Hour 2: Review DRC, place order
- **Milestone 4**: Order submitted to PCBWay

**Day 7-14: PCBWay Production** (5-7 business days)
- Day 7-8: PCBWay review and production start
- Day 9-13: PCB fabrication
- Day 14: Shipping begins
- **Milestone 5**: Boards manufactured and shipped

**Day 14-30: Shipping and Delivery** (varies by location)
- Standard shipping: 7-14 days
- Expedited shipping: 3-5 days
- **Milestone 6**: Boards delivered

### 9.2 Key Milestones Summary

| Milestone | Deliverable | Target Date | Status |
|-----------|-------------|-------------|--------|
| M1 | Schematic complete, ERC clean | Day 2 | ⬜ Not started |
| M2 | PCB layout complete, DRC clean | Day 5 | ⬜ Not started |
| M3 | Manufacturing files ready | Day 6 | ⬜ Not started |
| M4 | PCBWay order submitted | Day 7 | ⬜ Not started |
| M5 | Boards manufactured | Day 14 | ⬜ Not started |
| M6 | Boards delivered | Day 21-30 | ⬜ Not started |
| M7 | Boards inspected and verified | Day 30 | ⬜ Not started |

### 9.3 Parallel Task Timeline

**While waiting for PCBWay (Days 7-30)**:

- [ ] **inductor-design-specialist**: Design and wind 4 inductors
  - 20Hz: 3.5H (or adjusted value)
  - 30Hz: 2.8H
  - 60Hz: 1.5H
  - 100Hz: 0.77H
  - Estimated time: 20-30 hours total (5-8 hours per inductor)

- [ ] **bom-and-sourcing**: Order all components for assembly
  - 11 capacitors
  - 1 resistor
  - 9 screw terminals
  - Estimated time: 1-2 hours sourcing, 3-7 days delivery

- [ ] Prepare assembly workspace and tools
- [ ] Create assembly checklist and test procedures
- [ ] Design front panel and control layout (future module)

### 9.4 Critical Path Analysis

**Critical path** (cannot be parallelized):

1. Verify capacitor values → 2 hours
2. Create schematic → 6 hours
3. Create PCB layout → 12 hours
4. Generate manufacturing files → 3 hours
5. Submit to PCBWay → 2 hours
6. **Total critical path**: 25 hours + manufacturing time

**Parallel tasks** (can overlap with critical path):

- Inductor design (can start after capacitor verification)
- Component ordering (can start after BOM finalized)
- Documentation updates (ongoing throughout)

### 9.5 Contingency Time

**Add 20% buffer for unexpected issues**:

- Capacitor value ambiguity resolution: +2 hours
- DRC errors and fixes: +2 hours
- Gerber regeneration if PCBWay DRC fails: +3 hours
- Learning curve with KiCAD MCP: +2 hours
- **Total contingency**: +9 hours

**Realistic total time**: 34 hours work + 14-30 days manufacturing/shipping

---

## 10. Risk Assessment

**Identify potential issues and mitigation strategies**

### 10.1 Technical Risks

#### Risk 1: Capacitor Value Ambiguity (HIGH PRIORITY)

**Issue**: INDUCTOR_SPECS.md notes capacitor values may be nF instead of µF
**Impact**: CRITICAL - affects inductor design and frequency response
**Probability**: Medium (50%)
**Mitigation**:
- [ ] Verify original schematic FIRST (before any other work)
- [ ] Cross-reference Ian Thompson-Bell documentation
- [ ] If µF, proceed as planned
- [ ] If nF, recalculate inductors or revise frequencies
- [ ] Document decision in all relevant files

**Contingency Plan**:
- If capacitors are nF, options:
  1. Use different target frequencies (200Hz, 300Hz, 600Hz, 1kHz)
  2. Use µF capacitors instead (requires BOM update)
  3. Redesign inductor values for nF capacitors
- **Decision point**: Consult with circuit-design-specialist

#### Risk 2: Complex Connectivity Errors

**Issue**: 11 capacitors + 4 inductors + 2 selectors = complex wiring
**Impact**: HIGH - ERC or DRC errors, incorrect operation
**Probability**: Medium (40%)
**Mitigation**:
- [ ] Use clear, descriptive net labels
- [ ] Reference original schematic frequently
- [ ] Double-check all selector connections
- [ ] Run ERC multiple times during schematic creation
- [ ] Visual inspection before finalizing

**Contingency Plan**:
- If ERC fails: Methodically trace each net
- If circuit doesn't work after assembly: Test points allow troubleshooting

#### Risk 3: Star Ground Implementation Errors

**Issue**: Star ground critical for audio quality but easy to implement incorrectly
**Impact**: MEDIUM - noise, hum, degraded audio quality
**Probability**: Low (20%)
**Mitigation**:
- [ ] Follow PCB_LAYOUT.md star ground specification exactly
- [ ] Verify all grounds route to star point
- [ ] Check for ground loops (multiple paths to ground)
- [ ] Visual inspection of ground plane continuity
- [ ] DRC should catch most grounding errors

**Contingency Plan**:
- If grounding incorrect: Regenerate PCB layout (Phase 2)
- If discovered after fabrication: Wire modifications or rework

#### Risk 4: Inductor Terminal Labeling Confusion

**Issue**: 4 inductors with similar connectors, easy to mix up
**Impact**: MEDIUM - wrong frequency selected, requires rework
**Probability**: Low (15%)
**Mitigation**:
- [ ] Large, clear frequency labels on silkscreen (1.2mm height)
- [ ] Color-code wires to inductors (optional but helpful)
- [ ] Label both PCB and inductors with same frequency markings
- [ ] Include connection diagram on bottom silkscreen

**Contingency Plan**:
- If confusion occurs: Test each inductor position with LCR meter before final wiring

### 10.2 Manufacturing Risks

#### Risk 5: PCBWay DRC Failure

**Issue**: PCBWay's DRC may find errors our DRC missed
**Impact**: MEDIUM - delays, requires Gerber regeneration
**Probability**: Low (10%)
**Mitigation**:
- [ ] Run thorough DRC in KiCAD before submission
- [ ] Review PCBWay Gerber viewer carefully
- [ ] Use conservative design rules (0.5mm clearance, not 0.25mm minimum)
- [ ] E-test option ensures electrical integrity

**Contingency Plan**:
- If DRC fails: Download PCBWay report, fix in KiCAD, regenerate Gerbers, re-upload
- Typical turnaround: 2-4 hours

#### Risk 6: Board Dimensions Incorrect

**Issue**: Board too large or too small for intended enclosure
**Impact**: MEDIUM - may not fit, requires redesign
**Probability**: Very Low (5%)
**Mitigation**:
- [ ] Verify dimensions in multiple places (Edge.Cuts, PCBWay auto-detect)
- [ ] Measure with ruler tool in KiCAD
- [ ] Check mounting hole spacing matches enclosure
- [ ] Prototype first before ordering multiple boards

**Contingency Plan**:
- If too large: File or trim edges (not ideal)
- If too small: Add spacers or redesign enclosure
- If critical: Reorder with correct dimensions

#### Risk 7: Component Availability Issues

**Issue**: Components out of stock or discontinued
**Impact**: MEDIUM - delays assembly, may need design changes
**Probability**: Low (15%)
**Mitigation**:
- [ ] Verify component availability before finalizing design
- [ ] Use common component values (Vishay MKT1813 series is standard)
- [ ] Have alternate suppliers (Mouser, Digi-Key)
- [ ] Order components early (while PCBs are manufacturing)

**Contingency Plan**:
- If out of stock: Find alternate with same footprint and specs
- If discontinued: Redesign with available parts (may require new PCB)

### 10.3 Schedule Risks

#### Risk 8: PCBWay Production Delays

**Issue**: Manufacturing delays due to backlog, holidays, quality issues
**Impact**: LOW - inconvenience, schedule slip
**Probability**: Low (20%)
**Mitigation**:
- [ ] Order during non-peak times (avoid Chinese New Year, major holidays)
- [ ] Select "Expedited" if time-critical
- [ ] Monitor order status daily
- [ ] Communicate with PCBWay if delays occur

**Contingency Plan**:
- If delayed: Request status update, consider expedited shipping
- If critical: Use alternate vendor (OSH Park, JLCPCB) for future orders

#### Risk 9: Shipping Delays or Damage

**Issue**: Boards damaged in shipping or delayed by customs
**Impact**: LOW - schedule slip, possible replacement needed
**Probability**: Low (10%)
**Mitigation**:
- [ ] Select reliable shipping method (DHL, FedEx for international)
- [ ] Purchase shipping insurance if available
- [ ] Track shipment closely
- [ ] Inspect immediately upon delivery

**Contingency Plan**:
- If damaged: Document with photos, file claim with PCBWay
- If delayed: Contact shipping carrier, expedite if possible

### 10.4 Design Risks

#### Risk 10: Noise or Hum in Completed Circuit

**Issue**: Audio circuit picks up noise despite proper grounding
**Impact**: MEDIUM - requires troubleshooting, may need redesign
**Probability**: Low (20%)
**Mitigation**:
- [ ] Star grounding implemented correctly
- [ ] Ground plane continuous
- [ ] Adequate spacing from power transformers (system-level)
- [ ] Test points allow troubleshooting
- [ ] Follow classic Pultec grounding strategy

**Contingency Plan**:
- If noise present:
  1. Verify all ground connections
  2. Check for ground loops
  3. Add shielding if EMI issue
  4. Relocate inductors away from noise sources

#### Risk 11: Incorrect Frequency Response

**Issue**: Resonant peaks at wrong frequencies
**Impact**: MEDIUM - requires inductor adjustment or capacitor replacement
**Probability**: Medium (30%)
**Mitigation**:
- [ ] Verify capacitor values (nF vs µF) before building inductors
- [ ] Use precision capacitors (5% tolerance)
- [ ] Measure actual capacitor values with LCR meter
- [ ] Design inductors with adjustment capability (air gap tuning)
- [ ] Test each LC pair before final assembly

**Contingency Plan**:
- If frequency wrong:
  1. Measure actual capacitor value
  2. Measure actual inductor value
  3. Adjust inductor air gap or turns
  4. Replace capacitor if value drifted
  5. Document actual vs. designed values

### 10.5 Risk Mitigation Summary

**High Priority Risks** (address immediately):
1. Capacitor value ambiguity - **Verify first**
2. Complex connectivity - **Methodical schematic creation**

**Medium Priority Risks** (monitor closely):
3. Star ground implementation - **Follow spec exactly**
4. Component availability - **Check stock early**
5. Incorrect frequency response - **Test before final assembly**

**Low Priority Risks** (accept or monitor):
6. PCBWay DRC - **Thorough pre-check**
7. Manufacturing delays - **Plan buffer time**
8. Noise/hum - **Proper grounding + testing**

---

## 11. Success Criteria

**How to verify the workplan is complete and successful**

### 11.1 Phase-by-Phase Success Criteria

#### Phase 1 Success: Schematic Complete

- ✅ All 23 components added to schematic
- ✅ All component values verified against documentation
- ✅ Capacitor value ambiguity (nF vs µF) resolved
- ✅ Circuit wiring matches original Pultec topology
- ✅ Net labels applied to all critical signals
- ✅ Title block complete and accurate
- ✅ ERC zero errors (warnings justified)
- ✅ PDF schematic exported and readable
- ✅ Netlist generated successfully
- ✅ Documentation updated (if capacitor values changed)

**Verification Method**: Open schematic PDF, review ERC report, import netlist to PCB editor without errors

#### Phase 2 Success: PCB Layout Complete

- ✅ Board dimensions correct (100mm × 120mm)
- ✅ All components placed per PCB_LAYOUT.md
- ✅ Terminals on board edges for accessibility
- ✅ Star ground implemented at board center
- ✅ Ground plane continuous on bottom layer
- ✅ All traces routed (no airwires)
- ✅ Trace widths meet specifications (0.6-2.0mm)
- ✅ Silkscreen labels clear and correct
- ✅ Test points accessible
- ✅ DRC zero errors
- ✅ Visual inspection passed

**Verification Method**: Run DRC report (zero errors), visual inspection of 3D view, measure critical dimensions

#### Phase 3 Success: Manufacturing Files Ready

- ✅ All 7 Gerber files generated
- ✅ Drill files (PTH, NPTH) generated
- ✅ Drill map PDF created
- ✅ Assembly drawing PDF clear
- ✅ BOM CSV accurate
- ✅ Fabrication drawing complete
- ✅ All files verified in Gerber viewer
- ✅ ZIP package created and tested
- ✅ No errors in Gerber viewer
- ✅ All layers align correctly

**Verification Method**: Open all Gerbers in viewer, verify layer alignment, extract ZIP and re-check files

#### Phase 4 Success: PCBWay Order Complete

- ✅ Gerbers uploaded successfully
- ✅ Auto-detection correct (dimensions, layers)
- ✅ All specifications entered correctly
- ✅ PCBWay DRC passed (zero errors)
- ✅ Order placed and payment confirmed
- ✅ Order confirmation number saved
- ✅ Production completed
- ✅ Boards shipped
- ✅ Boards delivered
- ✅ Boards inspected and meet quality standards

**Verification Method**: PCBWay order status shows "Shipped" or "Delivered", physical inspection of boards

### 11.2 Final Deliverables Checklist

**Design Files**:
- [ ] `low-boost.kicad_pro` (project file)
- [ ] `low-boost.kicad_sch` (schematic, ERC clean)
- [ ] `low-boost.kicad_pcb` (PCB layout, DRC clean)
- [ ] `low-boost.net` (netlist)

**Documentation**:
- [ ] `low-boost-schematic.pdf` (readable, professional)
- [ ] `low-boost-assembly-top.pdf` (clear component placement)
- [ ] `low-boost-BOM.csv` (accurate, up-to-date)
- [ ] `low-boost-fabrication-drawing.pdf` (complete specifications)
- [ ] `README.md` (updated with actual outcomes)
- [ ] This `WORKPLAN.md` (completed with checkmarks and notes)

**Manufacturing Files** (in `gerbers/` subdirectory):
- [ ] 7 Gerber files (.gbr or Protel extensions)
- [ ] 2 Drill files (PTH, NPTH .drl)
- [ ] 1 Drill map (.pdf)
- [ ] `low-boost-gerbers-v1.0.zip` (complete package)

**Physical Deliverables**:
- [ ] 5 or 10 PCBs from PCBWay (as ordered)
- [ ] PCBs meet quality inspection
- [ ] No visible defects
- [ ] Correct dimensions (100mm × 120mm)
- [ ] Correct surface finish (ENIG or HASL)

### 11.3 Ready-for-Manufacturing Criteria

**Before submitting to PCBWay, all must be true**:

- [ ] Schematic matches original Pultec design intent
- [ ] All component values verified and correct
- [ ] PCB layout follows audio best practices (star ground, low noise)
- [ ] All terminals accessible from board edges
- [ ] Silkscreen labels clear, readable, and accurate
- [ ] DRC zero errors with conservative design rules
- [ ] Gerber files verified in viewer (all layers correct)
- [ ] Drill holes correct size and position
- [ ] Board dimensions verified (100mm × 120mm)
- [ ] Mounting holes correct (4× M3, 3mm from edges)
- [ ] Component availability verified (BOM items in stock)
- [ ] Budget approved for PCB order

**Final Sign-Off**: If all criteria met, design is READY FOR MANUFACTURING

### 11.4 Ready-for-Assembly Criteria

**After boards received, ready to assemble when**:

- [ ] PCBs inspected and meet quality standards
- [ ] All components received (11 caps, 1 resistor, 9 terminals)
- [ ] 4 inductors designed and wound (or in progress)
- [ ] Assembly tools available (soldering iron, solder, flux)
- [ ] Test equipment ready (multimeter, LCR meter, oscilloscope)
- [ ] Assembly drawing printed for reference
- [ ] Test procedure documented
- [ ] Workspace prepared

**Assembly Phase**: Not part of this workplan, but next step after board delivery

### 11.5 Success Metrics

**Quantitative Metrics**:

- [ ] ERC errors: 0 (target: 0)
- [ ] DRC errors: 0 (target: 0)
- [ ] Gerber files: 7 (target: 7)
- [ ] Board dimensions: 100mm × 120mm (±0.2mm)
- [ ] Components: 23 total (target: 23)
- [ ] Manufacturing time: 5-7 days (target: <10 days)
- [ ] Total project time: <25 hours work (target: <30 hours)

**Qualitative Metrics**:

- [ ] Schematic is clear and readable
- [ ] PCB layout is professional-looking
- [ ] Silkscreen labels are helpful for assembly
- [ ] Grounding strategy is correct for audio
- [ ] Manufacturing files are complete and correct
- [ ] Documentation is comprehensive
- [ ] Design can be reproduced by others

**Overall Success**: Low-Boost module PCB designed, verified, and manufactured with quality suitable for professional audio equipment

---

## 12. References

**All documentation and resources**

### 12.1 Project Documentation

**Module-Specific**:
- `/Users/orion/work/multi-channel-preamp/src/pultec/modules/low-boost/README.md`
- `/Users/orion/work/multi-channel-preamp/src/pultec/modules/low-boost/PCB_LAYOUT.md`
- `/Users/orion/work/multi-channel-preamp/src/pultec/modules/low-boost/BOM.csv`
- `/Users/orion/work/multi-channel-preamp/src/pultec/modules/low-boost/INDUCTOR_SPECS.md`

**System-Level**:
- `/Users/orion/work/multi-channel-preamp/src/pultec/docs/1.0/COMPONENT_VALUES.md`
- `/Users/orion/work/multi-channel-preamp/src/pultec/docs/1.0/SYSTEM_OVERVIEW.md`
- `/Users/orion/work/multi-channel-preamp/src/pultec/SCHEMATIC_CREATION_GUIDE.md`

**Original Design**:
- `/Users/orion/work/multi-channel-preamp/src/schematics/pultec-three-band-eq/pultec-three-band-eq.kicad_sch`
- `/Users/orion/work/multi-channel-preamp/reference/` (Ian Thompson-Bell documentation)

### 12.2 KiCAD Resources

**Official Documentation**:
- KiCAD 7.x Documentation: https://docs.kicad.org/7.0/en/
- KiCAD 8.x Documentation: https://docs.kicad.org/8.0/en/
- KiCAD Schematic Editor: https://docs.kicad.org/7.0/en/eeschema/eeschema.html
- KiCAD PCB Editor: https://docs.kicad.org/7.0/en/pcbnew/pcbnew.html

**Tutorials**:
- Getting Started with KiCAD: https://docs.kicad.org/7.0/en/getting_started_in_kicad/getting_started_in_kicad.html
- PCB Design Tutorial: https://www.youtube.com/kicad (official channel)

**Library Resources**:
- KiCAD Standard Libraries: https://kicad.github.io/
- Phoenix Contact Footprints: Included in standard KiCAD library
- Vishay Capacitor Models: Available from SnapEDA or Ultra Librarian

### 12.3 PCBWay Resources

**Website**: https://www.pcbway.com/

**Documentation**:
- PCB Specifications: https://www.pcbway.com/capabilities.html
- Gerber File Requirements: https://www.pcbway.com/helpcenter/technical_support/Gerber_File_Requirements.html
- Design for Manufacturing (DFM): https://www.pcbway.com/blog/help_center/PCB_Design_Tutorial___DFM.html

**Support**:
- Live Chat: Available on PCBWay website
- Email: support@pcbway.com
- Phone: Listed on contact page

### 12.4 Component Datasheets

**Capacitors**:
- Vishay MKT1813 Series: https://www.vishay.com/docs/28360/mkt1813.pdf

**Resistors**:
- Vishay MRS25 Series: https://www.vishay.com/docs/28705/mrs25.pdf

**Screw Terminals**:
- Phoenix Contact 1757 Series: https://www.phoenixcontact.com/
  - 1757019 (2-pos): Search Phoenix website for datasheet
  - 1757022 (3-pos): Search Phoenix website for datasheet
  - 1757025 (6-pos): Search Phoenix website for datasheet

### 12.5 Design Guidelines

**Audio PCB Design**:
- Audio Circuits: Design and Layout, Neil Muncy
- Grounding and Shielding, Henry Ott
- The Art of Electronics, Horowitz & Hill (Chapter on Audio)

**KiCAD Best Practices**:
- KiCAD Library Conventions: https://klc.kicad.org/
- PCB Design Best Practices: https://www.fedevel.com/

**Pultec EQ References**:
- Original Pultec EQP-1A schematics (public domain)
- Ian Thompson-Bell documentation (in `/reference/` directory)
- Classic Pultec service manuals

### 12.6 Tools and Software

**Required**:
- KiCAD 7.x or 8.x: https://www.kicad.org/download/

**Recommended**:
- Gerber Viewer: gerbv (open source) or KiCAD built-in
- PDF Reader: Adobe Acrobat, Preview (macOS), or Evince (Linux)
- Text Editor: VS Code, Sublime Text, or similar

**Optional**:
- LCR Meter: For verifying component values (BK Precision 889B, Keysight U1733C)
- Oscilloscope: For testing frequency response
- Function Generator: For signal injection

### 12.7 Supplier Links

**Component Suppliers**:
- Mouser Electronics: https://www.mouser.com/
- Digi-Key: https://www.digikey.com/
- Newark: https://www.newark.com/

**PCB Fabrication**:
- PCBWay: https://www.pcbway.com/
- JLCPCB: https://jlcpcb.com/ (alternate)
- OSH Park: https://oshpark.com/ (alternate, US-based)

**Inductor Components**:
- Hammond Manufacturing: https://www.hammfg.com/ (cores, laminations)
- MWS Wire: https://www.mwswire.com/ (magnet wire)
- Mouser/Digi-Key: (nomex, insulation tape, varnish)

### 12.8 Version Control

**Git Repository**: `/Users/orion/work/multi-channel-preamp/`

**Current Branch**: `feat/modular-pultec`

**Recent Commits** (relevant to this module):
- `db35355`: Initial modular design documentation
- `558fa27`: Added BOM and system overview
- `7e97ab9`: Added Ian Thompson-Bell reference docs

**Recommended Workflow**:
- Commit schematic after Phase 1 complete
- Commit PCB layout after Phase 2 complete
- Commit manufacturing files after Phase 3 complete
- Create tag: `low-boost-v1.0-ready-for-manufacturing`

---

## Appendix A: Quick Reference Checklists

### Schematic Quick Checklist (Phase 1)

```
☐ Capacitor values verified (nF vs µF)
☐ All 11 capacitors added
☐ R2 (56kΩ) added
☐ All 9 screw terminals added
☐ All components wired per topology
☐ Net labels applied
☐ Title block complete
☐ ERC zero errors
☐ PDF exported
☐ Netlist generated
```

### PCB Layout Quick Checklist (Phase 2)

```
☐ Board 100mm × 120mm
☐ 4 mounting holes at corners
☐ All terminals on board edges
☐ Capacitors in center area
☐ Star ground at X=50mm, Y=60mm
☐ Ground plane continuous
☐ All traces routed
☐ Silkscreen complete
☐ Test points added
☐ DRC zero errors
```

### Gerber Quick Checklist (Phase 3)

```
☐ F.Cu (top copper)
☐ B.Cu (bottom ground plane)
☐ F.SilkS (top silkscreen)
☐ B.SilkS (bottom silkscreen)
☐ F.Mask (top solder mask)
☐ B.Mask (bottom solder mask)
☐ Edge.Cuts (board outline)
☐ PTH drill file
☐ NPTH drill file
☐ All verified in Gerber viewer
☐ ZIP package created
```

### PCBWay Quick Checklist (Phase 4)

```
☐ Account created
☐ Gerbers uploaded
☐ Dimensions auto-detected correctly
☐ 2-layer specified
☐ FR-4 material
☐ 1.6mm thickness
☐ 1 oz copper
☐ Surface finish selected (ENIG/HASL)
☐ Green solder mask
☐ White silkscreen
☐ E-test selected
☐ PCBWay DRC passed
☐ Order placed
```

---

## Appendix B: File Naming Conventions

**KiCAD Project Files**:
- Project: `low-boost.kicad_pro`
- Schematic: `low-boost.kicad_sch`
- PCB: `low-boost.kicad_pcb`
- Netlist: `low-boost.net`

**Exported Documentation**:
- Schematic PDF: `low-boost-schematic.pdf`
- Assembly Drawing: `low-boost-assembly-top.pdf`
- BOM: `low-boost-BOM.csv`
- Fabrication Drawing: `low-boost-fabrication-drawing.pdf`

**Manufacturing Files** (Gerbers):
- Top Copper: `low-boost-F_Cu.gbr` or `low-boost.GTL`
- Bottom Copper: `low-boost-B_Cu.gbr` or `low-boost.GBL`
- Top Silkscreen: `low-boost-F_SilkS.gbr` or `low-boost.GTO`
- Bottom Silkscreen: `low-boost-B_SilkS.gbr` or `low-boost.GBO`
- Top Solder Mask: `low-boost-F_Mask.gbr` or `low-boost.GTS`
- Bottom Solder Mask: `low-boost-B_Mask.gbr` or `low-boost.GBS`
- Board Outline: `low-boost-Edge_Cuts.gbr` or `low-boost.GM1`

**Drill Files**:
- Plated Holes: `low-boost-PTH.drl`
- Non-Plated Holes: `low-boost-NPTH.drl`
- Drill Map: `low-boost-drl_map.pdf`

**Archive**:
- Gerber Package: `low-boost-gerbers-v1.0.zip`

---

## Appendix C: Troubleshooting Guide

### Common KiCAD Issues

**Issue: Component footprint not found**
- Solution: Install required library (Phoenix footprints) or use generic footprint

**Issue: Netlist import fails**
- Solution: Re-run ERC, verify all pins connected, regenerate netlist

**Issue: DRC shows clearance errors**
- Solution: Increase trace spacing, adjust component placement, verify design rules

**Issue: Ground plane not filling**
- Solution: Check net assignment (must be "GND"), verify clearances, rebuild copper pour

**Issue: Via not connecting to plane**
- Solution: Check thermal relief settings, verify via net matches plane net

### Common PCBWay Issues

**Issue: Auto-detection wrong dimensions**
- Solution: Verify Edge.Cuts layer is closed polygon, regenerate Gerbers

**Issue: DRC fails at PCBWay**
- Solution: Download report, fix errors in KiCAD, regenerate Gerbers

**Issue: Silkscreen on pads warning**
- Solution: Usually auto-corrected by PCBWay, or enable "subtract mask from silk" in plot settings

**Issue: Drill file format error**
- Solution: Use Excellon format, decimal units, ensure PTH/NPTH separated

---

## End of Workplan

**Document Status**: Complete and ready for execution
**Last Updated**: 2025-10-26
**Next Action**: Begin Phase 1 - Verify capacitor values

**For questions or issues during execution, consult**:
- This workplan (comprehensive step-by-step guide)
- Module README.md (component and circuit details)
- PCB_LAYOUT.md (layout specifications)
- SCHEMATIC_CREATION_GUIDE.md (KiCAD workflow)
- Specialized agents (circuit-design-specialist, pcb-layout-engineer, etc.)

---

**Ready to begin? Start with Section 3.1: Critical Pre-Work - Verify Capacitor Values**
