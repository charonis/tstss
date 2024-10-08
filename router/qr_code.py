from fastapi import APIRouter, Request, Form, Response
from shemas import Qr_code
from repository import  S3Client
from fastapi.responses import Response , RedirectResponse
from utils import create_unique_key
import json

router_qr = APIRouter(prefix="/qr_code", tags=["qrCode"])

@router_qr.get("/get_qr/{unique_key}") #TODO:ПЕРЕПИСАН
async def get_qr(unique_key: str):
    x = S3Client()
    image_qr = await x.get_qr_file(unique_key)
    return Response(content=image_qr, media_type="image/png")
    

@router_qr.post("/add_qr") #TODO:ПЕРЕПИСАН
async def add_qr( info: Qr_code):
    x = S3Client()
    info.unique_key = create_unique_key()
    name_folder = await x.create_folder(info.unique_key)
    await x.upload_file(name_folder, info)
    await x.upload_qr_file(info.unique_key, name_folder)
    return info.unique_key
   


@router_qr.delete("/remove_qr/{unique_key}") #TODO:ПЕРЕПИСАН
async def remove_qr(unique_key: str):
    x = S3Client()
    await x.delete_qr_file(unique_key)
    return {"you qr-code delete"}


@router_qr.get("/get_date") #TODO:ПЕРЕПИСАН
async def get_date(unique_key:str):
    x = S3Client()
    
    res = await x.get_file(unique_key)
    bb = Qr_code.model_validate(json.loads(str(res, encoding="utf-8")))
    return bb
    

