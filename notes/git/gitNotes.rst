### Changing to a remote directory

> git checkout --track -b <remote-branch>
 You can ommit the --track, the important one is the -b the --track is to allow you to fetch new changes or to push

### Creating a pull request to vauxoo-dev

> git clone vauxoo <branch_name>
> git checkout -b <your_branch_name>
> git push vauxoo-dev <your_branch_name>


### To delete those anoying branches

git branch -d -r remote/branch
