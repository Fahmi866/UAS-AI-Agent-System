# 🤖 Customer Support AI Agent with Sentiment Routing

[![Framework - LangChain](https://img.shields.io/badge/Framework-LangChain-blue?style=for-the-badge)](https://python.langchain.com/)
[![Workflow - LangGraph](https://img.shields.io/badge/Workflow-LangGraph-orange?style=for-the-badge)](https://langchain-ai.github.io/langgraph/)
[![Monitoring - LangSmith](https://img.shields.io/badge/Monitoring-LangSmith-darkgreen?style=for-the-badge)](https://smith.langchain.com/)
[![LLM - Groq](https://img.shields.io/badge/LLM-Groq--Llama3.3-red?style=for-the-badge)](https://console.groq.com/)

Proyek ini adalah sistem **AI Agent pintar berbasis NLP/LLM** yang dibangun untuk memenuhi tugas **Ujian Akhir Semester (UAS)**. Sistem ini mengintegrasikan ekosistem AI modern dari LangChain untuk otomatisasi penanganan keluhan pelanggan secara dinamis menggunakan analisis sentimen waktu nyata (*real-time*).

---

## 📌 1. Detail Proyek & Arsitektur

Aplikasi ini mengimplementasikan agen cerdas yang dapat mengalirkan data secara sirkular berdasarkan emosi pengguna. Input pengguna dianalisis, dikategorikan, lalu diarahkan ke penanganan yang paling sesuai agar meminimalkan konflik (*conflict de-escalation*).

### 🔄 Alur Kerja Sistem (Graph Workflow)
Sistem ini menggunakan arsitektur berbasis Graf di mana alur eksekusi ditentukan oleh hasil keluaran dari node analisis sentimen:

1. **Node Analisis Sentimen**: Menerima input teks, melakukan klasifikasi emosional.
2. **Conditional Router**: Memeriksa *state* sentimen. Jika terdapat indikasi komplain berat, diarahkan ke jalur penanganan khusus, jika tidak akan diarahkan ke jalur respon standar.

Sistem ini dibangun atas **3 Library Wajib** dengan peran sebagai berikut:

| Library | Fitur yang Digunakan | Kegunaan di Dalam Proyek |
| :--- | :--- | :--- |
| **LangChain** | `ChatPromptTemplate`, `ChatGroq`, LCEL (`prompt \| llm`) | Mengelola interaksi dengan LLM, menyusun cetakan instruksi (*prompting*), dan mengeksekusi inferensi model. |
| **LangGraph** | `StateGraph`, `Nodes`, `Conditional Edges`, `END` | Membangun arsitektur agen berbasis graf, mengelola status memori data (`AgentState`), dan melakukan *routing* otomatis berdasarkan hasil analisis sentimen. |
| **LangSmith** | `Tracing`, `Project Tracking` | Melakukan pemantauan penuh terhadap performa agen, melacak penggunaan token, mengukur kecepatan respons (*latency*), serta kebutuhan *debugging*. |

---

## 📸 2. Screenshots & Bukti Implementasi

### A. Demo Eksekusi Terminal (VS Code)
Berikut adalah bukti bahwa LangGraph berhasil melakukan percabangan alur kerja secara dinamis di terminal local:
![Screenshot Terminal](https://via.placeholder.com/800x400.png?text=Tempatkan+Screenshot+Terminal+VS+Code+Anda+Disini)

### B. Dashboard Monitoring LangSmith
Berikut adalah bukti pelacakan visual graf dan detail token/latency yang terekam otomatis di platform LangSmith:
![Screenshot LangSmith](https://via.placeholder.com/800x400.png?text=Tempatkan+Screenshot+Dashboard+LangSmith+Anda+Disini)

---

## 🚀 3. Cara Menjalankan Program (Instalasi Lokal)

Ikuti langkah-langkah di bawah ini untuk menjalankan sistem AI Agent ini di komputer lokal Anda:

### Langkah 1: Kloning Repositori
Buka terminal Anda dan unduh repositori ini:
```bash
git clone [https://github.com/Fahmi866/UAS-AI-Agent-System.git](https://github.com/Fahmi866/UAS-AI-Agent-System.git)
cd UAS-AI-Agent-System