import os
from typing import TypedDict
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END

# 1. Load API Keys dari file .env
load_dotenv()

# 2. Inisialisasi LLM Gratis (MENGGUNAKAN MODEL TERBARU YANG AKTIF)
# Model llama3-8b-8192 sudah dihapus oleh Groq, digantikan oleh llama-3.3-70b-versatile
llm = ChatGroq(
    temperature=0.7,
    model_name="llama-3.3-70b-versatile"
)

# 3. Definisikan State (Tempat penyimpanan data yang mengalir di alur LangGraph)
class AgentState(TypedDict):
    user_input: str
    sentiment: str
    response: str

# --- NODE 1: Analisis Sentimen (Menggunakan LangChain) ---
def analyze_sentiment(state: AgentState):
    print("\n[INFO] Menjalankan Node: ANALISIS SENTIMEN")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Analisis input berikut. Jika user terlihat marah, kecewa, atau komplain berat, balas dengan satu kata saja: 'NEGATIF'. Jika biasa saja, bertanya, atau ramah, balas: 'NETRAL'."),
        ("user", "{input}")
    ])
    chain = prompt | llm
    result = chain.invoke({"input": state["user_input"]})
    return {"sentiment": result.content.strip().upper()}

# --- NODE 2: Respon Standar (Menggunakan LangChain) ---
def handle_neutral(state: AgentState):
    print("[INFO] Menjalankan Node: RESPON STANDAR")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Anda adalah asisten AI yang ramah. Jawab pertanyaan user dengan jelas dan sopan menggunakan Bahasa Indonesia."),
        ("user", "{input}")
    ])
    chain = prompt | llm
    result = chain.invoke({"input": state["user_input"]})
    return {"response": result.content}

# --- NODE 3: Respon Penenang (Menggunakan LangChain) ---
def handle_negative(state: AgentState):
    print("[INFO] Menjalankan Node: RESPON PENENANG (USER MARAH)")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "User sedang marah/kecewa. Tugas Anda adalah meminta maaf dengan tulus atas ketidaknyamanan ini, menenangkan mereka, dan memberikan solusi terbaik dalam Bahasa Indonesia."),
        ("user", "{input}")
    ])
    chain = prompt | llm
    result = chain.invoke({"input": state["user_input"]})
    return {"response": result.content}

# --- ROUTER: Fungsi penentu arah alur (LangGraph Routing) ---
def route_based_on_sentiment(state: AgentState):
    if "NEGATIF" in state["sentiment"]:
        return "ke_node_negatif"
    else:
        return "ke_node_netral"

# 4. Membangun Alur Kerja Berbasis Graf (LangGraph)
workflow = StateGraph(AgentState)

# Daftarkan fungsi-fungsi di atas sebagai Node
workflow.add_node("analisis_sentimen", analyze_sentiment)
workflow.add_node("respon_netral", handle_neutral)
workflow.add_node("respon_negatif", handle_negative)

# Tentukan titik mulai alur aplikasi
workflow.set_entry_point("analisis_sentimen")

# Buat percabangan otomatis setelah analisis sentimen
workflow.add_conditional_edges(
    "analisis_sentimen",
    route_based_on_sentiment,
    {
        "ke_node_netral": "respon_netral",
        "ke_node_negatif": "respon_negatif"
    }
)

# Hubungkan akhir node ke titik SELESAI (END)
workflow.add_edge("respon_netral", END)
workflow.add_edge("respon_negatif", END)

# Compile graf menjadi aplikasi utuh
app = workflow.compile()

# 5. Uji Coba Program (Demo Aplikasi)
if __name__ == "__main__":
    print("=========================================")
    print("       SISTEM AGENT AI DIJALANKAN        ")
    print("=========================================")
    
    # TES KASUS 1: Menguji respon saat user marah
    print("\n--- UJI COBA 1 (Input Negatif) ---")
    input_1 = "Aplikasi kalian jelek banget! Transaksi saya gagal tapi saldo terpotong!"
    print(f"User: {input_1}")
    hasil_1 = app.invoke({"user_input": input_1})
    print(f"AI: {hasil_1['response']}")
    
    print("\n" + "="*40)
    
    # TES KASUS 2: Menguji respon saat user bertanya biasa
    print("\n--- UJI COBA 2 (Input Netral) ---")
    input_2 = "Halo, bagaimana cara mendaftar akun baru?"
    print(f"User: {input_2}")
    hasil_2 = app.invoke({"user_input": input_2})
    print(f"AI: {hasil_2['response']}")