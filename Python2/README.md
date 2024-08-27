mkdir venv: Cette commande crée un nouveau répertoire appelé venv dans le répertoire actuel. Ce répertoire servira de conteneur pour notre environnement virtuel.

cd venv: Cette commande change le répertoire de travail actuel pour le nouveau répertoire venv que nous venons de créer.

ls: Cette commande liste le contenu du répertoire venv. Comme nous venons de créer ce répertoire, il est actuellement vide, donc aucune sortie n'est affichée.

python -m venv .venv: Cette commande utilise le module venv de Python pour créer un nouvel environnement virtuel dans un répertoire caché appelé .venv (commençant par un point) dans le répertoire actuel. L'option -m est utilisée pour exécuter le module en tant que script. Cela crée une copie isolée de l'interpréteur Python ainsi que d'autres fichiers nécessaires pour l'environnement virtuel.

source .venv/bin/activate: Cette commande active l'environnement virtuel en exécutant le script d'activation situé dans le répertoire .venv/bin/. L'activation de l'environnement virtuel ajuste les variables d'environnement telles que PATH pour que les commandes Python pointent vers les exécutables de l'environnement virtuel au lieu de ceux du système global. Cela signifie que lorsque vous exécutez des commandes Python, elles seront exécutées à l'intérieur de l'environnement virtuel, isolées du système global.

pip install -U pip: est utilisée pour mettre à jour le gestionnaire de paquets pip lui-même sur votre système Python.

pip freeze > requirements.txt: vous créez un fichier texte appelé "requirements.txt" qui contient une liste des packages Python installés dans votre environnement, avec leurs versions correspondantes. Cela peut être utile pour partager la configuration de votre environnement avec d'autres personnes ou pour créer une spécification de dépendances pour votre projet.

pip install -r requirements.txt: est utilisée pour automatiser l'installation de tous les packages requis pour un projet Python, en se basant sur une liste spécifiée dans un fichier "requirements.txt". Cela facilite la gestion des dépendances du projet et assure une reproductibilité cohérente de l'environnement de développement.