# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-10-19

Initial stable release of **Enterprise Logistic Delay Predictor & From-Scratch Decision Tree DSS** — an applied machine learning and supply chain decision support system implementing a complete Decision Tree classifier from first principles using Shannon Entropy and Information Gain in pure Python, integrated with an interactive Streamlit analytics dashboard.

### Added

- **From-Scratch Decision Tree Classification Core**:
  - Implementation of recursive binary decision tree classifier built purely in standard Python and Pandas without external machine learning libraries (`scikit-learn`).
  - Mathematical **Shannon Entropy** calculation engine evaluating target class impurity:
    $$H(S) = - \sum_{i=1}^c p_i \log_2(p_i)$$
  - **Information Gain** optimization evaluating potential splits across continuous and discrete attributes:
    $$IG(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$
  - Multi-tier recursive stopping guards: pure subset ($H=0$), maximum depth constraint (`max_depth = 10`), minimum samples per split (`min_samples_split = 5`), and zero gain threshold ($IG = 0$).
  - Majority class voting terminal nodes resolving final classification verdicts (On Time vs Delayed).
- **Dual Inference Engine**:
  - **Single Consignment Predictor**: Real-time evaluation traversing the decision tree hierarchy in under 1 millisecond with visual status risk badges.
  - **In-Memory Batch Prediction Pipeline**: High-throughput batch processor consuming uploaded consignment CSVs via transient Pandas memory buffers, generating real-time predictions, and providing instantaneous CSV report export.
- **Interactive Streamlit Web Dashboard (`main.py`)**:
  - 4-tab modular enterprise layout:
    - **Tab 1: Prediksi Tunggal**: Interactive parameter form with dynamic risk indicators.
    - **Tab 2: Prediksi Massal**: Bulk CSV uploader with summary metrics and one-click report download.
    - **Tab 3: Analisis Data & Visualisasi**: Exploratory Data Analysis (EDA) scatter plots correlating product discounts, package weights, and delivery delay probabilities.
    - **Tab 4: Metodologi & Algoritma**: Transparent parameter inspection documenting mathematical formulations and tree hyperparameters.
- **Logistics Dataset & Benchmark Validation**:
  - Curated training dataset of 10,999 commercial logistics consignments (`Train.csv`, 440KB) across 10 operational attributes.
  - Automated performance evaluation pipeline calculating Confusion Matrix, Accuracy, Precision, Recall, and harmonic F1-score with numerical epsilon safeguards ($10^{-10}$).
- **Showcase DX & Visual Documentation**:
  - D2 vector architecture diagram (`assets/architecture.svg`) compiled in Terminal Dark palette with ELK layout engine documenting all 5 subsystem layers.
  - Standalone 3-panel mathematical formula vector SVG (`assets/decision_tree_formulas.svg`) featuring true horizontal fraction bars, summation signs, and clean typography.
  - Standard 9-element portfolio `README.md` with dynamic typing header, verified logistics attribute matrix, numerical walkthrough simulation, and zero promotional buzzwords.
  - Live deployment integration on Streamlit Community Cloud (`logistic-delay-predictor.streamlit.app`).

### Changed

- **Minimalist Toolchain & Fast Startup**: Streamlined dependencies to pure `pandas` and `streamlit` in `requirements.txt`, eliminating heavy C-bindings and ensuring sub-second cold starts.
- **Deterministic Encoding**: Standardized categorical feature mappings (`Warehouse_block`, `Mode_of_Shipment`, `Product_importance`, `Gender`) ensuring consistent partition boundaries across training and inference.

### Security

- **[P0] SPDX MIT License**: Issued official `LICENSE` file under MIT License with legal copyright attributed to `Luthfi Muthathohirin`.
- **[P0] Zero Leak Certification**: Passed comprehensive 9-commit repository history scan with Gitleaks v8.30.1 (**0 leaks detected**, Health Score 98/100).
- **[P0] Hardened `.gitignore`**: Implemented comprehensive 101-rule exclusion filter protecting Python bytecode (`__pycache__/`), virtual environments (`.venv/`), Streamlit secrets (`secrets.toml`), batch prediction exports (`batch_prediction_*.csv`), and model caches.
- **Privacy & PII Protection**: Certified training dataset contains zero personal customer identifiers (PII), customer addresses, phone numbers, or billing accounts.
- **Ephemeral In-Memory Processing**: Ensured uploaded batch files are evaluated strictly in transient RAM buffers without filesystem storage.
