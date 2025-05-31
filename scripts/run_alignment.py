import subprocess

input_file = "data/panthera_tigris_cleaned.fasta"
output_file = "data/panthera_tigris_aligned.fasta"

cmd = [
    "muscle",
    "-align", input_file,
    "-output", output_file
]

result = subprocess.run(cmd, capture_output=True, text=True)

if result.returncode == 0:
    print(f"Alignment complete. Output saved to {output_file}")
else:
    print("Alignment failed")
    print(result.stderr)