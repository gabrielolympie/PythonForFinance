## Evaluation Project: Groups of five
#### Constraints:
- Implement a Kanban-style project management tool
- Modularization: Structure the project with separation of responsibilities

#### Deliverables for Evaluation:
- GitHub repository with authenticated submission tracking (for separate evaluations)
- Project Report comprising the following details:

Team Organization: Roles adopted, Backlog tracking

Project Description: Developed code, Implemented features, Used libraries

Business Insights: Analysis of results, Data interpretation, Expected business value

Pain Points: Blocking or limiting aspects

Next Steps: How to continue or improve the project professionally

Conclusions: Learnings gained

Evaluation: Open feedback and suggestions for course improvements

#### Project choice checklist:
Each project should include:
- A clear business case: What need does it cover? Who is supposed to use it? What is the expected value?
- A data source: At least one source of external data (can be document, online resources, datasets, books...)
- An analytic pipeline: A way to extract value from the data by performing additional analysis and visualization
- A deliverable: A way to expose the analytics / value, be it through a dashboard, a simple UI or an Excel file.

#### Example
##### Purpose
The purpose of the tool is to provide a simple way to get basic analytics from news articles, at article level and at category level.

##### Data Source
The source will be web data, scraped with the Newspaper3k library on a news website to be decided.

##### Analytics
- Article level: Sentiment, word count, categorize
- Macro level: Sentiment by category, word count by category, number of articles by category

##### UI
Simple UI with two pages, one to explore the articles, and one to visualize the macro KPIs per category.