from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(title="TecnoApp API (mock)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Atendimento(BaseModel):
    nome: str
    endereco: str
    descricao: str
    categoria: str
    urgencia: str = "normal"  # normal | medio | urgente

ATENDIMENTOS: List[dict] = []

@app.get("/", tags=["health"])
def health_check():
    return {"status": "ok", "service": "TecnoApp API (mock)"}

@app.get("/atendimentos", response_model=List[dict], tags=["atendimentos"])
def listar_atendimentos():
    return ATENDIMENTOS

@app.post("/atendimentos", status_code=201, tags=["atendimentos"])
def criar_atendimento(payload: Atendimento):
    novo = payload.dict()
    novo["id"] = len(ATENDIMENTOS) + 1
    novo["status"] = "em_aberto" 
    ATENDIMENTOS.append(novo)
    return novo

@app.get("/atendimentos/{atendimento_id}", tags=["atendimentos"])
def obter_atendimento(atendimento_id: int):
    for a in ATENDIMENTOS:
        if a["id"] == atendimento_id:
            return a
    raise HTTPException(status_code=404, detail="Atendimento não encontrado")

@app.put("/atendimentos/{atendimento_id}/status", tags=["atendimentos"])
def atualizar_status(atendimento_id: int, status: str):
    for a in ATENDIMENTOS:
        if a["id"] == atendimento_id:
            a["status"] = status
            return a
    raise HTTPException(status_code=404, detail="Atendimento não encontrado")
