#!/usr/bin/env python3
"""Delega en ``Cari-GIK/scripts/bootstrap_cari_gik_vault.py`` (misma CLI)."""
from __future__ import annotations

import runpy
import sys
from pathlib import Path


def main() -> None:
    repo = Path(__file__).resolve().parents[2]
    target = repo / "Cari-GIK" / "scripts" / "bootstrap_cari_gik_vault.py"
    if not target.is_file():
        raise SystemExit(f"No se encuentra {target}")
    sys.argv[0] = str(target)
    runpy.run_path(str(target), run_name="__main__")


if __name__ == "__main__":
    main()
