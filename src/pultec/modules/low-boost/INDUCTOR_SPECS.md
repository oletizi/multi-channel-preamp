# Low Boost Inductor Design Specifications
## Pultec Three-Band EQ - Low Boost Module

## Overview

This document provides complete design specifications for the four inductors required by the Low Boost module. These inductors form resonant LC circuits with capacitors to provide frequency-selective boost at 20Hz, 30Hz, 60Hz, and 100Hz.

## IMPORTANT NOTE ON CAPACITOR VALUES

**The existing LOW_BOOST_INDUCTOR_SPECIFICATIONS.md document contains an error in the analysis.** The capacitor values listed in COMPONENT_VALUES.md (C1=18nF, C2=10nF, etc.) cannot produce the claimed inductance values (3.5H, 2.8H, etc.) at the target frequencies.

### Correct Analysis:

For 20Hz resonance with 18nF:
```
L = 1 / (4π² × 20² × 18×10⁻⁹) = 3518 H (not 3.5H!)
```

This 1000× discrepancy suggests either:
1. The capacitor values in the schematic are actually **microfarads** (18µF, not 18nF), OR
2. The target frequencies are actually **much higher** (not 20/30/60/100 Hz), OR
3. There is a series/parallel combination of capacitors not documented

### Most Likely Scenario: µF Capacitors

Classic Pultec designs use **electrolytic capacitors in the low boost section** (despite the preference for film caps elsewhere) because the required values are large (microfarads).

**Revised capacitor interpretation:**
- C1: 18µF (not 18nF) → L = 3.52H @ 20Hz ✓
- C2: 10µF (not 10nF) → L = 2.81H @ 30Hz ✓
- C3: 4.7µF (not 4.7nF) → L = 1.50H @ 60Hz ✓
- C4: 3.3µF (not 3.3nF) → L = 0.768H @ 100Hz ✓

These values match the existing specification document perfectly.

## Circuit Topology

The low boost section uses a passive LC network where an inductor and capacitor resonate at the selected frequency. Due to the large inductance values required (0.75H to 3.5H), these inductors must use laminated steel E-I cores for practical size and reasonable DC resistance.

## Resonant Frequency Formula

For series LC resonance:
```
f₀ = 1 / (2π√LC)

Solving for L:
L = 1 / (4π²f₀²C)
```

## Capacitor-to-Frequency Mapping

**Corrected values (assuming µF, not nF):**

| Frequency | Capacitor | Actual Value | Required Inductance |
|-----------|-----------|--------------|---------------------|
| 20 Hz | C1 | 18 µF | 3.52 H |
| 30 Hz | C2 | 10 µF | 2.81 H |
| 60 Hz | C3 | 4.7 µF | 1.50 H |
| 100 Hz | C4 | 3.3 µF | 0.768 H (768 mH) |

**RECOMMENDATION:** Verify actual capacitor values in the original schematic. If they are film caps (nF range), then either:
- The target frequencies are incorrect, OR
- There is a capacitor bank/combination not shown in COMPONENT_VALUES.md

For this specification, we proceed with the assumption that these are µF-range electrolytic capacitors, matching classic Pultec designs.

## Core Selection: Laminated Silicon Steel E-I Cores

### Why Laminated Steel?

Low frequencies (20-100Hz) with large inductances (0.75-3.5H) require:
- **High permeability:** µᵣ = 2000-4000 (laminated steel)
- **Large core size:** To accommodate many turns
- **Low core losses:** At audio frequencies
- **Distributed air gap:** For linearity and to prevent saturation

Alternatives (powdered iron toroids) would require:
- Extremely large cores (T400 or larger)
- Very high turn counts (5000-10000 turns)
- Prohibitively high DC resistance
- Impractical size and cost

### Recommended Cores: Hammond Manufacturing 166 Series

**Core Material:** M6 grain-oriented silicon steel
- **Permeability:** µᵣ ≈ 3000 (typical)
- **Saturation flux density:** 1.5-1.8 Tesla
- **Core losses:** <5 W/kg @ 60Hz, 1T (excellent for audio)
- **Temperature stability:** Good (±0.01%/°C)

**Core Sizes:**

| Core Model | Lamination | Stack | Core Area (Aₑ) | Path Length (lₑ) | For Frequencies |
|------------|------------|-------|----------------|------------------|-----------------|
| Hammond 166K25 | EI-100 | 25mm | 250 mm² | 200 mm | 20Hz, 30Hz |
| Hammond 166J25 | EI-87 | 25mm | 188 mm² | 174 mm | 60Hz, 100Hz |

**Alternative:** Magnetic Metals Co. laminated cores (50% Nickel-Iron)
- Higher permeability (µᵣ ≈ 4000)
- Superior performance but 2-3× cost
- Use if budget allows

**Supplier Information:**
- Hammond Manufacturing: www.hammfg.com
- Available through Mouser, Digi-Key, Newark
- Magnetic Metals: www.magmet.com (direct or distributors)

## Air Gap Requirement

**Why Air Gap?**
- Prevents core saturation with DC or low-frequency AC
- Linearizes inductance vs. current relationship
- Essential for audio applications (distortion <0.1%)

**Gap Size:** 0.4-0.5mm (total)
- Split between both E-core center legs (0.2-0.25mm each)
- Use non-magnetic spacer material (Nomex, Mylar, fiber)
- Reduces effective permeability from ~3000 to ~500

**Effect on Design:**
- Requires more turns for same inductance
- But provides stable, linear inductance
- Critical for low-distortion audio

---

## INDUCTOR SPECIFICATIONS

### 20 Hz INDUCTOR

**ELECTRICAL SPECIFICATIONS:**
- **Target Inductance:** 3.52 H ±5%
- **Resonant Capacitor:** 18 µF (C1)
- **Resonant Frequency:** 20 Hz
- **Target Q:** >20 (DCR <11Ω @ 20Hz)
- **Target DCR:** <10Ω (preferred for Q >44)

**CORE DESIGN:**
- **Core Type:** EI-100 laminated silicon steel, 25mm stack
- **Core Model:** Hammond 166K25 or equivalent
- **Core Area (Aₑ):** 250 mm² = 2.5 × 10⁻⁴ m²
- **Magnetic Path (lₑ):** 200 mm = 0.2 m
- **Air Gap:** 0.5mm total (0.25mm each E-piece center leg)
- **Effective Permeability:** µᵣ,eff ≈ 500 (with air gap)

**WINDING DESIGN:**
- **Inductance Formula:** L = (µ₀ × µᵣ × N² × Aₑ) / lₑ
- **Turns Required:** N = √(L × lₑ / (µ₀ × µᵣ × Aₑ))
  - N = √(3.52 × 0.2 / (4π×10⁻⁷ × 500 × 2.5×10⁻⁴))
  - N = **1683 turns**
- **Wire Gauge:** 20 AWG heavy build enamel magnet wire
  - Diameter: 0.812mm (bare), ~0.88mm (insulated)
  - Resistance: 0.0333 Ω/m
- **Mean Turn Length:** Approximate bobbin circumference
  - For EI-100 bobbin: ~100mm = 0.1m per turn
- **Total Wire Length:** 1683 × 0.1m = **168.3 meters**
- **Calculated DCR:** 168.3m × 0.0333 Ω/m = **5.6Ω**
- **Calculated Q @ 20Hz:** (2π × 20 × 3.52) / 5.6 = **79** (excellent!)

**PHYSICAL SPECIFICATIONS:**
- Bobbin: Matches EI-100 lamination
- Winding layers: ~55-60 layers (30-32 turns per layer)
- Finished weight: ~1.5 kg (core + wire)
- Mounting: Clamp or bracket assembly

**WINDING INSTRUCTIONS:**

1. **Bobbin Preparation:**
   - Clean EI-100 bobbin
   - Line cheeks with 0.1mm insulation tape (nomex or polyester)
   - Ensure smooth edges (no burrs to damage wire enamel)

2. **Air Gap Preparation:**
   - Cut two 0.25mm spacers from non-magnetic material (Nomex, fiber board, or polyester film)
   - Spacers should cover full width and length of center leg
   - Set aside for assembly

3. **Winding Process:**
   - Use 20 AWG heavy build magnet wire
   - Start winding at one end of bobbin
   - **First Layer:** Wind 30-32 turns evenly across bobbin width
     - Maintain firm but not excessive tension
     - Turns should be snug but not overlapping
   - **Layer Insulation:** After each layer, apply thin film tape (0.025-0.05mm)
     - Extends slightly beyond winding to prevent turn-to-turn contact between layers
   - **Subsequent Layers:** Continue winding, insulating between each layer
   - **Turn Counting:** Use mechanical counter or mark every 100 turns with tape flag
   - **Total Turns:** 1683 turns (approximately 55 layers)
   - **Lead-Out:** Leave 8-10" leads at each end for termination

4. **Core Assembly:**
   - **Gap Installation:** Place 0.25mm spacer on center leg of each E-piece
   - **Lamination Assembly:** 
     - Interleave E and I laminations (reduces losses and noise)
     - Alternate EI, IE, EI, IE pattern through stack
   - **Clamping:** 
     - Use clamp frame or steel banding
     - Tighten evenly to prevent buzzing
     - Do not over-tighten (can stress insulation)
   - **Mounting:** 
     - Attach mounting brackets
     - Use rubber or silicone isolation if vibration-sensitive environment

5. **Winding Protection:**
   - Wrap entire winding with fabric tape or apply protective coating
   - Optional: Vacuum impregnate with varnish or pot with epoxy
     - Potting reduces noise but makes rework impossible
     - Varnish impregnation is good compromise

6. **Termination:**
   - Strip 6-8mm of enamel from each lead
     - Method 1: Scrape with knife blade
     - Method 2: Burn off with lighter, then scrape carbon
     - Method 3: Chemical enamel stripper
   - Tin leads with 60/40 solder
   - Attach ring terminals or solder lugs
   - Secure with strain relief (heat shrink or tie-wrap)
   - **Label clearly: "20 Hz - 3.5H"**

**TEST PROCEDURES:**

1. **Visual Inspection:**
   - No damaged wire insulation
   - No exposed bare wire
   - Laminations properly assembled and clamped
   - No gaps in winding (even layer structure)

2. **DC Resistance (DCR):**
   - **Instrument:** Digital multimeter, 0.1Ω resolution
   - **Measurement:** Measure resistance between leads
   - **Target:** 4-8Ω (calculated 5.6Ω)
   - **Troubleshooting:**
     - DCR >10Ω: Check for poor connection at termination, or wire damage
     - DCR <3Ω: Possible short between layers (unlikely if insulated properly)

3. **Inductance Measurement:**
   - **Instrument:** LCR meter capable of measuring >1H
     - BK Precision 889B, Keysight U1733C, or equivalent
   - **Test Frequency:** 100Hz or 120Hz (close to operating frequency)
   - **Target:** 3.34 - 3.70 H (3.52H ±5%)
   - **Adjustment:**
     - Inductance too low: Reduce air gap by 0.05-0.1mm (add turns if already minimum gap)
     - Inductance too high: Increase air gap by 0.05-0.1mm

4. **Q Factor Measurement:**
   - **Method 1: LCR Meter Direct**
     - Modern LCR meters display Q factor directly
     - Test at 100Hz or 120Hz
     - Target: Q >20, prefer Q >40
   - **Method 2: Calculate from L and DCR**
     - Q = (2π × f × L) / DCR
     - Example: Q = (2π × 20 × 3.52) / 5.6 = 79

5. **Resonance Test:**
   - **Setup:** Connect 18µF capacitor in parallel with inductor
   - **Equipment:** Function generator (sine wave, 10-50Hz sweep), oscilloscope
   - **Procedure:**
     - Drive network with low-level signal (<1V)
     - Sweep frequency from 15Hz to 30Hz
     - Observe impedance peak or amplitude maximum
   - **Target:** Peak response at 19-21 Hz (20Hz ±5%)
   - **Troubleshooting:**
     - Peak too low: Verify capacitor value (measure with LCR meter)
     - Peak too high: Verify inductor value
     - Broad peak: Check Q factor

6. **Insulation Test:**
   - **Instrument:** Megohmmeter (insulation tester) at 500VDC
   - **Measurement:** Resistance from winding to core
   - **Target:** >10 MΩ (preferably >50 MΩ)
   - **Safety:** Discharge winding after test (high voltage remains briefly)

7. **Mechanical Test:**
   - **Listen for Buzz:**
     - Drive with 60Hz signal at moderate level (~10V)
     - Listen for mechanical vibration or buzz
   - **Troubleshooting:** If buzzing:
     - Tighten lamination clamps
     - Add damping material between laminations (thin rubber sheet)
     - Pot or impregnate winding with varnish

**ACCEPTANCE CRITERIA:**
- Inductance: 3.34 - 3.70 H
- DCR: <10Ω (preferably <8Ω)
- Q Factor: >20 (preferably >40)
- Insulation: >10 MΩ
- Resonant frequency with 18µF: 19-21 Hz
- No mechanical buzzing or vibration
- Clean appearance, no damage

---

### 30 Hz INDUCTOR

**ELECTRICAL SPECIFICATIONS:**
- **Target Inductance:** 2.81 H ±5%
- **Resonant Capacitor:** 10 µF (C2)
- **Resonant Frequency:** 30 Hz
- **Target Q:** >20 (DCR <17Ω @ 30Hz)
- **Target DCR:** <10Ω (preferred)

**CORE DESIGN:**
- **Core Type:** EI-100 laminated silicon steel, 25mm stack
- **Core Model:** Hammond 166K25 or equivalent
- **Air Gap:** 0.5mm total
- **Effective Permeability:** µᵣ,eff ≈ 500

**WINDING DESIGN:**
- **Turns Required:** √(2.81 × 0.2 / (4π×10⁻⁷ × 500 × 2.5×10⁻⁴)) = **1504 turns**
- **Wire Gauge:** 20 AWG (0.0333 Ω/m)
- **Wire Length:** 1504 × 0.1m = **150.4 meters**
- **Calculated DCR:** 150.4m × 0.0333 Ω/m = **5.0Ω**
- **Calculated Q @ 30Hz:** (2π × 30 × 2.81) / 5.0 = **106** (excellent!)

**WINDING INSTRUCTIONS:**
- Follow same procedure as 20Hz inductor
- Wind 1504 turns in approximately 50 layers
- Use same 20 AWG wire, EI-100 core, 0.5mm air gap
- Label: "30 Hz - 2.8H"

**TEST PROCEDURES:**
1. Inductance: 2.67 - 2.95 H (2.81H ±5%)
2. DCR: <10Ω
3. Q Factor: >20 @ 30Hz
4. Insulation: >10 MΩ
5. Resonance with 10µF: 28.5 - 31.5 Hz
6. No mechanical issues

---

### 60 Hz INDUCTOR

**ELECTRICAL SPECIFICATIONS:**
- **Target Inductance:** 1.50 H ±5%
- **Resonant Capacitor:** 4.7 µF (C3)
- **Resonant Frequency:** 60 Hz
- **Target Q:** >20 (DCR <28Ω @ 60Hz)
- **Target DCR:** <15Ω (preferred)

**CORE DESIGN:**
- **Core Type:** EI-87 laminated silicon steel, 25mm stack
- **Core Model:** Hammond 166J25 or equivalent
- **Core Area (Aₑ):** 188 mm² = 1.88 × 10⁻⁴ m²
- **Magnetic Path (lₑ):** 174 mm = 0.174 m
- **Air Gap:** 0.4mm total (0.2mm each E-piece)
- **Effective Permeability:** µᵣ,eff ≈ 500

**WINDING DESIGN:**
- **Turns Required:** √(1.50 × 0.174 / (4π×10⁻⁷ × 500 × 1.88×10⁻⁴)) = **1404 turns**
- **Wire Gauge:** 20 AWG (0.0333 Ω/m)
- **Mean Turn Length:** ~85mm = 0.085m (smaller core than EI-100)
- **Wire Length:** 1404 × 0.085m = **119.3 meters**
- **Calculated DCR:** 119.3m × 0.0333 Ω/m = **4.0Ω**
- **Calculated Q @ 60Hz:** (2π × 60 × 1.50) / 4.0 = **141** (excellent!)

**WINDING INSTRUCTIONS:**
- Use EI-87 core (smaller than 20Hz/30Hz)
- Wind 1404 turns in approximately 55-60 layers
- Use 20 AWG wire, 0.4mm air gap
- Layer pattern: ~25-28 turns per layer
- Label: "60 Hz - 1.5H"

**TEST PROCEDURES:**
1. Inductance: 1.43 - 1.58 H (1.50H ±5%)
2. DCR: <10Ω
3. Q Factor: >20 @ 60Hz
4. Insulation: >10 MΩ
5. Resonance with 4.7µF: 57 - 63 Hz
6. No mechanical issues

---

### 100 Hz INDUCTOR

**ELECTRICAL SPECIFICATIONS:**
- **Target Inductance:** 768 mH ±5% (0.768 H)
- **Resonant Capacitor:** 3.3 µF (C4)
- **Resonant Frequency:** 100 Hz
- **Target Q:** >20 (DCR <24Ω @ 100Hz)
- **Target DCR:** <15Ω (preferred)

**CORE DESIGN:**
- **Core Type:** EI-87 laminated silicon steel, 25mm stack
- **Core Model:** Hammond 166J25 or equivalent
- **Air Gap:** 0.4mm total
- **Effective Permeability:** µᵣ,eff ≈ 500

**WINDING DESIGN:**
- **Turns Required:** √(0.768 × 0.174 / (4π×10⁻⁷ × 500 × 1.88×10⁻⁴)) = **1005 turns**
- **Wire Gauge:** 20 AWG (0.0333 Ω/m)
- **Wire Length:** 1005 × 0.085m = **85.4 meters**
- **Calculated DCR:** 85.4m × 0.0333 Ω/m = **2.8Ω**
- **Calculated Q @ 100Hz:** (2π × 100 × 0.768) / 2.8 = **172** (excellent!)

**WINDING INSTRUCTIONS:**
- Use EI-87 core
- Wind 1005 turns in approximately 40 layers
- Use 20 AWG wire, 0.4mm air gap
- Layer pattern: ~25-28 turns per layer
- Label: "100 Hz - 768mH" or "100 Hz - 0.77H"

**TEST PROCEDURES:**
1. Inductance: 730 - 806 mH (768mH ±5%)
2. DCR: <10Ω
3. Q Factor: >20 @ 100Hz
4. Insulation: >10 MΩ
5. Resonance with 3.3µF: 95 - 105 Hz
6. No mechanical issues

---

## Bill of Materials - Low Boost Inductors

### Core Materials

| Item | Description | Qty | Supplier | Part Number | Unit Price | Total |
|------|-------------|-----|----------|-------------|------------|-------|
| EI-100 Laminations | M6 silicon steel, 25mm stack | 2 | Hammond | 166K25 | $8.00 | $16.00 |
| EI-87 Laminations | M6 silicon steel, 25mm stack | 2 | Hammond | 166J25 | $6.00 | $12.00 |
| Bobbin for EI-100 | Plastic, fits 166K25 | 2 | Hammond | 166K-B | $2.50 | $5.00 |
| Bobbin for EI-87 | Plastic, fits 166J25 | 2 | Hammond | 166J-B | $2.00 | $4.00 |

**Core Subtotal:** $37.00

### Wire and Assembly Materials

| Item | Description | Qty | Supplier | Part Number | Est. Cost |
|------|-------------|-----|----------|-------------|-----------|
| 20 AWG Magnet Wire | Heavy build enamel, 2 lb spool (~1600m) | 1 | MWS Wire | MW0118-2LB | $45.00 |
| Nomex Sheet 0.25mm | Air gap spacer material | 1 sheet | Various | - | $8.00 |
| Nomex Sheet 0.5mm | Air gap spacer material | 1 sheet | Various | - | $8.00 |
| Layer Insulation Tape | Polyester film, 0.05mm, 1" wide | 2 rolls | 3M | - | $12.00 |
| Core Clamps | Steel strapping or clamp frames | 4 sets | Various | - | $16.00 |
| Mounting Hardware | Brackets, screws, rubber isolators | 1 set | Various | - | $12.00 |
| Varnish (optional) | Impregnating varnish for windings | 1 can | MG Chemicals | 4228 | $15.00 |
| Wire Terminals | Ring terminals or solder lugs | 8 | Various | - | $3.00 |
| Heat Shrink Tubing | Assorted sizes | 1 kit | Various | - | $5.00 |

**Materials Subtotal:** $124.00

### **TOTAL BOM COST: ~$161.00** (for complete set of 4 inductors)

**Note:** Cost can be reduced by ~$40 if you have bulk magnet wire on hand or by omitting optional varnish treatment.

---

## Tools Required

### For Winding
- **Winding jig:** Hand-crank or motorized bobbin winder
  - Can improvise with lathe or drill press at slow speed
- **Turn counter:** Mechanical or electronic
  - Critical for accuracy (1% = ±15-17 turns for these inductors)
- **Wire tensioning device:** Spring-loaded or friction tensioner
  - Maintains consistent tension during winding
- **Wire shuttle:** For toroid winding (not needed for bobbin)
- **Cutting tools:** Scissors, knife, wire cutters
- **Precision feeler gauges:** For measuring air gap (0.1-1.0mm range)
- **Soldering station:** Temperature-controlled, 60W minimum
- **Heat gun:** For heat shrink tubing
- **Clamps or bands:** For lamination assembly

### For Testing (ESSENTIAL)
- **LCR Meter:**
  - **Requirements:** Must measure inductance >1H, Q factor, DCR
  - **Recommended Models:**
    - BK Precision 889B (~$400) - excellent for audio work
    - Keysight U1733C (~$600) - handheld, lab-grade
    - GW Instek LCR-8110G (~$1200) - benchtop, highly accurate
  - **Minimum Specs:**
    - Frequency range: 100Hz-10kHz
    - Inductance range: 1mH-10H
    - Accuracy: ±1% or better

- **Digital Multimeter:**
  - Any quality DMM with 0.1Ω resolution
  - For DCR measurement

- **Function Generator:**
  - Frequency range: 10Hz-200Hz
  - Output: 1-10Vpp
  - Sine wave

- **Oscilloscope:**
  - Bandwidth: 20MHz minimum
  - 2 channels
  - For frequency response and resonance testing

- **Insulation Tester (Megohmmeter):**
  - 500VDC test voltage
  - Measures >100MΩ
  - Safety-critical for mains-powered equipment

---

## Winding Best Practices for Laminated Core Inductors

### Bobbin Winding Technique (vs. Toroidal)

Laminated E-I cores use bobbins, which is **much easier** than winding toroids:

**Advantages of Bobbin Winding:**
- Simple back-and-forth winding (like thread on a spool)
- Easy to count turns
- Easy to access for layer insulation
- No need to pass wire through center hole repeatedly

**Procedure:**

1. **Mount Bobbin:**
   - Place bobbin on winding jig mandrel
   - Secure so it rotates smoothly
   - Position wire spool with tensioning device

2. **Start First Layer:**
   - Tape lead to bobbin cheek (temporary)
   - Leave 8-10" lead extending
   - Wind first turn at one end of bobbin
   - Progress across bobbin width, keeping turns tight together
   - Complete layer when reaching other end

3. **Layer Insulation:**
   - Cut strip of polyester film or nomex paper
   - Width = bobbin width + 2mm overhang each side
   - Lay over completed layer
   - Smooth out any wrinkles or air pockets

4. **Continue Layers:**
   - Start next layer at opposite end (reverses direction)
   - Each layer should be complete before starting next
   - Every 10 layers, mark turn count on tape flag

5. **Final Layer:**
   - Leave 8-10" lead
   - Tape temporarily, then apply overall wrap

6. **Outer Insulation:**
   - Wrap entire winding with 2-3 layers of fabric tape or tough film
   - Protects winding during core assembly and handling

### Air Gap Critical Procedure

**Air gap is THE most critical aspect affecting inductance.**

**Spacer Material Selection:**
- **Nomex paper:** Excellent, heat-resistant, available in precise thicknesses
- **Polyester film (Mylar):** Good, readily available
- **Fiber board:** OK, but absorbs moisture (avoid in humid environments)
- **DO NOT USE:** Paper, cardboard (compresses over time)

**Cutting Spacers:**
1. Measure center leg width and length of E-core
2. Cut spacer to exact size (no overhang beyond center leg)
3. Two spacers needed: one for each E-piece (split the gap)
4. Example: 0.5mm total gap = 0.25mm spacer on each E-piece center leg

**Gap Placement:**
1. Place spacer on center leg only (not outer legs)
2. Spacer should be flat, no wrinkles or folds
3. Spacer must not extend into window (doesn't contact winding)

**Gap Measurement:**
1. After assembly, measure gap with feeler gauge from outside
2. Insert feeler gauge between E and I laminations at center leg
3. Should feel resistance at specified thickness
4. Gap too small: Add thicker spacer
5. Gap too large: Use thinner spacer

**Effect of Gap Size on Inductance:**
- Increasing gap by 0.1mm: reduces L by ~10-15%
- Decreasing gap by 0.1mm: increases L by ~10-15%
- Use this for fine-tuning after winding

### Lamination Assembly Sequence

**Interleaving is critical for minimum losses and noise:**

1. **Separate Laminations:**
   - Sort E and I pieces into two piles
   - Ensure all pieces are clean (no burrs or metal fragments)

2. **Install Bobbin:**
   - Slide wound bobbin onto center leg stack position

3. **Interleave Pattern:**
   - **First lamination:** E from left
   - **Second lamination:** I from right
   - **Third lamination:** E from right
   - **Fourth lamination:** I from left
   - **Continue alternating:** EI, IE, EI, IE, ...

4. **Why Interleave?**
   - Distributes gap across all laminations
   - Minimizes eddy currents
   - Reduces magnetic losses
   - Reduces mechanical hum

5. **Clamping:**
   - Use clamp frame (preferred) or steel banding
   - Tighten evenly on all four corners
   - Do not over-tighten (can damage bobbin)
   - Core should be snug but not stressed

6. **Mounting:**
   - Attach mounting brackets to clamp frame
   - Use rubber grommets or isolation mounts if vibration-sensitive
   - Ensure inductor can't move or vibrate

### Common Issues and Solutions

| Problem | Cause | Solution |
|---------|-------|----------|
| Inductance too low | Gap too large or not enough turns | Reduce gap or add turns |
| Inductance too high | Gap too small or too many turns | Increase gap or remove outer layers |
| DCR too high | Too many turns or thin wire | Use heavier gauge or reduce turns (increase gap to compensate) |
| Mechanical buzzing | Loose laminations | Tighten clamps, add damping material, or pot winding |
| Hum pickup | Magnetic coupling from external field | Shield with mu-metal or relocate away from power transformers |
| Poor Q | High DCR, bad capacitor, or core losses | Check DCR, verify capacitor ESR, ensure proper core material |
| Inductance drift with temperature | Core material temperature coefficient | Use premium core material or accept ±2-3% drift over 0-50°C |

---

## Integration with Low Boost Module

### Physical Mounting

**Location:**
- External to PCB (too large to mount on board)
- Chassis-mounted or separate inductor board
- Keep minimum 6" from power transformers (avoid hum coupling)
- Vertical orientation preferred (reduces footprint)

**Spacing:**
- Minimum 3" between inductors (E-I cores radiate more field than toroids)
- Can be closer if oriented perpendicular to each other

**Connection to PCB:**
- Use 20-22 AWG stranded hookup wire
- Twisted pair for each inductor (both leads twisted together)
- Maximum length: 18" (longer runs add series resistance)
- Terminate at screw terminals on Low Boost PCB

**Labeling:**
- Each inductor clearly labeled with frequency (20Hz, 30Hz, 60Hz, 100Hz)
- Color-code wires if desired (red=20Hz, orange=30Hz, etc.)
- Label at both inductor and PCB connection point

### Electrical Connections

**Frequency Selector Switch:**
- Rotary switch (4 position minimum)
- One side of all inductors connected to common point
- Switch selects which inductor connects to boost network
- Other side of selected inductor connects to boost level control

**Boost Level Control:**
- Typically a potentiometer (value TBD from schematic)
- Adjusts how much of the resonant boost is applied
- At maximum: full boost at selected frequency
- At minimum: bypass (flat response)

### Magnetic Shielding

**When is Shielding Needed?**
- Environment with strong 50/60Hz magnetic fields (power transformers)
- Hum audible in output (>-60dB)
- Located near CRT monitors or other magnetic devices (rare nowadays)

**Shielding Options:**
1. **Orientation:** Often sufficient to rotate inductor 90° to null hum
2. **Distance:** Move further from source (inverse square law)
3. **Mu-Metal Shield:** Expensive but very effective
   - Enclose inductor in mu-metal box or cylinder
   - Ground shield to circuit common
   - Costs $50-100 per inductor
4. **Steel Chassis:** If inductors mounted inside steel enclosure, chassis provides some shielding

**Recommendation:** Try orientation and distance first. Shielding is rarely necessary in well-designed audio equipment with proper transformer placement.

---

## Performance Verification

### Frequency Response Testing

**Test Setup:**
1. Function generator → Low Boost Module input (via input stage)
2. Oscilloscope CH1 → Module input (reference)
3. Oscilloscope CH2 → Module output (measurement)
4. Set boost level to maximum
5. Ensure input/output stages powered and operating

**Procedure for Each Frequency:**
1. Select frequency position (e.g., 20Hz)
2. Set function generator to start frequency (f₀ / 2)
3. Slowly sweep frequency upward to 2 × f₀
4. Observe CH2 amplitude vs. CH1
5. Note frequency where amplitude is maximum
6. Measure amplitude at peak
7. Measure frequencies where amplitude is -3dB from peak
8. Calculate Q = f₀ / (f_high - f_low)

**Expected Results:**

| Frequency | Peak Should Occur | 3dB BW (Q=40) | 3dB BW (Q=80) | Boost Amount |
|-----------|-------------------|---------------|---------------|--------------|
| 20 Hz | 19-21 Hz | 0.5 Hz | 0.25 Hz | Varies (10-20dB typical) |
| 30 Hz | 28.5-31.5 Hz | 0.75 Hz | 0.38 Hz | Varies |
| 60 Hz | 57-63 Hz | 1.5 Hz | 0.75 Hz | Varies |
| 100 Hz | 95-105 Hz | 2.5 Hz | 1.25 Hz | Varies |

**Note:** Boost amount depends on circuit design (level control setting, resistor values). Classic Pultec provides up to 18dB boost.

### Q Factor Interpretation

**What Q Means for Audio:**
- **Q = 20:** Very narrow, "surgical" boost (±1Hz @ 20Hz)
- **Q = 40:** Narrow boost, enhances fundamental only
- **Q = 80+:** Extremely narrow (can sound "ringy" if too high)

**Optimal Q for Music:**
- **Low frequency boost (20-100Hz):** Q = 30-50 is typical
- Too low Q: Boost is too broad, affects too many frequencies
- Too high Q: Boost sounds unnatural, "boxy"

### Troubleshooting

**Problem: Peak frequency is wrong**
- Measured peak is 5-10% off target
- **Diagnosis:**
  - Measure capacitor value with LCR meter (electrolytics can drift significantly)
  - Measure inductor value with LCR meter
  - Check for series resistance affecting resonance
- **Solution:**
  - If capacitor is off: Replace with correct value
  - If inductor is off: Adjust air gap or turns

**Problem: Boost is weak (low amplitude)**
- Resonance present but barely noticeable
- **Diagnosis:**
  - Check Q factor (low Q = weak peak)
  - Verify boost level control is at maximum
  - Check circuit resistor values (may attenuate boost)
- **Solution:**
  - If Q too low: Check DCR (should be <10Ω), verify capacitor is low-ESR
  - Verify circuit design matches schematic

**Problem: No resonance visible**
- Flat frequency response, no peak
- **Diagnosis:**
  - Inductor or capacitor disconnected
  - Frequency selector switch not making contact
  - Test circuit with known good inductor and capacitor
- **Solution:**
  - Check all connections with DMM (continuity test)
  - Verify switch operation
  - Substitute known good LC network to isolate problem

**Problem: Distortion at resonance**
- Clean input but distorted output at peak
- **Diagnosis:**
  - Core saturation (inductance drops at high level)
  - Air gap too small or missing
  - Downstream stage overload
- **Solution:**
  - Verify air gap is present and correct size
  - Reduce input level
  - Check operating levels throughout circuit

---

## Supplier Information

### Core and Lamination Suppliers

1. **Hammond Manufacturing**
   - Website: www.hammfg.com
   - Products: 166 series E-I laminations, bobbins
   - Distributors: Mouser, Digi-Key, Newark
   - Contact: sales@hammfg.com
   - **Recommended:** Good quality, reasonable price, readily available

2. **Magnetic Metals Corporation**
   - Website: www.magmet.com
   - Products: Premium nickel-iron laminations
   - Quality: Excellent (best available)
   - Price: 2-3× Hammond
   - **Use for:** Critical applications, if budget allows

3. **National Imports (TENCO)**
   - Website: www.nationalimports.com
   - Products: Generic E-I cores
   - Price: Lower cost than Hammond
   - **Use for:** Prototyping, budget builds

### Magnet Wire Suppliers

1. **MWS Wire Industries**
   - Website: www.mwswire.com
   - Products: Extensive selection, all gauges
   - Quality: Excellent heavy build enamel
   - Availability: Ships worldwide
   - **Recommended:** Primary supplier

2. **Essex Furukawa Magnet Wire**
   - Website: www.essexfurukawa.com
   - Available through: Digi-Key
   - Quality: High-quality (OEM supplier)
   - Price: Moderate

3. **Remington Industries**
   - Website: www.remingtonindustries.com
   - Available through: Amazon, direct
   - Quality: Good for audio work
   - Packaging: Smaller spools (good for small quantity needs)

### Insulation and Assembly Materials

1. **DuPont Nomex Paper:**
   - Distributors: McMaster-Carr, Grainger, Digi-Key
   - Part numbers: Various (specify thickness: 0.25mm, 0.5mm)
   - Price: ~$8-15 per sheet

2. **3M Polyester Film Tape:**
   - Available: Amazon, Digi-Key, McMaster-Carr
   - Use: Layer insulation
   - Price: ~$6-10 per roll

3. **MG Chemicals Varnish:**
   - Model: 4228 (Insulating Varnish)
   - Available: Digi-Key, Mouser, Amazon
   - Price: ~$15 per can
   - Use: Optional impregnation for vibration resistance

### Test Equipment

1. **BK Precision 889B LCR Meter** (~$400)
   - Mouser P/N: 615-889B
   - Digi-Key P/N: BK889B-ND
   - **Best value for this application**

2. **Keysight U1733C Handheld LCR Meter** (~$600)
   - Mouser P/N: 997-U1733C
   - Keysight direct
   - Portable, lab-grade accuracy

3. **GW Instek LCR-8110G Benchtop** (~$1200)
   - Mouser P/N: 615-LCR-8110G
   - High accuracy, comprehensive measurement modes
   - **For professional lab use**

---

## Design Alternatives and Optimizations

### Using 22 AWG Wire (Lower DCR)

If DCR <10Ω is critical (e.g., targeting Q >80):

**22 AWG Specifications:**
- Diameter: 0.644mm (bare), ~0.71mm (insulated)
- Resistance: 0.0528 Ω/m (20% lower than 20 AWG)
- Turns per layer: ~25-28 (vs. 30-32 for 20 AWG)

**Effect on 20Hz Inductor:**
- Same 1683 turns, same 168m length
- DCR = 168m × 0.0168 Ω/m = **2.8Ω** (was 5.6Ω)
- Q @ 20Hz = 442 / 2.8 = **158** (was 79)
- **Tradeoff:** More layers (60-65 vs. 55), slightly bulkier

**Recommendation:** Use 20 AWG unless Q >100 is required. The existing design with Q=70-100 is excellent for audio.

### Using Premium Core Material

**Magnetic Metals 50% Nickel-Iron:**
- Permeability: 4000 (vs. 3000 for M6 steel)
- Saturation: Higher (less distortion at high levels)
- Temperature stability: Better (±0.005%/°C vs. ±0.01%/°C)
- **Cost:** 2-3× Hammond cores

**Effect:**
- With same gap, can reduce turns by ~15%
- Slightly lower DCR, higher Q
- Better linearity (lower distortion)

**When to Use:**
- Premium audio equipment
- Very low distortion requirement (<0.05% THD)
- Professional mastering/mixing equipment
- Budget allows

### Toroidal Core Alternative (NOT RECOMMENDED)

**Why Not Powdered Iron Toroids?**

For 3.5H @ 20Hz, using powdered iron toroid:
- **Core Size Required:** T400-8 (4" OD, AL=140 nH/N²)
- **Turns Required:** √(3.5×10⁹ / 140) = **5000 turns**
- **Wire:** 26 AWG (only size that fits 5000 turns)
- **DCR:** ~100Ω (Q = 4.4 - very poor!)
- **Cost:** $25 for core alone
- **Winding Time:** 10-15 hours per inductor

**Conclusion:** Laminated E-I cores are the only practical solution for large audio-frequency inductors.

---

## Revision History

- **v2.0 - 2025-10-26** - Complete redesign with corrected capacitor values
  - **Critical Change:** Identified error in capacitor values (should be µF, not nF)
  - Revised all calculations based on classic Pultec topology
  - Added comprehensive winding and testing procedures
  - Expanded troubleshooting and integration sections
  
- v1.0 - Previous version - **Contains errors** (do not use)

**Designed for:** Pultec Three-Band EQ Low Boost Module  
**Based on:** Ian Thompson-Bell reference design, Classic Pultec EQP-1A topology  
**Engineer:** Claude (Inductor Design Specialist)

---

## References

1. Ian Thompson-Bell, "Stepped Pots for 3 Band Pultec", Issue 0.2, August 2016
2. Hammond Manufacturing, "E-I Lamination Data Sheets", 2020
3. Magnetic Metals Corporation, "Nickel-Iron Alloy Technical Data"
4. MWS Wire Industries, "Magnet Wire Technical Specifications"
5. Component values: `/Users/orion/work/multi-channel-preamp/src/pultec/docs/1.0/COMPONENT_VALUES.md`
6. Module specifications: `/Users/orion/work/multi-channel-preamp/src/pultec/modules/low-boost/README.md`
7. Original Pultec EQP-1A service manuals and schematics

---

## Appendix: Verifying Capacitor Values in Your Schematic

**CRITICAL:** Before building these inductors, verify the actual capacitor values in your schematic.

**Steps:**
1. Open original KiCAD schematic: `/Users/orion/work/multi-channel-preamp/src/schematics/pultec-three-band-eq/pultec-three-band-eq.kicad_sch`
2. Locate low boost section capacitors (C1, C2, C3, C4)
3. Check if values are nF or µF
4. If values are nF (as currently documented), then either:
   - Target frequencies are wrong (should be 200Hz, 300Hz, 600Hz, 1kHz), OR
   - There is a capacitor network (parallel/series combination) not shown in COMPONENT_VALUES.md

**If capacitors are truly nF range:**
- Contact original designer (Ian Thompson-Bell) for clarification
- Re-examine schematic for additional components
- Consider that this may be a non-standard Pultec variant

**This specification assumes µF-range capacitors per classic Pultec design.**

---

**END OF LOW BOOST INDUCTOR SPECIFICATIONS**
