from Bio import SeqIO


def sequence_length(sequence):
    """Return the length of a sequence."""
    return len(sequence)


def fasta_lengths(input_file):
    """Return sequence IDs and lengths from a FASTA file."""
    results = []

    for record in SeqIO.parse(input_file, "fasta"):
        results.append({
            "id": record.id,
            "length": sequence_length(record.seq)
        })

    return results


def main():
    input_file = "/run/media/nabil2004/New Volume/Nabil project/sequence_analysis_toolkit/data/example.fasta"

    results = fasta_lengths(input_file)

    for result in results:
        print(f"{result['id']}\t{result['length']} bp")


if __name__ == "__main__":
    main()