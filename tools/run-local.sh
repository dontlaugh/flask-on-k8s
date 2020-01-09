#!/bin/bash

export DEBUG="true"
export MONGO_URI="mongodb://testuser:testpassword!@127.0.0.1:27017/db"
python app.py
