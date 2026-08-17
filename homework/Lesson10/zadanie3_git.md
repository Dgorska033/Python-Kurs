PS D:\Python Kurs> mkdir konflikt-git


    Directory: D:\Python Kurs


Mode                 LastWriteTime         Length Name                                                                                                                           
----                 -------------         ------ ----                                                                                                                           
d-----         9.08.2026     16:56                konflikt-git                                                                                                                   


PS D:\Python Kurs> cd konflikt-git
PS D:\Python Kurs\konflikt-git> git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: will change to "main" in Git 3.0. To configure the initial branch name
hint: to use in all of your new repositories, which will suppress this warning,
hint: call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
hint:
hint: Disable this message with "git config set advice.defaultBranchName false"
Initialized empty Git repository in D:/Python Kurs/konflikt-git/.git/
PS D:\Python Kurs\konflikt-git> New-Item konflikt.txt


    Directory: D:\Python Kurs\konflikt-git


Mode                 LastWriteTime         Length Name                                                                                                                           
----                 -------------         ------ ----                                                                                                                           
-a----         9.08.2026     16:58              0 konflikt.txt                                                                                                                   


PS D:\Python Kurs\konflikt-git> code konflikt.txt
PS D:\Python Kurs\konflikt-git> git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        konflikt.txt

nothing added to commit but untracked files present (use "git add" to track)
PS D:\Python Kurs\konflikt-git> git add konflikt.txt
PS D:\Python Kurs\konflikt-git> git commit -m "Dodano pierwszą linię tekstu"
[master (root-commit) bf25df3] Dodano pierwszą linię tekstu
 1 file changed, 1 insertion(+)
 create mode 100644 konflikt.txt
PS D:\Python Kurs\konflikt-git> git branch zmiana-a
PS D:\Python Kurs\konflikt-git> git branch zmiana-b
PS D:\Python Kurs\konflikt-git> git branch
* master
  zmiana-a
  zmiana-b
PS D:\Python Kurs\konflikt-git> get switch zmiana-a
get : The term 'get' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify tha
t the path is correct and try again.
At line:1 char:1
+ get switch zmiana-a
+ ~~~
    + CategoryInfo          : ObjectNotFound: (get:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS D:\Python Kurs\konflikt-git> git switch zmiana-a
Switched to branch 'zmiana-a'
PS D:\Python Kurs\konflikt-git> git status
On branch zmiana-a
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   konflikt.txt

no changes added to commit (use "git add" and/or "git commit -a")
PS D:\Python Kurs\konflikt-git> 
PS D:\Python Kurs\konflikt-git> git add konflikt.txt
PS D:\Python Kurs\konflikt-git> git commit -m "feat: dodano zmianę na gałęzi A"
[zmiana-a 280f1aa] feat: dodano zmianę na gałęzi A
 1 file changed, 1 insertion(+), 1 deletion(-)
PS D:\Python Kurs\konflikt-git> git switch master
Switched to branch 'master'
PS D:\Python Kurs\konflikt-git> git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   konflikt.txt

no changes added to commit (use "git add" and/or "git commit -a")
PS D:\Python Kurs\konflikt-git> git add konflikt.txt
PS D:\Python Kurs\konflikt-git> git commit -m "feat: Dodano zmianę na poziomie master"
[master 33f11f3] feat: Dodano zmianę na poziomie master
 1 file changed, 1 insertion(+), 1 deletion(-)
PS D:\Python Kurs\konflikt-git> git merge zmiana-a
Auto-merging konflikt.txt
CONFLICT (content): Merge conflict in konflikt.txt
Automatic merge failed; fix conflicts and then commit the result.
PS D:\Python Kurs\konflikt-git> git add konflikt.txt
PS D:\Python Kurs\konflikt-git> git status
On branch master
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        modified:   konflikt.txt

PS D:\Python Kurs\konflikt-git> git commit -m "merge: rozwiązano konflikt w konflikt.txt"
[master 1977f42] merge: rozwiązano konflikt w konflikt.txt
PS D:\Python Kurs\konflikt-git> git status
On branch master
nothing to commit, working tree clean
PS D:\Python Kurs\konflikt-git> 