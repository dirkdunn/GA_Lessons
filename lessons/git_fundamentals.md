# Git Fundamentals

### LEARNING OBJECTIVES
**After this lesson, you will be able to:**  

- Explain what version control is
- Explain why developers use version control
- Explain the process of how git works
- Distinguish between local and remote repositories
- Understand basic git commands like init, add, commit, push, pull and clone  
- Create remotes and push to them   
- Create a repository on Github
- Describe how branching and merging allows for collaboration during development
- Create, checkout, and merge branches
- Explain how remotes work
- Clone remote repositories  

***
### What is Version Control?

* Version Control is used to manage the changes to documents, computer programs, web sites, and other collections of information.
* Version Control provides:
    - a database containing a history of changes to a set of files
    - a set of commands for managing that database

### What is Version Control Good For?

* Manage Changes Over Time  
    - Save various points in the development of your work  
    - Let's us view the changes we've made over time 
    - Manage multiple versions of a software project  
* Sharing & Collaboration  
    - Share your work with other developers 
    - Work effectively as a team on a single project  
    - Allow others to modify your work in a controlled way  
    - Make multiple changes to a project in parallel  
    - Merge parallel changes in a controlled way  
* Experimentation  
    - Experiment with various ideas and either keep or discard your experiments  
    - Keep multiple changes isolated until they are ready to be integrated  

***

> Instructor Note:  On the whiteboard, draw a diagram of the following:
- working area  
- stage  
- git repository (.git)  

### Visualizing the Workflow
Git is a program that resides on our computers. When used on a project, it creates a database locally that stores our code and changes that we've made to it over time.

That local database is called a "local repository"

We also have the ability to send these changes to other places, so that other developers can pull this code to their own computers and make their own modifications to it, and then merge it back up to that place.

The place that we send the code is called the "remote repository"

<figure>
  <img src="https://www.git-tower.com/learn/content/01-git/01-ebook/en/01-command-line/04-remote-repositories/01-introduction/basic-remote-workflow.png" alt="Local and remote">
  <br>
  <figcaption>The table below has all of the key words from this diagram bolded. </figcaption>
</figure>

### Git Basics
Let's go through this list of commands, and see what they do on a conceptual level.

| Action | Command |
| :--- | :--- |
| Create new git repository | `git init` |
| Copy (**clone**) an existing repository from the internet (remote) onto your computer (local)| `git clone <repo url>`|
| Check status of git repo | `git status` |
| Check differences since last commit | `git diff <filename>` |
| Add file to git repo (**stage** for commit) | `git add <filename>` |
| Add (**stage**) all edited files in the current directory | `git add .` |
| **Commit** (save) a version into the local repository | `git commit -m "message describing changes"` |
| **Push** commits to GitHub (remote repository) | `git push <remote> <branch>` |
| **Pull** commits from the remote repository | `git pull <remote> <branch>` |
| Show version history | `git log <filename>` |
| Get help with git commands | `git help <command>` |

> Instructor Note: Using the diagram, go through each of the above commands, and show what happens when we use them.

### Initial Setup

Check if Git exists:
```
$ git
```

Check your Git Config:
```
$ git config --list
$ git config user.name
```

Set your identity:
```
$ git config --global user.name "John Doe"    
$ git config --global user.email johndoe@example.com
```

### Creating a repo on Github

Although this lesson will not be focusing on Github, we are going to set up a "remote repository".
![Creating a repository](https://content.screencast.com/users/ddunn91/folders/Jing/media/1daab91b-a632-4cbb-be01-3ea3db666280/00000036.png)

1. Click on the "+" icon in the header bar to the right.
2. Fill out the information about the repository

That's it, we've created a repository. Now let's go over how to communicate with it over Git on our command line

> The distinguishment between Git and Github is very important. **Git** is the tool that we use to track and move our files. **Github** is simply where we are storing these files.

### Creating a local repo
Create a new local Git repository:

```
$ cd ~/ga/wdi/exercises/learning-git
$ mkdir sample1  
$ cd sample1  
$ git init
```

* What just happened?
* Did your Shell Prompt change?

### Connecting our local repo to the remote
```
$ git remote add origin <URI>
```

* What's happening here?
What we did here is tell our local repository where our remote repository is located.

### Our first commit

Add some files:

```
$ touch README.md hello.txt  
$ git status                  # What is an untracked file?
$ git add -A                  # Now the files are in the stage
$ git status
```

Commit the changes:

```
$ git commit -m "Added 2 files."
$ git status
$ git log
```

We've just done two things here:

1. We have staged all files that have been modified since the last commit
2. We have saved those changes into our local repository.


### Pushing to the remote repository

Now that we have saved these changes to the local repository, we can replicate, or **"push"** these same changes to a git repository located somewheres else.

```
$ git push origin master
```

The syntax for this is: `git push <remote> <branch>`, the "git push" command wants to know two things, where to send the changes, and which branch to send it down. The remote we named "origin" that we added earlier is this address, and "master" is our default branch.

> Instructor note: view these changes up on github, show what happened once we pushed our code.

That was a lot of information! Let's get some practice by playing a git simulation game.
[Code School: Try Git](https://try.github.io/)

<!--- Describe how branching and merging allows for collaboration during development) -->

### Branching and merging
What if we want to build a feature into our program, but we don't want it to be in our main code until it's **perfecto**?

What if two developers are working on two seperate things that could conflict with eachother at the same time?

This is where branching comes in. Branching in Git allows us to "break off" where we currently are in our program to **seperate workspace**, where we can make our new modifications, without disrupting our main codebase. Check it out:

![Git Branch](https://i.stack.imgur.com/eCgrM.png)

> Instructor note: draw and explain this timeline on the board.

As Git monitors the changes we have made over time to our software, we can model it in our heads as a timeline, like such above, with each dot across the timeline being a **commit** to the code.

By default, when we create a repository, we are given one branch by default that git monitors our changes on, this is called the **master** branch, you can think of this as the main timeline of our code's history.

We can achieve branching with the following command:

```
$ git branch <branchname>
```
This command will create a new branch in git. We can then switch to that branch with the checkout command:

```
$ git checkout <branchname>
```

Or, alternatively:
```
$ git checkout -b branchname
```
this command will create a new branch in git, and then switch to that branch, all in one command.

**Cloning Repositories**
So far we have set up our repository from scratch, however, this isn't always the case. Sometimes we want to take an existing remote repository and bring it onto our computer locally.

The last thing we will do in this lesson is clone our WDI-10 class repo to our home directory in our filesystem.
```
$ git clone <URI>
```

<a name="conclusion"></a>
## Conclusion (15 mins)
* Review Git Terminology:
    - repository - a collection of related commits that form a directed acyclic graph
    - commit - a snapshot of the working tree at a giving time (along with a message of what changed)
    - the index (stage) - a staging area where we list changes we want to commit
    - branch - a set of commits that form a linear progression of changes
    - master - the default name for the "main" development branch
    - tag - an optional label on a commit
    - HEAD - what is currently checked out
    - working area - the directory and subdirectories containing the files we are currently working on
* Review Questions:  
    - Can someone tell me what a Git Repository is?
    - What are some key components of a Git repo?
    - Can someone describe an important Git command (get several responses from students)

***

### Hungry for More?
#### References
- [Git Cheat Sheet](https://raw.githubusercontent.com/ATL-WDI-Curriculum/local-and-remote-git/master/images/Git-Cheat-Sheet.png)
- [Github Pages](https://pages.github.com/)
- [Jekyll](https://jekyllrb.com/)

#### Readings
- [Git Documentation](https://git-scm.com/documentation)
- [Forking on Github](https://help.github.com/articles/fork-a-repo/)
- [Syncing a fork](https://help.github.com/articles/syncing-a-fork/)

#### Videos
- [Lynus Travalds on Git](https://www.youtube.com/watch?v=4XpnKHJAok8)
