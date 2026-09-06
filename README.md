# Sequence Analysis Toolkit

A collection of simple Python command-line scripts for performing common DNA sequence analysis tasks.

This project was built to practice **Python programming, biological sequence analysis, file handling, and basic bioinformatics workflows**.

## Features

The toolkit currently includes:

* GC content calculation
* DNA reverse complement
* DNA → protein translation
* Motif searching
* FASTA statistics
* Sequence length calculation

## Project Structure

```text
sequence-analysis-toolkit/
│
├── data/
│   └── # Input FASTA/sequence files
│
├── scripts/
│   ├── gc_content.py
│   ├── reverse_complement.py
│   ├── translate_dna.py
│   ├── motif_search.py
│   ├── fasta_stats.py
│   └── sequence_length.py
│
├── results/
│   └── # Analysis outputs
│
├── tests/
│   └── # Test files
│
├── README.md
├── requirements.txt
└── LICENSE
```

## Requirements

* Python 3.10+
* Biopython

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the individual scripts from the project root.

### 1. GC Content

Calculate the GC content of a DNA sequence:

```bash
python scripts/gc_content.py
```

Example:

```text
Sequence: ATGCGATCGATC
GC Content: 50.00%
```

### 2. Reverse Complement

Generate the reverse complement of a DNA sequence:

```bash
python scripts/reverse_complement.py
```

Example:

```text
Input:  ATGCGT
Output: ACGCAT
```

### 3. DNA Translation

Translate a DNA sequence into a protein sequence:

```bash
python scripts/translate_dna.py
```

Example:

```text
DNA:     ATGGCCATTGTA
Protein: MAIV
```

### 4. Motif Search

Search for a specific nucleotide motif:

```bash
python scripts/motif_search.py
```

Example:

```text
Sequence: ATGCGATGCGAT
Motif: ATG
Positions: 1, 6
```

### 5. FASTA Statistics

Calculate basic statistics from a FASTA file:

```bash
python scripts/fasta_stats.py
```

Possible statistics include:

```text
Number of sequences
Total sequence length
Minimum length
Maximum length
Average length
```

### 6. Sequence Length

Calculate the length of a DNA sequence:

```bash
python scripts/sequence_length.py
```

Example:

```text
Sequence length: 1500 bp
```

## Example Workflow

A simple sequence-analysis workflow can be performed as:

```text
DNA Sequence
     │
     ├── Sequence Length
     │
     ├── GC Content
     │
     ├── Reverse Complement
     │
     ├── Motif Search
     │
     └── Translation
```

For FASTA files:

```text
FASTA File
    │
    ▼
FASTA Statistics
    │
    ├── Number of sequences
    ├── Total length
    ├── Average length
    ├── Minimum length
    └── Maximum length
```

## Learning Objectives

This project focuses on developing practical skills in:

* Python programming
* Functions and modules
* File handling
* Command-line execution
* DNA sequence manipulation
* FASTA file processing
* Biopython
* Basic bioinformatics automation
* Unit testing
* Git and GitHub project management

## Future Improvements

Planned improvements include:

* [ ] Add command-line arguments using `argparse`
* [ ] Add FASTA/FASTQ input support
* [ ] Add nucleotide composition analysis
* [ ] Add codon usage analysis
* [ ] Add ORF detection
* [ ] Add sequence validation
* [ ] Improve error handling
* [ ] Expand unit tests
* [ ] Add automated testing with GitHub Actions
* [ ] Create a unified command-line interface

## Testing

Tests will be added to verify that the sequence-analysis functions produce expected results.

Run the test suite with:

```bash
pytest
```

## Technologies

* **Python**
* **Biopython**
* **pytest**
* **Git**
* **GitHub**

## Author

**Musaddique Mubin Nabil**

Microbiology Student
Rajshahi University

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
