

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.coderbridge.com%2Fimg%2Ftechbridge%2Fimages%2Fhuli%2Fhacktoberfest.png&f=1&nofb=1)

# Fun With Python

![](https://img.shields.io/github/stars/ManthanShettigar/FunWithPython) ![](https://img.shields.io/github/watchers/ManthanShettigar/FunWithPython) ![](https://img.shields.io/github/forks/ManthanShettigar/FunWithPython)

> This is a collection of scripts, games, bots, scraper and tools written in python


### Project List 
- [**blackjack game**](/black_jackgame)
- [**coffee machine**](/coffeemachine)
- [**guess the number**](/guess_the_number)
- [**higherlowergame**](/higherlowergame)
- [**random password generator**](/random_password_generator)
- [**Rock Paper Scissor**](/rock_paper_scissor)
- [**Anime quote generator**](/anime_quote_generator)
- [**gesture volume control**](/gesture_volume_control)
- [**heart disease prediction**](/Heart_Disease_Prediction)
- [**Flappy Bird**](/Flappy-Bird )

### Prerequisite
- [Python3+](https://www.python.org/)


### Workflow for execution
###### Steps
1. Clone the repository
2. Change to any project directory
3. Execute the python script
Example:
```shell
git clone https://github.com/ManthanShettigar/FunWithPython.git
cd FunWithPython/black_jackgame
python blackjack.py
```



### Workflow for contribution
###### Steps
1. Star and fork the repository.
2. Clone the repositry
``` 
git clone https://github.com/<YourUserName>/FunWithPython
```

3. Add a remote for the original repository.
``` 
git remote add upstream https://github.com/ManthanShettigar/FunWithPython.git
```
4. Navigate to the project and create a branch.
```
cd FunWithPython
git checkout -b <branch name>
```
5. Add/Make the required changes and **always fetch upstream changes _to avoid merge conflicts_**
```
git pull upstream master
```
6. Commit the changes.
```
git add <file name(s)>
git commit -m "Change Message"
```
7. Push it to your repository
```
git push origin <branch name>
```
8. Once pushed. check your repository.
9. Clicking on contribute button you can open a **```pull request```**.
10. Fill the details and click on **```Create pull request```**.

# FAQ!

    1.Why do merge confilcts occur

>Ans. Suppose you forked the repository, now some other contributor who forked the same repository did some changes and added a PR , the maintainer will check it and finding no visible issues, will merge the PR to the main branch now the repository on your profile is frozen, the updates on the original repository don't reflect on the forked repository of your profile hence dont reflect on your local machine sice you cloned it before the changes.
now since you create changes of your own in your local machine, and try to create a PR there will be a merge conflict because the original repository is ahead some changes which are not pulled down and implemented on your local machine,that is the reason of merge conflcits.


    2. how to avoid merge conflicts ?

> when you fork the repository there is a remote usually called **'origin'** that is referencing to the forked repository on your profile. you have to add another remote usually called **"upstream"** that references the original repository , now before making any changes of your own,  pull down changes made in the original repository using the command ` git pull upstream master` and then the changes are reflected in your local machine now you can add changes and commit them _CONFLICT-LESSLY._

    3. do we create another feature branch or work on the main branch?

> Yes,create a feature branch and work on that branch, don't make changes to the main/master branch.