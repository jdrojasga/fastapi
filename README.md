### Installation
The next steps being executed in the terminal, and you have to be in the source folder of this repo.
1. Install [uv](https://github.com/astral-sh/uv). 
```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```
2. Create a virtual environment in which you will install all the dependencies required in the project: 
```bash 
uv venv .venv
```
3. Activate the virtual environment 
```bash 
source .venv/bin/activate
```
4. Install the project to be able to execute the custom command line: 
```bash 
uv pip install -e .
```
5. Test that everything is working 
```bash 
uv run api
``` 
or 
```bash 
api
```
6. If you want to deactivate the environment just execute:
```bash 
deactivate
```

When you are working in VSCode and need to configure a Python interpreter to execute anything, just select the virtual environment created with uv help: ```('.venv': venv)```.