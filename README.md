# Wikipedia Scraper

## Introduction

This project delivers a JSON format file with information about historical leaders from several countries
This project deals with:

- API connection
- Scrapping
- Data cleaning
- JSON files
  This project implements the must have requirements from the Wikipedia Scrapper brief

## Description

The project contains two code files:

- A Jupyter notebook _wikipedia_scraper.ipynb_
- A Python file _leaders_scraper.py_

  And two data files:

- An depecrated version of the results : _sample.json_
- The final file: _leaders.json_

## Requirements

- Python version: Python 3.10.4
- Recommended IDE : VsCode with Jupyter Notebook extension.

## Installation

1. Download the directory or pull it from its repository
2. Create a Python virtual environment using the requirements file in this directory:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   python -m pip install -r requirements.txt
   ```

## Usage

### Jupyter notebook 'wikipedia_scraper.ipynb'

1.  Run the cells one by one according to the written instructions

### Python file 'leaders_scraper.py'

2. Open your terminal in the appropiate directory
3. Run the file with

**IMPORTANT** Running the Python file in its entirety or in its defect, the cells in the Jupyter notebook that save the json files, will overwrite _leaders.json_
