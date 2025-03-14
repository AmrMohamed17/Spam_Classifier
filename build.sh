#!/bin/bash
# Install only necessary packages with minimal dependencies
pip install --no-cache-dir -r requirements.txt --no-deps
pip install --no-cache-dir numpy==1.21.4
pip install --no-cache-dir scipy==1.7.3 --no-deps