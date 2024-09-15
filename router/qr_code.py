from fastapi import APIRouter, Request, Form, Response
from shemas import Qr_code
from repository import Repository, S3Client
from fastapi.responses import Response , RedirectResponse
from utils import create_unique_key

router_qr = APIRouter(prefix="/qr_code", tags=["qrCode"])

@router_qr.get("/get_qr/{unique_key}")
async def get_qr(unique_key: str):
    x = S3Client()
    image_qr = await x.get_qr_file(unique_key)
    return Response(content=image_qr, media_type="image/png")
    

@router_qr.post("/add_qr")
async def add_qr( info: Qr_code , res: Response):
    x = S3Client()
    info.unique_key = create_unique_key()
    await Repository.create_qr(info)
    
    await x.upload_qr_file(info.unique_key)
    return info.unique_key
   


@router_qr.delete("/remove_qr/{unique_key}")
async def remove_qr(unique_key: str):
    x = S3Client()
    await Repository.delete_qr(unique_key)
    await x.delete_qr_file(unique_key)
    return {"you qr-code delete"}


@router_qr.get("/get_date")
async def get_date(unique_key:str):
    response = await Repository.get_date_user(unique_key)
    return response.model_dump()


@router_qr.get("/test_bd")
async def test_bd():
    x = Repository()
    
    response = await x.test_bd_aa()
    return response

