#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 to run this script."
    exit 1
fi

# Run the Python script
python3 instruction_selection.py