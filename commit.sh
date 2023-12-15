#!/bin/bash

# Demande à l'utilisateur d'entrer le message de commit
read -p "Entrez le message de commit: " commit_message

# Ajoute tous les fichiers modifiés à l'index Git
git add -A

# Effectue le commit avec le message fourni
git commit -m "$commit_message"

# Pousse les modifications vers le dépôt distant
git push

echo "Les modifications ont été poussées avec succès."
