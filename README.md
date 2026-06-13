# 🤖 Customer Support AI Agent with Sentiment Routing

Proyek ini adalah sistem AI Agent berbasis NLP/LLM yang dibangun menggunakan **LangChain**, **LangGraph**, dan **LangSmith**. Sistem ini dirancang untuk mendeteksi sentimen input pengguna secara otomatis dan memberikan respon yang dipersonalisasi secara dinamis (ramah untuk pertanyaan umum, penenang untuk keluhan/komplain).

## 🚀 Fitur Utama
- **Sentiment-Based Routing**: Mengalihkan alur percakapan secara otomatis berdasarkan emosi pengguna.
- **State Management**: Mengelola riwayat dan status percakapan secara terstruktur menggunakan LangGraph.
- **Full Traceability**: Setiap eksekusi dipantau dan di-debug secara real-time via LangSmith.
- **Cost-Effective**: Menggunakan LLM gratis berkualitas tinggi via Groq API (`llama-3.3-70b-versatile`).

## 🛠️ Tech Stack & Library Wajib
1. **LangChain**: Digunakan untuk manajemen LLM, pembuatan prompt template, dan penyusunan LLM Chain (`prompt | llm`).
2. **LangGraph**: Digunakan untuk membangun arsitektur Agent berbasis *State Graph* dengan percabangan kondisional (*conditional routing*).
3. **LangSmith**: Platform observability untuk monitoring latency, token usage, dan debugging alur kerja graf secara visual.
4. **Groq Cloud API**: Penyedia akses LLM gratis berkecepatan tinggi.

## 📦 Cara Menjalankan Program di Lokal

### 1. Kloning Repository
```bash
git clone [https://github.com/USERNAME_ANDA/UAS_Agent_LLM.git](https://github.com/USERNAME_ANDA/UAS_Agent_LLM.git)
cd UAS_Agent_LLM