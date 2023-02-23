import mdtraj as md
import numpy as np
import pandas as pd

# Load the trajectory and topology files
traj = md.load("trajectory.xtc", top="topology.pdb")

# Calculate the RMSD and RMSF of the complex
rmsd = md.rmsd(traj, traj, 0)
rmsf = md.rmsf(traj, 0)

# Calculate the binding energy of the complex
# (using the MM-PBSA method)
complex_energy = md.compute_energy(t, 'amber99sbildn', igb=5,
                                    forcefield_files=['amber99sbildn.xml', 'tip3p.xml'],
                                    parameter_files=['frcmod.ionsjc_tip3p', 'frcmod.ions234lm_126_tip3p'])

ligand_energy = md.compute_energy(t.top.select('resname LIG'), 'amber99sbildn', igb=5,
                                  forcefield_files=['amber99sbildn.xml', 'tip3p.xml'],
                                  parameter_files=['frcmod.ionsjc_tip3p', 'frcmod.ions234lm_126_tip3p'])

protein_energy = md.compute_energy(t.top.select('protein'), 'amber99sbildn', igb=5,
                                    forcefield_files=['amber99sbildn.xml', 'tip3p.xml'],
                                    parameter_files=['frcmod.ionsjc_tip3p', 'frcmod.ions234lm_126_tip3p'])

binding_energy = complex_energy - ligand_energy - protein_energy

# Calculate the SASA of the protein and ligand
sasa_protein = md.shrake_rupley(traj, mode='residue', probe_radius=0.14,
                                 atom_indices=traj.top.select('protein'))
sasa_ligand = md.shrake_rupley(traj, mode='residue', probe_radius=0.14,
                                atom_indices=traj.top.select('resname LIG'))

# Save the results in separate CSV files
pd.DataFrame(rmsd, columns=['time (ps)', 'RMSD (nm)']).to_csv('rmsd.csv', index=False)
pd.DataFrame(rmsf, columns=['Residue', 'RMSF (nm)']).to_csv('rmsf.csv', index=False)
pd.DataFrame(binding_energy, columns=['time (ps)', 'Binding Energy (kJ/mol)']).to_csv('binding_energy.csv', index=False)
pd.DataFrame(sasa_protein, columns=['time (ps)', 'SASA Protein (nm^2)']).to_csv('sasa_protein.csv', index=False)
pd.DataFrame(sasa_ligand, columns=['time (ps)', 'SASA Ligand (nm^2)']).to_csv('sasa_ligand.csv', index=False)
