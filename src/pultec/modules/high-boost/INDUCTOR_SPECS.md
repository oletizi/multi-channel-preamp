# High Boost Inductor Design Specifications
## Pultec Three-Band EQ - High Boost Module

## Overview

This document provides complete design specifications for the seven inductors required by the High Boost module. These inductors form resonant LC circuits with capacitors to provide frequency-selective boost at 3kHz, 4kHz, 5kHz, 8kHz, 10kHz, 12kHz, and 16kHz.

## Circuit Topology

The high boost section uses a passive LC network where an inductor and capacitor resonate at the selected frequency. The Q control (QMAX potentiometer, typically 470Ω) adjusts the bandwidth of the boost peak.

## Resonant Frequency Formula

For series LC resonance:
```
f₀ = 1 / (2π√LC)

Solving for L:
L = 1 / (4π²f₀²C)
```

## Capacitor-to-Frequency Mapping

Based on component values from COMPONENT_VALUES.md and typical Pultec designs:

| Frequency | Capacitor | Value | Required Inductance |
|-----------|-----------|-------|---------------------|
| 3 kHz | C32 | 10 nF | 281.4 mH |
| 4 kHz | C14/C15 | 4.7 nF | 336.8 mH |
| 5 kHz | C16 | 3.3 nF | 307.0 mH |
| 8 kHz | C17 | 1 nF | 395.8 mH |
| 10 kHz | C2a2 | 470 pF | 538.9 mH |
| 12 kHz | (estimate) | 330 pF | 533.0 mH |
| 16 kHz | (estimate) | 220 pF | 449.8 mH |

**Note:** Frequencies above 10kHz use estimated capacitor values typical for Pultec designs. Verify actual values from complete schematic.

## Core Selection: Powdered Iron Toroids

### Recommended Core Material: Micrometals Type 26 (Yellow/White)
- **Permeability (µᵢ):** 75
- **Frequency range:** 10 kHz - 1 MHz (excellent for audio HF)
- **Advantages:** Distributed air gap, stable, predictable, minimal distortion
- **Temperature coefficient:** ~40 ppm/°C

### Core Sizes and Specifications

For inductances in the 280-540 mH range with Type 26 material:

| Core Size | OD | ID | Height | AL (nH/N²) | Recommended For |
|-----------|----|----|--------|------------|-----------------|
| T106-26 | 1.06" | 0.56" | 0.44" | 135 | 3-5 kHz (larger L) |
| T90-26 | 0.90" | 0.52" | 0.31" | 95 | 8-16 kHz (smaller L) |
| T80-26 | 0.80" | 0.50" | 0.25" | 60 | Alternative for 8-16 kHz |

**Supplier:** Micrometals (www.micrometals.com), available through Mouser, Digi-Key

---

## INDUCTOR SPECIFICATIONS

### 3 kHz INDUCTOR

**ELECTRICAL SPECIFICATIONS:**
- **Target Inductance:** 281.4 mH ±5%
- **Resonant Capacitor:** 10 nF (C32)
- **Resonant Frequency:** 3000 Hz
- **Target Q:** >30 (DCR <18Ω @ 3kHz)

**DESIGN:**
- **Core:** Micrometals T106-26 (Yellow/White)
- **Core AL:** 135 nH/N²
- **Turns Required:** N = √(L/AL) = √(281.4×10⁶ nH / 135 nH/N²) = **1443 turns**
- **Wire Gauge:** 28 AWG (0.321mm diameter, 0.214 Ω/m)
- **Average Turn Length:** π × (OD + ID)/2 = π × (1.06" + 0.56")/2 × 25.4mm/inch ≈ 65mm = 0.065m
- **Wire Length:** 1443 turns × 0.065m = 93.8 meters
- **Calculated DCR:** 93.8m × 0.214 Ω/m = 20.1Ω
- **Calculated Q:** (2π × 3000 × 0.2814) / 20.1 = 264 (excellent, but check actual DCR)

**Note on DCR:** Calculated DCR of 20Ω gives Q=264, which is excellent. If actual DCR is higher due to winding path, use 26 AWG (0.135 Ω/m) for lower resistance.

**WINDING INSTRUCTIONS:**
1. Use 28 AWG heavy build enamel magnet wire
2. Start winding through center hole, maintaining consistent tension
3. Wind in neat layers, progressing around the toroid
4. Count turns carefully - use counter or mark every 100 turns
5. Approximately 5-6 layers will be needed
6. Leave 6" leads on each end for termination
7. Secure final wrap with kapton tape or heat-shrink

**TERMINATION:**
- Strip 1/4" of enamel from each lead (scrape with knife or burn off)
- Tin leads with solder
- Attach to screw terminal or solder lugs
- Label: "3kHz - 281mH"

**TEST PROCEDURE:**
1. **Inductance:** Measure with LCR meter @ 1kHz or 10kHz
   - Target: 267-296 mH (281mH ±5%)
   - Adjust: Add/remove turns if needed (each turn changes L by ~0.14mH)
2. **DCR:** Measure with DMM
   - Target: <25Ω (for Q >30)
3. **Resonance Test:** Connect with 10nF capacitor, sweep 2-4kHz
   - Verify peak at 3kHz ±5%
4. **Q Measurement:** Measure 3dB bandwidth, Q = f₀/BW₃dB
   - Target: Q >30

---

### 4 kHz INDUCTOR

**ELECTRICAL SPECIFICATIONS:**
- **Target Inductance:** 336.8 mH ±5%
- **Resonant Capacitor:** 4.7 nF (C14 or C15)
- **Resonant Frequency:** 4000 Hz
- **Target Q:** >30 (DCR <21Ω @ 4kHz)

**DESIGN:**
- **Core:** Micrometals T106-26 (Yellow/White)
- **Core AL:** 135 nH/N²
- **Turns Required:** √(336.8×10⁶ / 135) = **1577 turns**
- **Wire Gauge:** 28 AWG (0.214 Ω/m)
- **Wire Length:** 1577 × 0.065m = 102.5 meters
- **Calculated DCR:** 102.5m × 0.214 Ω/m = 21.9Ω
- **Calculated Q:** (2π × 4000 × 0.3368) / 21.9 = 386 (excellent)

**WINDING INSTRUCTIONS:**
1. Use 28 AWG heavy build enamel magnet wire
2. Wind 1577 turns evenly around T106-26 toroid
3. Approximately 6 layers
4. Leave 6" leads
5. Secure and label: "4kHz - 337mH"

**TEST PROCEDURE:**
1. Inductance: 320-354 mH (336.8mH ±5%)
2. DCR: <25Ω
3. Resonance with 4.7nF: peak at 4kHz ±5%
4. Q: >30

---

### 5 kHz INDUCTOR

**ELECTRICAL SPECIFICATIONS:**
- **Target Inductance:** 307.0 mH ±5%
- **Resonant Capacitor:** 3.3 nF (C16)
- **Resonant Frequency:** 5000 Hz
- **Target Q:** >30 (DCR <24Ω @ 5kHz)

**DESIGN:**
- **Core:** Micrometals T106-26 (Yellow/White)
- **Core AL:** 135 nH/N²
- **Turns Required:** √(307.0×10⁶ / 135) = **1507 turns**
- **Wire Gauge:** 28 AWG (0.214 Ω/m)
- **Wire Length:** 1507 × 0.065m = 98.0 meters
- **Calculated DCR:** 98.0m × 0.214 Ω/m = 21.0Ω
- **Calculated Q:** (2π × 5000 × 0.307) / 21.0 = 460 (excellent)

**WINDING INSTRUCTIONS:**
1. Use 28 AWG heavy build enamel magnet wire
2. Wind 1507 turns evenly around T106-26 toroid
3. Approximately 6 layers
4. Leave 6" leads
5. Secure and label: "5kHz - 307mH"

**TEST PROCEDURE:**
1. Inductance: 292-322 mH (307mH ±5%)
2. DCR: <25Ω
3. Resonance with 3.3nF: peak at 5kHz ±5%
4. Q: >30

---

### 8 kHz INDUCTOR

**ELECTRICAL SPECIFICATIONS:**
- **Target Inductance:** 395.8 mH ±5%
- **Resonant Capacitor:** 1 nF (C17)
- **Resonant Frequency:** 8000 Hz
- **Target Q:** >30 (DCR <33Ω @ 8kHz)

**DESIGN:**
- **Core:** Micrometals T90-26 or T106-26
- **Core AL (T90-26):** 95 nH/N²
- **Turns Required:** √(395.8×10⁶ / 95) = **2041 turns**
- **Wire Gauge:** 30 AWG (0.255mm, 0.340 Ω/m)
- **Average Turn Length (T90):** π × 0.71" × 25.4 = 56.7mm = 0.0567m
- **Wire Length:** 2041 × 0.0567 = 115.7 meters
- **Calculated DCR:** 115.7m × 0.340 Ω/m = 39.3Ω
- **Calculated Q:** (2π × 8000 × 0.3958) / 39.3 = 506 (excellent)

**Alternative: Use T106-26 with 28 AWG for lower DCR**
- **Turns:** √(395.8×10⁶ / 135) = 1711 turns
- **Wire:** 28 AWG, length = 111.2m
- **DCR:** 23.8Ω (better Q)

**WINDING INSTRUCTIONS:**
1. Use 30 AWG for T90-26 OR 28 AWG for T106-26
2. Wind carefully - higher turn count
3. Multiple layers (7-8 for T90, 6-7 for T106)
4. Leave 6" leads
5. Secure and label: "8kHz - 396mH"

**TEST PROCEDURE:**
1. Inductance: 376-416 mH (395.8mH ±5%)
2. DCR: <40Ω (T90) or <30Ω (T106)
3. Resonance with 1nF: peak at 8kHz ±5%
4. Q: >30

---

### 10 kHz INDUCTOR

**ELECTRICAL SPECIFICATIONS:**
- **Target Inductance:** 538.9 mH ±5%
- **Resonant Capacitor:** 470 pF (C2a2)
- **Resonant Frequency:** 10000 Hz
- **Target Q:** >30 (DCR <50Ω @ 10kHz)

**DESIGN:**
- **Core:** Micrometals T90-26 (Yellow/White)
- **Core AL:** 95 nH/N²
- **Turns Required:** √(538.9×10⁶ / 95) = **2382 turns**
- **Wire Gauge:** 30 AWG (0.340 Ω/m)
- **Wire Length:** 2382 × 0.0567m = 135.1 meters
- **Calculated DCR:** 135.1m × 0.340 Ω/m = 45.9Ω
- **Calculated Q:** (2π × 10000 × 0.5389) / 45.9 = 738 (excellent)

**WINDING INSTRUCTIONS:**
1. Use 30 AWG heavy build enamel magnet wire
2. Wind 2382 turns evenly around T90-26 toroid
3. Approximately 9-10 layers
4. Take care with thin wire - don't pull too hard
5. Leave 6" leads
6. Secure and label: "10kHz - 539mH"

**TEST PROCEDURE:**
1. Inductance: 512-566 mH (538.9mH ±5%)
2. DCR: <50Ω
3. Resonance with 470pF: peak at 10kHz ±5%
4. Q: >30

---

### 12 kHz INDUCTOR

**ELECTRICAL SPECIFICATIONS:**
- **Target Inductance:** 533.0 mH ±5%
- **Resonant Capacitor:** ~330 pF (estimated)
- **Resonant Frequency:** 12000 Hz
- **Target Q:** >30 (DCR <60Ω @ 12kHz)

**DESIGN:**
- **Core:** Micrometals T90-26 (Yellow/White)
- **Core AL:** 95 nH/N²
- **Turns Required:** √(533.0×10⁶ / 95) = **2369 turns**
- **Wire Gauge:** 30 AWG (0.340 Ω/m)
- **Wire Length:** 2369 × 0.0567m = 134.3 meters
- **Calculated DCR:** 134.3m × 0.340 Ω/m = 45.7Ω
- **Calculated Q:** (2π × 12000 × 0.533) / 45.7 = 882 (excellent)

**WINDING INSTRUCTIONS:**
1. Use 30 AWG heavy build enamel magnet wire
2. Wind 2369 turns evenly around T90-26 toroid
3. Approximately 9-10 layers
4. Leave 6" leads
5. Secure and label: "12kHz - 533mH"

**TEST PROCEDURE:**
1. Inductance: 506-560 mH (533mH ±5%)
2. DCR: <50Ω
3. Resonance test: verify frequency with known capacitor
4. Q: >30

---

### 16 kHz INDUCTOR

**ELECTRICAL SPECIFICATIONS:**
- **Target Inductance:** 449.8 mH ±5%
- **Resonant Capacitor:** ~220 pF (estimated)
- **Resonant Frequency:** 16000 Hz
- **Target Q:** >30 (DCR <72Ω @ 16kHz)

**DESIGN:**
- **Core:** Micrometals T90-26 (Yellow/White)
- **Core AL:** 95 nH/N²
- **Turns Required:** √(449.8×10⁶ / 95) = **2177 turns**
- **Wire Gauge:** 30 AWG (0.340 Ω/m)
- **Wire Length:** 2177 × 0.0567m = 123.4 meters
- **Calculated DCR:** 123.4m × 0.340 Ω/m = 42.0Ω
- **Calculated Q:** (2π × 16000 × 0.4498) / 42.0 = 1078 (excellent)

**WINDING INSTRUCTIONS:**
1. Use 30 AWG heavy build enamel magnet wire
2. Wind 2177 turns evenly around T90-26 toroid
3. Approximately 8-9 layers
4. Leave 6" leads
5. Secure and label: "16kHz - 450mH"

**TEST PROCEDURE:**
1. Inductance: 427-472 mH (449.8mH ±5%)
2. DCR: <45Ω
3. Resonance test: verify frequency with known capacitor
4. Q: >30

---

## Bill of Materials - High Boost Inductors

### Core Materials

| Item | Description | Qty | Supplier | Part Number | Unit Price | Total |
|------|-------------|-----|----------|-------------|------------|-------|
| T106-26 Toroid | 1.06" OD, Type 26, AL=135 | 3 | Micrometals | T106-26 | $2.50 | $7.50 |
| T90-26 Toroid | 0.90" OD, Type 26, AL=95 | 4 | Micrometals | T90-26 | $1.80 | $7.20 |

**Core Subtotal:** $14.70

### Wire and Materials

| Item | Description | Qty | Supplier | Part Number | Est. Cost |
|------|-------------|-----|----------|-------------|-----------|
| 28 AWG Magnet Wire | Heavy build enamel, 1 lb spool (~785m) | 1 | MWS Wire | MW80-1 | $22.00 |
| 30 AWG Magnet Wire | Heavy build enamel, 1 lb spool (~1250m) | 1 | MWS Wire | MW82-1 | $20.00 |
| Kapton Tape | High temp polyimide tape, 1/2" | 1 roll | 3M | 5413 | $8.00 |
| Heat Shrink | Assorted sizes | 1 kit | Various | - | $5.00 |
| Mounting Hardware | Standoffs, screws, tie-downs | 1 set | Various | - | $8.00 |

**Materials Subtotal:** $63.00

### **TOTAL BOM COST: ~$77.70** (for complete set of 7 inductors)

---

## Tools Required

### For Winding
- **Toroid winding jig** or hand-wind with patience
- **Turn counter** (mechanical or electronic)
- Wire tensioning guide (cardboard shuttle or commercial tool)
- Sharp knife or wire stripper for removing enamel
- Soldering iron and 60/40 solder
- Kapton tape or heat shrink tubing
- Label maker or permanent marker

### For Testing
- **LCR Meter** (essential)
  - Recommended: BK Precision 889B, Keysight U1733C
  - Frequency range: 100Hz-10kHz minimum
  - Accuracy: ±1% or better
  - Must measure L, DCR, and Q

- **Capacitor Decade Box** (for resonance testing)
  - Range: 100pF-10µF
  - Accuracy: ±2% or better

- **Function Generator** (for resonance verification)
  - Frequency range: 1kHz-20kHz
  - Output: 1Vpp minimum

- **Oscilloscope** (for frequency response)
  - Bandwidth: 50MHz minimum
  - 2 channels

- **Digital Multimeter** (for DCR measurement)
  - 0.1Ω resolution

---

## Winding Best Practices

### Toroidal Winding Technique

1. **Preparation:**
   - Clean hands and workspace (wire enamel is delicate)
   - Prepare wire shuttle: wind 5-10 meters onto cardboard or plastic shuttle
   - Place toroid core on non-slip surface

2. **Starting the Wind:**
   - Leave 6" lead extending from starting point
   - Secure lead temporarily with tape
   - Pass shuttle through center hole
   - Wind first turn snug against core surface

3. **Progressive Winding:**
   - Wind turns close together, no gaps
   - Maintain consistent tension (firm but not tight)
   - Each turn should lie flat against previous
   - Wind evenly around circumference
   - Reload shuttle as needed

4. **Layer Transitions:**
   - When first layer completes circumference, start second layer
   - Second layer winds over first layer at same location
   - Continue building layers concentrically
   - For Type 26 material, insulation between layers is optional (distributed gap prevents saturation)

5. **Turn Counting:**
   - Use mechanical or electronic counter
   - Mark every 100 turns with tape flag
   - Double-check count before terminating

6. **Finishing:**
   - Leave 6" lead at end
   - Secure final turn with kapton tape
   - Remove enamel from last 1/4" of each lead
   - Tin leads with solder
   - Label with frequency and inductance

### Common Issues and Solutions

| Problem | Cause | Solution |
|---------|-------|----------|
| Wire breaks | Too much tension or damaged enamel | Reduce tension, inspect wire before winding |
| Inductance too low | Not enough turns | Add turns (each turn adds ~L/N to total) |
| Inductance too high | Too many turns | Remove outer layer of turns |
| High DCR | Too many turns or thin wire | Use heavier gauge wire or larger core |
| Uneven winding | Inconsistent tension | Maintain steady tension, use winding jig |
| Wire won't tin | Enamel not removed | Scrape more thoroughly or use hotter iron |

### DCR Reduction Strategies

If measured DCR exceeds target:

1. **Use heavier gauge wire:**
   - 28 AWG instead of 30 AWG (but needs more space)
   - Recalculate turns for same inductance

2. **Use larger core:**
   - Larger core = longer mean turn length BUT fewer turns needed
   - Net effect can reduce DCR

3. **Parallel connection:**
   - Wind two identical inductors
   - Connect in parallel: L_total = L/2, DCR_total = DCR/2
   - Doubles the parts count but halves DCR

4. **Accept higher DCR:**
   - Q >30 is still excellent for audio
   - Slightly lower Q = slightly broader peak (may be preferable)

---

## Integration with High Boost Module

### Physical Mounting

**Recommended Approach:**
- Mount all 7 inductors on a separate inductor board or chassis-mounted bracket
- Use plastic or nylon standoffs (non-magnetic, non-conductive)
- Space inductors at least 2" apart to minimize mutual coupling
- Orient toroids with axes perpendicular to each other if space-constrained

**Connection to PCB:**
- Use 22-24 AWG stranded hookup wire
- Twisted pair for each inductor (both leads twisted together)
- Maximum run length: 12" (short runs minimize stray capacitance)
- Connect to screw terminals on High Boost PCB

**Labeling:**
- Each inductor clearly labeled with frequency
- Color-code wires (e.g., frequency order: 3k=red, 4k=orange, etc.)
- Label both inductor and cable at PCB connection

### Electrical Connections

**From PCB Frequency Selector to Inductors:**
- Frequency selector switch (rotary, 7 positions) on front panel
- Common point connects to one side of all inductors via screw terminal bus
- Switched point selects one inductor at a time
- Other side of inductor connects to boost network return

**QMAX Connection:**
- 470Ω potentiometer (QMAX) in series with inductor
- Adjusts damping = adjusts Q = adjusts bandwidth
- Lower resistance = higher Q = sharper peak
- Higher resistance = lower Q = broader peak

### Shielding Considerations

**Magnetic Field Coupling:**
- Toroidal cores are self-shielding (fields contained within core)
- Spacing of 2" between inductors prevents significant mutual coupling
- No additional shielding typically required

**If Hum is Present:**
- Ensure inductors are away from power transformers (12"+ separation)
- Rotate inductor orientation to null hum
- Add mu-metal shield only if necessary (expensive, usually overkill)

---

## Performance Verification

### Frequency Response Testing

**Test Setup:**
1. Function generator → High Boost Module input
2. Oscilloscope Channel 1 → Module input (reference)
3. Oscilloscope Channel 2 → Module output (measurement)
4. Set boost level to maximum, Q to minimum damping (highest Q)

**Procedure for Each Frequency:**
1. Select frequency position (e.g., 3kHz)
2. Sweep function generator from f₀/2 to 2×f₀ (e.g., 1.5kHz to 6kHz for 3kHz position)
3. Observe output on scope
4. Note frequency of peak amplitude
5. Measure amplitude at peak
6. Measure frequencies where amplitude drops to -3dB from peak
7. Calculate Q = f₀ / (f_high - f_low)

**Expected Results:**

| Frequency | Peak Should Occur | 3dB Bandwidth (Q=30) | 3dB Bandwidth (Q=50) |
|-----------|-------------------|----------------------|----------------------|
| 3 kHz | 2850-3150 Hz | 100 Hz | 60 Hz |
| 4 kHz | 3800-4200 Hz | 133 Hz | 80 Hz |
| 5 kHz | 4750-5250 Hz | 167 Hz | 100 Hz |
| 8 kHz | 7600-8400 Hz | 267 Hz | 160 Hz |
| 10 kHz | 9500-10500 Hz | 333 Hz | 200 Hz |
| 12 kHz | 11400-12600 Hz | 400 Hz | 240 Hz |
| 16 kHz | 15200-16800 Hz | 533 Hz | 320 Hz |

### Q Factor vs. QMAX Setting

The QMAX potentiometer (470Ω) in series with the inductor adds resistance, reducing Q:

```
Q_actual = ωL / (DCR + R_QMAX)
```

**Example for 3kHz inductor (L=281mH, DCR=20Ω):**
- QMAX at 0Ω (maximum Q): Q = (2π×3000×0.281) / 20 = 264
- QMAX at 235Ω (half): Q = (2π×3000×0.281) / 255 = 20.7
- QMAX at 470Ω (minimum Q): Q = (2π×3000×0.281) / 490 = 10.8

This demonstrates the QMAX control's effectiveness in adjusting boost character from sharp/surgical (high Q) to broad/musical (low Q).

### Troubleshooting

**Problem: Peak frequency is off target**

*Symptoms:* Measured resonant frequency doesn't match expected

*Diagnosis:*
1. Verify capacitor value with LCR meter
2. Verify inductor value with LCR meter
3. Check for parallel capacitance (long wires, cable capacitance)

*Solutions:*
- If frequency too low: inductance or capacitance too high
  - Remove turns from inductor OR use smaller capacitor
- If frequency too high: inductance or capacitance too low
  - Add turns to inductor OR use larger capacitor

**Problem: Low Q (broad, weak peak)**

*Symptoms:* Peak is barely noticeable, bandwidth very wide

*Diagnosis:*
1. Measure DCR of inductor (should be <50Ω)
2. Check QMAX setting (should be at minimum resistance for test)
3. Measure capacitor ESR (should be <1Ω for film caps)

*Solutions:*
- High DCR: Rewind with heavier gauge wire
- QMAX set wrong: Rotate to minimum resistance end
- Bad capacitor: Replace with quality film cap

**Problem: Multiple peaks or ripples**

*Symptoms:* Frequency response shows multiple peaks or oscillations

*Diagnosis:*
1. Check for oscillation in active stages (input/output amps)
2. Verify grounding is correct (no ground loops)
3. Check for component placement issues (stray coupling)

*Solutions:*
- Add decoupling at active stages
- Improve grounding scheme
- Separate inductor physically from high-gain stages

---

## Supplier Information

### Core Suppliers
1. **Micrometals Inc.** - www.micrometals.com
   - Direct manufacturer of powdered iron toroids
   - Type 26 material specifically designed for audio
   - Available through Mouser, Digi-Key, Newark

2. **Mouser Electronics** - www.mouser.com
   - Mouser P/N: Micrometals T106-26, T90-26, etc.
   - Online ordering, fast shipping

3. **Digi-Key** - www.digikey.com
   - Full line of Micrometals products
   - Excellent stock and availability

### Wire Suppliers
1. **MWS Wire Industries** - www.mwswire.com
   - Extensive magnet wire selection
   - Heavy build enamel in all gauges
   - Small quantity sales (by the pound)

2. **Remington Industries** - www.remingtonindustries.com
   - Good value, smaller spools available
   - Available on Amazon for quick delivery

3. **Essex Furukawa** - www.essexfurukawa.com
   - High-quality magnet wire
   - Available through distributors (Digi-Key)

### Test Equipment
1. **BK Precision** - www.bkprecision.com
   - Model 889B LCR meter (~$400)
   - Excellent for inductor measurement

2. **Keysight Technologies** - www.keysight.com
   - U1733C handheld LCR meter (~$600)
   - Laboratory-grade accuracy

3. **GW Instek** - www.gwinstek.com
   - Budget LCR meters (~$200-300)
   - Adequate for this application

---

## Revision History

- **v1.0 - 2025-10-26** - Initial complete design specification
- Designed for: Pultec Three-Band EQ High Boost Module
- Based on: Ian Thompson-Bell reference design
- Engineer: Claude (Inductor Design Specialist)

---

## References

1. Ian Thompson-Bell, "Stepped Pots for 3 Band Pultec", Issue 0.2, August 2016
2. Micrometals, "Powder Core Catalog", 2020
3. Component values: `/Users/orion/work/multi-channel-preamp/src/pultec/docs/1.0/COMPONENT_VALUES.md`
4. Module specifications: `/Users/orion/work/multi-channel-preamp/src/pultec/modules/high-boost/README.md`
5. Project documentation: `/Users/orion/work/multi-channel-preamp/src/pultec/`

---

**END OF HIGH BOOST INDUCTOR SPECIFICATIONS**
