#!/usr/bin/env python
from fastapi import FastAPI
from dotenv import read_dotenv

read_dotenv()
app = FastAPI()
