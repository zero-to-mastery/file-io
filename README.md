# Create a Spotify Data Logger 

Create a data processing file I/O script that reads data from a CSV file containing Spotify data and performs some basic analysis on it. 

The script an be adapted to work with nearly any backend programming language. This README provides an overview of the project and explains how to adapt it to your chosen programming language.

Table of Contents
- [Project Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Customization](#customization)
- [License](#license)

<h2 id="overview">Project Overview</h2>
The project consists of a script that reads data from a CSV file (spotify-2023.csv) and performs some or all of the following tasks. **Note: the project must minimally find the number of results (Challenge #1) to qualify for as a submission:**

1. Load Spotify data from the CSV file.
2. Create a folder for your project with your github handler. 
3. Complete the first challenge below. The other challenges are optional.
4. Add your folder with your project to the submissions folder of this repo.

### Challenges
1. Write a script to identify the number of songs in the file.
2. Write a script that identify the number of songs in the key of E.
3. Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.

<h2 id="prerequisites">Prerequisites</h2>
Before adapting this project to your chosen programming language, ensure that you have the following prerequisites:

- A backend programming language of your choice.
- A library or method for reading and parsing CSV files, if not built-in to your language of choice.
- The CSV file (spotify-2023.csv) containing Spotify data that you want to analyze. Make sure to adjust the filename and path as needed.

<h2 id="getting-started">Getting Started</h2>
The usage instructions will vary depending on your chosen programming language. Below are the general steps to adapt this project:

**Clone or Download:** Clone or download this repository to your local machine.

**Choose Your Backend Language:** Open the project directory and create a new script or file in your chosen backend programming language. You will replicate the functionality provided by the Node.js script.

**Prerequisites:** Ensure you have the required prerequisites for your chosen programming language, such as libraries for file I/O and CSV parsing.

**Adapt File I/O:** Replace the file I/O code in the Node.js script with the file I/O methods provided by your chosen language. This includes reading data from the CSV file (spotify-2023.csv).

**Adapt CSV Parsing:** Replace the CSV parsing code with the CSV parsing library or method available in your programming language.

**Customize Data Processing:** Adjust the data processing and analysis logic as needed to match the syntax and conventions of your chosen language.

**Run Your Script:** Execute your adapted script using the appropriate command or method for your backend programming language.

<h2 id="license">License</h2>
This project is licensed under the MIT License - see the LICENSE file for details. You are free to modify and distribute the adapted code as needed for your own projects.