from fastapi import FastAPI

app = FastAPI()

@app.get("/api/shops")
def get_shops():
    return [
        {"id": 1, "name": "Bakery House", "discount": 40, "closing": "20:00"},
        {"id": 2, "name": "Cafe Smile", "discount": 50, "closing": "21:00"}
    ]

@app.get("/api/cart")
def get_cart():
    return {"items": [], "total": 0}
