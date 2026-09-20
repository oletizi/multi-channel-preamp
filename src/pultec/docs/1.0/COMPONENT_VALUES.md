# Component Values — Pultec Three-Band EQ

**Corrected 2026-09-20.** The previous revision of this file had its section
assignments scrambled. See "What was wrong" at the end; the error propagated
into several downstream documents that have not all been fixed.

## Sources

Two, and they agree on every capacitor position:

- **Topology** — exact `kicad-cli` netlist export of
  `src/schematics/pultec-three-band-eq/pultec-three-band-eq.kicad_sch`
  at commit `c0f6f39`. This is the board that was manufactured.
- **Values** — Ian Thompson-Bell, *Pultec 3 Band EQ Documentation*
  (`reference/3BandPultec/P3bandDoc.pdf`), pages 2–4.

"Position" is the selector-terminal pin the capacitor's far end lands on, read
from the netlist rather than inferred. `‖` marks two capacitors sharing one
position — the doc's "spaces on the PCB for up to two capacitors per boost/cut
frequency".

---

## Low Cut

Between the `/HI BOOST OUT` node and `Lo Cut Sel Snd` (J5).

| Freq | Position | Components | Doc |
|------|----------|------------|-----|
| 20 Hz | p1 | C1 18n | 18n |
| 30 Hz | p2 | C2 10n | 10n |
| 60 Hz | p3 | C3 4.7n ‖ C7 1n | 4n7 + 1n |
| 100 Hz | p4 | C4 3n3 | 3n3 |
| 150 Hz | p5 | C5 2n2 | 2n2 |
| 200 Hz | p6 | C6 1n8 | 1n8 |

Controls: `Low Cut Lvl` (J7), `Low Cut Sel Ret` (J9). Pot: 470K LOG.

The 60 Hz position is the doc's one exception — "single components are used for
all but one cut frequency". The netlist independently shows C3 and C7 sharing
position 3.

## Low Boost

Between GND and `Lo Boost Sel Ret` (J10).

| Freq | Position | Components | Doc |
|------|----------|------------|-----|
| 20 Hz | p1 | C18 330n | 330n |
| 30 Hz | p2 | C19 220n | 220n |
| 60 Hz | p3 | C20 120n | 120n |
| 100 Hz | p4 | C21 68n | 68n |
| 150 Hz | p5 | C22 47n | 47n |
| 200 Hz | p6 | C23 33n | 33n |

Resistor: R2 56K. Controls: `Lo Boost Lvl` (J11), `Lo Boost Sel Snd` (J6).
Pot: 47K LOG.

**No inductors.** The Pultec low section is an RC shelving network. This is
already recorded in `modules/low-boost/BOM.csv` ("NO HAND-WOUND INDUCTORS
REQUIRED") and is the point the documents listed below get wrong.

## High Boost

Between `Hi Boost L Snd` (J15) and `Hi Boost Sel Rtn` (J8). Inductive build,
using the doc's `Cboost` column with the VTB9042 fitted.

| Freq | Position | Components | Doc Cboost | Doc Lboost |
|------|----------|------------|-----------|-----------|
| 3 kHz | p6 | C14 4n7 | 4n7 | 0.6H |
| 4 kHz | p5 | C15 4n7 ‖ C2a2 470pF | 4n7 + 470pF | 0.3H |
| 5 kHz | p4 | C16 3n3 | 3n3 | 0.3H |
| 8 kHz | p3 | C17 1nF ‖ C4a2 1nF | 1n + 1n | 0.2H |
| 10 kHz | p2 | C34 1nF ‖ C5a2 1n5 | 1n + 1n5 | 0.1H |
| 16 kHz | p1 | C35 1nF | 1n | 0.1H |

Controls: `Hi Boost Lvl` (J21), `Hi Boost Q` (J20), `Hi Boost Sel Snd` (J13).
Pots: 47K LIN boost, 10K LIN Qmax.

The `pultec-inductor-board` breakout exposes taps at 600mH / 300mH / 200mH /
100mH — the four distinct values of the `Lboost` column.

**R3 = 4K7 is disputed.** The doc gives two mutually exclusive builds: the
poor-man's build uses the `Cpoorboost` values, shorts out the inductor and HiQ
pins, and sets Qmax = 4K7; the inductive build uses `Cboost` and a Qmax of
nominally 470R, which the doc says "has been found in tests to give a maximum Q
similar to that indicated by the published curves of the original Pultec EQP1A".
This design uses `Cboost` and has inductor taps, so it is the inductive build,
but carries the poor-man's resistor value. Worth measuring on the board.

For reference, the unused `Cpoorboost` column is 15n+1n, 10n+2n2, 10n, 4n7+1n,
4n7, 1n+1n5.

## High Cut

Between the `/LO BOOST IN` node and `Hi Cut Sel Ret` (J12).

| Freq | Position | Components | Doc Ccut |
|------|----------|------------|---------|
| 3 kHz | p1 | C24 47n ‖ C30 33n | 47n + 33n |
| 4 kHz | p2 | C25 47n ‖ C31 10n | 47n + 10n |
| 5 kHz | p3 | C26 47n | 47n |
| 8 kHz | p4 | C27 22n ‖ C32 10n | 22n + 10n |
| 10 kHz | p5 | C28 22n ‖ C33 2n2 | 22n + 2n2 |
| 16 kHz | p6 | C29 15n | 15n |

Resistor: R1 430R. Controls: `Hi Cut Lvl` (J4), `Hi Cut Sel Snd` (J3).

## Mid Boost / Cut

C8–C13 and C36–C41, all **placeholder values** in the schematic (`Mid C1A` …
`Mid C6B`). Six selector positions with A/B pairs.

The doc (page 3) specifies eleven mid frequencies using a VTB9050, so the
schematic implements a six-position subset and which six is unrecorded:

| Freq | L | C | | Freq | L | C |
|------|---|---|-|------|---|---|
| 200 | 2H | 330n | | 2K | 0.45H | 12n + 2n2 |
| 300 | 2H | 150n | | 3K | 0.45H | 4n7 + 1n5 |
| 500 | 2H | 47n | | 4K | 0.22H | 4n7 + 2n2 |
| 700 | 2H | 22n + 3n3 | | 5K | 0.22H | 4n7 |
| 1K | 1H | 22n + 3n3 | | 7K | 0.1H | 2n2 + 1n |
| 1K5 | 1H | 12n | | | | |

Control: `Mid Lvl` (J29), labelled "47 Log" in the schematic, matching the doc.

## Interface

`IN` (J1), `OUT` (J2), GND. The doc notes the output "should be loaded with not
less than 470K".

All capacitors are non-polarised film. All inter-board connections are screw
terminals.

---

## What was wrong

The previous revision assigned:

- **C1–C7 to Low Boost.** They are on the low **cut** selector.
- **C18–C22 to High Cut.** They are on the low **boost** selector.
- **C29, C32, C33 to High Boost.** They are high **cut**.
- **C23 33n and C24 47n to Low Cut.** C23 is low boost; C24 is high cut.
- **C34, C35, C4a2, C5a2 to Low Boost** as coupling capacitors. They are high
  boost selector capacitors.

Documents derived from the wrong assignment, not yet corrected:

- `LOW_BOOST_INDUCTOR_SPECIFICATIONS.md` and `INDUCTOR_SUMMARY.md` specify four
  low-boost inductors (3.52H, 2.81H, 1.50H, 0.768H; ~$161 and 12–16 hours of
  winding). The low section needs none.
- `modules/low-boost/INDUCTOR_SPECS.md` caught the 1000x impossibility
  (`L = 1/(4π²·20²·18nF) = 3518 H, not 3.5H`) but diagnosed it as an
  nF/µF unit error rather than a section mix-up.
- `modules/high-boost/INDUCTOR_SPECS.md` maps `C32 10nF -> 3 kHz`; C32 is high
  cut.
- `modules/{low-cut,high-boost,high-cut}/*.kicad_sch` are byte-identical stubs
  containing this file's incorrect `C23 33n` / `C24 47n` pair, unconnected.
  `modules/low-boost/low-boost.kicad_sch` has no capacitors at all.

`modules/low-boost/BOM.csv` and `component-values-verified.md` are correct —
that module was checked against the doc's page 4 `Cboost` column, and its
corrected values agree with this file.
