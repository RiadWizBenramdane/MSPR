from fastapi import Depends, FastAPI, HTTPException, Header
from jose import jwt
from fastapi.security import HTTPBearer
from fastapi_auth_jwt import AuthJWT
from typing import Optional
from datetime import datetime, timedelta
from passlib.context import CryptContext
import requests
import qrcode
import io
import base64
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


app = FastAPI()

# Define the endpoint of the CRM's API
crm_endpoint = "https://615f5fb4f7254d0017068109.mockapi.io/api/v1"

# Define JWT auth
auth_jwt = AuthJWT(
    secret_key="SECRET_KEY",
    algorithms=["HS256"],
)

bearer_scheme = HTTPBearer()

def generate_qr_code(unique_id: str)->str:
    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(unique_id)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Convert image to base64 string
    with io.BytesIO() as buffer:
        qr_image.save(buffer, format="PNG")
        qr_image_base64 = base64.b64encode(buffer.getvalue()).decode()

    return qr_image_base64

@app.get("/protected")
async def protected(token: str = Depends(auth_jwt)):
    return {"message": "This route is protected by JWT authentication"}

@app.get("/send_qr_code/{email}")
async def send_qr_code(email: str, token: str = Depends(bearer_scheme)):
    # Retrieve user from CRM
    user = await get_data_from_crm(f"/users/{email}")
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Generate QR code
    qr_code = generate_qr_code(email)

    # Send email with QR code
    sender_email = "tonkawapaye@gmail.com"
    receiver_email = get_data_from_crm(crm_endpoint,token)["email"]
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Your QR code athentifiacator "
    text = MIMEText("Please use this QR code to authenticate in the mobile app.")
    message.attach(text)
    image = MIMEImage(base64.b64decode(qr_code))
    message.attach(image)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, "123456789$ABC$abc")
        server.sendmail(sender_email, receiver_email, message.as_string())

    return {"message": "QR code sent successfully"}

# Function for sending GET requests to the CRM's API
async def get_data_from_crm(path: str, token: str = Depends(auth_jwt)):
    url = crm_endpoint + path
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Function for sending POST requests to the CRM's API
async def post_data_to_crm(path: str, data: dict, token: str = Depends(auth_jwt)):
    url = crm_endpoint + path
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Function for sending PUT requests to the CRM's API
async def put_data_to_crm(path: str, data: dict, token: str = Depends(auth_jwt)):
    url = crm_endpoint + path
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.put(url, json=data, headers=headers)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Function for sending DELETE requests to the CRM's API
async def delete_data_from_crm(path: str, data: dict, token: str = Depends(auth_jwt)):
    url = crm_endpoint + path
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url, json=data, headers=headers)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()
