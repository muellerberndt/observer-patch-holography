#!/usr/bin/env python3
"""
PDG Particle Data Downloader
Fetches particle masses from the PDG database via the official pdg Python package.
Exports to CSV and JSON.

Install: pip install pdg pandas
"""

import json
import pdg
import pandas as pd
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent / "pdg_data"
OUTPUT_DIR.mkdir(exist_ok=True)

# (PDG name or mcid, label, fallback PDG property ID, unit of fallback)
# Some particles (light quarks, pi0) need direct property lookup because
# the .mass attribute fails in the 2025 API.
PARTICLES = [
    # Quarks
    ("u", "up quark", "Q002M", "MeV"),
    ("d", "down quark", "Q001M", "MeV"),
    ("s", "strange quark", "Q003M", "MeV"),
    ("c", "charm quark", "Q004M", "GeV"),
    ("b", "bottom quark", "Q005M", "GeV"),
    ("t", "top quark", None, "GeV"),
    # Leptons
    ("e-", "electron", None, "GeV"),
    ("mu-", "muon", None, "GeV"),
    ("tau-", "tau", None, "GeV"),
    # Gauge bosons
    ("W+", "W boson", None, "GeV"),
    ("Z0", "Z boson", None, "GeV"),
    # Higgs
    ("H", "Higgs boson", None, "GeV"),
    # Hadrons
    ("p", "proton", None, "GeV"),
    ("n", "neutron", None, "GeV"),
    ("pi+", "pion (charged)", None, "GeV"),
    ("pi0", "pion (neutral)", "S009M", "MeV"),
    ("K+", "kaon (charged)", None, "GeV"),
    ("K0", "kaon (neutral)", None, "GeV"),
    (3122, "Lambda", None, "GeV"),
]


def fetch_mass(api, pdg_id, fallback_prop, unit):
    """Get mass in GeV and uncertainties for a particle."""
    # Try standard particle lookup first
    try:
        if isinstance(pdg_id, int):
            p = api.get_particle_by_mcid(pdg_id)
        else:
            p = api.get_particle_by_name(pdg_id)

        mass = p.mass
        if mass is not None:
            err_plus, err_minus = None, None
            try:
                for m in p.masses():
                    s = m.best_summary()
                    if s is not None:
                        err_plus = s.error_positive
                        err_minus = s.error_negative
                        break
            except Exception:
                pass
            return mass, err_plus, err_minus
    except Exception:
        pass

    # Fallback: direct property ID lookup (light quarks, pi0)
    if fallback_prop is not None:
        try:
            item = api.get(fallback_prop)
            s = item.best_summary()
            if s is not None and s.value is not None:
                val = s.value
                ep = s.error_positive
                em = s.error_negative
                if unit == "MeV":
                    val /= 1000.0
                    if ep is not None:
                        ep /= 1000.0
                    if em is not None:
                        em /= 1000.0
                return val, ep, em
        except Exception as e:
            print(f"  Fallback failed for {fallback_prop}: {e}")

    return None, None, None


def main():
    print("Connecting to PDG database...")
    api = pdg.connect()
    print(f"PDG edition: {api.edition}\n")

    rows = []
    for entry in PARTICLES:
        pdg_id, label, fallback_prop, unit = entry
        mass, err_plus, err_minus = fetch_mass(api, pdg_id, fallback_prop, unit)
        if mass is not None:
            print(f"  {label:25s}  {mass:.10g} GeV  (+{err_plus} / {err_minus})")
        else:
            print(f"  {label:25s}  no mass data")
        rows.append({
            "particle": label,
            "pdg_name": str(pdg_id),
            "mass_GeV": mass,
            "err_plus_GeV": err_plus,
            "err_minus_GeV": err_minus,
        })

    df = pd.DataFrame(rows)

    csv_path = OUTPUT_DIR / "particle_masses.csv"
    df.to_csv(csv_path, index=False)
    print(f"\nSaved CSV -> {csv_path}")

    json_path = OUTPUT_DIR / "particle_masses.json"
    records = df.to_dict(orient="records")
    with open(json_path, "w") as f:
        json.dump(records, f, indent=2)
    print(f"Saved JSON -> {json_path}")

    print(f"\nTotal particles: {len(df)}")
    print(f"With mass data: {df['mass_GeV'].notna().sum()}")


if __name__ == "__main__":
    main()
