#!/usr/bin/env python
from fastapi import FastAPI
import dotenv

dotenv.read_dotenv()
app = FastAPI()
