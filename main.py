from fastapi import FastAPI
from router.qr_code import router_qr
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(title="qr-code")


origins = [
    "https://qr-code-front-three.vercel.app",
    "http://localhost:5173",
    "https://localhost:5173",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization","Accept", "Access-Control-Allow-Methods", 'sec-fetch-mode' ],
)

app.include_router(router_qr)


