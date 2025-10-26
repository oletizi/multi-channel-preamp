# Pultec Three-Band EQ - Modular System Overview

## System Architecture

The Pultec three-band EQ is divided into the following modules:

```
┌─────────────┐    ┌──────────┐    ┌───────────┐    ┌───────────┐    ┌──────────┐    ┌──────────────┐
│   Input     │───▶│  Low Cut │───▶│ Low Boost │───▶│High Boost │───▶│ High Cut │───▶│    Output    │
│   Stage     │    │  Module  │    │  Module   │    │  Module   │    │  Module  │    │    Stage     │
│ (Built)     │    │          │    │           │    │           │    │          │    │  (Built)     │
└─────────────┘    └──────────┘    └───────────┘    └───────────┘    └──────────┘    └──────────────┘
                         │               │                │                │
                         │               │                │                │
                    ┌────▼────┐     ┌────▼────┐      ┌───▼────┐      ┌───▼────┐
                    │ Freq    │     │ Freq    │      │ Freq   │      │ Freq   │
                    │ Select  │     │ Select  │      │ Select │      │ Select │
                    │ + Level │     │ + Level │      │+ Level │      │+ Level │
                    └─────────┘     └─────────┘      │  + Q   │      └────────┘
                                                      └────────┘
                                          │
                                     ┌────▼────┐
                                     │ Hand-   │
                                     │ Wound   │
                                     │ Inductors│
                                     └─────────┘
```

## Module Summary

### 1. Low Cut Module
- **Function**: Frequency-selective attenuation at low frequencies
- **Frequencies**: 20Hz, 30Hz, 60Hz, 100Hz (typical)
- **Components**: 2 capacitors, screw terminals
- **Controls**: Frequency selector, cut level
- **Size**: Small (~5cm × 5cm estimated)

### 2. Low Boost Module
- **Function**: Frequency-selective boost at low frequencies
- **Frequencies**: 20Hz, 30Hz, 60Hz, 100Hz (typical)
- **Components**: 11 capacitors, 1 resistor, screw terminals
- **External**: 4 hand-wound inductors (one per frequency)
- **Controls**: Frequency selector, boost level
- **Size**: Medium-Large (~8cm × 10cm estimated)

### 3. High Boost Module
- **Function**: Frequency-selective boost at high frequencies with bandwidth control
- **Frequencies**: 3kHz, 4kHz, 5kHz, 8kHz, 10kHz, 12kHz, 16kHz (typical)
- **Components**: 8 capacitors, 1 resistor, screw terminals
- **External**: 7 hand-wound inductors (one per frequency)
- **Controls**: Frequency selector, boost level, bandwidth (Q)
- **Size**: Large (~10cm × 12cm estimated)

### 4. High Cut Module
- **Function**: Frequency-selective attenuation at high frequencies
- **Frequencies**: 5kHz, 10kHz, 20kHz (typical)
- **Components**: 11 capacitors, 1 resistor, screw terminals
- **Controls**: Frequency selector, cut level
- **Size**: Medium (~7cm × 9cm estimated)

## Signal Flow

1. **Input Stage** (already built) → provides buffering and impedance matching
2. **Low Cut** → attenuates selected low frequencies
3. **Low Boost** → boosts selected low frequencies (classic Pultec low shelf)
4. **High Boost** → boosts selected high frequencies with adjustable Q
5. **High Cut** → attenuates selected high frequencies
6. **Output Stage** (already built) → provides makeup gain and output buffering

## Control Panel Layout Suggestion

```
┌────────────────────────────────────────────────────────────┐
│                  PULTEC THREE-BAND EQUALIZER               │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  LOW FREQUENCY                    HIGH FREQUENCY           │
│                                                            │
│  ┌─────┐  ┌─────┐           ┌─────┐  ┌─────┐  ┌─────┐   │
│  │BOOST│  │ CUT │           │BOOST│  │  Q  │  │ CUT │   │
│  │ LVL │  │ LVL │           │ LVL │  │     │  │ LVL │   │
│  └─────┘  └─────┘           └─────┘  └─────┘  └─────┘   │
│                                                            │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐  │
│  │  FREQ   │   │  FREQ   │   │  FREQ   │   │  FREQ   │  │
│  │ BOOST   │   │  CUT    │   │ BOOST   │   │  CUT    │  │
│  │ SELECT  │   │ SELECT  │   │ SELECT  │   │ SELECT  │  │
│  └─────────┘   └─────────┘   └─────────┘   └─────────┘  │
│                                                            │
│  20/30/60/100   20/30/60/100   3/4/5/8     5/10/20       │
│     Hz             Hz         10/12/16 kHz    kHz         │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

## Inter-Module Connections

All modules connect via screw terminals with the following signal paths:

### Power (if needed)
- Ground: Common ground bus connecting all modules

### Audio Signal Path
- Low Cut IN ← Input Stage OUT
- Low Cut OUT → Low Boost IN
- Low Boost OUT → High Boost IN
- High Boost OUT → High Cut IN
- High Cut OUT → Output Stage IN

### Control Connections
Each module has:
- Frequency selector send/return (to rotary switch on front panel)
- Level control connections (to front panel potentiometer)
- High Boost also has Q control connection

### External Components
- **Low Boost**: Requires 4 hand-wound inductors
- **High Boost**: Requires 7 hand-wound inductors

## Bill of Materials Summary

| Module | PCB Cost | Components | Total (Est.) |
|--------|----------|------------|--------------|
| Low Cut | $5.00 | $4.75 | $9.75 |
| Low Boost | $8.00 | $16.20 | $24.20 |
| High Boost | $10.00 | $19.20 | $29.20 |
| High Cut | $8.00 | $13.90 | $21.90 |
| **Total** | **$31.00** | **$54.05** | **$85.05** |

*Note: Does not include:*
- Front panel components (potentiometers, rotary switches, knobs)
- Inductors (hand-wound)
- Wire for interconnections
- Enclosure

## Testing and Integration Procedure

### Phase 1: Individual Module Testing
1. Build and test Low Cut module standalone
2. Build and test Low Boost module with test inductors
3. Build and test High Boost module with test inductors
4. Build and test High Cut module standalone

### Phase 2: Signal Chain Integration
1. Connect Input Stage → Low Cut → Output Stage, verify signal flow
2. Add Low Boost to chain, verify
3. Add High Boost to chain, verify
4. Add High Cut to complete chain, verify

### Phase 3: Frequency Response Testing
1. Inject sine wave sweep, measure frequency response
2. Verify boost/cut frequencies match design
3. Adjust inductor values if needed
4. Document final inductor specifications

### Phase 4: Final Integration
1. Wire all modules into enclosure
2. Connect front panel controls
3. Full frequency response characterization
4. THD+N measurements
5. Documentation of final performance

## Recommended Tools and Equipment

### For Assembly
- Soldering iron with temperature control
- Solder (60/40 or lead-free)
- Wire cutters, strippers
- Multimeter
- Magnifier for inspection

### For Testing
- Audio interface or signal generator
- Oscilloscope (optional but helpful)
- Multimeter (continuity, resistance, capacitance)
- LCR meter (for inductor measurement)
- Audio analyzer software (REW, ARTA, etc.)

### For Inductor Winding
- Inductor cores (powdered iron or ferrite)
- Magnet wire (various gauges)
- LCR meter for measurement
- Winding jig or mandrel

## Next Steps

1. Review module designs and BOMs
2. Order PCBs from manufacturer (provide Gerber files)
3. Order components from Mouser or similar
4. Design and wind inductors
5. Assemble modules one at a time
6. Test and integrate systematically

## Version History
- v1.0: Initial modular design extracted from monolithic schematic
