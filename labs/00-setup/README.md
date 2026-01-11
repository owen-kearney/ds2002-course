# Lab 00: Setup

The goal of this activity is to get you comfortable with starting up Codespaces for your exercises, labs, and project, and to familiarize you with the process of submitting your work for grading.

## Setup

You can use the  <a href="https://github.com/codespaces/" target="_new"><b>GitHub Codespaces</b></a>for these exercises. Open that page and click on "New Codespace" and select your ***forked course repository*** repository.

> If you haven'f created the fork yet, go to Codespaces as described in the [courses general setup instructions](../../setup/README.md) file. 

**Advanced: Optional** - If you set up software tools on your own computer, for an additional challenge, complete these exercises on your local laptop using either the MacOS Terminal (Mac) or Git Bash (Windows). You may need to modify some commands accordingly.

## Instructions:

1. Start up Codespaces: On GitHub go to your forked repository, click the green **Code** button
2. Select the **Codespaces** tab
3. Click **Create codespace on main** (or select a branch)
4. GitHub will automatically detect and use the default devcontainer configuration
5. Wait for the codespace to initialize (this may take a few minutes)
6. Once your codespace is running, open the terminal. The terminal will show at the bottom of your Codespaces window.
   ![Terminal in Codespaces](../../docs/images/codespaces-terminal.png)
7. In the terminal window, enter this command and hit <Enter>/<Return>:

8. Check the hostname of your system:
   ```bash
   hostname
   ```
   
   The output should look similar to this:
   ```bash
   codespaces-57da94
   ```

9.  Post the output in the class poll (url will be shared in class). 

10. **Optional** - On your own computer

    If you have a terminal application installed on your own computer and run the `hostname` command there.


11. Submit your work on Canvas

- Create a secret Gist (a special kind of GitHub repository), name it "Lab-00-YOUR_COMPUTING_ID" (replace with your actual computing ID) as described in [Submitting Labs instructions](## Submitting Labs).
- In your Gist, create a new text file `submission.txt`
- In the submission.txt file, add on three lines the following information
```bash
Computing id: <your computing id>
GitHub username: <your GitHub username>
hostname: <the output from the hostname command above>
```  
- Copy and Paste the Gist URL to the Lab assignment in Canvas.

**Congratulations! You are all set for the next class activities.**

