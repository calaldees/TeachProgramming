Version Control
===============

1. Create a github account
2. Create a repository
    1. Create a repo on github `myTest`
    2. Open the repo with gitpod online environment `https://gitpod.io#PASTE_REPO_URL_HERE`
    3. Create a markdown file with a shopping list (e.g. `shopping.md`?)
        * ```markdown
            * eggs
            * bacon
            * cheese
            * flour
            ```
    4. Track the file with `git add shopping.md` [KEY CONCEPT 1: Files must be 'tracked' to be version controlled]
    5. `git commit -a` - enter a message - (check github web - has it updated?) [KEY CONCEPT 2: every commit has a description of the change]
    6. `git push` (check github web - has it updated?) [KEY CONCEPT 3: You have a copy of the repo locally, this needs to be pushed upstream]
    7. Look at the commit history
3. Branch
    1. create a `git branch test1`
    2. see branches with `git branch`
    3. change branch `git checkout test1`
    4. see branches with `git branch`
    5. Add an item to `shopping.md`
    6. `git status` to see the overview of files
    7. `git diff` to see the changes [KEY CONCEPT 5: You can see your changes]
    8. `git commit -a` and `git push`
    9. Check github web - branches dropdown (is your branch there?)
    10. change branch `git checkout main`
    11. Check the shopping list was as it was before
    12. change branch `git checkout test1`
    13. Check the shopping list has your addition [KEY CONCEPT 6: You can switch between multiple branches in different states]
4. Another Branch
    1. `git checkout main`
    2. create a new branch `git branch test2`
    3. Add an item to `shopping.md`
    4. `git commit -a` and `git push` [KEY CONCEPT 7: You can have any number of branches]
5. Merge both branches into main
    1. `git checkout main`
    2. `git merge test1`
    3. `git merge test2`
    4. resolve the merge conflict - remove all the added guff [KEY CONCEPT 8: some conflicts must be explicitly be resolved by humans]
    5. `git commit -a` and `git push`
6. Pull request
    1. create a `fork` of another classmates repository (find it on github and click fork in top right) [KEY CONCEPT 9: You can easily copy and build on top of others work]
    2. Open the repo with gitpod online environment `https://gitpod.io#PASTE_FORKED_REPO_URL_HERE`
    3. Make a change
    4. `git commit -a` and `git push`
    5. Use Github to create a `pull request` to request they add your change - see what it looks like [KEY CONCEPT 10: You have tools to integrate your changes with the original work]

* Version control is the cornerstone of all software collaboration
* Many online services support github integration `repl.it`, `hack.md`
* `GitHub.com` and `GitLab.com` are just a websites - `git` is the version control system - you can use git without ever touching github
* I have shown your the full command line use of git - there are many graphical tools to support this flow - can these concepts be used for students to collaborate?
