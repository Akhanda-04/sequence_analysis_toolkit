# Sequence Analysis Toolkit

A collection of small Python tools for performing common DNA, RNA, and sequence-analysis tasks. The project is built with Python and Biopython and is designed for practical bioinformatics learning and reusable command-line workflows.

## Features

* Calculate sequence length
* GC content calculation
* Reverse complement
* DNA translation
* Motif search
* FASTA statistics

## Installation

Create the environment:

```bash
mamba env create -f environment.yml
```

Activate the environment:

```bash
mamba activate sequence-toolkit
```

## Usage

### Sequence Length

Calculate the length of sequences in a FASTA file:

```bash
python3 scripts/sequence_length.py
```

Example output:

```text
NT_033779.5:11011312-11012135    824 bp
```

More usage examples will be added as additional tools are implemented.

## Project Structure

```text
sequence_analysis_toolkit/
│
├── data/
├── scripts/
│   ├── gc_content.py
│   ├── reverse_complement.py
│   ├── translate_dna.py
│   ├── motif_search.py
│   ├── fasta_stats.py
│   └── sequence_length.py
├── results/
├── tests/
├── README.md
├── environment.yml
└── LICENSE
```

## Skills Demonstrated

* Python
* Biopython
* FASTA parsing
* Sequence analysis
* File I/O
* Functions and modular programming
* Command-line workflows
* Conda/Mamba environment management
* Git/GitHub

## Testing

Run the test suite with:

```bash
pytest
```

## Future Improvements

* Add comprehensive automated tests
* Add support for FASTQ files
* Add command-line options for input and output files
* Generate summary reports for multiple FASTA sequences
* Improve error handling and input validation

## Author

Nabil
