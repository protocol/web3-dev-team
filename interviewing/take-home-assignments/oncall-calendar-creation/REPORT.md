# Purpose
As requested by the takehome assignment, below is a report answering the requested question.

# Setup
## Install Dependencies
```shell
conda install pandas # For easily working with structured data (joins, sorts)
conda install openpyxl # Required for Pandas to read in .xlsx files
conda install gcsa # Higher-level library for interfacing with Google Calendar
```

I'm assuming you have an environment where can read/run .ipynb notebooks (e.g., JupyterLab, Visual Studo Code, PyCharm).

## Download/Store Input Data
``oncall-calendar-creation.ipynb`` expects a file in the same directory named ``Oncall Calendar Creation Input Data.xlsx``.  This file was created by exporting the Google Sheet input data as an .xlsx file.

## GCP Setup
Note: these steps are based on https://google-calendar-simple-api.readthedocs.io/en/latest/getting_started.html and https://developers.google.com/calendar/quickstart/python
1. [Create a GCP project](https://developers.google.com/workspace/guides/create-project)
2. [Enable the Google Calendar API](https://developers.google.com/workspace/guides/create-project#enable-api)
3. [Generate Authroization credentials for a desktop application](https://developers.google.com/workspace/guides/create-credentials)

``oncall-calendar-creation.ipynb`` expects a ``credentials.json`` file in the same directory. 

# Design Decisions
1. I'm using Pandas because it makes it quick/easy to read in Excel files and do joins/sorts across the sheets.
2. I opted for [google-calendar-simple-api](https://github.com/kuzmoyev/google-calendar-simple-api) instead of [Google's Python API](https://developers.google.com/calendar/quickstart/python) because of the easier interface to work with.
3. I opted for a simple scheduling algorithm where for each rotation, I schedule one engineer per week as a recurring event (recurring every 8 weeks).  I'm not mindful of what team an oncall is on, thus it's possible for a team to have multiple consecutive weeks of having a team member oncall.  I don't know if that matters though.
4. The update story is currently non-existent.  Duplicate events will get generated each time the notebook is run.

# Time Spent
I recorded the steps I took and the time spent in ``worklog.md``.

# Areas To Improve
If I had more time, I would invest in itmes like:
1. Read input data from Google Sheets directly
2. Record/store the created calendar event ids so have a handle for being able to make updates.
3. Wrap this as a CLI that accepts input parameters.
4. Programatically create the maintenance oncall calendar.
5. Do "fairer scheduling" (if that is even desired) 