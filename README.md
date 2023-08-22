# FastAPI Cheat Sheet 🚀

#### Installation ⚙️
```bash
pip install fastapi
pip install uvicorn
```

#### Basic Usage 🌐
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World! 🌍"}
```

#### Request Handling 📥
- **Path Parameters:**
```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

- **Query Parameters:**
```python
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

- **Request Body:**
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None

@app.post("/items/")
async def create_item(item: Item):
    return item
```

#### Response Handling 📤
- **JSON Response:**
```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

- **Custom Response Model:**
```python
class ItemResponse(BaseModel):
    name: str
    description: str

@app.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int):
    return {"name": "Item Name", "description": "Item Description"}
```

#### Path Operations 🛤️
- **GET, POST, PUT, DELETE:**
```python
@app.get("/get-example")
@app.post("/post-example")
@app.put("/put-example")
@app.delete("/delete-example")
```

#### Dependency Injection 🧩
```python
from fastapi import Depends

def get_db():
    db = ...
    return db

@app.get("/items/")
async def read_items(db: Database = Depends(get_db)):
    return db.query(...)
```

#### Authentication 🔐
- **OAuth2 with Password Flow:**
```python
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": form_data.username, "token_type": "bearer"}

@app.get("/secure-data")
async def get_secure_data(token: str = Depends(oauth2_scheme)):
    return {"message": "You have access to secure data"}
```

#### Background Tasks 📨
```python
from fastapi import BackgroundTasks

def send_email(background_tasks: BackgroundTasks, email: str):
    # Logic to send email
    pass

@app.post("/send-email")
async def send_email_route(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email)
    return {"message": "Email sent"}
```

#### File Upload 📁
```python
from fastapi import File, UploadFile

@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    # Process the uploaded file
    return {"filename": file.filename}
```

#### WebSocket 🌐
```python
from fastapi import WebSocket

class WebSocketEndpoint(WebSocket):
    async def on_connect(self, websocket: WebSocket):
        await websocket.accept()
    
    async def on_receive(self, websocket: WebSocket, data: str):
        await websocket.send_text(f"You said: {data}")
    
    async def on_disconnect(self, websocket: WebSocket, close_code: int):
        pass
```

#### Exception Handling ❗
```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Item not found")
    return {"item_id": item_id}
```

Feel free to sprinkle in these emojis to make your FastAPI journey even more enjoyable! 😄 For more detailed information, refer to the [official documentation](https://fastapi.tiangolo.com/).
