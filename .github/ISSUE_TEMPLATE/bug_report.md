---
name: Bug Report
about: Report an algorithmic anomaly, division-by-zero error, or UI issue in Logistic Delay Predictor
title: "[BUG] "
labels: bug
assignees: ''
---

## Description

A clear and concise description of what the mathematical or application bug is.

## Steps to Reproduce

1. Open application locally or via Streamlit Cloud
2. Navigate to tab '...' (Prediksi Tunggal / Prediksi Massal / Analisis Data / Metodologi)
3. Input consignment parameters or upload test batch CSV:
   - Warehouse block: ...
   - Mode of shipment: ...
   - Cost of product: ...
   - Discount offered: ...
   - Weight in gms: ...
4. Trigger prediction or batch analysis
5. Observe error or anomalous calculation output at '...'

## Expected Behavior

A clear and concise description of what you expected to happen (e.g. tree traverses to valid leaf node within 1ms, Information Gain computed without floating-point exception, bulk CSV processes all rows without schema error).

## Actual Behavior / Error Traceback

What actually happened (e.g. `ZeroDivisionError: float division by zero`, `ValueError: cannot convert float NaN to integer`, tree recursion depth exceeded, Streamlit file uploader crash).

```text
Paste terminal error output or browser console traceback here
```

## Consignment & Parameter Details (if applicable)

| Parameter | Input Value | Attribute Type |
|---|---|---|
| **Warehouse Block** | e.g. Block A / B / C / D / F | Categorical |
| **Mode of Shipment** | e.g. Flight / Ship / Road | Categorical |
| **Product Cost ($)** | e.g. 250 | Continuous |
| **Discount Offered (%)** | e.g. 65 | Continuous |
| **Weight in Grams** | e.g. 1850 | Continuous |
| **Prior Purchases** | e.g. 3 | Discrete Integer |

## System & Execution Environment

| Parameter | Value |
|---|---|
| **Execution Environment** | Streamlit Community Cloud / Local Python venv |
| **Operating System** | Windows 11 / Ubuntu 22.04 / macOS |
| **Python Version** | e.g. Python 3.10.12 / 3.11.8 / 3.12.2 |
| **Streamlit Version** | e.g. 1.32.0 |
| **Pandas Version** | e.g. 2.2.0 |
| **Browser & Version** | e.g. Chrome 129 / Edge / Firefox |

## Additional Context

Add any other context about the problem here (e.g. sample consignment row triggering the bug, screenshot of the tree evaluation breakdown).
