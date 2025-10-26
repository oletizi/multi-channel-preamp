# Complete Inductor Specifications Summary
## Pultec Three-Band EQ - All Modules

This document provides a quick-reference summary of all 11 hand-wound inductors required for the Pultec three-band equalizer project.

**Complete specifications available in:**
- Low Boost: `/Users/orion/work/multi-channel-preamp/src/pultec/modules/low-boost/INDUCTOR_SPECS.md`
- High Boost: `/Users/orion/work/multi-channel-preamp/src/pultec/modules/high-boost/INDUCTOR_SPECS.md`

---

## Low Boost Section (4 Inductors)

### Critical Note: Capacitor Values

**The component values document lists capacitors in nanofarads (nF), but classic Pultec designs use microfarads (µF) for low boost.** This specification assumes µF values matching traditional Pultec topology.

**Verify actual capacitor values in your schematic before building!**

### Low Boost Inductor Summary Table

| Frequency | Capacitor | Inductance | Core | Turns | Wire | DCR | Q @ f₀ | Cost/ea |
|-----------|-----------|------------|------|-------|------|-----|--------|---------|
| **20 Hz** | 18 µF | 3.52 H | EI-100, 25mm | 1683 | 20 AWG | 5.6Ω | 79 | ~$40 |
| **30 Hz** | 10 µF | 2.81 H | EI-100, 25mm | 1504 | 20 AWG | 5.0Ω | 106 | ~$38 |
| **60 Hz** | 4.7 µF | 1.50 H | EI-87, 25mm | 1404 | 20 AWG | 4.0Ω | 141 | ~$32 |
| **100 Hz** | 3.3 µF | 0.768 H | EI-87, 25mm | 1005 | 20 AWG | 2.8Ω | 172 | ~$28 |

**Core Type:** Laminated silicon steel (M6), Hammond 166 series  
**Air Gap:** 0.4-0.5mm (distributed for linearity)  
**Total Cost:** ~$161 (all 4 inductors with materials)  
**Build Time:** ~12-16 hours total (3-4 hours per inductor)

### Key Specifications - Low Boost

**Design Requirements:**
- High inductance (0.75H to 3.5H)
- Low DC resistance (<10Ω target)
- High Q factor (>20 minimum, >40 preferred)
- Linear operation (no saturation distortion)
- Operating frequency: 20-100 Hz

**Construction:**
- Bobbin winding (easier than toroidal)
- Multiple layers (40-60 layers depending on frequency)
- Layer insulation required
- Air gap critical for linearity
- Lamination interleaving reduces losses

**Testing:**
- LCR meter required (must measure >1H)
- Verify inductance ±5%
- Measure DCR (<10Ω)
- Test resonance with correct capacitor
- Q factor >20 minimum

---

## High Boost Section (7 Inductors)

### High Boost Inductor Summary Table

| Frequency | Capacitor | Inductance | Core | Turns | Wire | DCR | Q @ f₀ | Cost/ea |
|-----------|-----------|------------|------|-------|------|-----|--------|---------|
| **3 kHz** | 10 nF (C32) | 281.4 mH | T106-26 | 1443 | 28 AWG | 20.1Ω | 264 | ~$12 |
| **4 kHz** | 4.7 nF (C14/15) | 336.8 mH | T106-26 | 1577 | 28 AWG | 21.9Ω | 386 | ~$13 |
| **5 kHz** | 3.3 nF (C16) | 307.0 mH | T106-26 | 1507 | 28 AWG | 21.0Ω | 460 | ~$12 |
| **8 kHz** | 1.0 nF (C17) | 395.8 mH | T90-26 | 2041 | 30 AWG | 39.3Ω | 506 | ~$10 |
| **10 kHz** | 470 pF (C2a2) | 538.9 mH | T90-26 | 2382 | 30 AWG | 45.9Ω | 738 | ~$11 |
| **12 kHz** | 330 pF (est) | 533.0 mH | T90-26 | 2369 | 30 AWG | 45.7Ω | 882 | ~$11 |
| **16 kHz** | 220 pF (est) | 449.8 mH | T90-26 | 2177 | 30 AWG | 42.0Ω | 1078 | ~$10 |

**Core Type:** Powdered iron toroid, Micrometals Type 26 (Yellow/White)  
**Core Sizes:** T106-26 (larger L) and T90-26 (smaller L)  
**No Air Gap:** Type 26 material has distributed air gap (stable, predictable)  
**Total Cost:** ~$78 (all 7 inductors with materials)  
**Build Time:** ~14-18 hours total (2-3 hours per inductor)

### Key Specifications - High Boost

**Design Requirements:**
- Medium inductance (280-540 mH)
- Moderate DC resistance (<50Ω acceptable)
- Very high Q factor (>30 minimum, typically 200-1000)
- Stable across audio frequency range (3-16 kHz)
- Works with QMAX control (470Ω pot for bandwidth adjustment)

**Construction:**
- Toroidal winding (self-shielding, compact)
- Multiple layers (6-10 layers)
- Turn counting critical (use counter)
- No layer insulation required (distributed gap core)
- Final wrapping with kapton tape

**Testing:**
- LCR meter @ 1kHz or 10kHz
- Verify inductance ±5%
- Measure DCR (<50Ω for HF inductors)
- Test resonance with correct capacitor
- Q factor >30 minimum

---

## Complete Project Summary

### Total Inductor Count: 11
- Low Boost: 4 inductors (20Hz, 30Hz, 60Hz, 100Hz)
- High Boost: 7 inductors (3kHz, 4kHz, 5kHz, 8kHz, 10kHz, 12kHz, 16kHz)

### Total Estimated Cost: ~$239
- Low Boost: ~$161 (larger cores, more wire)
- High Boost: ~$78 (smaller cores, finer wire)

### Total Build Time: ~26-34 hours
- Low Boost: 12-16 hours (bobbin winding, lamination assembly)
- High Boost: 14-18 hours (toroid winding, many turns)

### Required Skills:
- **Basic:** Steady hands, patience, ability to count
- **Intermediate:** Soldering, wire stripping, mechanical assembly
- **Advanced:** LCR meter operation, frequency response measurement
- **No special training required** - detailed instructions provided

### Required Tools:
**Essential:**
- LCR meter ($200-600) - **MUST HAVE**
- Winding jig (hand-crank or motorized) ($50-200 or DIY)
- Turn counter ($20-50)
- Soldering station ($50-100)
- Digital multimeter ($30-100)

**Nice to Have:**
- Function generator + oscilloscope (frequency response testing)
- Insulation tester/megohmmeter (safety verification)
- Capacitor decade box (resonance testing)

---

## Comparison: Low Boost vs. High Boost

| Aspect | Low Boost (20-100Hz) | High Boost (3-16kHz) |
|--------|----------------------|----------------------|
| **Inductance Range** | 0.75H - 3.5H (large) | 280mH - 540mH (medium) |
| **Core Type** | Laminated E-I steel | Powdered iron toroid |
| **Core Size** | Large (EI-87, EI-100) | Medium (T90, T106) |
| **Wire Gauge** | 20 AWG (thicker) | 28-30 AWG (thinner) |
| **Turn Count** | 1000-1700 turns | 1400-2400 turns |
| **DC Resistance** | 2.8-5.6Ω (low) | 20-46Ω (moderate) |
| **Q Factor** | 70-170 (high) | 260-1080 (very high) |
| **Winding Style** | Bobbin (easy) | Toroidal (tedious) |
| **Air Gap** | Required (0.4-0.5mm) | Built-in (distributed) |
| **Assembly** | Lamination stack | No assembly (toroid) |
| **Difficulty** | Medium | Medium-High |
| **Cost per Unit** | $28-40 | $10-13 |

---

## Quick Reference: Core Selection

### Low Boost Cores (Laminated Steel)

**Hammond 166K25 (EI-100, 25mm stack):**
- Use for: 20Hz, 30Hz
- Core area: 250mm²
- Path length: 200mm
- Approx cost: $8 + $2.50 bobbin

**Hammond 166J25 (EI-87, 25mm stack):**
- Use for: 60Hz, 100Hz
- Core area: 188mm²
- Path length: 174mm
- Approx cost: $6 + $2 bobbin

### High Boost Cores (Powdered Iron Toroid)

**Micrometals T106-26 (1.06" OD, Type 26):**
- Use for: 3kHz, 4kHz, 5kHz
- AL value: 135 nH/N²
- Approx cost: $2.50

**Micrometals T90-26 (0.90" OD, Type 26):**
- Use for: 8kHz, 10kHz, 12kHz, 16kHz
- AL value: 95 nH/N²
- Approx cost: $1.80

---

## Wire Requirements

### Low Boost Wire

**20 AWG Heavy Build Enamel Magnet Wire:**
- Diameter: 0.812mm bare, ~0.88mm insulated
- Resistance: 0.0333 Ω/m (33.3 Ω/km)
- Total length needed: ~525 meters (for all 4 inductors)
- Recommended purchase: 2 lb spool (~1600m) for $45
- Supplier: MWS Wire Industries MW0118-2LB

### High Boost Wire

**28 AWG Heavy Build Enamel Magnet Wire:**
- Use for: 3kHz, 4kHz, 5kHz
- Diameter: 0.321mm bare
- Resistance: 0.214 Ω/m
- Total needed: ~294 meters (3 inductors)
- Recommended: 1 lb spool (~785m) for $22

**30 AWG Heavy Build Enamel Magnet Wire:**
- Use for: 8kHz, 10kHz, 12kHz, 16kHz
- Diameter: 0.255mm bare
- Resistance: 0.340 Ω/m
- Total needed: ~508 meters (4 inductors)
- Recommended: 1 lb spool (~1250m) for $20

---

## Testing Summary

### Minimum Required Tests (All Inductors)

1. **Visual Inspection:**
   - No damaged wire insulation
   - Secure mechanical assembly
   - Clean terminations

2. **DC Resistance (DCR):**
   - Measure with digital multimeter
   - Low Boost: <10Ω target
   - High Boost: <50Ω target

3. **Inductance:**
   - Measure with LCR meter
   - Must be within ±5% of target
   - Low Boost: Test @ 100-120Hz
   - High Boost: Test @ 1kHz or 10kHz

4. **Resonance Test (Recommended):**
   - Connect with specified capacitor
   - Sweep frequency around target
   - Verify peak at correct frequency
   - Measure bandwidth (Q factor)

5. **Insulation Test (Safety-Critical for Mains Equipment):**
   - Megohmmeter @ 500VDC
   - Winding to core: >10MΩ

### Acceptance Criteria

**All inductors must meet:**
- Inductance: Target ±5%
- DCR: Within specified maximum
- Q Factor: Above specified minimum
- Insulation: >10MΩ
- No mechanical noise or buzzing
- Resonance at correct frequency (±5%)

---

## Build Order Recommendation

### Phase 1: Start with High Boost (Learn Technique)
**Reason:** Smaller, faster, easier to test

1. Build 3kHz inductor first (T106-26, 28 AWG)
   - Moderate turn count (1443)
   - Good introduction to toroid winding
   - Easy to test with function generator

2. Build 5kHz inductor (T106-26, 28 AWG)
   - Similar to 3kHz, practice technique

3. Build remaining high boost inductors (4kHz, then 8-16kHz)
   - Build confidence before tackling low boost

### Phase 2: Low Boost (Larger, More Complex)
**Reason:** Requires more time, lamination assembly skill

1. Build 100Hz inductor first (EI-87, smallest)
   - Learn bobbin winding technique
   - Practice lamination assembly
   - Lowest turn count of low boost

2. Build 60Hz inductor (EI-87)
   - Same core size, more turns

3. Build 30Hz and 20Hz inductors (EI-100, largest)
   - Most time-consuming
   - Build after mastering technique

### Alternative: Build by Frequency Priority

If you want to test specific frequencies first:
1. Build 60Hz and 3kHz first (common "problem" frequencies in mixing)
2. Build 100Hz and 5kHz next
3. Complete remaining frequencies

---

## Troubleshooting Quick Reference

### Inductance Too Low
- **Cause:** Not enough turns, or air gap too large
- **Solution:** Add turns, or reduce air gap (laminated cores only)

### Inductance Too High
- **Cause:** Too many turns, or air gap too small
- **Solution:** Remove outer layers, or increase air gap

### DCR Too High (Low Q)
- **Cause:** Too many turns, thin wire, poor connections
- **Solution:** Use heavier gauge wire, check terminations, reduce turns (adjust gap to compensate)

### Resonance Frequency Wrong
- **Cause:** Wrong capacitor or inductor value
- **Solution:** Measure both with LCR meter, adjust accordingly

### Mechanical Buzzing
- **Cause:** Loose laminations (laminated cores only)
- **Solution:** Tighten clamps, add damping material, or pot winding

### Hum Pickup
- **Cause:** Magnetic coupling from power transformer
- **Solution:** Relocate inductor (6"+ away), rotate orientation, or add shielding

---

## Supplier Quick Reference

### Cores
- **Hammond Manufacturing** (www.hammfg.com) - Laminated E-I cores
  - Via Mouser, Digi-Key, Newark
- **Micrometals** (www.micrometals.com) - Powdered iron toroids
  - Via Mouser, Digi-Key

### Wire
- **MWS Wire Industries** (www.mwswire.com) - Primary recommendation
- **Remington Industries** (www.remingtonindustries.com) - Via Amazon
- **Essex Furukawa** - Via Digi-Key

### Test Equipment
- **BK Precision 889B** (~$400) - Best value LCR meter
- **Keysight U1733C** (~$600) - Handheld, lab-grade
- **GW Instek** (~$200-300) - Budget option

### Materials
- **McMaster-Carr** - Nomex paper, insulation materials
- **3M** - Tapes, films
- **MG Chemicals** - Varnishes, coatings

---

## Important Warnings

### Capacitor Value Discrepancy - Low Boost

**The component values document lists low boost capacitors as nanofarads (18nF, 10nF, etc.), but the inductance values in the existing specification (3.5H, 2.8H, etc.) require microfarads (18µF, 10µF, etc.).**

**Before building low boost inductors:**
1. Open original KiCAD schematic
2. Verify actual capacitor values (nF or µF?)
3. If nF (as documented):
   - Recalculate target frequencies, OR
   - Find additional capacitor network not documented
4. If µF (classic Pultec):
   - Proceed with this specification

**This specification assumes µF capacitors per traditional Pultec EQP-1A design.**

### High Boost Capacitors

High boost capacitor values above 10kHz are estimated based on typical Pultec frequency spacing. Verify actual values from complete schematic before building those inductors.

### Safety

- **Insulation testing is critical** for mains-powered equipment
- **Discharge capacitors** after high-voltage testing
- **Wear safety glasses** when cutting wire or handling cores
- **Avoid inhaling** varnish or epoxy fumes (use in ventilated area)

---

## Timeline Estimate

### For Experienced Builder:
- **High Boost (all 7):** 14-16 hours
  - ~2 hours per inductor average
- **Low Boost (all 4):** 10-12 hours
  - ~2.5-3 hours per inductor average
- **Total:** 24-28 hours

### For First-Time Builder:
- **High Boost (all 7):** 18-22 hours
  - Learning curve, slower initial builds
- **Low Boost (all 4):** 14-18 hours
  - Lamination assembly takes practice
- **Total:** 32-40 hours

### Plus Testing Time:
- **Basic tests** (L, DCR): ~1 hour per inductor
- **Resonance/frequency response tests:** ~2 hours per frequency (if doing comprehensive testing)

---

## Next Steps

1. **Verify Capacitor Values:** Check original schematic for actual low boost capacitor values
2. **Order Materials:** Cores, wire, insulation materials (~$240 total)
3. **Obtain Test Equipment:** LCR meter is essential (do not proceed without one)
4. **Review Detailed Specs:** Read complete specifications in module directories
5. **Build Prototype:** Start with one high boost inductor (3kHz recommended)
6. **Test Thoroughly:** Verify all parameters before proceeding to remaining inductors
7. **Complete High Boost Set:** Finish all 7 high boost inductors
8. **Build Low Boost Set:** Tackle the 4 larger low boost inductors
9. **Integration:** Install in modules, connect to PCBs, test complete system

---

## Document Revision History

- **v1.0 - 2025-10-26** - Initial summary document
  - Compiled from detailed specifications in module directories
  - Highlighted capacitor value discrepancy for low boost section
  - Added quick-reference tables and troubleshooting guides

---

## Related Documents

**Detailed Specifications:**
- `/Users/orion/work/multi-channel-preamp/src/pultec/modules/low-boost/INDUCTOR_SPECS.md`
- `/Users/orion/work/multi-channel-preamp/src/pultec/modules/high-boost/INDUCTOR_SPECS.md`

**Component Values:**
- `/Users/orion/work/multi-channel-preamp/src/pultec/docs/1.0/COMPONENT_VALUES.md`

**Module Documentation:**
- `/Users/orion/work/multi-channel-preamp/src/pultec/modules/low-boost/README.md`
- `/Users/orion/work/multi-channel-preamp/src/pultec/modules/high-boost/README.md`

**System Overview:**
- `/Users/orion/work/multi-channel-preamp/src/pultec/docs/1.0/SYSTEM_OVERVIEW.md`

**Reference Design:**
- `/Users/orion/work/multi-channel-preamp/reference/pultec-style-eq/SteppedPotsfor3BandPultecv0.2.pdf`

---

**Designed for:** Pultec Three-Band EQ Modular Design  
**Engineer:** Claude (Inductor Design Specialist)  
**Date:** 2025-10-26

---

**END OF INDUCTOR SUMMARY**
