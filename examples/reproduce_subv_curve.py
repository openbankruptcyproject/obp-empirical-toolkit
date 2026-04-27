#!/usr/bin/env python3
"""Reproduce the Subchapter V adoption curve SVG from the published dataset."""

import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATASET = REPO_ROOT / "datasets" / "subv_quarterly.csv"


def load_data():
    with open(DATASET) as f:
        reader = csv.DictReader(f)
        return [(row["quarter"], int(row["sub_v_filings"])) for row in reader]


def build_svg(data):
    W, H = 980, 460
    pad_l, pad_r, pad_t, pad_b = 70, 30, 30, 80
    plot_w = W - pad_l - pad_r
    plot_h = H - pad_t - pad_b
    max_v = max(v for _, v in data) * 1.1
    bar_w = plot_w / len(data) * 0.8
    bar_gap = plot_w / len(data) * 0.2

    bars = []
    for i, (q, v) in enumerate(data):
        x = pad_l + i * (bar_w + bar_gap)
        h = (v / max_v) * plot_h
        y = H - pad_b - h
        if q.startswith("2020") or q.startswith("2021"):
            color = "#5a9bd5"
        elif q.startswith("2022") or q.startswith("2023"):
            color = "#2e75b6"
        else:
            color = "#a64d79"
        bars.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" fill="{color}"><title>{q}: {v}</title></rect>')

    return f'''<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
{"".join(bars)}
</svg>'''


if __name__ == "__main__":
    data = load_data()
    print(f"Loaded {len(data)} quarters of Sub V data")
    print(f"Range: {data[0]} -> {data[-1]}")
    print(f"Max quarterly volume: {max(v for _, v in data)}")
    svg = build_svg(data)
    out = REPO_ROOT / "examples" / "subv_chart.svg"
    out.write_text(svg)
    print(f"Wrote: {out}")
