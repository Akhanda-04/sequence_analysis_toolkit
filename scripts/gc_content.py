from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

records = SeqIO.parse(
    "/run/media/nabil2004/New Volume/Nabil project/sequence_analysis_toolkit/data/example.fasta",
    "fasta"
)

for record in records:
    gc = gc_fraction(record.seq) * 100

    print(f"Sequence: {record.id}")
    print(f"Length: {len(record.seq)} bp")
    print(f"GC Content: {gc:.2f}%")
    print()