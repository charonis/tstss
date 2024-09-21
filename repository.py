from datebase import session_async, engine
from shemas import Qr_code
from models import User
from aiobotocore.session import get_session
from contextlib import asynccontextmanager
from config import settings
from utils import qr
from sqlalchemy import select, text

class Repository:
    
    # @classmethod
    # async def create_qr(cls, info_qr: Qr_code ):
    #     async with session_async() as session:
    #         info_qr_dict = info_qr.model_dump()
    #         date = User(**info_qr_dict)
    #         session.add(date)
    #         await session.commit()
    #         return {f"your unique_key = {info_qr_dict["unique_key"]}, your will get a qr_code by this unique_key"}
    
    @classmethod
    async def create_qr(cls, info_qr: Qr_code):
        async with session_async() as session:
            try:
                info_qr_dict = info_qr.model_dump()
                date = User(**info_qr_dict)
                session.add(date)
                await session.commit()
                return {f"your unique_key = {info_qr_dict["unique_key"]}, your will get a qr_code by this unique_key"}
            finally:
                await session.close()
        
    @classmethod
    async def delete_qr(cls, name:str):
        async with session_async() as session:
            quary = (
                select(User).filter(User.unique_key == name)
            )
            response = await session.execute(quary)
            # print(response)
            await session.delete(response.scalars().first())
            await session.commit()
            
    @classmethod
    async def get_date_user(cls, name:str):
        async with session_async() as session:
            quary = (
                select(User).filter(User.unique_key == name)
            )
            response = await session.execute(quary)
            res = response.scalars().all()
            return Qr_code.model_validate(res[0],from_attributes=True)
        
    @classmethod
    async def test_bd_aa(cls):
        async with engine.connect() as conn:
            res = await conn.execute(text("SELECT 1,2,3 UNION select 4,5,6"))
            return res




            
class S3Client:
    def __init__(self) -> None:
        self.config = {
            # "aws_access_key_id": f"3597cf1a4b4a4273a7f170bfd859462b",
            "aws_access_key_id": f"{settings.ACCESS_KEY}",
            
            "aws_secret_access_key": f"{settings.KEY_ID}",
            "endpoint_url": "https://s3.storage.selcloud.ru"
        }
        self.bucket_name = "test-public-bucket1"
        self.session = get_session()
                
    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client 
            
            
    async def upload_qr_file(self, name: str):
        file_name = f"{name}"
        async with self.get_client() as client:
            await client.put_object(
                Bucket=self.bucket_name,
                Key=f"qrcode/{file_name}",
                Body=qr(name),
                ContentType="image/png"
                )      
            # pass
    async def get_qr_file(self,  name:str):
        async with self.get_client() as client:
            response = await client.get_object(Bucket=self.bucket_name, Key=f"qrcode/{name}")
            async with response['Body'] as stream:
                image_data = await stream.read()
            # image = Image.open(BytesIO(image_data))
            # print(type(image_data))
            # image.show()
            return image_data
        
    async def delete_qr_file(self, name:str):
        async with self.get_client() as client:
            objects_to_delete = [{ "Key": f"qrcode/{name}"} ]
            await client.delete_objects(Bucket = self.bucket_name, Delete={"Objects": objects_to_delete})
            
            
            
            
            
            
            
            
            