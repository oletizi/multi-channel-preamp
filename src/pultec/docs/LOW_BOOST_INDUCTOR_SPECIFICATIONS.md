# Low Boost Inductor Design Specifications

## Overview

This document provides complete design specifications for the four inductors required by the Low Boost module of the Pultec three-band EQ. These inductors form resonant LC circuits with the capacitors in the low boost section to provide frequency-selective boost at 20Hz, 30Hz, 60Hz, and 100Hz.

## Circuit Topology

The low boost section uses a passive LC network where:
- Signal passes through the 47K (High Boost) and 4.7K (High Cut) resistor divider
- An LC resonant circuit in parallel with the 4.7K resistor provides frequency-selective boost
- Different capacitors are selected via rotary switch for each frequency
- Inductors are connected via screw terminals for each frequency position

## Design Requirements

### Electrical Requirements
- Resonant frequencies: 20Hz, 30Hz, 60Hz, 100Hz
- Target Q factor: >20 (for good selectivity and low losses)
- DC resistance: Minimize to reduce insertion loss
- Operating voltage: 100V peak-to-peak (audio signal)
- Temperature stability: ±5% over 0-50°C operating range

### Physical Requirements
- Mounting: External to PCB, connected via screw terminals
- Size: Reasonable for audio equipment (toroidal preferred)
- Shielding: Desirable to minimize hum pickup
- Accessibility: Easy to measure and replace if needed

## Inductor Calculations

### Resonant Frequency Formula
For a parallel LC circuit:
```
f₀ = 1 / (2π√(LC))

Rearranging for L:
L = 1 / (4π²f₀²C)
```

### Capacitor Values from Circuit
Based on COMPONENT_VALUES.md and Ian Thompson-Bell's schematic:

| Frequency | Capacitor(s) | Total Capacitance |
|-----------|--------------|-------------------|
| 20 Hz | C1 (18nF) | 18nF |
| 30 Hz | C2 (10nF) | 10nF |
| 60 Hz | C3 (4.7nF) | 4.7nF |
| 100 Hz | C4 (3.3nF) | 3.3nF |

### Required Inductance Values

| Frequency | Capacitance | Calculated L | Rounded L |
|-----------|-------------|--------------|-----------|
| 20 Hz | 18 nF | 3.51 H | 3.5 H |
| 30 Hz | 10 nF | 2.81 H | 2.8 H |
| 60 Hz | 4.7 nF | 1.50 H | 1.5 H |
| 100 Hz | 3.3 nF | 0.768 H | 750 mH |

## Core Selection

### Core Technology: Laminated E-I Steel

**Rationale:**
- Low frequencies (20-100Hz) require large inductances (0.75-3.5H)
- Laminated steel cores provide high permeability (μ = 2000-4000)
- Excellent for audio frequencies with low hysteresis
- Good availability and reasonable cost
- Traditional choice for audio inductors

### Recommended Cores

**Option 1: Hammond Manufacturing 166 Series E-I Laminations**
- Material: M6 grain-oriented silicon steel
- Permeability: ~3000
- Low core losses at audio frequencies
- Available in multiple sizes

**Option 2: Magnetic Metals Laminated E-I Cores**
- Material: 50% Nickel-Iron (Permalloy)
- Permeability: ~4000
- Superior performance but higher cost
- Excellent temperature stability

### Specific Core Recommendations

**For 20Hz and 30Hz (3.5H and 2.8H):**
- Hammond 166K25 or similar
- EI-100 lamination (25mm stack)
- Core area: ~250mm²
- Window area: Adequate for 500+ turns

**For 60Hz and 100Hz (1.5H and 0.75H):**
- Hammond 166J25 or similar
- EI-87 lamination (25mm stack)
- Core area: ~188mm²
- Window area: Adequate for 300+ turns

## Wire Gauge Selection

### Design Considerations
1. **DC Resistance (DCR):** Lower is better - reduces insertion loss
2. **Winding Space:** Must fit required turns in core window
3. **Current Handling:** Audio signals are low current (<10mA typically)
4. **Availability:** Standard magnet wire sizes

### Wire Gauge Recommendations

**20 AWG (0.812mm diameter)**
- Resistance: 33.3 Ω/km = 0.0333 Ω/m
- Good balance of low DCR and reasonable size
- Easily sources as magnet wire (enamel insulated)
- Recommended for all four inductors

**Alternative: 22 AWG (0.644mm diameter)**
- Resistance: 52.8 Ω/km = 0.0528 Ω/m
- If winding space is tight
- Slightly higher DCR but still acceptable

**Note:** Use heavy build enamel insulation for reliability

## Detailed Inductor Specifications

---

## 20 Hz INDUCTOR

### Target Specifications
- **Inductance:** 3.5 H ±5%
- **Resonant Capacitor:** 18 nF (C1)
- **Resonant Frequency:** 20 Hz
- **Target DCR:** <75 Ω (Q >20 at 20Hz)
- **Core:** EI-100, 25mm stack

### Design Calculations

**Inductance Formula:**
```
L = (μ₀ × μᵣ × N² × Aₑ) / lₑ

Where:
- μ₀ = 4π × 10⁻⁷ H/m (permeability of free space)
- μᵣ = effective relative permeability (~3000 for M6 steel with air gap)
- N = number of turns
- Aₑ = effective core area (m²)
- lₑ = effective magnetic path length (m)
```

**For EI-100 lamination:**
- Aₑ = 250 mm² = 2.5 × 10⁻⁴ m²
- lₑ ≈ 200 mm = 0.2 m
- With air gap for linearity: μᵣ,eff ≈ 500

**Calculating turns:**
```
N = √(L × lₑ / (μ₀ × μᵣ × Aₑ))
N = √(3.5 × 0.2 / (4π × 10⁻⁷ × 500 × 2.5 × 10⁻⁴))
N ≈ 1675 turns
```

### Final Specification

| Parameter | Value |
|-----------|-------|
| **Inductance** | 3.5 H ±5% |
| **Core Type** | EI-100 laminated steel |
| **Stack Height** | 25 mm |
| **Air Gap** | 0.5 mm (for linearity) |
| **Wire Gauge** | 20 AWG heavy build enamel |
| **Number of Turns** | 1675 turns |
| **Winding Pattern** | Layer wound, interleaved if space permits |
| **Wire Length** | ~84 m (estimated) |
| **DCR (calculated)** | 2.8 Ω |
| **Q Factor (20Hz)** | 157 (excellent) |
| **Mounting** | Bobbin with mounting brackets |

### Winding Instructions

1. **Preparation:**
   - Clean EI-100 laminations (25mm stack)
   - Prepare bobbin with insulation tape on cheeks
   - Cut air gap spacer: 0.5mm non-magnetic material (Nomex, fiber)

2. **Winding:**
   - Use 20 AWG heavy build magnet wire
   - Wind 1675 turns in progressive layers
   - Layer distribution: ~33 turns per layer × 51 layers
   - Insulate between layers with thin film tape (0.05mm)
   - Keep tension consistent to avoid loose windings
   - Bring out leads with strain relief

3. **Assembly:**
   - Insert 0.5mm gap spacer in center leg
   - Assemble E and I laminations (interleaved)
   - Clamp or band laminations securely
   - Apply protective coating or potting compound
   - Install mounting hardware

4. **Termination:**
   - Tin wire ends with solder
   - Connect to screw terminal block or solder lugs
   - Label clearly: "20 Hz - 3.5H"

### Test Procedures

1. **Visual Inspection:**
   - Check for damaged insulation
   - Verify no exposed wire
   - Confirm secure assembly

2. **Inductance Measurement:**
   - Use LCR meter at 100Hz or 120Hz
   - Target: 3.5H ±5% (3.33H to 3.68H)
   - If low: add turns
   - If high: remove turns or increase air gap slightly

3. **DC Resistance:**
   - Measure with DMM
   - Target: <5 Ω
   - Higher DCR indicates possible short or improper wire

4. **Resonance Test:**
   - Connect in parallel with 18nF capacitor
   - Apply swept sine wave (10Hz-50Hz)
   - Verify peak response at ~20Hz
   - Measure Q factor from bandwidth

5. **Insulation Test:**
   - Measure resistance core-to-winding: >10MΩ
   - Hi-pot test: 500VDC for 1 minute (optional)

### Acceptance Criteria

- Inductance: 3.33H to 3.68H (3.5H ±5%)
- DCR: <10 Ω (Q >44)
- Insulation: >10 MΩ
- Resonant frequency with 18nF: 19-21 Hz
- No mechanical noise or buzzing
- Clean appearance, no damage

---

## 30 Hz INDUCTOR

### Target Specifications
- **Inductance:** 2.8 H ±5%
- **Resonant Capacitor:** 10 nF (C2)
- **Resonant Frequency:** 30 Hz
- **Target DCR:** <60 Ω (Q >20 at 30Hz)
- **Core:** EI-100, 25mm stack

### Design Calculations

**Using same core as 20Hz inductor for consistency:**
- Core: EI-100, Aₑ = 2.5 × 10⁻⁴ m², lₑ = 0.2 m
- Air gap: 0.5 mm, μᵣ,eff ≈ 500

**Calculating turns:**
```
N = √(2.8 × 0.2 / (4π × 10⁻⁷ × 500 × 2.5 × 10⁻⁴))
N ≈ 1500 turns
```

### Final Specification

| Parameter | Value |
|-----------|-------|
| **Inductance** | 2.8 H ±5% |
| **Core Type** | EI-100 laminated steel |
| **Stack Height** | 25 mm |
| **Air Gap** | 0.5 mm |
| **Wire Gauge** | 20 AWG heavy build enamel |
| **Number of Turns** | 1500 turns |
| **Winding Pattern** | Layer wound |
| **Wire Length** | ~75 m (estimated) |
| **DCR (calculated)** | 2.5 Ω |
| **Q Factor (30Hz)** | 211 (excellent) |
| **Mounting** | Bobbin with mounting brackets |

### Winding Instructions

1. **Preparation:**
   - Clean EI-100 laminations (25mm stack)
   - Prepare bobbin with insulation
   - Cut 0.5mm air gap spacer

2. **Winding:**
   - Use 20 AWG heavy build magnet wire
   - Wind 1500 turns in layers
   - Layer distribution: ~33 turns per layer × 46 layers
   - Insulate between layers
   - Maintain consistent tension
   - Bring out leads with strain relief

3. **Assembly:**
   - Insert 0.5mm gap spacer in center leg
   - Assemble and clamp laminations
   - Apply protective coating
   - Install mounting hardware

4. **Termination:**
   - Tin and connect wire ends
   - Label: "30 Hz - 2.8H"

### Test Procedures

1. **Inductance Measurement:**
   - Target: 2.8H ±5% (2.66H to 2.94H)
   - Adjust turns if needed

2. **DC Resistance:**
   - Target: <5 Ω

3. **Resonance Test:**
   - Connect with 10nF capacitor
   - Verify peak at ~30Hz

4. **Insulation Test:**
   - Core-to-winding: >10MΩ

### Acceptance Criteria

- Inductance: 2.66H to 2.94H
- DCR: <10 Ω
- Insulation: >10 MΩ
- Resonant frequency with 10nF: 28.5-31.5 Hz
- No mechanical defects

---

## 60 Hz INDUCTOR

### Target Specifications
- **Inductance:** 1.5 H ±5%
- **Resonant Capacitor:** 4.7 nF (C3)
- **Resonant Frequency:** 60 Hz
- **Target DCR:** <35 Ω (Q >20 at 60Hz)
- **Core:** EI-87, 25mm stack

### Design Calculations

**Using smaller EI-87 core:**
- Core: EI-87, Aₑ = 1.88 × 10⁻⁴ m², lₑ = 0.174 m
- Air gap: 0.4 mm, μᵣ,eff ≈ 500

**Calculating turns:**
```
N = √(1.5 × 0.174 / (4π × 10⁻⁷ × 500 × 1.88 × 10⁻⁴))
N ≈ 1400 turns
```

### Final Specification

| Parameter | Value |
|-----------|-------|
| **Inductance** | 1.5 H ±5% |
| **Core Type** | EI-87 laminated steel |
| **Stack Height** | 25 mm |
| **Air Gap** | 0.4 mm |
| **Wire Gauge** | 20 AWG heavy build enamel |
| **Number of Turns** | 1400 turns |
| **Winding Pattern** | Layer wound |
| **Wire Length** | ~65 m (estimated) |
| **DCR (calculated)** | 2.2 Ω |
| **Q Factor (60Hz)** | 257 (excellent) |
| **Mounting** | Bobbin with mounting brackets |

### Winding Instructions

1. **Preparation:**
   - Clean EI-87 laminations (25mm stack)
   - Prepare bobbin with insulation
   - Cut 0.4mm air gap spacer

2. **Winding:**
   - Use 20 AWG heavy build magnet wire
   - Wind 1400 turns in layers
   - Layer distribution: ~30 turns per layer × 47 layers
   - Insulate between layers
   - Maintain consistent tension

3. **Assembly:**
   - Insert 0.4mm gap spacer
   - Assemble and clamp laminations
   - Apply protective coating

4. **Termination:**
   - Tin and connect wire ends
   - Label: "60 Hz - 1.5H"

### Test Procedures

1. **Inductance Measurement:**
   - Target: 1.5H ±5% (1.43H to 1.58H)

2. **DC Resistance:**
   - Target: <5 Ω

3. **Resonance Test:**
   - Connect with 4.7nF capacitor
   - Verify peak at ~60Hz

4. **Insulation Test:**
   - Core-to-winding: >10MΩ

### Acceptance Criteria

- Inductance: 1.43H to 1.58H
- DCR: <10 Ω
- Insulation: >10 MΩ
- Resonant frequency with 4.7nF: 57-63 Hz
- No mechanical defects

---

## 100 Hz INDUCTOR

### Target Specifications
- **Inductance:** 750 mH ±5%
- **Resonant Capacitor:** 3.3 nF (C4)
- **Resonant Frequency:** 100 Hz
- **Target DCR:** <25 Ω (Q >20 at 100Hz)
- **Core:** EI-87, 25mm stack

### Design Calculations

**Using EI-87 core:**
- Core: EI-87, Aₑ = 1.88 × 10⁻⁴ m², lₑ = 0.174 m
- Air gap: 0.4 mm, μᵣ,eff ≈ 500

**Calculating turns:**
```
N = √(0.75 × 0.174 / (4π × 10⁻⁷ × 500 × 1.88 × 10⁻⁴))
N ≈ 990 turns
```

### Final Specification

| Parameter | Value |
|-----------|-------|
| **Inductance** | 750 mH ±5% |
| **Core Type** | EI-87 laminated steel |
| **Stack Height** | 25 mm |
| **Air Gap** | 0.4 mm |
| **Wire Gauge** | 20 AWG heavy build enamel |
| **Number of Turns** | 990 turns |
| **Winding Pattern** | Layer wound |
| **Wire Length** | ~46 m (estimated) |
| **DCR (calculated)** | 1.5 Ω |
| **Q Factor (100Hz)** | 314 (excellent) |
| **Mounting** | Bobbin with mounting brackets |

### Winding Instructions

1. **Preparation:**
   - Clean EI-87 laminations (25mm stack)
   - Prepare bobbin with insulation
   - Cut 0.4mm air gap spacer

2. **Winding:**
   - Use 20 AWG heavy build enamel wire
   - Wind 990 turns in layers
   - Layer distribution: ~30 turns per layer × 33 layers
   - Insulate between layers
   - Maintain consistent tension

3. **Assembly:**
   - Insert 0.4mm gap spacer
   - Assemble and clamp laminations
   - Apply protective coating

4. **Termination:**
   - Tin and connect wire ends
   - Label: "100 Hz - 750mH"

### Test Procedures

1. **Inductance Measurement:**
   - Target: 750mH ±5% (713mH to 788mH)

2. **DC Resistance:**
   - Target: <5 Ω

3. **Resonance Test:**
   - Connect with 3.3nF capacitor
   - Verify peak at ~100Hz

4. **Insulation Test:**
   - Core-to-winding: >10MΩ

### Acceptance Criteria

- Inductance: 713mH to 788mH
- DCR: <10 Ω
- Insulation: >10 MΩ
- Resonant frequency with 3.3nF: 95-105 Hz
- No mechanical defects

---

## Bill of Materials

### Core Materials

| Item | Description | Qty | Supplier | Part Number | Est. Cost |
|------|-------------|-----|----------|-------------|-----------|
| EI-100 Laminations | M6 silicon steel, 25mm stack | 2 sets | Hammond | 166K25 | $8.00 ea |
| EI-87 Laminations | M6 silicon steel, 25mm stack | 2 sets | Hammond | 166J25 | $6.00 ea |
| Bobbin EI-100 | Plastic bobbin for EI-100 | 2 | Hammond | 166K-Bobbin | $2.00 ea |
| Bobbin EI-87 | Plastic bobbin for EI-87 | 2 | Hammond | 166J-Bobbin | $1.50 ea |

**Core Material Subtotal:** ~$35.00

### Wire and Assembly Materials

| Item | Description | Qty | Supplier | Part Number | Est. Cost |
|------|-------------|-----|----------|-------------|-----------|
| Magnet Wire | 20 AWG heavy build enamel | 300m spool | MWS Wire | MW0118 | $25.00 |
| Insulation Tape | Polyimide film tape, 0.05mm | 1 roll | 3M | P/N TBD | $8.00 |
| Gap Material | 0.5mm Nomex sheet | 1 sheet | Various | - | $5.00 |
| Gap Material | 0.4mm Nomex sheet | 1 sheet | Various | - | $5.00 |
| Mounting Hardware | Brackets, screws, standoffs | 1 set | Various | - | $10.00 |
| Potting Compound | Optional, epoxy or wax | 1 container | MG Chemicals | 832TC | $12.00 |

**Assembly Materials Subtotal:** ~$65.00

### **Total BOM Cost: ~$100.00** (for complete set of 4 inductors)

---

## Supplier Information

### Core Suppliers
1. **Hammond Manufacturing** - www.hammfg.com
   - E-I laminations, bobbins
   - North American distributor: Mouser, Digi-Key

2. **Magnetic Metals** - www.magmet.com
   - Premium laminations for critical applications
   - Direct or through distributors

3. **National Imports** - www.nationalimports.com
   - Generic E-I cores at lower cost
   - Good for prototyping

### Wire Suppliers
1. **MWS Wire Industries** - www.mwswire.com
   - Extensive magnet wire selection
   - Heavy build enamel in all gauges

2. **Essex Furukawa Magnet Wire** - www.essexfurukawa.com
   - High-quality magnet wire
   - Available through Digi-Key

3. **Remington Industries** - www.remingtonindustries.com
   - Good value, smaller spools available

### Tools and Equipment Suppliers
1. **Digi-Key Electronics** - www.digikey.com
2. **Mouser Electronics** - www.mouser.com
3. **Newark Electronics** - www.newark.com

---

## Tools Required

### For Winding
- Hand winding jig or lathe with turn counter
- Wire tensioning device
- Scissors/wire cutters
- Soldering iron and solder
- Heat shrink tubing
- Insulation tape dispenser

### For Testing
- **LCR Meter** (essential)
  - Recommended: BK Precision 889B or similar
  - Frequency range: 100Hz-1kHz
  - Accuracy: ±0.5%

- **Digital Multimeter** (for DCR)
  - Any quality DMM with 0.1Ω resolution

- **Function Generator** (for resonance testing)
  - Frequency range: 10Hz-200Hz
  - Output: 1Vpp minimum

- **Oscilloscope** (for resonance testing)
  - Bandwidth: 20MHz minimum

- **Insulation Tester** (optional)
  - 500VDC megohmmeter

### For Assembly
- Clamps or bands for lamination assembly
- Non-magnetic spacer material (plastic, brass)
- Precision feeler gauges (for air gap)
- Label maker or tags

---

## Winding Best Practices

### General Guidelines

1. **Workspace Setup:**
   - Clean, well-lit area
   - Stable mounting for winding jig
   - Wire spool holder with adjustable tension

2. **Wire Handling:**
   - Do not kink or damage enamel insulation
   - Maintain consistent tension (not too tight)
   - Avoid sharp bends at terminations

3. **Layer Winding:**
   - Wind layers evenly, no crossovers
   - Progress from one end to other smoothly
   - Each layer should lie flat before next layer
   - Insulate between layers with thin tape

4. **Turn Counting:**
   - Use mechanical or electronic counter
   - Mark every 100 turns for verification
   - Double-check final count before terminating

5. **Bobbin Preparation:**
   - Insulate bobbin cheeks with tape
   - Leave clearance for final wrapping
   - Provide holes or slots for lead exit

### Air Gap Procedure

1. **Gap Material:**
   - Use non-magnetic, non-conductive material
   - Nomex, Mylar, or fiber spacers
   - Thickness tolerance: ±0.05mm

2. **Gap Placement:**
   - Place in center leg of E lamination
   - Gap should span full width of leg
   - Both E halves should have gap for symmetry

3. **Gap Adjustment:**
   - Measure inductance after assembly
   - Increase gap to reduce inductance
   - Decrease gap to increase inductance
   - Typical adjustment: 0.1mm changes L by ~10-15%

### Common Issues and Solutions

| Problem | Cause | Solution |
|---------|-------|----------|
| Inductance too low | Not enough turns or gap too large | Add turns or reduce gap |
| Inductance too high | Too many turns or gap too small | Remove turns or increase gap |
| High DCR | Poor connections or damaged wire | Check terminations, rewire if needed |
| Buzzing/humming | Loose laminations | Tighten clamps or add potting |
| Low insulation | Damaged wire or contamination | Check for pinched wire, clean core |
| Unstable inductance | Temperature-dependent core | Use better core material or accept drift |

---

## Integration with Low Boost Module

### Physical Mounting

**Option 1: External Mounting (Recommended)**
- Mount inductors on chassis or separate board
- Connect to PCB via screw terminals
- Allows easy access for measurement and replacement
- Keeps magnetic components away from sensitive circuitry

**Option 2: PCB-Adjacent Mounting**
- Mount on standoffs near Low Boost PCB
- Short wire runs to screw terminals
- More compact but harder to service

### Electrical Connections

**From PCB to Inductors:**
- Use stranded hookup wire, 22-24 AWG
- Twisted pair recommended to minimize pickup
- Keep wire runs <30cm for low frequencies
- Label both ends clearly with frequency designation

**Screw Terminal Connections:**
- Use ring terminals for reliability
- Crimp and solder for best connection
- Observe polarity marking (if inductors have polarity)

### Shielding (Optional)

**For environments with strong magnetic fields:**
- Enclose inductors in mu-metal shield
- Ground shield to circuit common
- Increases cost but reduces hum pickup
- Typically not necessary in well-designed chassis

---

## Performance Verification

### Frequency Response Testing

**Equipment Setup:**
1. Function generator → Low Boost Module → Oscilloscope
2. Set frequency selector to each position (20/30/60/100 Hz)
3. Set boost level to maximum
4. Sweep frequency around target

**Expected Results:**

| Frequency | Sweep Range | Peak Frequency | 3dB Bandwidth | Q Factor |
|-----------|-------------|----------------|---------------|----------|
| 20 Hz | 10-40 Hz | 20 Hz ±5% | <3 Hz | >20 |
| 30 Hz | 15-60 Hz | 30 Hz ±5% | <5 Hz | >20 |
| 60 Hz | 30-120 Hz | 60 Hz ±5% | <10 Hz | >20 |
| 100 Hz | 50-200 Hz | 100 Hz ±5% | <15 Hz | >20 |

### Q Factor Measurement

**Method 1: 3dB Bandwidth Method**
```
Q = f₀ / Δf₃dB

Where:
- f₀ = resonant frequency
- Δf₃dB = bandwidth between -3dB points
```

**Method 2: LCR Meter**
- Modern LCR meters can measure Q directly
- Test at or near resonant frequency
- Compare measured Q to calculated

**Acceptable Q Range:**
- Minimum: Q >20 (adequate performance)
- Target: Q >50 (good performance)
- Excellent: Q >100 (minimal losses)

### Troubleshooting Low Q

If measured Q is lower than expected:

1. **Check DCR:** High resistance reduces Q
   - Verify wire gauge and connections
   - Look for damaged wire or poor terminations

2. **Check Capacitor:** ESR affects Q
   - Use high-quality film capacitors
   - Verify capacitance value is correct

3. **Check Core:** Core losses reduce Q
   - Verify proper core material (M6 silicon steel)
   - Check for damaged or misaligned laminations
   - Ensure air gap is present for linearity

4. **Check External Loading:** Circuit resistance affects Q
   - Measure Q with inductor disconnected from circuit
   - Compare to in-circuit measurement

---

## Long-Term Reliability

### Expected Lifetime
- **Typical:** 20+ years with proper construction
- **Failure Modes:** Wire insulation breakdown, core oxidation
- **MTBF:** >100,000 hours (inductor alone)

### Maintenance Requirements
- **Annual:** Visual inspection, verify mounting security
- **Every 5 years:** Inductance verification, DCR check
- **As needed:** Clean dust/debris, check connections

### Storage Recommendations
- Store in dry environment (<60% RH)
- Protect from physical damage
- Keep away from strong magnetic fields
- If potted, check for cracking or separation

---

## Alternative Core Technologies

While laminated E-I cores are recommended, alternative technologies may be considered:

### Powdered Iron Toroids

**Advantages:**
- Self-shielding (toroidal geometry)
- No air gap required
- Compact size

**Disadvantages:**
- Lower permeability than laminated steel
- More turns required (higher DCR)
- Hand winding toroids is tedious
- Limited availability in large sizes for low frequencies

**Suitable Materials:**
- Micrometals -8 material (35μ) - not ideal, too low
- Magnetics W material (90μ) - marginal
- Not recommended for <100Hz due to size/DCR constraints

### Ferrite Cores

**Advantages:**
- High permeability available
- Low cost

**Disadvantages:**
- Higher losses at low frequency
- Temperature sensitive
- Fragile (ceramic material)

**Assessment:** Not recommended for audio inductor applications

### Recommendation: Stick with laminated E-I steel cores for best performance

---

## Cost Analysis

### Per-Inductor Cost Breakdown

| Component | 20Hz | 30Hz | 60Hz | 100Hz |
|-----------|------|------|------|-------|
| Core & bobbin | $10 | $10 | $7.50 | $7.50 |
| Wire (~$0.08/m) | $6.70 | $6.00 | $5.20 | $3.70 |
| Assembly materials | $2.00 | $2.00 | $2.00 | $2.00 |
| **Subtotal** | **$18.70** | **$18.00** | **$14.70** | **$13.20** |

### **Total Cost for Complete Set: ~$64.60**

### Commercial Alternatives

**Custom Wound Inductors:**
- Typical cost: $50-150 per inductor
- Lead time: 4-8 weeks
- Minimum order quantities may apply

**Surplus/Vintage Inductors:**
- Unpredictable availability
- May require modification
- Values may not match exactly

**Assessment:** Hand-winding is most cost-effective for low quantities

---

## Revision History

- v1.0 - 2025-10-26 - Initial complete design specification
- Designed for: Pultec Three-Band EQ Low Boost Module
- Based on: Ian Thompson-Bell reference design
- Engineer: Claude (Inductor Design Specialist)

---

## References

1. Ian Thompson-Bell, "Stepped Pots for 3 Band Pultec", Issue 0.2, August 2016
2. Hammond Manufacturing, E-I Lamination Data Sheets
3. Magnetic Metals, Nickel-Iron Alloy Technical Data
4. MWS Wire Industries, Magnet Wire Technical Specifications
5. "Inductor Design Handbook" - Various Authors
6. Project documentation: /Users/orion/work/multi-channel-preamp/src/pultec/

---

## Appendix A: Calculation Worksheets

### Inductance Calculation Template

```
Given:
- Target frequency: f₀ = ____ Hz
- Capacitance: C = ____ nF = ____ × 10⁻⁹ F

Calculate Required Inductance:
L = 1 / (4π²f₀²C)
L = 1 / (4 × π² × ____² × ____ × 10⁻⁹)
L = ____ H

Calculate Number of Turns:
Given core parameters:
- Effective area: Aₑ = ____ m²
- Magnetic path length: lₑ = ____ m
- Effective permeability: μᵣ,eff = ____

N = √(L × lₑ / (μ₀ × μᵣ × Aₑ))
N = √(____ × ____ / (4π × 10⁻⁷ × ____ × ____))
N = ____ turns

Calculate DCR:
Wire resistance: R_wire = ____ Ω/m
Wire length: l_wire = π × d_avg × N = ____ m
DCR = R_wire × l_wire = ____ Ω

Calculate Q Factor:
X_L = 2πfL = 2 × π × ____ × ____ = ____ Ω
Q = X_L / DCR = ____ / ____ = ____
```

---

## Appendix B: Test Report Template

### Low Boost Inductor Test Report

**Inductor Designation:** ______ Hz

**Date:** __________
**Technician:** __________
**Serial Number:** __________

#### Visual Inspection
- [ ] No visible damage to wire insulation
- [ ] Laminations properly assembled
- [ ] Secure mounting hardware
- [ ] Clear labeling
- [ ] Notes: ________________________________

#### Electrical Measurements

| Parameter | Specification | Measured | Pass/Fail |
|-----------|---------------|----------|-----------|
| Inductance @ 120Hz | _____ H ±5% | _____ H | |
| DC Resistance | <10 Ω | _____ Ω | |
| Core-to-Winding Insulation | >10 MΩ | _____ MΩ | |

#### Resonance Test

| Parameter | Specification | Measured | Pass/Fail |
|-----------|---------------|----------|-----------|
| Resonant Frequency | _____ Hz ±5% | _____ Hz | |
| Q Factor | >20 | _____ | |
| 3dB Bandwidth | _____ Hz | _____ Hz | |

#### Overall Assessment
- [ ] PASS - Ready for installation
- [ ] CONDITIONAL - Notes: ________________________________
- [ ] FAIL - Reason: ________________________________

**Signature:** __________
**Date:** __________

---

## Appendix C: Troubleshooting Guide

### Problem: Cannot achieve target inductance

**Symptoms:** Measured inductance consistently wrong

**Diagnostic Steps:**
1. Verify turn count is correct
2. Check core assembly (all laminations in place?)
3. Measure air gap with feeler gauge
4. Verify core material (is it actually silicon steel?)

**Solutions:**
- Add/remove turns to adjust inductance
- Adjust air gap (wider gap = less inductance)
- Replace core if damaged or incorrect material

### Problem: High DC resistance

**Symptoms:** DCR >10Ω, low Q factor

**Diagnostic Steps:**
1. Check wire gauge (should be 20 AWG)
2. Measure wire length (compare to calculated)
3. Check termination connections
4. Verify no partial shorts between layers

**Solutions:**
- Use heavier gauge wire (18 AWG)
- Improve termination connections
- Reduce number of turns if possible
- Check for damaged wire, rewind if necessary

### Problem: Mechanical buzzing at resonance

**Symptoms:** Audible vibration when driven at resonant frequency

**Diagnostic Steps:**
1. Check lamination clamping
2. Verify bobbin is secure to core
3. Check for loose turns in winding

**Solutions:**
- Tighten lamination clamps/bands
- Pot or wax impregnate winding
- Use damping material between laminations
- Ensure mounting is vibration-isolated

### Problem: Resonant frequency off-target

**Symptoms:** Peak response not at expected frequency

**Diagnostic Steps:**
1. Verify capacitor value with LCR meter
2. Measure inductance accurately
3. Check for parallel capacitance (cable, circuit)
4. Verify test setup is correct

**Solutions:**
- Adjust inductance to compensate
- Replace capacitor if value is wrong
- Minimize cable length in test setup
- Recalculate with actual measured values

---

**END OF SPECIFICATION DOCUMENT**
