# Pultec EQ Module - PCB Size Comparison

## Visual Size Comparison (to scale)

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                                                                                │
│  HIGH BOOST MODULE (120mm × 140mm) - LARGEST                                  │
│  ┌────────────────────────────────────────────────────────────────────────┐   │
│  │  ○                                                                  ○  │   │
│  │  [BOOST_SEL_SND ══════] [BOOST_SEL_RET ══════]                        │   │
│  │                                                                        │   │
│  │  [IN]     C14  C15  C16  C17  C2a2                      [3kHz  IND ]  │   │
│  │                                                          [4kHz  IND ]  │   │
│  │           C29  C32  C33                                 [5kHz  IND ]  │   │
│  │                                                          [8kHz  IND ]  │   │
│  │                     R3                                  [10kHz IND ]  │   │
│  │                                                          [12kHz IND ]  │   │
│  │                                                          [16kHz IND ]  │   │
│  │                                                                        │   │
│  │                                                                    [OUT]   │
│  │  [BOOST_LVL ═] [BOOST_L_SND ═] [BOOST_Q ═] [GND]                     │   │
│  │  ○                                                                  ○  │   │
│  └────────────────────────────────────────────────────────────────────────┘   │
│  8 capacitors, 1 resistor, 10 terminals, 7 inductor connections               │
│  Q control, most complex module                                               │
└────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  LOW BOOST MODULE (100mm × 120mm) - LARGE                           │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  ○                                                        ○  │   │
│  │  [BOOST_SEL_SND ══════] [BOOST_SEL_RET ══════]               │   │
│  │                                                               │   │
│  │  [IN]   C1  C2  C3  C4  C5                    [20Hz  IND]    │   │
│  │                                                [30Hz  IND]    │   │
│  │         C4a2 C5a2                             [60Hz  IND]    │   │
│  │                                                [100Hz IND]    │   │
│  │         C6  C7                                               │   │
│  │                                                          [OUT]   │
│  │         C34     R2      C35                                  │   │
│  │                                                               │   │
│  │  [CUT_SEL_SND ═] [BOOST_LVL ═] [GND]                        │   │
│  │  ○                                                        ○  │   │
│  └──────────────────────────────────────────────────────────────┘   │
│  11 capacitors, 1 resistor, 9 terminals, 4 inductor connections     │
│  Most capacitors of all modules                                     │
└──────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│                                                            │
│  HIGH CUT MODULE (90mm × 100mm) - MEDIUM                  │
│  ┌────────────────────────────────────────────────────┐   │
│  │  ○                                              ○  │   │
│  │  [CUT_SEL_SND ══════] [CUT_SEL_RET ══════]         │   │
│  │                                                     │   │
│  │  [IN]   C18  C19  C20  C21  C22  C25               │   │
│  │                                                     │   │
│  │         C26  C27  C28                          [OUT]   │
│  │                                                     │   │
│  │         C30  C31      R1                           │   │
│  │                                                     │   │
│  │  [CUT_LVL ═]       [GND]                           │   │
│  │  ○                                              ○  │   │
│  └────────────────────────────────────────────────────┘   │
│  11 capacitors, 1 resistor (430Ω critical), 6 terminals   │
│  Duplicate capacitor values (3×47nF, 2×22nF)              │
└────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│                                          │
│  LOW CUT MODULE (60mm × 60mm) - SMALL   │
│  ┌──────────────────────────────────┐   │
│  │  ○                            ○  │   │
│  │      [CUT_SEL_RET ═] [CUT_LVL]   │   │
│  │                                   │   │
│  │  [IN]    C23    C24          [OUT]   │
│  │                                   │   │
│  │                                   │   │
│  │         [GND]                     │   │
│  │  ○                            ○  │   │
│  └──────────────────────────────────┘   │
│  2 capacitors, 5 terminals               │
│  Simplest module                         │
└──────────────────────────────────────────┘
```

## Size Summary Table

| Module | Width | Height | Area | Complexity |
|--------|-------|--------|------|------------|
| **Low Cut** | 60mm | 60mm | 3,600mm² | Simple |
| **Low Boost** | 100mm | 120mm | 12,000mm² | Complex |
| **High Boost** | 120mm | 140mm | 16,800mm² | Very Complex |
| **High Cut** | 90mm | 100mm | 9,000mm² | Moderate |

## Component Density Comparison

| Module | Components | Terminals | Density | Notes |
|--------|-----------|-----------|---------|-------|
| **Low Cut** | 2 caps | 5 | Very Low | Simplest, most open layout |
| **Low Boost** | 11 caps + 1R | 9 | Medium-High | Most components |
| **High Boost** | 8 caps + 1R | 10 | Medium | 7 inductor terminals add complexity |
| **High Cut** | 11 caps + 1R | 6 | Medium-High | Same cap count as Low Boost |

## Mounting Pattern (All Modules)

All modules use the same mounting hole pattern (M3 holes, 3mm from edges):

- **Low Cut**: 54mm × 54mm spacing
- **Low Boost**: 94mm × 114mm spacing
- **High Boost**: 114mm × 134mm spacing
- **High Cut**: 84mm × 94mm spacing

## Board Thickness Comparison (Side View)

```
All modules: 1.6mm thick (standard FR-4)

                    Component height varies:
                    ┌─────────────────────┐
                    │  Screw terminals:   │  ~10mm above PCB
                    │  Phoenix 1757       │
                    ├─────────────────────┤
                    │  Capacitors:        │  ~8mm above PCB
                    │  MKT1813            │
                    ├─────────────────────┤
                    │  Resistors:         │  ~6mm above PCB
                    │  MRS25              │
                    └─────────────────────┘
                    ┌═════════════════════┐  PCB surface (top)
                    │ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │  1.6mm
                    └═════════════════════┘  PCB surface (bottom)
                         │         │
                         └─────────┘  Solder joints: ~2mm below PCB
```

## Recommended Standoff Heights

For proper clearance and wire routing:

| Module | Standoff Height | Bottom Clearance | Top Clearance | Total Height |
|--------|----------------|------------------|---------------|--------------|
| **Low Cut** | 10mm | 12mm | 50mm | 62mm |
| **Low Boost** | 12mm | 14mm | 60mm | 74mm |
| **High Boost** | 15mm | 17mm | 70mm | 87mm |
| **High Cut** | 12mm | 14mm | 60mm | 74mm |

**Note**: Top clearance is for wire routing and access to screw terminals.

## Enclosure Size Recommendation

If mounting all four modules in a single enclosure:

### Horizontal Layout (Side-by-Side)
```
Total width: 60 + 100 + 120 + 90 + (4 × 30mm spacing) = 490mm
Total depth: 140mm (largest board) + 2 × 30mm clearance = 200mm
Total height: 87mm (High Boost) + 20mm clearance = 110mm
```

**Recommended enclosure**: 500mm (W) × 200mm (D) × 120mm (H)
- Allows 30mm spacing between modules
- 30mm clearance front and back for wiring
- 20mm clearance top and bottom for ventilation

### Vertical Layout (Stacked)
```
Total width: 120mm (widest board) + 2 × 30mm clearance = 180mm
Total depth: 140mm (longest board) + 2 × 30mm clearance = 200mm
Total height: 4 × 87mm (max module height) + (4 × 40mm spacing) = 508mm
```

**Recommended enclosure**: 200mm (W) × 200mm (D) × 520mm (H)
- Allows 40mm spacing between modules (vertical stack)
- 30mm clearance all sides for wiring
- Vertical rack-mount configuration possible

## Weight Estimates

| Module | PCB Weight | Component Weight | Total Weight | Notes |
|--------|-----------|------------------|--------------|-------|
| **Low Cut** | 8g | 15g | ~25g | Lightest module |
| **Low Boost** | 25g | 50g | ~75g | Heaviest due to component count |
| **High Boost** | 35g | 45g | ~80g | Largest board |
| **High Cut** | 20g | 45g | ~65g | Medium weight |

**Total system weight** (4 modules): ~245g (excludes inductors, enclosure, wiring)

**Inductor weight estimate**:
- Low Boost (4 inductors): ~200-400g (large laminated cores)
- High Boost (7 inductors): ~100-150g (smaller powdered iron toroids)
- **Total with inductors**: ~545-795g

## Power Consumption

**All modules are passive** (no active components, no power consumption).
- No power supply connections required
- No heat dissipation
- No cooling requirements

## Signal Path Lengths

Approximate signal path lengths through each module:

| Module | Min Path | Max Path | Average | Notes |
|--------|----------|----------|---------|-------|
| **Low Cut** | 40mm | 60mm | 50mm | Shortest paths |
| **Low Boost** | 80mm | 150mm | 115mm | Varies by frequency selection |
| **High Boost** | 100mm | 180mm | 140mm | Longest paths (7 inductors) |
| **High Cut** | 70mm | 130mm | 100mm | Varies by frequency selection |

**Total signal chain**: ~150-220mm (6-9 inches) through all four modules

## Terminal Count Summary

Total screw terminal connections for complete system:

| Connection Type | Count | Terminal Size | Wire Gauge |
|----------------|-------|---------------|------------|
| Signal I/O | 10 | 2-pos | 22-24 AWG |
| Ground | 5 | 2-pos | 20-22 AWG |
| Frequency selectors | 10 | 3-6 pos | 22-24 AWG |
| Level controls | 6 | 2-3 pos | 22-24 AWG |
| Q control | 1 | 3-pos | 22-24 AWG |
| Inductors (Low Boost) | 4 | 2-pos | 18-22 AWG |
| Inductors (High Boost) | 7 | 2-pos | 18-24 AWG |
| **Total terminals** | **43** | | |

## Cost Summary

| Module | PCB Cost | Component Cost | Total Cost | Cost per cm² |
|--------|----------|----------------|------------|--------------|
| **Low Cut** | $5.00 | $4.75 | $9.75 | $0.27 |
| **Low Boost** | $8.00 | $16.20 | $24.20 | $0.20 |
| **High Boost** | $10.00 | $19.20 | $29.20 | $0.17 |
| **High Cut** | $8.00 | $13.90 | $21.90 | $0.24 |
| **Total** | **$31.00** | **$54.05** | **$85.05** | **$0.21** |

**Cost breakdown**:
- PCBs: 36% of total cost
- Passive components (caps, resistors): 25% of total cost
- Screw terminals: 39% of total cost

**Cost per module** (average): $21.26

## Fabrication Time Estimates

| Module | PCB Fab | Assembly | Testing | Total Time | Notes |
|--------|---------|----------|---------|------------|-------|
| **Low Cut** | 5-10 days | 30 min | 15 min | 5-10 days | Fastest assembly |
| **Low Boost** | 5-10 days | 90 min | 30 min | 5-10 days | Most components |
| **High Boost** | 5-10 days | 120 min | 45 min | 5-10 days | Most complex |
| **High Cut** | 5-10 days | 90 min | 30 min | 5-10 days | Medium complexity |

**Total project time**:
- PCB fabrication: 5-10 days (all modules can be ordered simultaneously)
- Assembly: ~5.5 hours total (can be done over 1-2 days)
- Testing: ~2 hours total (module-level + system integration)
- Inductor design and winding: 1-3 days (separate task)

## Design Trade-offs Summary

### Low Cut Module
- **Pro**: Smallest, simplest, cheapest
- **Con**: Still requires dedicated PCB (could have been integrated)
- **Decision**: Standalone PCB maintains modularity and testability

### Low Boost Module
- **Pro**: Comprehensive frequency selection (6 positions)
- **Con**: Large board due to 11 capacitors
- **Decision**: Board size necessary for component count and inductor terminals

### High Boost Module
- **Pro**: Most versatile (7 frequencies + Q control)
- **Con**: Largest board, most inductor connections
- **Decision**: Size justified by functionality (classic Pultec high-frequency shaping)

### High Cut Module
- **Pro**: Good component density (11 caps on medium board)
- **Con**: R1 (430Ω) is critical component, must be exact value
- **Decision**: R1 placement and test points critical for verification

## Comparison to Monolithic Design

Original monolithic schematic vs. modular design:

| Aspect | Monolithic | Modular (4 PCBs) | Trade-off |
|--------|-----------|------------------|-----------|
| **Board size** | ~150mm × 150mm | 60-120mm per module | Smaller individual boards |
| **Total area** | ~22,500mm² | ~41,400mm² | 84% more total area (includes spacing) |
| **Assembly** | Single board | 4 separate boards | More complex assembly |
| **Testing** | All-at-once | Per-module | Easier troubleshooting |
| **Cost** | ~$40-50 | ~$85 | Higher cost for modularity |
| **Flexibility** | Fixed | Swappable modules | Much higher flexibility |
| **Repairability** | Difficult | Easy (replace module) | Significantly easier |

**Conclusion**: Modular design trades cost and total area for flexibility, testability, and repairability.

---

**Revision History**:
- **v1.0** (2025-10-26): Initial board size comparison document

**Author**: PCB Layout Engineer (Claude)
**Project**: Pultec Three-Band Equalizer - Modular Design
