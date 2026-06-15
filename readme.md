class RegisterUser(BaseModel):
    name: str
    email: str
    password: str

class LoginUser(BaseModel):
    email: str
    password: str


@app.get("/")
def root():
    return {"message": "Auth API Running"}

@app.post("/register")
def register(user: RegisterUser):

    if user.email in users:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    users[user.email] = {
        "name": user.name,
        "password": user.password
    }

    return {"message": "User registered successfully"}

    # Login
@app.post("/login")
def login(user: LoginUser):

    if user.email not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if users[user.email]["password"] != user.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    return {
        "message": "Login successful"
    }


# Logout
@app.post("/logout")
def logout():
    return {
        "message": "Logout successful"
    }