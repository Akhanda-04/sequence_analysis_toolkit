from Bio import SeqIO

records = SeqIO.parse(
    "/run/media/nabil2004/New Volume/Nabil project/sequence_analysis_toolkit/data/example.fasta",
    "fasta"
)

for record in records:
    print(record.id)
    print(record.seq)