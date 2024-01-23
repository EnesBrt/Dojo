#!/bin/bash

# Fonction pour effectuer le commit et le push
perform_git_operations() {
    local commit_message=$1

    # Ajoute tous les fichiers modifiés à l'index Git
    git add -A

    # Effectue le commit avec le message fourni
    git commit -m "$commit_message"

    # Pousse les modifications vers le dépôt distant
    git push

    echo "Les modifications ont été poussées avec succès."
}

# Demande à l'utilisateur d'entrer le message de commit
read -p "Entrez le message de commit: " commit_message

# Appelle la fonction avec le message de commit
perform_git_operations "$commit_message"
