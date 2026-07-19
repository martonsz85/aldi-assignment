#!/usr/bin/python3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()

# In-memory config store
config_store = {}

VERSION = os.getenv("APPVERSION", "unknown")
ENVIRONMENT = os.getenv("ENVIRONMENT", "unknown")


class ConfigItem(BaseModel):
    name: str
    value: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": VERSION}


@app.get("/env")
def env():
    return {"environment": ENVIRONMENT}


@app.post("/config")
def create_config(item: ConfigItem):
    config_store[item.name] = item.value
    return {"name": item.name, "value": item.value}


@app.get("/config/{name}")
def get_config(name: str):
    if name not in config_store:
        raise HTTPException(status_code=404, detail="Config not found")
    return {"name": name, "value": config_store[name]}


@app.delete("/config/{name}")
def delete_config(name: str):
    if name in config_store:
        del config_store[name]
        return {"deleted": True}
    raise HTTPException(status_code=404, detail="Config not found")
