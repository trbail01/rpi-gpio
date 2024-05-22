#!/bin/bash

# Create a Python virtual environment named myenv
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install the RPLCD package
pip install RPLCD

# Notify the user
echo "Virtual environment 'myenv' created and RPLCD installed."

# Keep the virtual environment activated for further use
exec "$SHELL"
