#!/bin/bash
    SOURCE_BRANCH="feat/architecture-report"

    # Ottiene le branch, pulisce gli spazi e rimuove la branch sorgente
    BRANCHES=$(git branch | sed 's/*//g' | grep -v "$SOURCE_BRANCH")

    git checkout "$SOURCE_BRANCH"

    for branch in $BRANCHES; do
      branch=$(echo "$branch" | xargs)
      echo "----------------------------------------"
      echo "Aggiornamento su: $branch"
      
      git checkout "$branch"
      git checkout "$SOURCE_BRANCH" -- .github
      
      if [[ -n $(git status --porcelain .github) ]]; then
        git add .github
        git commit -m "ci: aggiornamento automatico configurazioni .github"
        git push origin "$branch"
        echo "✓ Branch $branch aggiornata!"
      else
        echo "– La branch $branch è già allineata."
      fi
    done

    git checkout "$SOURCE_BRANCH"
    echo "----------------------------------------"
    echo "Fatto! Tutto aggiornato."
    ```
    Salva e chiudi il file.
  
  
    Ora torna sul tuo terminale Git Bash e lancia nuovamente il comando:
    ```bash
    ./copy_everywhere.sh
    ```