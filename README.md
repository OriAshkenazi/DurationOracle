**Duration Oracle Application**

**User Guide**

**1. Introduction**

This guide provides instructions for setting up and using the Duration
Oracle Application. This application is a self-contained desktop app
that uses a pre-trained machine-learning model to estimate the duration
of projects based on certain parameters.

**2. Prerequisites**

The user will need Python installed on their computer to run this
application. If Python is not installed, it can be downloaded from the
official Python website:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

The application has been tested on Python 3.7+.

**3. Installation**

**Step 1: Clone the repository or download the application code**

If you have Git installed, you can clone the repository by running the
following command in the terminal/command prompt:

**git clone <[https://github.com/OriAshkenazi/DurationOracle](https://github.com/OriAshkenazi/DurationOracle)>**

Alternatively, you can download a zip file of the project from the
repository page and extract it.

**Step 2: Install the necessary Python packages**

Open the terminal/command prompt, navigate to the directory containing
the application code, and install the necessary Python packages using
pip (Python\'s package installer). The required packages are Flask and
Pywebview. Run the following command:

**pip install Flask pywebview keras tensorflow pandas**

This installs Flask and Pywebview, which are needed for the
application\'s UI and server functionality, as well as keras and
tensorflow for loading and using the pre-trained model, and pandas for
handling data.

**Step 3: Launch the application**

In the terminal/command prompt, navigate to the directory containing the
application code. Then, run the Flask application (app.py) by using the
following command:

**python app.py**

This command starts the backend server. Keep this running and open
another terminal/command prompt window.

In the new terminal/command prompt window, navigate to the same
directory and run the window script (window.py) using the following
command:

**python window.py**

This command opens the application in a new window.

**4. Using the Application**

The application window contains input fields for entering the parameters
based on which the duration of the project will be predicted.

-   **Price Estimation \[million NIS\]:** Enter the estimated price of
    the project in millions of NIS.

-   **Complexity:** Select the complexity of the project from the
    options - \'Simple\', \'Normal\', and \'Complex\'.

-   **Type:** Select the type of the project from the options -
    \'Building\' and \'Infrastructure\'.

After filling in the required details, click on the \"Predict Duration\"
button. The application will display the estimated duration of the
project in years, months, and days.

If any changes are made to the input fields after a duration prediction
has been displayed, the prediction and the \"Predict Duration\" button
will turn red. They will turn green again once a new duration prediction
is displayed.

**5. Troubleshooting**

-   **Python or pip not recognized:** If the terminal/command prompt
    does not recognize \'python\' or \'pip\', it is likely that Python
    was not added to the PATH during its installation. Refer to
    Python\'s official installation instructions and ensure that Python
    is correctly installed and added to the PATH.

-   **Package installation failed:** If pip fails to install a package,
    it might be due to an older version of pip. Try updating pip using
    **python -m pip install \--upgrade pip** and then install the
    packages again.

-   **The application doesn\'t start or an error is displayed:** Make
    sure that both the Flask server (app.py) and the application window
    (window.py) are running. Both need to be started from separate
    terminal/command prompt windows.

In case of other problems, refer to the error message displayed in the
terminal/command prompt, or contact the application support.
