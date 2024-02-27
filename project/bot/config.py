class Config:
    token: str
    secret: str

    def __init__(self, token, secret):
        self.token = token
        self.secret = secret
