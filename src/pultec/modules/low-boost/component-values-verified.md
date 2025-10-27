# LOW-BOOST MODULE - Component Values (Verified)

**Module**: Low Boost (Pultec Three-Band EQ)
**Date Verified**: 2025-10-26
**Authoritative Source**: Ian Thompson-Bell "Pultec 3 Band EQ Documentation" (P3bandDoc.pdf), Page 4
**Status**: ✅ **VERIFIED CORRECT**

---

## Correct Component Values

From Ian Thompson-Bell documentation, Page 4 "Pultec Lo Boost/Cut" table, **Cboost column**:

### Boost Capacitors (Main Selector Network)

| Ref | Value | Frequency | Type | Voltage | Tolerance |
|-----|-------|-----------|------|---------|-----------|
| C1 | **330 nF** | 20 Hz boost | Film | 63V min | ±10% |
| C2 | **220 nF** | 30 Hz boost | Film | 63V min | ±10% |
| C3 | **120 nF** | 60 Hz boost | Film | 63V min | ±10% |
| C4 | **68 nF** | 100 Hz boost | Film | 63V min | ±10% |
| C5 (optional) | **47 nF** | 150 Hz boost | Film | 63V min | ±10% |
| C6 (optional) | **33 nF** | 200 Hz boost | Film | 63V min | ±10% |

**Part Numbers**:
- WIMA MKS2 series (10% tolerance) - all values available
- Panasonic ECQV series (5% tolerance) - all values available
- Lead spacing: 0.2" (5.08mm) radial

### Coupling Capacitors

| Ref | Value | Function | Type |
|-----|-------|----------|------|
| C34 | 1 nF | Input coupling | WIMA FKS2 (5%) |
| C35 | 1 nF | Output coupling | WIMA FKS2 (5%) |

---

## Resistors

| Ref | Value | Type | Tolerance | Power | Notes |
|-----|-------|------|-----------|-------|-------|
| R2 | 56 kΩ | Metal film | ±1% | 1/4W | Or 50k LOG potentiometer per Ian Thompson-Bell BOM |

**Part Number**: Vishay MRS25 or equivalent quality 1% metal film

---

## Screw Terminals

| Ref | Positions | Function | Part Number |
|-----|-----------|----------|-------------|
| J_IN | 2 | Signal input | Phoenix 1757019 |
| J_OUT | 2 | Signal output | Phoenix 1757019 |
| J_BOOST_SEL_SND | 6 | Frequency selector send | Phoenix 1757051 |
| J_BOOST_SEL_RET | 6 | Frequency selector return | Phoenix 1757051 |
| J_BOOST_LVL | 3 | Boost level control | Phoenix 1757022 |
| J_GND | 2 | Ground connection | Phoenix 1757019 |

**Series**: Phoenix Contact MSTB 2,5 (5.08mm pitch)

---

## Important Notes

### NO Hand-Wound Inductors Required

The Ian Thompson-Bell low boost section does **NOT** use separate hand-wound inductors like the mid-boost and high-boost sections. It works with the resistive network and capacitors only.

**Inductors are used in**:
- **Mid Boost**: VTB9050 (2H tapped inductor) for 200 Hz - 7 kHz
- **High Boost**: VTB9042 (1H tapped inductor) for 3 - 16 kHz (optional)
- **Low Boost**: NO separate inductors

### Previous Documentation Error

Earlier documentation incorrectly specified:
- ❌ Capacitor values: 18nF, 10nF, 4.7nF, 3.3nF (these are for LOW CUT section)
- ❌ Hand-wound inductors with Henry-range values

**Correct values** (from Ian Thompson-Bell page 4):
- ✅ Capacitor values: 330nF, 220nF, 120nF, 68nF (Cboost column)
- ✅ No separate inductors needed

---

## Component Count Summary

| Category | Count | Notes |
|----------|-------|-------|
| Film Capacitors (boost) | 4-6 | 330nF, 220nF, 120nF, 68nF required; 47nF, 33nF optional |
| Film Capacitors (coupling) | 2 | 1nF each |
| Metal Film Resistors | 1 | 56kΩ |
| Screw Terminals | 6 | Various positions |
| **TOTAL PCB Components** | 9-11 | No external inductors |

---

## BOM Cost Estimate

| Component | Qty | Unit Price | Total |
|-----------|-----|------------|-------|
| 330nF film cap | 1 | $0.70 | $0.70 |
| 220nF film cap | 1 | $0.60 | $0.60 |
| 120nF film cap | 1 | $0.55 | $0.55 |
| 68nF film cap | 1 | $0.50 | $0.50 |
| 1nF film cap | 2 | $0.40 | $0.80 |
| 56kΩ resistor | 1 | $0.25 | $0.25 |
| Phoenix terminals | 6 | $0.75-1.90 | ~$8.00 |
| **TOTAL** | | | **~$11.40** |

---

## Reference

**Ian Thompson-Bell "Pultec 3 Band EQ Documentation"**
- Copyright © 2011
- Page 4: "Pultec Lo Boost/Cut" component table
- Cboost column: 330n, 220n, 120n, 68n, 47n, 33n
