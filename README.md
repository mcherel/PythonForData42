# PythonForData42

## FLAKE8
```sh
pip uninstall flake8
pip install flake8
```

Determine the installation path: Confirm the path where flake8 is installed:

```sh

ls ~/.local/bin | grep flake8

```

Add to PATH: If flake8 is located in ~/.local/bin, you can add this directory to your PATH. Open your shell configuration file (.bashrc, .zshrc, etc.) and add the following line:

```sh

export PATH=$PATH:~/.local/bin
```
Reload the shell configuration: After updating your configuration file, reload it:

```sh

source ~/.bashrc  # or source ~/.zshrc
```
Verify: Check if flake8 is now accessible:

```sh

    flake8 --version
```
If it’s still not working, you can always use flake8 as a Python module to lint your files:

```sh

python -m flake8 ex00/
```