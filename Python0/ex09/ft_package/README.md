Create your first package in python the way you want, it will appear in the list of
installed packages when you type the command "pip list" and display its characteristics
when you type "pip show -v ft_package"
```
pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/eagle/ft_package
Author: eagle
Author-email: eagle@42.fr
License: MIT
Location: /home/eagle/...
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
```
The package will be installed via pip using one of the following commands (both
should work):
•pip install ./dist/ft_package-0.0.1.tar.gz
•pip install ./dist/ft_package-0.0.1-py3-none-any.whl
Your package must be able to be called from a script like this one:
from ft_package import count_in_list
```
print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```


### Étapes pour Gérer le Package

1. **Créer les distributions :**
    
    ```bash
    python setup.py sdist bdist_wheel
    
    ```
    
2. **Installer le package localement :**
    
    ```bash
    pip install ./dist/ft_package-0.0.1.tar.gz
    # ou
    pip install ./dist/ft_package-0.0.1-py3-none-any.whl
    
    ```
    
3. **Vérifier l'installation :**
    
    ```bash
    pip list
    pip show -v ft_package
    
    ```
    
4. **Tester le package avec un script :**
    
    Créez un fichier `test_script.py` :
    
    ```python
    # test_script.py
    
    from ft_package import count_in_list
    
    print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
    print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
    
    ```
    
    Exécutez le script :
    ```
    python3 test_script.py
    ```
