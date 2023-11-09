from fastapi import FastAPI
from pathlib import Path
import yaml

app = FastAPI(debug=True)

# pyyaml を使ってAPI仕様書をロード
oas_doc = yaml.safe_load(
    (Path(__file__).parent / 'oas.yaml').read_text()
)
# FastAPI の openapi プロパティを上書きし、API仕様書を返すようにする
app.openapi = lambda: oas_doc

from src.ch06.orders.api import api
