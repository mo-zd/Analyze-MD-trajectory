# Analysis of Ligand-Protein Complex Trajectory with Gromacs and MDTraj

This repository contains a Python script for analyzing the trajectory of a ligand-protein complex using Gromacs and MDTraj. The script performs four types of analysis on the trajectory:

    RMSD (Root Mean Square Deviation)
    RMSF (Root Mean Square Fluctuation)
    Binding Energy (MM-PBSA)
    SASA (Solvent Accessible Surface Area)

## Getting Started

To use this script, you'll need to have Gromacs and MDTraj installed on your system. You'll also need a trajectory file in Gromacs XTC format and a topology file in PDB format.

Once you have these files, you can run the script with the following command:

    python analyze_trajectory.py -t topology.pdb -x trajectory.xtc

This will perform the analysis on the trajectory and save the results in separate CSV files.
Requirements

    Gromacs (version 5.0 or later)
    MDTraj (version 1.9 or later)
    Python (version 3.6 or later)
    Pandas (version 1.0 or later)

## Usage
#### Command Line Options

    -t, --topology: Path to topology file in PDB format
    -x, --trajectory: Path to trajectory file in Gromacs XTC format
    -o, --output: Path to output directory (default: current directory)

#### Output Files

The script will save the following analysis results in separate CSV files:

    rmsd.csv: RMSD of the complex over time
    rmsf.csv: RMSF of the complex over time
    binding_energy.csv: Binding energy of the complex over time
    sasa.csv: SASA of the protein and ligand over time

## License

This code is released under the MIT License.
