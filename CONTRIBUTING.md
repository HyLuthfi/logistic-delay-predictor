# Contributing to Enterprise Logistic Delay Predictor

Thank you for your interest in contributing to **Enterprise Logistic Delay Predictor & From-Scratch Decision Tree DSS** — an open-source machine learning and supply chain decision support system built from first principles.

This project is maintained by **Luthfi Muthathohirin**.

---

## 🛠️ Architecture & Development Setup

The repository is intentionally architected with minimal dependencies to demonstrate fundamental computer science and machine learning concepts in pure Python:

```text
logistic-delay-predictor/
├── main.py                        # Streamlit Dashboard & From-Scratch Decision Tree Engine
├── Train.csv                      # Logistics benchmark dataset (10,999 records)
├── requirements.txt               # Lightweight dependencies (pandas, streamlit)
├── LICENSE                        # MIT License
├── docs/                          # D2 architecture specifications (architecture.d2)
├── assets/                        # Compiled vector SVG architecture and formula cards
└── .github/ISSUE_TEMPLATE/        # Standardized issue reporting templates
```

### 1. Prerequisites

- **Python**: Version 3.10, 3.11, or 3.12 (Python 3.11+ recommended)
- **Pip / Virtual Environment**: Standard Python toolchain

### 2. Local Setup & Virtual Environment

```bash
# Clone the repository
git clone https://github.com/HyLuthfi/logistic-delay-predictor.git
cd logistic-delay-predictor

# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate       # Linux/macOS
.venv\Scripts\activate          # Windows

# Upgrade pip and install minimal dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Running Local Application

Launch the Streamlit dashboard locally:

```bash
streamlit run main.py
```

The application will be accessible at `http://localhost:8501`. Test both single prediction parameter forms and bulk CSV batch processing.

---

## 🌿 Contribution Workflow

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally and configure upstream tracking:
   ```bash
   git clone https://github.com/<your-username>/logistic-delay-predictor.git
   cd logistic-delay-predictor
   git remote add upstream https://github.com/HyLuthfi/logistic-delay-predictor.git
   ```
3. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feat/your-feature-name
   ```
4. Implement your enhancements adhering to first-principles machine learning standards.
5. Verify local numerical stability and UI execution via `streamlit run main.py`.
6. Commit your changes following the Conventional Commits specification.
7. Open a **Pull Request** against `main` of the upstream repository.

---

## 📐 Commit Convention

This repository strictly enforces [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):

| Prefix | Scope / Usage |
|---|---|
| `feat(scope):` | New feature, splitting criterion, or UI component |
| `fix(scope):` | Bug fix in mathematical splitting, entropy guard, or batch pipeline |
| `docs(scope):` | Documentation updates, mathematical proofs, README edits |
| `chore(scope):` | Tooling, dependencies, repository hygiene |
| `refactor(scope):` | Code refactoring without mathematical behavior mutation |
| `perf(scope):` | Performance optimization (vectorization via Pandas, pruning) |
| `test(scope):` | Adding numerical verification test cases |
| `security(scope):` | Security hardening, input sanitization, dependency patches |

**Valid Examples:**
```text
feat(tree): implement Gini Impurity criterion as an alternative to Shannon Entropy
fix(entropy): add numerical epsilon guard to prevent log2(0) floating-point exception
perf(split): accelerate continuous threshold search using sorted unique feature values
docs(readme): add mathematical formulation for Information Gain ratio
```

---

## 🔬 Guidelines for Contributing From-Scratch Algorithms

We welcome contributions expanding the fundamental decision tree implementation (e.g. **Gini Impurity (CART)**, **Gain Ratio (C4.5)**, **Variance Reduction (Regression Trees)**, **Post-Pruning Algorithms**, or **From-Scratch Random Forest**):

### 1. Mathematical Rigor & Numerical Safeguards

- **Strict First-Principles Policy**: The core tree algorithms must remain implemented in pure Python and Pandas. **Do not import or depend on `sklearn.tree`, `xgboost`, or `lightgbm`** in the core algorithmic paths.
- **Logarithmic Zero Guard**: When evaluating class probabilities $p_i$, always protect against $\log_2(0)$ with a bounds check:
  ```python
  def entropi(y):
      if len(y) == 0:
          return 0.0
      p = y.value_counts(normalize=True)
      return -float(np.sum([pi * np.log2(pi) for pi in p if pi > 0]))
  ```
- **Continuous vs Discrete Partitioning**:
  - Continuous attributes (e.g. `Discount_offered`, `Weight_in_gms`, `Cost_of_the_Product`) must be evaluated using binary threshold inequalities: $S_{\text{left}} = \{x \mid x[k] \le v\}$.
  - Categorical attributes (e.g. `Warehouse_block`, `Mode_of_Shipment`) must be evaluated using exact equality matching: $S_{\text{left}} = \{x \mid x[k] == v\}$.
- **Overfitting Regularization**: Ensure all recursive splitting routines respect tree depth constraints (`max_depth`) and minimum split samples (`min_samples_split`).

### 2. Performance & Memory Guidelines

- Continuous split search can be computationally expensive on large datasets. Optimize threshold scans by evaluating candidate thresholds at midpoints of sorted unique feature values rather than every row.
- In batch prediction mode, ensure data manipulation remains in-memory via Pandas DataFrames. Do not persist temporary files to disk.

---

## 📦 Logistics Data Maintenance & Privacy Ethics

When working with supply chain records and benchmark datasets:

1. **Zero Personally Identifiable Information (PII)**: Logistics datasets must never contain real customer names, phone numbers, residential street addresses, or payment credentials. All identifiers must be masked or anonymized.
2. **Ephemeral In-Memory Processing**: Uploaded files in the Streamlit application must reside strictly in temporary RAM buffers (`io.BytesIO`) and be discarded when the browser session terminates.
3. **Data Integrity**: Never falsify or fabricate delivery delay outcomes. Benchmark records must reflect realistic operational distributions.

---

## 🔒 Security Vulnerability Reporting

If you identify a security issue, vulnerability, or secret leakage, **please do not open a public GitHub issue**. Contact the maintainer directly via email: `luthfirg2502@gmail.com`.

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
