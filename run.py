import os

# List of scripts to run in order
scripts = ['ngramcounter.py', 'analyze.py', 'finalsort.py']

# Construct the full path to the scripts directory
scripts_dir = os.path.join(os.getcwd(), "scripts")

# Run the scripts in the order specified
for script in scripts:
    # Construct the full path to the script
    script_path = os.path.join(scripts_dir, script)
    # Run the script
    os.system(f"python3 {script_path}")

# Remove the output files
os.remove("output.txt")
os.remove("ngramoutput.txt")

# Print the first 10 lines of FinalResults.txt
with open("FinalResults.txt") as f:
    for i in range(10):
        print(f.readline())
