"""
=============================================================================
  CAMPUS ELEVATOR WAITING TIME DISTRIBUTION SIMULATION
  Discrete-Event Queue Simulation with Monte Carlo Methods

  UPDATED VERSION:
  ─────────────────────────────────────────────────────────────────────────
  ✔ Fixed overlapping titles and labels
  ✔ Increased spacing between graphs
  ✔ Improved layout readability
  ✔ Added safer layout handling
  ✔ Improved axis label spacing
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import os

# ============================================================================
# REPRODUCIBILITY
# ============================================================================

np.random.seed(42)

# Number of Monte Carlo runs
N = 10_000

# ============================================================================
# DISTRIBUTION PARAMETERS
# ============================================================================

# 1. Exponential Distribution
exp_rate = 1 / 20
exp_sample = np.random.exponential(scale=1 / exp_rate, size=N)

# 2. Normal Distribution
norm_mu = 75
norm_sigma = 25

norm_sample = np.random.normal(
    loc=norm_mu,
    scale=norm_sigma,
    size=N
)

# 3. Poisson Distribution
poisson_lambda = 4

poisson_sample = np.random.poisson(
    lam=poisson_lambda,
    size=N
)

# 4. Binomial Distribution
binom_n = 10
binom_p = 0.75

binom_sample = np.random.binomial(
    n=binom_n,
    p=binom_p,
    size=N
)

# 5. Triangular Distribution
tri_low = 10
tri_mode = 25
tri_high = 60

tri_sample = np.random.triangular(
    left=tri_low,
    mode=tri_mode,
    right=tri_high,
    size=N
)

# ============================================================================
# COMPOSITE WAITING TIME ESTIMATION
# ============================================================================

congestion_penalty = poisson_sample * 8

waiting_time = (
    norm_sample
    + tri_sample
    + congestion_penalty
)

waiting_time = np.clip(waiting_time, 5, 600)

# ============================================================================
# PERCENTILES
# ============================================================================

p10, p25, p50, p75, p90 = np.percentile(
    waiting_time,
    [10, 25, 50, 75, 90]
)

# ============================================================================
# COLOR PALETTE
# ============================================================================

BG = "#0D1117"
PANEL = "#161B22"

ACCENT = "#58A6FF"
GREEN = "#3FB950"
ORANGE = "#F78166"
PURPLE = "#BC8CFF"
YELLOW = "#D29922"
TEAL = "#39C5CF"

TEXT = "#E6EDF3"
SUBTEXT = "#8B949E"

DIST_COLORS = [
    ACCENT,
    GREEN,
    ORANGE,
    PURPLE,
    TEAL
]

DIST_LABELS = [
    "① Exponential\nStudent Arrival Intervals",
    "② Normal\nElevator Waiting Delay",
    "③ Poisson\nStudents Arriving",
    "④ Binomial\nSuccessful Boarding",
    "⑤ Triangular\nElevator Travel Time"
]

DIST_SAMPLES = [
    exp_sample,
    norm_sample,
    poisson_sample,
    binom_sample,
    tri_sample
]

DIST_BINS = [
    40,
    40,
    range(0, 15),
    range(0, 12),
    40
]

# ============================================================================
# FIGURE LAYOUT (FIXED)
# ============================================================================

fig = plt.figure(
    figsize=(22, 16),
    facecolor=BG
)

fig.suptitle(
    "Campus Elevator Waiting Time Distribution Simulation (N = 10,000)",
    fontsize=22,
    fontweight="bold",
    color=TEXT,
    y=0.985
)

gs = GridSpec(
    3,
    3,
    figure=fig,
    hspace=1.00,   # increased spacing
    wspace=0.45,
    left=0.06,
    right=0.97,
    top=0.86,      # lowered graphs
    bottom=0.08
)

# ============================================================================
# AXIS STYLING
# ============================================================================

def style_ax(ax, title, xlabel, ylabel="Frequency"):

    ax.set_facecolor(PANEL)

    ax.set_title(
        title,
        color=TEXT,
        fontsize=12,
        fontweight="bold",
        pad=14
    )

    ax.set_xlabel(
        xlabel,
        color=SUBTEXT,
        fontsize=9,
        labelpad=10
    )

    ax.set_ylabel(
        ylabel,
        color=SUBTEXT,
        fontsize=9,
        labelpad=10
    )

    ax.tick_params(
        colors=SUBTEXT,
        labelsize=8
    )

    for spine in ax.spines.values():
        spine.set_edgecolor("#30363D")

    ax.grid(
        axis="y",
        color="#21262D",
        linewidth=0.8,
        linestyle="--"
    )

# ============================================================================
# HISTOGRAMS 1–5
# ============================================================================

positions = [
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 0),
    (1, 1)
]

for idx, (row, col) in enumerate(positions):

    ax = fig.add_subplot(gs[row, col])

    data = DIST_SAMPLES[idx]
    color = DIST_COLORS[idx]
    bins = DIST_BINS[idx]

    # Discrete distributions
    if idx in (2, 3):

        vals, cnts = np.unique(data, return_counts=True)

        ax.bar(
            vals,
            cnts / N * 100,
            color=color,
            alpha=0.85,
            edgecolor=BG,
            linewidth=0.6,
            width=0.6
        )

        ax.set_ylabel(
            "Probability (%)",
            color=SUBTEXT,
            fontsize=8
        )

    # Continuous distributions
    else:

        ax.hist(
            data,
            bins=bins,
            color=color,
            alpha=0.80,
            edgecolor=BG,
            linewidth=0.4
        )

    style_ax(
        ax,
        DIST_LABELS[idx],
        xlabel=[
            "Seconds",
            "Seconds",
            "# Students",
            "# Successful Boardings",
            "Seconds"
        ][idx]
    )

    # Mean line
    mu = np.mean(data)

    ax.axvline(
        mu,
        color="white",
        linewidth=1.2,
        linestyle="--",
        alpha=0.7
    )

    ax.text(
        mu,
        ax.get_ylim()[1] * 0.88,
        f"μ={mu:.2f}",
        color="white",
        fontsize=7,
        ha="left",
        va="top",
        bbox=dict(
            boxstyle="round,pad=0.2",
            fc=PANEL,
            ec=color,
            lw=0.8
        )
    )

# ============================================================================
# MAIN WAITING TIME DISTRIBUTION
# ============================================================================

ax6 = fig.add_subplot(gs[1, 2])

ax6.hist(
    waiting_time,
    bins=60,
    density=True,
    color=ACCENT,
    alpha=0.75,
    edgecolor=BG,
    linewidth=0.3
)

ymax6 = ax6.get_ylim()[1]

for pct, val, col, lbl in [

    (10, p10, GREEN, "P10"),
    (50, p50, YELLOW, "P50"),
    (90, p90, ORANGE, "P90")

]:

    ax6.axvline(
        val,
        color=col,
        linewidth=1.5,
        linestyle="--"
    )

    ax6.text(
        val + 5,
        ymax6 * 0.60,
        f"{lbl}\n{val:.0f} sec",
        color=col,
        fontsize=7,
        va="top",
        bbox=dict(
            boxstyle="round,pad=0.25",
            fc=PANEL,
            ec=col,
            lw=0.8
        )
    )

style_ax(
    ax6,
    "⑥ Composite Elevator Waiting Time Distribution",
    "Waiting Time (seconds)",
    "Density"
)

# ============================================================================
# WAITING TIME PROBABILITIES
# ============================================================================

ax7 = fig.add_subplot(gs[2, 0])

slots = [
    "Fast\n(<60s)",
    "Moderate\n(60-120s)",
    "Heavy\n(120-240s)",
    "Extreme\n(240+s)"
]

slot_probs = [

    np.mean(waiting_time < 60) * 100,

    np.mean(
        (waiting_time >= 60)
        & (waiting_time < 120)
    ) * 100,

    np.mean(
        (waiting_time >= 120)
        & (waiting_time < 240)
    ) * 100,

    np.mean(waiting_time >= 240) * 100
]

colors7 = [
    YELLOW,
    GREEN,
    ORANGE,
    PURPLE
]

bars = ax7.bar(
    slots,
    slot_probs,
    color=colors7,
    alpha=0.85,
    edgecolor=BG,
    linewidth=0.5
)

for bar, prob in zip(bars, slot_probs):

    ax7.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.5,
        f"{prob:.1f}%",
        ha="center",
        va="bottom",
        color=TEXT,
        fontsize=8,
        fontweight="bold"
    )

style_ax(
    ax7,
    "⑦ Waiting Time Probability Analysis",
    "Waiting Category",
    "Probability (%)"
)

plt.setp(ax7.get_xticklabels(), rotation=5)

# ============================================================================
# FLOOR REQUEST DISTRIBUTION
# ============================================================================

ax8 = fig.add_subplot(gs[2, 1])

floors = np.arange(1, 11)

requests = np.random.poisson(
    lam=[5, 8, 10, 14, 16, 15, 12, 9, 6, 4]
)

ax8.bar(
    floors,
    requests,
    color=ACCENT,
    alpha=0.8,
    edgecolor=BG
)

style_ax(
    ax8,
    "⑧ Floor Request Frequency",
    "Floor Number",
    "Requests"
)

# ============================================================================
# PERCENTILE SUMMARY TABLE
# ============================================================================

ax9 = fig.add_subplot(gs[2, 2])

ax9.set_facecolor(PANEL)
ax9.axis("off")

table_data = [

    ["P10 — Fastest Likely Wait", f"{p10:.0f} sec", GREEN],
    ["P25 — Low Congestion", f"{p25:.0f} sec", TEAL],
    ["P50 — Most Likely Wait", f"{p50:.0f} sec", YELLOW],
    ["P75 — Heavy Congestion", f"{p75:.0f} sec", ORANGE],
    ["P90 — Worst Case Wait", f"{p90:.0f} sec", ORANGE]

]

ax9.set_title(
    "⑨ Elevator Waiting Summary",
    color=TEXT,
    fontsize=12,
    fontweight="bold",
    pad=14
)

for i, (label, time_str, col) in enumerate(table_data):

    y = 0.85 - i * 0.17

    ax9.add_patch(
        mpatches.FancyBboxPatch(
            (0.02, y - 0.07),
            0.96,
            0.14,
            boxstyle="round,pad=0.01",
            linewidth=1,
            edgecolor=col,
            facecolor=BG,
            transform=ax9.transAxes
        )
    )

    ax9.text(
        0.08,
        y,
        label,
        transform=ax9.transAxes,
        color=SUBTEXT,
        fontsize=8,
        va="center"
    )

    ax9.text(
        0.92,
        y,
        time_str,
        transform=ax9.transAxes,
        color=col,
        fontsize=10,
        fontweight="bold",
        va="center",
        ha="right"
    )

# ============================================================================
# FOOTER
# ============================================================================

fig.text(
    0.5,
    0.015,
    "Monte Carlo DES · N=10,000 simulations · "
    "Distributions: Exponential · Normal · Poisson · Binomial · Triangular",
    ha="center",
    color=SUBTEXT,
    fontsize=8
)

# ============================================================================
# FINAL LAYOUT FIX
# ============================================================================

fig.subplots_adjust(
    top=0.86,
    bottom=0.08,
    hspace=1.00,
    wspace=0.45
)

# ============================================================================
# SAVE FIGURE
# ============================================================================

output_file = "elevator_waiting_time_histograms.png"

try:

    plt.savefig(
        output_file,
        dpi=150,
        bbox_inches="tight",
        facecolor=BG
    )

    print(f"✔ Figure saved → {os.path.abspath(output_file)}")

except Exception as e:

    print(f"⚠ Could not save figure: {e}")

plt.show()

# ============================================================================
# CONSOLE SUMMARY
# ============================================================================

print("\n=== ELEVATOR WAITING TIME SUMMARY ===")

print(f"P10 Fastest Likely Wait : {p10:.0f} sec")
print(f"P25 Low Congestion      : {p25:.0f} sec")
print(f"P50 Most Likely Wait    : {p50:.0f} sec")
print(f"P75 Heavy Congestion    : {p75:.0f} sec")
print(f"P90 Worst Case Wait     : {p90:.0f} sec")

print("\nWaiting Time Probabilities:")

for slot, prob in zip(slots, slot_probs):

    print(f"{slot:<22} {prob:.1f}%")
