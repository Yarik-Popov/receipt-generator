# hack-the-change-2023
Hack the Change 2023 Repo for the Dr.Racket team
## Introduction
The goal of the project is helping people to get rid of waste of food. The webapp could let you make a meal with the ingredients that almost expired in your fridge. ChatGPT will tell you what to make by them.
## Style guide
We will be following the Python style guide
- Variables and functions are snake case `my_var` `my_func()`
- Classes are upper pascal case `MyClass`
- Constants are upper snake case `MY_CONSTANT`
- The only things that should be in global scope are imports (this is the only place they should be), function and class declarations, global variables and constants. No running code that produces side-effects should be in global scope

## Branches
- Branches should be small and merged in quickly
- Convention `<name>/<feature>`. Ex: `yarik/cool-feature`

## Environment
- Create a python environement by running `python3 -m venv .venv`
- Source it `source .venv/bin/activate` on Mac/Linux/WSL
- Run `pip install -r requirements.txt`
