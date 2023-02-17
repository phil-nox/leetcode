# Git usefull cmds

### 🔻 Good looking git log
```git log --pretty=oneline```

```
    18b0840bd1096732d5c31fe73453bf2530d5214e (HEAD -> main) 21_12_2022 - day00_b 
    920ce7282d192599c359d5f76e02ce70282ff2b5 21_12_2022 - day00_a  
    9d448caa86c8c97d36f0766fe5c5faba5c307b53 21_12_2022 - day00
```

```git status; git log --format="%C(auto) %h %s"```
```
     e8bf2de 2023_02_17 - 927__ - easy - 783 <<< DFS - InOrder
     9b0b99a 2023_02_16 - 928__ - easy - 104 <<< nice_code for BFS thx_2_Tanya
```
---

### 🔻 Squash/merge two last commits to one
https://stackoverflow.com/a/2568581  
```git rebase --interactive HEAD~2```
---

### 🔻 Fixup old commit (like add missing file)
https://stackoverflow.com/a/3828861
```
git add ...                           # Stage a fix
git commit --fixup=a0b1c2d3           # Perform the commit to fix broken a0b1c2d3
git rebase -i --autosquash a0b1c2d3~1 # Now merge fixup commit into broken commit
```
---


### 🔻 Look at old commit and back
```
git checkout 4298cd7            # detaching HEAD & switching to '4298cd7'
git diff --name-only HEAD^      # diff list of files with prev commit
git switch -                    # switching to original state
```
---

