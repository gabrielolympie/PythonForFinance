# PythonForFinance
Repository to hold the PythonForFinance course for Audencia

## Planning
| Date       | Time Slot       | Validated                                         |
|------------|-----------------|---------------------------------------------------|
| 15/09      | 13h30 - 17h45   | Introduction                                      |
| 22/09      | 13h30 - 17h45   | Variable, loops, conditions                       |
| 24/09      | 13h30 - 17h45   | Fonctions, Classes, Scripts et API                |
| 06/10      | 13h30 - 17h45   | Libraries, package manager, dataframe et data viz |
| 08/10      | 13h30 - 17h45   | Backend / Frontend integration                    |
| 14/10      | 13h30 - 17h45   | GenAI / LLMs for development                      |

## Course Content (previsionnal)
- Seance 1 : Introduction
  - Amphi
    - History of python
    - Examples of python projects in enterprise
    - Python project lifecycle and basics of agile development
    - Structure of a python project in enterprise
    - Using GIT (repo, push, pull, pull request etc.)
    - Python in 2025 (AI / Adoption / Challenges)
    - Presentation of the red thread project
    - Presentation of the evaluation project
  - TD
    - Installing python
    - Setting up an IDE (VS Code)
    - Setting up AI in the ide
    - First python program: Hello World
- Seance 2 : Python Basics
  - Amphi
    - Data types (int, float, string, bool)
    - Data structures (list, tuple, dict, set)
    - Operators (arithmetic, comparison, logical)
    - Conditions (if, elif, else)
    - Loops (for, while)
    - Basic algorithmic optimization (type simplification, complexity, stop conditions)
  - TD
    - Loading a tweet dataset json into a list of dictionaries
    - Defining an appropriate data model
    - Implementing a filter on the number of likes and the presence of verbatims
    - Extracting high-level KPIs (number of tweets, number of likes, number of retweets, number of followers, number of following)
- Seance 3 : Functions, Classes, Scripts and API
  - Amphi
    - Learning to define a function
    - Learning to define a pipeline
    - Learning to define a class
    - When to use a class, when to use a function
    - Basic notions of inheritance and design patterns
    - Learning to run a .py
    - Learning to use an API
  - TD
    - Creating a function to calculate the number of words in a text
    - Creating a function to remove stop words in a text
    - Creating a Tweet class to standardize tweet processing
    - Creating a cleaning and enrichment pipeline for tweets
    - Learning to query a simple API
- Seance 4 : Libraries, package manager, dataframe and data viz
  - Amphi
    - Understanding how a package manager works
    - Installing libraries
    - Browsing a documentation and being autonomous on a library
    - Introduction to Pandas
    - Introduction to Plotly
    - Learning to install a git library: https://github.com/JustAnotherArchivist/snscrape
  - TD
    - Installing pandas / plotly
    - Adapting previous functions to use a pandas dataframe
    - Creating data aggregation queries to extract KPIs
    - Visualizing results and trends with Plotly
    - Retrieving tweets with SNScrape
    - Simple sentiment analysis with text blob
    - Bonus: creating a wordcloud
- Seance 5 : Backend / Frontend
  - Amphi
    - What are the differences between back-end and front-end development
    - Creating a simple fastapi backend
    - Creating a simple client to query fastapi
    - Setting up a basic interface in gradio / streamlit
  - TD
    - Modularizing previous functions and serving them via a fastapi backend
    - Creating a simple interface to query the backend
    - Allowing data ingestion directly via the interface
- Seance 6 : GenAI / LLMs
  - Amphi
    - How generative AI integrates into python development
    - What is an "agent" and how to query it
  - TD
    - Adding a sentiment analysis / title / paraphrasing tool to tweets