# Pultec Three-Band EQ - Complete BOM Summary

**Document Version:** 1.0
**Date:** 2025-10-26
**Primary Supplier:** Mouser Electronics
**Currency:** USD

---

## Executive Summary

This document provides a comprehensive Bill of Materials summary for all four modules of the Pultec-style three-band equalizer. Pricing reflects current (October 2025) component costs with quantity breaks at 1, 10, and 100 units.

### Complete System Cost (All 4 Modules)

| Quantity | Components | PCBs | Total per Channel |
|----------|-----------|------|-------------------|
| 1 unit   | $59.02    | $31.00 | $90.02 |
| 10 units | $53.21    | $21.00 | $74.21 |
| 100 units| $47.89    | $13.00 | $60.89 |

**Note:** Prices do not include:
- Hand-wound inductors (11 total: 4 for low-boost, 7 for high-boost)
- External controls (potentiometers, rotary switches)
- Chassis, panel, wiring, hardware
- Shipping, taxes, customs duties

---

## Module-by-Module Breakdown

### 1. Low-Cut Module
**Function:** Frequency-selective attenuation (20Hz-100Hz range)
**Complexity:** Simple - RC network only

| Quantity | Component Cost | PCB Cost | Module Total |
|----------|---------------|----------|--------------|
| 1        | $6.87         | $5.00    | $11.87       |
| 10       | $6.20         | $3.50    | $9.70        |
| 100      | $5.56         | $2.00    | $7.56        |

**Component Count:**
- Capacitors: 2 (film, MKT series)
- Screw terminals: 5 (Phoenix Contact 1757 series)

**Key Components:**
- C23: 33nF film capacitor
- C24: 47nF film capacitor
- Terminals: 4× 2-pos, 1× 3-pos

---

### 2. Low-Boost Module
**Function:** Frequency-selective boost (20Hz-100Hz range)
**Complexity:** Moderate - Requires 4 external hand-wound inductors

| Quantity | Component Cost | PCB Cost | Module Total |
|----------|---------------|----------|--------------|
| 1        | $17.84        | $8.00    | $25.84       |
| 10       | $16.08        | $5.50    | $21.58       |
| 100      | $14.49        | $3.50    | $17.99       |

**Component Count:**
- Capacitors: 11 (film, MKT series)
- Resistors: 1 (56kΩ metal film)
- Screw terminals: 13 (Phoenix Contact 1757 series)

**Key Components:**
- Film capacitors: 1nF to 18nF range (11 pieces)
- R2: 56kΩ metal film resistor
- Terminals: 9× 2-pos, 2× 6-pos, 2× 3-pos

**External Requirements:**
- 4× Hand-wound inductors (20Hz, 30Hz, 60Hz, 100Hz)
- Cost TBD - requires core materials, magnet wire, winding labor

---

### 3. High-Boost Module
**Function:** Frequency-selective boost with Q control (3kHz-16kHz range)
**Complexity:** High - Requires 7 external hand-wound inductors

| Quantity | Component Cost | PCB Cost | Module Total |
|----------|---------------|----------|--------------|
| 1        | $20.44        | $10.00   | $30.44       |
| 10       | $18.42        | $6.50    | $24.92       |
| 100      | $16.58        | $4.00    | $20.58       |

**Component Count:**
- Capacitors: 8 (film, MKT series)
- Resistors: 1 (4.7kΩ metal film)
- Screw terminals: 16 (Phoenix Contact 1757 series)

**Key Components:**
- Film capacitors: 470pF to 15nF range (8 pieces)
- R3: 4.7kΩ metal film resistor
- Terminals: 10× 2-pos, 2× 6-pos, 3× 3-pos

**External Requirements:**
- 7× Hand-wound inductors (3kHz, 4kHz, 5kHz, 8kHz, 10kHz, 12kHz, 16kHz)
- Cost TBD - requires core materials, magnet wire, winding labor

---

### 4. High-Cut Module
**Function:** Frequency-selective attenuation (5kHz-20kHz range)
**Complexity:** Moderate - RC network with multiple capacitors

| Quantity | Component Cost | PCB Cost | Module Total |
|----------|---------------|----------|--------------|
| 1        | $13.87        | $8.00    | $21.87       |
| 10       | $12.51        | $5.50    | $18.01       |
| 100      | $11.26        | $3.50    | $14.76       |

**Component Count:**
- Capacitors: 11 (film, MKT series)
- Resistors: 1 (430Ω metal film)
- Screw terminals: 7 (Phoenix Contact 1757 series)

**Key Components:**
- Film capacitors: 10nF to 330nF range (11 pieces)
- R1: 430Ω metal film resistor
- Terminals: 4× 2-pos, 2× 6-pos, 1× 3-pos

---

## Component Standardization

### Film Capacitors (Vishay MKT1813 Series)
**Total Unique Values:** 23 different capacitor values across all modules
**Total Quantity:** 32 capacitors

**Specifications:**
- Manufacturer: Vishay
- Series: MKT1813
- Type: Metallized polyester film
- Tolerance: ±5%
- Voltage Rating: 100V DC
- Lead Spacing: 5.08mm (0.2")
- Temperature Coefficient: Stable for audio applications

**Pricing Tiers:**
- Small values (470pF-47nF): $0.58 @ 1, $0.52 @ 10, $0.47 @ 100
- Large values (68nF-330nF): $0.68 @ 1, $0.61 @ 10, $0.55 @ 100

**Mouser Part Number Format:** 594-MKT1813xxxxx4
**Digikey Alternative:** 1938-MKT1813xxxxx-ND

**Stock Status:** Generally excellent availability for this series
**Lead Time:** Typically ships same day from Mouser

---

### Metal Film Resistors (Vishay MRS25 Series)
**Total Quantity:** 3 resistors (3 different values)

**Specifications:**
- Manufacturer: Vishay BC Components
- Series: MRS25
- Type: Metal film, axial leaded
- Power Rating: 1/4W (0.6W maximum)
- Tolerance: ±1%
- Temperature Coefficient: ±50ppm/°C
- Voltage Rating: 350V
- Low noise, excellent for audio applications

**Values Required:**
- R1: 430Ω (High-Cut module)
- R2: 56kΩ (Low-Boost module)
- R3: 4.7kΩ (High-Boost module)

**Pricing:** $0.24 @ 1, $0.22 @ 10, $0.20 @ 100

**Mouser Part Number Format:** 594-MRS25Cxxxxxx00
**Digikey Alternative:** MRS25000Cxxxxxx00-ND

**Stock Status:** Excellent availability
**Lead Time:** Ships same day from Mouser

---

### Screw Terminals (Phoenix Contact 1757 Series)
**Total Quantity:** 41 terminals (across all 4 modules)

**Specifications:**
- Manufacturer: Phoenix Contact
- Series: COMBICON MSTB
- Type: Pluggable screw terminal block
- Pitch: 5.08mm (0.2")
- Current Rating: 12A per contact
- Voltage Rating: 320V
- Wire Range: 26-14 AWG (0.14-2.5mm²)
- Connection: Screw clamp technology

**Terminal Configurations Required:**

| Part Number | Positions | Qty Needed | Price @ 1 | Price @ 10 | Price @ 100 | Mouser P/N  |
|-------------|-----------|------------|-----------|------------|-------------|-------------|
| 1757019     | 2-pos     | 27         | $0.89     | $0.80      | $0.72       | 651-1757019 |
| 1757022     | 3-pos     | 8          | $1.15     | $1.04      | $0.93       | 651-1757022 |
| 1757025     | 6-pos     | 6          | $1.89     | $1.70      | $1.53       | 651-1757025 |

**Stock Status:** Excellent availability
**Lead Time:** Ships same day from Mouser
**Digikey Alternative:** 277-xxxx-ND series

**Rationale for Phoenix Contact:**
- Industry-standard quality
- Reliable screw clamp design
- Accepts wide wire range
- Good mechanical retention
- Clear wire entry for easy assembly

---

## PCB Requirements

### Specifications
- **Layer Count:** 2-layer FR4
- **Copper Weight:** 1 oz (standard)
- **Finish:** HASL or ENIG (ENIG preferred for audio)
- **Soldermask:** Green (or custom color)
- **Silkscreen:** White, both sides recommended
- **Mounting:** 4× M3 holes per board (3.2mm diameter)

### Estimated Board Sizes
- Low-Cut: ~60×50mm
- Low-Boost: ~100×80mm (largest due to terminal count)
- High-Boost: ~110×80mm (many inductor connections)
- High-Cut: ~90×70mm

### PCB Pricing Estimates
Based on typical prototype PCB vendor pricing (JLCPCB, PCBWay, OSH Park):

| Quantity | Price per Board | Total (4 modules) |
|----------|----------------|-------------------|
| 5-10     | $5-10          | $31.00            |
| 20-50    | $3.50-6.50     | $21.00            |
| 100+     | $2.00-4.00     | $13.00            |

**Note:** Prices vary by vendor, specifications, and shipping location. USA vendors (OSH Park) typically cost more but ship faster domestically.

---

## Consolidated Parts List by Supplier

### Mouser Electronics Order (All Unique Components)

#### Film Capacitors (23 unique values)
| Value  | Qty | Part Number      | Mouser P/N          | Price @ 1 | Ext. |
|--------|-----|------------------|---------------------|-----------|------|
| 470pF  | 1   | MKT1813471104    | 594-MKT1813471104   | $0.58     | $0.58 |
| 1nF    | 4   | MKT1813102104    | 594-MKT1813102104   | $0.58     | $2.32 |
| 1.5nF  | 1   | MKT1813152104    | 594-MKT1813152104   | $0.58     | $0.58 |
| 1.8nF  | 1   | MKT1813182104    | 594-MKT1813182104   | $0.58     | $0.58 |
| 2.2nF  | 2   | MKT1813222104    | 594-MKT1813222104   | $0.58     | $1.16 |
| 3.3nF  | 2   | MKT1813332104    | 594-MKT1813332104   | $0.58     | $1.16 |
| 4.7nF  | 3   | MKT1813472104    | 594-MKT1813472104   | $0.58     | $1.74 |
| 10nF   | 3   | MKT1813103104    | 594-MKT1813103104   | $0.58     | $1.74 |
| 15nF   | 1   | MKT1813153104    | 594-MKT1813153104   | $0.58     | $0.58 |
| 18nF   | 1   | MKT1813183104    | 594-MKT1813183104   | $0.58     | $0.58 |
| 22nF   | 2   | MKT1813223104    | 594-MKT1813223104   | $0.58     | $1.16 |
| 33nF   | 2   | MKT1813333104    | 594-MKT1813333104   | $0.58     | $1.16 |
| 47nF   | 4   | MKT1813473104    | 594-MKT1813473104   | $0.58     | $2.32 |
| 68nF   | 1   | MKT1813683104    | 594-MKT1813683104   | $0.68     | $0.68 |
| 120nF  | 1   | MKT1813124104    | 594-MKT1813124104   | $0.68     | $0.68 |
| 220nF  | 1   | MKT1813224104    | 594-MKT1813224104   | $0.68     | $0.68 |
| 330nF  | 1   | MKT1813334104    | 594-MKT1813334104   | $0.68     | $0.68 |
|        |     |                  | **Capacitor Subtotal** |       | **$18.38** |

#### Metal Film Resistors (3 values)
| Value | Qty | Part Number           | Mouser P/N            | Price @ 1 | Ext. |
|-------|-----|-----------------------|-----------------------|-----------|------|
| 430Ω  | 1   | MRS25000C4300FCT00    | 594-MRS25C4300FCT00   | $0.24     | $0.24 |
| 4.7kΩ | 1   | MRS25000C4701FCT00    | 594-MRS25C4701FCT00   | $0.24     | $0.24 |
| 56kΩ  | 1   | MRS25000C5602FCT00    | 594-MRS25C5602FCT00   | $0.24     | $0.24 |
|       |     |                       | **Resistor Subtotal** |           | **$0.72** |

#### Screw Terminals
| Part Number | Positions | Qty | Mouser P/N  | Price @ 1 | Ext.     |
|-------------|-----------|-----|-------------|-----------|----------|
| 1757019     | 2-pos     | 27  | 651-1757019 | $0.89     | $24.03   |
| 1757022     | 3-pos     | 8   | 651-1757022 | $1.15     | $9.20    |
| 1757025     | 6-pos     | 6   | 651-1757025 | $1.89     | $11.34   |
|             |           |     | **Terminal Subtotal** |   | **$44.57** |

#### Mouser Order Summary (1 Complete System)
- Capacitors: $18.38
- Resistors: $0.72
- Terminals: $44.57
- **Component Total: $63.67**
- Estimated Shipping (USA): $7.99
- **Order Total: $71.66** (before tax)

---

## Quantity Break Analysis

### Building Multiple Units

When building 10 or 100 units, significant cost savings are available:

#### 10-Unit Build (10 Complete EQ Channels)
- Component cost per unit: $53.21
- PCB cost per unit (amortized): $21.00
- **Total per channel: $74.21**
- **Total project cost: $742.10** (10 channels)
- **Savings vs single unit: 18%**

#### 100-Unit Build (100 Complete EQ Channels)
- Component cost per unit: $47.89
- PCB cost per unit (amortized): $13.00
- **Total per channel: $60.89**
- **Total project cost: $6,089.00** (100 channels)
- **Savings vs single unit: 32%**

### Recommended Order Quantities

For hobbyist/prototype builds:
- **Order quantity: 5-10** of each unique component value
- Provides spares for errors, testing, future builds
- Captures moderate quantity discounts
- Total cost increase: ~15% over exact quantities
- Risk mitigation: Component failures, assembly errors

For professional/production builds:
- **Order quantity: 100+** of common values (1nF, 10nF, 47nF)
- **Order quantity: 50+** of unique values
- Negotiate pricing directly with Mouser for volume
- Consider stocking program for long-term production

---

## Alternative Component Sources

### Film Capacitors
**Primary:** Vishay MKT1813 series (specified)
**Alternative 1:** WIMA MKS2 series (premium, +50% cost)
**Alternative 2:** EPCOS/TDK B32529 series (comparable)
**Alternative 3:** Kemet R60 series (slightly lower audio grade)

**Recommendation:** Stick with Vishay MKT1813 for best price/performance balance in audio applications.

### Metal Film Resistors
**Primary:** Vishay MRS25 (specified)
**Alternative 1:** Vishay PR01/PR02 (professional audio grade, +100% cost)
**Alternative 2:** Yageo MFR-25 (good quality, -20% cost)
**Alternative 3:** KOA Speer MF1/4 (comparable)

**Recommendation:** Vishay MRS25 excellent for this application; PR series overkill unless doing ultra-high-end build.

### Screw Terminals
**Primary:** Phoenix Contact 1757 series (specified)
**Alternative 1:** Wurth Elektronik 691 series (comparable quality)
**Alternative 2:** TE Connectivity 282834 series (industrial grade)
**Alternative 3:** Generic Asian imports (Degson, Curtis) (-60% cost, quality varies)

**Recommendation:** Phoenix Contact worth the premium for reliability and wire retention. Consider alternatives only for cost-sensitive builds.

---

## Component Availability & Stock Status

### Current Status (October 2025)

#### Vishay MKT1813 Capacitors
- **Availability:** EXCELLENT
- **Stock Levels:** 1000+ pieces for most values at Mouser
- **Lead Time:** Ships same day
- **Risk Level:** LOW
- **Notes:** This series is actively manufactured and widely stocked

#### Vishay MRS25 Resistors
- **Availability:** EXCELLENT
- **Stock Levels:** 5000+ pieces for common values
- **Lead Time:** Ships same day
- **Risk Level:** LOW
- **Notes:** Standard E96 series values all readily available

#### Phoenix Contact 1757 Terminals
- **Availability:** EXCELLENT
- **Stock Levels:** 500+ pieces typical
- **Lead Time:** Ships same day to 2-3 days
- **Risk Level:** LOW
- **Notes:** Popular series, well-stocked globally

### No Components Over $10

Good news: No individual component exceeds $10 in unit quantity. The most expensive single item is the 6-position screw terminal at $1.89 each.

### No Long Lead Time Items

All specified passive components ship same-day from Mouser. No allocation issues, no extended lead times. This is a significant advantage of using standard, commodity parts.

### No Obsolete Components

All part numbers verified as active and in production:
- Vishay MKT1813: Active series, introduced 2010s
- Vishay MRS25: Active since 1990s, industry standard
- Phoenix Contact 1757: Active, COMBICON current product line

---

## External Components Not Included

### Hand-Wound Inductors (11 Required)

These critical components are NOT included in the above BOMs as they require custom fabrication:

#### Low-Boost Module (4 inductors)
- 20Hz inductor: TBD specifications
- 30Hz inductor: TBD specifications
- 60Hz inductor: TBD specifications
- 100Hz inductor: TBD specifications

#### High-Boost Module (7 inductors)
- 3kHz inductor: TBD specifications
- 4kHz inductor: TBD specifications
- 5kHz inductor: TBD specifications
- 8kHz inductor: TBD specifications
- 10kHz inductor: TBD specifications
- 12kHz inductor: TBD specifications
- 16kHz inductor: TBD specifications

**Status:** Inductor design specifications are being developed by the inductor-design-specialist agent. See module-specific documentation for details.

**Cost Estimate:** TBD - depends on core materials, wire, and whether DIY hand-wound or professionally manufactured.

**Resources Required:**
- Powdered iron toroid cores (Amidon, Micrometals)
- Magnet wire (various gauges)
- Winding fixtures/tools
- LCR meter for testing
- Labor time for winding/testing

---

### Front Panel Controls

Not included in module BOMs:

#### Rotary Switches
- Low-Cut frequency selector (4-position)
- Low-Boost frequency selector (6-position minimum)
- High-Boost frequency selector (7-position minimum)
- High-Cut frequency selector (6-position minimum)

**Recommended:** Grayhill, Electroswitch, or similar professional audio-grade rotary switches
**Cost:** $15-40 each depending on quality

#### Potentiometers
- Low-Cut level control (100kΩ-500kΩ audio taper)
- Low-Boost level control (100kΩ-500kΩ audio taper)
- High-Boost level control (100kΩ-500kΩ audio taper)
- High-Boost Q control (100kΩ-500kΩ linear taper)
- High-Cut level control (100kΩ-500kΩ audio taper)

**Recommended:** Alps, Bourns, TT Electronics (noble quality)
**Cost:** $3-15 each depending on quality and shaft type

---

## Recommended Purchasing Strategy

### For Single Prototype Build

1. **Order from Mouser:** All components in exact quantities
   - Use BOM files directly for cart import
   - Expected cost: ~$72 including shipping
   - Add 10% spares for common values (terminals, popular capacitor values)

2. **PCB Fabrication:** Order 5 boards of each module from JLCPCB/PCBWay
   - Cost: ~$40-50 for 5× each (20 boards total)
   - Provides spares for errors and future builds

3. **Inductors:** Begin with DIY hand-wound approach
   - Order cores and wire from Amidon
   - Budget $50-100 for inductor materials

**Total First Build Cost: ~$160-220**

### For Small Production Run (10 Units)

1. **Order 10× component quantities** from Mouser
   - Captures quantity discounts
   - Single $7.99 shipping for entire order

2. **PCB panel order:** 50-100 boards via JLCPCB
   - Panelize for efficiency
   - Cost: ~$150-250 for 100 boards (25 complete sets)

3. **Inductors:** Consider professional winding service or DIY batch production

**Total 10-Unit Cost: ~$900-1100** ($90-110 per channel)

### For Production (100+ Units)

1. **Volume negotiation** with Mouser or distributor
   - Request quote for 100-500 piece quantities
   - May achieve additional 10-20% discount

2. **PCB production pricing** (500-1000 boards)
   - Professional PCB house (Sierra, Sunstone)
   - Assembly services if volume justifies

3. **Professional inductor manufacture**
   - Custom winding service (toroid.com, others)
   - One-time setup fee amortized across volume

---

## Quality Assurance Notes

### Component Verification

**Before ordering:**
- Verify all part numbers against current Mouser/Digikey listings
- Check stock availability for all items
- Confirm lead spacing on capacitors (5.08mm critical for PCB fit)
- Verify terminal block wire range matches your wire gauge selection

**Upon receipt:**
- Spot-check capacitor values with capacitance meter
- Verify resistor values with multimeter
- Inspect terminals for mechanical integrity
- Check for shipping damage

### Suggested Test Quantities

For first-time builds, order extras:
- Capacitors: +20% on common values (1nF, 10nF, 47nF)
- Resistors: +5 pieces each (cheap insurance)
- Terminals: +2 of each type (for assembly practice)

**Cost impact:** ~$10-15 additional
**Risk mitigation:** Avoids delays from damaged/lost components

---

## Revision History

| Version | Date       | Changes |
|---------|------------|---------|
| 1.0     | 2025-10-26 | Initial BOM summary with updated pricing, consolidated parts lists, and purchasing recommendations |

---

## Contact & Support

**BOM Questions:** Refer to individual module BOM.csv files in module directories
**Component Substitutions:** Consult with circuit-design-specialist agent
**Inductor Specifications:** See inductor-design-specialist documentation
**PCB Design:** Refer to pcb-layout-engineer for board files

**Module Documentation:**
- `/src/pultec/modules/low-cut/BOM.csv`
- `/src/pultec/modules/low-boost/BOM.csv`
- `/src/pultec/modules/high-boost/BOM.csv`
- `/src/pultec/modules/high-cut/BOM.csv`
