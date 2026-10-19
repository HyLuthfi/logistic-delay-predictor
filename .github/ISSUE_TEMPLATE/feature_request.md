---
name: Feature Request
about: Propose a new splitting criterion, ensemble algorithm, or visualization feature for Logistic Delay Predictor
title: "[FEATURE] "
labels: enhancement
assignees: ''
---

## Problem Statement

A clear and concise description of the machine learning limitation or missing supply chain decision capability.

*Example: "When constructing deep decision trees, standard Information Gain is biased towards attributes with numerous distinct values; implementing C4.5 Gain Ratio would penalize high-cardinality partitions."*

## Proposed Solution

A clear and concise description of what feature, splitting criterion, or visual component you want added:
- Mathematical or algorithmic formulation of the proposed from-scratch technique.
- Strategic business benefit for supply chain risk mitigation, delivery delay forecasting, or tree interpretability.
- Target user persona (Supply Chain Analyst, Data Scientist, Logistics Operations Manager, ML Student).

## Architectural Impact

| Subsystem Layer | Yes / No / Description |
|---|---|
| **Data Ingestion & Preprocessing** | |
| **Mathematical Splitting Engine** | |
| **Recursive Tree Builder** | |
| **Inference Engine (Single / Batch)** | |
| **Streamlit Analytics Dashboard** | |
| **Data Visualization & Charts** | |

## Proposed Algorithm Specifications (if applicable)

If this proposal introduces a new from-scratch tree or ensemble method (e.g. Gini Impurity, Gain Ratio, Random Forest from scratch, Cost-Complexity Pruning):

| Parameter | Specifications |
|---|---|
| **Algorithm / Criterion Name** | e.g. Gini Impurity (CART) / Gain Ratio (C4.5) / Random Forest |
| **Mathematical Formulation** | e.g. $Gini(S) = 1 - \sum p_i^2$ or $GainRatio = IG / SplitInfo$ |
| **Computational Complexity** | Expected scaling relative to $N$ samples and $M$ features |
| **Zero-Dependency Policy** | Confirmed pure Python + Pandas (no external ML library imports) |

## Proposed Visualizations (if applicable)

If this proposal introduces new interactive charts or diagnostic plots:

| Parameter | Specifications |
|---|---|
| **Visualization Type** | e.g. ROC-AUC Curve / Precision-Recall Trade-off / Tree Graph Hierarchy |
| **Plotting Library** | Matplotlib / Seaborn / Streamlit native charts |
| **Interactivity** | Static figure vs dynamic interactive component |

## Alternatives Considered

A clear and concise description of any alternative solutions, heuristics, or workarounds you've explored.

## Additional Context

Add any other context, algorithmic research papers, or UI mockups here.
