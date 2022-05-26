# apim-data-populator

1. Create tenants, roles, users
2. Add scope assignments for roles
3. Add api categories
4. Add rate limiting policies

## System Requirements
You need the latest versions of `Python` and `PIP` installed in your machine. Then run these commands using pip to install required python packages.

`pip install json`  
`pip install base64`  
`pip install requests`  

## Getting Started

1. Download the source code using the command `git clone https://github.com/binodmx/apim-data-populator.git`
2. Check `config.py` file to change configurations according to APIM version you are using
3. Make sure APIM is up and running
4. Run `python run.py` command to populate data
