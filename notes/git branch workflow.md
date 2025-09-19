# git branching strategy
## The main Gold 
main is the stable branch if you have master you should update your git to the newset version
## THe standard worflow
The `main` branch is always stable and deployable. All new work is done on **feature branches**.

1. **start from an update main:**
    ```bash
    git checkout main
    git pull origin main
    ```
    2.  **Create a new feature branch:**
    ```bash
    # Use a descriptive name with a prefix
    git checkout -b feat/user-authentication
    # or: fix/header-styling
    # or: docs/update-readme
    ```

3.  **Do your work, add, and commit:**
    ```bash
    git add .
    git commit -m "feat: add login form with validation"
    ```
4.  **Push your branch and create a PR:**
    ```bash
    git push -u origin feat/user-authentication
    # Then go to GitHub to open a Pull Request 
    # or merge locally 
    git checkout main
    git pull origin main
    git merge feat/new-button
    ```

5.  **After PR is merged, clean up locally:**
    ```bash
    git checkout main
    git pull origin main # Get the merged code
    git branch -d feat/user-authentication # Delete the old branch
    ```
    ## Branch Naming Conventions
- `feat/`: A new feature
- `fix/`: A bug fix
- `docs/`: Documentation changes
- `chore/`: Maintenance tasks (e.g., updating config files)