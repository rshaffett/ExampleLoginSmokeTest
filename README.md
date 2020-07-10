# ExampleLoginSmokeTest
Automation Tests for VoterVoice Login Page
## Quick Start
*If you have Python version 3 setup already then ignore the guides else please refer to the guides below for setting up python.*

## Step 1: Get the Project/Repo on Local Machine
1. To keep the setup from being too lengthy outside of getting python setup we are just going to download the repo to a destination on your machine via the Download Zip option on the Code dropdown.

## Step 2: Navigate to the Repo on Local Machine in Terminal
1. I would recommend typing in the Command Prompt/Terminal ```cd path\to\where\repo\is\LoginSmokeTest\```

## Step 3: Installing All Required Packages
1. Inside of the directory that has been navigated to, we will need to run the following ```python3 -m pip install -r requirements.txt```

## Step 4: Creating File to Store Environment Variables For Use in Tests
1. Create a file a file in the project directory either manually called ```.env``` or via the Terminal with ```touch .env```
2. Add to the file manually the username and password or by ```nano .env``` and insert:
   ```
   VUSER=<UserName>
   PASS=<Password>
   ```
3. Save and exit the file manually or press ```Ctrl + X``` and then type ```Y``` and hit ```Enter```.

## Step 5: Running the Tests
1. After installing all the dependencies, run the command ```python3 pytest login_smoke_tests.py```

## Step 6: Checking the Results
1. Once Pytest has successfully finished running, inside of the project directory will be a text file called ```results.txt```. This will contain the test results for the 5 login tests.


## Python Setup Install Instructions

## For Windows

### Step 1: Download the Python 3 Installer

1. Open a browser window and navigate to the [Download page for Windows] (https://www.python.org/downloads/windows/) at python.org.
Underneath the heading at the top that says Python Releases for Windows, click on the link for the Latest Python 3 Release - Python 3.x.x. 
2. Scroll to the bottom and select either Windows x86-64 executable installer for 64-bit or Windows x86 executable installer for 32-bit. 

![alt text](https://phoenixnap.com/kb/wp-content/uploads/2019/04/python-for-windows.png)

### Step 2: Run the Installer

1. Once you have chosen and downloaded an installer, simply run it by double-clicking on the downloaded file. A dialog should appear that looks something like this:

**Important: You want to be sure to check the box that says Add Python 3.x to PATH as shown to ensure that the interpreter will be placed in your execution path.**

![alt text](https://phoenixnap.com/kb/wp-content/uploads/2019/04/python-setup.png)

2. Then just click Install Now. That should be all there is to it. A few minutes later you should have a working Python 3 installation on your system.

### Step 4: Verify Python Was Installed On Windows

1. Open the Command Prompt
2. Type ```python``` into the Command Prompt and it will display the python version and other information, as well as put you in an environment ready to run python code, below:
![alt text](https://phoenixnap.com/kb/wp-content/uploads/2019/04/verify-python-install-1.png)


## For Mac

### Step 1: Installing Homebrew
1. Paste this into the terminal ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"```

### Step 2: Adding Python as an Environment Variable
1. Open the terminal and input ``` vim .bash_profile``` and press enter
2. Press the ```i``` key to write to the file and put ```export PATH="/usr/local/opt/python/libexec/bin:$PATH"``` on a new line
3. Press the ```esc``` key and type ```:wq``` to save and close the file.

### Step 3: Verify Python Was Installed On Mac via Homebrew
1. Open the Terminal and type ```python3 --version```
2. The version number should appear on the next line stating ```Python 3.x.x```

## For Linux

### Step 1: First, install development packages required to build Python.

On Debian:
```
$ sudo apt update
$ sudo apt install build-essential zlib1g-dev \
libncurses5-dev libgdbm-dev libnss3-dev \
libssl-dev libreadline-dev libffi-dev curl
```
On Fedora:
```
$ sudo dnf groupinstall development
```
Step 2: Download the stable latest release of Python 3

Visit the official Python website and download the latest version of Python 3. After the download is complete, you hav a .tar.xz archive file (a "tarball") containing the source code of Python.

Step 3: Extract the tarball

Once the download is complete, extract the tarball by either using the extractor application of your choice or the Linux tar command, for example:
```
$ tar -xf Python-3.?.?.tar.xz
```
Step 4: Configure the script

Once the Python tarball has been extracted, navigate to the configure script and execute it in your Linux terminal with:
```
$ cd Python-3.*
./configure
```
The configuration may take some time. Wait until it is successfully finishes before proceeding.

Step 5: Start the build process

If you already have a version of Python installed on your system and you want to install the new version alongside it, use this command:
```
$ sudo make altinstall
```
The build process may take some time.

If you want to replace your current version of Python with this new version, you should uninstall your current Python package using your package manager (such as apt or dnf) and then install:
```
$ sudo make install
```

Step 6: Verify the installation

If you haven't encountered any errors, the latest Python is now installed on your Linux system. To verify it, write one of these commands in your terminal:
```
python3 --version
```
