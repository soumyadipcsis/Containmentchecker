# AntarBhukti

AntarBhukti is a verification tool for evolving software, designed to verify changes between two versions of SFCs (Sequential Function Charts) — a source and a target. It is specifically tailored for use with OSCAT application benchmarks.

---

## Features

- **Compare SFCs:** Verifies the correctness of software evolution using textual SFC representations.
- **Easy to Use:** Simple command line interface for fast verification tasks.
- **Benchmark Suite:** Works on all 80 OSCAT benchmark applications. Benchmrak-Source-OSCAT.py for source SFC and Benchmarks-Upgrade-OSCAT.py for upgraded SFC.
- **Superior Performance:** Outperforms [verifaps](https://formal.kastel.kit.edu/~weigl/verifaps/index.html) in coverage and flexibility.
- **Open ST Reference:** Reference ST code for the OSCAT library is available in the [SamaTulyata4PLC](https://github.com/soumyadipcsis/SamaTulyata4PLC) repository.

---

## Getting Started
Dependency files drivier.py, sfc.py, sfc_verifier.py
### Prerequisites

- Python 3.x, z3.

### Usage

```sh
python3 driver.py <source_SFC.txt> <target_SFC.txt>
```
- `<source_SFC.txt>`: Path to the source SFC file.
- `<upgraded_SFC.txt>`: Path to the upgraded (evolved) SFC file.

### Example

```sh
python3 driver.py sfc_old.txt sfc_new.txt
```

---

## OSCAT Benchmarks

AntarBhukti has been tested on all 80 OSCAT automation benchmarks for robust and reliable verification.

---

## Reference

- For Structured Text (ST) code for the OSCAT library, see the [SamaTulyata4PLC](https://github.com/soumyadipcsis/SamaTulyata4PLC) repository.

---


## License



---

## Acknowledgements

- Inspired by the need for robust SFC verification in industrial automation.
- Thanks to the OSCAT project and the verifaps tool for foundational ideas.
