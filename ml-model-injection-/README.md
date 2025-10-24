# 🧩 Malicious Code Injection in Machine Learning Models (TFG)

This project is my **Final Degree Project (TFG)**, focused on exploring and mitigating **security vulnerabilities in machine learning model serialization**.  
It investigates how adversarial payloads can be embedded into ML artifacts and proposes **detection and defense mechanisms** to secure the AI supply chain.

---

## 🧠 Overview
The research explores multiple attack surfaces in the ML lifecycle — from unsafe deserialization to poisoned models — using **controlled and non-destructive experiments** with both **PyTorch** and **TensorFlow**.

The study covers:
- Insecure serialization methods (`__reduce__`, custom deserialization hooks, pickle/HDF5/SavedModel)
- Malicious payload injection and tensor manipulation
- Model-poisoning through altered preprocessing
- Safe detection and mitigation scripts
- Recommendations for secure model loading and artifact validation

---

## 📂 Repository Structure

ml-model-injection/
│
├── codigo/
│ ├── ataque_metodos/ # Tests comparing safe vs. unsafe model methods
│ │ ├── safe_model/ # Secure serialization example
│ │ └── unsafe_model/ # Vulnerable serialization example
│ │ ├── detection.py # Validation and comparison script
│ │ ├── inject_tensor.py # Controlled tensor-level injection demo
│ │ └── tensorflow_codeinject.py# Safe TensorFlow deserialization test
│ │
│ ├── ataque_payload/ # Experiments with adversarial payload injection
│ │ ├── add_payload.py # Controlled embedding of non-malicious payloads
│ │ ├── inject_attack.py # Simulated injection process (safe)
│ │ ├── detection.py # Payload detection script
│ │ ├── cats_and_dogs_mobilenet.py # Model used for testing (transfer learning)
│ │ ├── ModeloEject.pt # Example model for controlled test
│ │ └── gato.jpg # Sample input image
│ │
│ ├── ataque_reduce/ # Research on PyTorch reduce and deserialization
│ │ ├── inject_reduce.py # Controlled test for reduce vulnerability
│ │ ├── detection.py # Detection script for reduce-based payloads
│ │ ├── ModeloDetect.pt # Sample model
│ │ └── gato.jpg
│ │
│ └── cats_and_dogs_filtered/ # Dataset used in all experiments
│ ├── train/
│ └── validation/
│
├── material_adicional/ # Complementary resources
│ ├── videos.zip # Recorded demonstrations (safe examples)
│ └── material_adicional.zip # Extra references and figures
│
├── TFG_Ángel_Antequera_Gómez.pdf # Full written report (Final Degree Project)
│
└── README.md # Documentation (this file)

---

## 🧰 Highlights
- Analysis of **serialization vulnerabilities** in PyTorch and TensorFlow  
- Controlled **payload injection** and **tensor manipulation** demonstrations   
- **Dataset** (`cats_and_dogs_filtered`) for reproducible experiments  
- Complete **academic report** and visual demonstrations in `/material_adicional/`

---

## ⚙️ Tech Stack
Python · PyTorch · TensorFlow · Keras · NumPy · Pandas · Matplotlib 

---

## 📄 Included Files
- **`TFG_Ángel_Antequera_Gómez.pdf`** — Full academic report (methodology, results, and references).  
- **`codigo/`** — All controlled experimental code, detection tools, and dataset.  
- **`material_adicional/`** — Videos and supporting materials for demonstrations.  

---

## 💬 Notes
- All scripts and demonstrations are **non-destructive** and serve educational and research purposes only.  
- No harmful or malicious payloads are distributed.  
- All tests were executed in isolated environments with academic supervision.

---

## 💡 Purpose
This project aims to raise awareness about **security risks in AI workflows**, highlighting how model artifacts can be potential attack vectors — and how to detect and mitigate them responsibly.  
It reflects my broader goal of building **secure, trustworthy, and explainable AI systems**.

---

## ⚠️ Disclaimer
All experiments and code included in this repository are intended strictly for **research and educational purposes**.  
No harmful or malicious use is intended.  
If you reproduce or extend this work, please follow applicable laws, academic ethics, and responsible disclosure practices.