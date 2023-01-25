# Git usefull cmds

### Good looking git log
```git log --pretty=oneline```
```
18b0840bd1096732d5c31fe73453bf2530d5214e (HEAD -> main) 21_12_2022 - day00_b 
920ce7282d192599c359d5f76e02ce70282ff2b5 21_12_2022 - day00_a  
9d448caa86c8c97d36f0766fe5c5faba5c307b53 21_12_2022 - day00
```

### Squash/merge two last commits to one
https://stackoverflow.com/a/2568581  
```git rebase --interactive HEAD~2```