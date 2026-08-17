PS D:\Python Kurs> git clone https://github.com/Dgorska033/Python-mini-project.git                  
Cloning into 'Python-mini-project'...
warning: You appear to have cloned an empty repository.
PS D:\Python Kurs> cd Python-mini-project
PS D:\Python Kurs\Python-mini-project> projekt.md
projekt.md : The term 'projekt.md' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was includ
ed, verify that the path is correct and try again.
At line:1 char:1
+ projekt.md
+ ~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (projekt.md:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS D:\Python Kurs\Python-mini-project> New-Item projekt.md


    Directory: D:\Python Kurs\Python-mini-project


Mode                 LastWriteTime         Length Name                                                                                                                           
----                 -------------         ------ ----                                                                                                                           
-a----         9.08.2026     12:29              0 projekt.md                                                                                                                     


PS D:\Python Kurs\Python-mini-project> code projekt.md 
PS D:\Python Kurs\Python-mini-project> git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        projekt.md

nothing added to commit but untracked files present (use "git add" to track)
PS D:\Python Kurs\Python-mini-project> git add projekt.md
PS D:\Python Kurs\Python-mini-project> git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   projekt.md

PS D:\Python Kurs\Python-mini-project> git commit -m "docs: dodano opis projektu"
[main (root-commit) fe52531] docs: dodano opis projektu
 1 file changed, 22 insertions(+)
 create mode 100644 projekt.md
PS D:\Python Kurs\Python-mini-project> git switch -c feature-readme
Switched to a new branch 'feature-readme'
PS D:\Python Kurs\Python-mini-project> git branch
* feature-readme
  main
PS D:\Python Kurs\Python-mini-project> 
                                             
PS D:\Python Kurs\Python-mini-project> git status
On branch feature-readme
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   projekt.md

no changes added to commit (use "git add" and/or "git commit -a")
PS D:\Python Kurs\Python-mini-project> git add projekt.md
PS D:\Python Kurs\Python-mini-project> git commit -m "docs: dodano opis grupy docelowej"
[feature-readme 8f3e63c] docs: dodano opis grupy docelowej
 1 file changed, 3 insertions(+)
PS D:\Python Kurs\Python-mini-project> git push -u origin feature-readme
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 905 bytes | 905.00 KiB/s, done.
Total 6 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/Dgorska033/Python-mini-project.git
 * [new branch]      feature-readme -> feature-readme
branch 'feature-readme' set up to track 'origin/feature-readme'.
PS D:\Python Kurs\Python-mini-project> git branch -a
* feature-readme
  main
  remotes/origin/feature-readme
PS D:\Python Kurs\Python-mini-project> git push -u origin main
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'main' on GitHub by visiting:
remote:      https://github.com/Dgorska033/Python-mini-project/pull/new/main
remote: 
To https://github.com/Dgorska033/Python-mini-project.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
PS D:\Python Kurs\Python-mini-project> git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
PS D:\Python Kurs\Python-mini-project> git pull
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (1/1), 913 bytes | 130.00 KiB/s, done.
From https://github.com/Dgorska033/Python-mini-project
   fe52531..8e7964f  main       -> origin/main
Updating fe52531..8e7964f
Fast-forward
 projekt.md | 3 +++
 1 file changed, 3 insertions(+)
PS D:\Python Kurs\Python-mini-project> git branch -d feature-readme
Deleted branch feature-readme (was 8f3e63c).
PS D:\Python Kurs\Python-mini-project> git branch
* main
PS D:\Python Kurs\Python-mini-project> git push origin --delete feature-readme
To https://github.com/Dgorska033/Python-mini-project.git
 ! [remote rejected] feature-readme (refusing to delete the current branch: refs/heads/feature-readme)
error: failed to push some refs to 'https://github.com/Dgorska033/Python-mini-project.git'
PS D:\Python Kurs\Python-mini-project> git push origin --delete feature-readme
error: unable to delete 'feature-readme': remote ref does not exist
error: failed to push some refs to 'https://github.com/Dgorska033/Python-mini-project.git'
PS D:\Python Kurs\Python-mini-project> git branch -a
* main
  remotes/origin/HEAD -> origin/feature-readme
  remotes/origin/feature-readme
  remotes/origin/main
PS D:\Python Kurs\Python-mini-project> git fetch --prune
From https://github.com/Dgorska033/Python-mini-project
 - [deleted]         (none)      -> origin/feature-readme
   refs/remotes/origin/HEAD has become dangling after refs/remotes/origin/feature-readme was deleted
 * [new branch]      branch-main -> origin/branch-main
PS D:\Python Kurs\Python-mini-project> git branch -a
* main
  remotes/origin/branch-main
  remotes/origin/main
PS D:\Python Kurs\Python-mini-project> 

