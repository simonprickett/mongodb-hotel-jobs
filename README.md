# MongoDB/CrateDB CDC Demonstration

## Introduction

TODO

## Prerequisites

To run this project you'll need to install the following software:

* Python 3 ([download](https://www.python.org/downloads/)) - we've tested this project with Python 3.12 on macOS Sequoia.
* Git command line tools ([download](https://git-scm.com/downloads)).
* Your favorite code editor, to edit configuration files and browse/edit the code if you wish.  [Visual Studio Code](https://code.visualstudio.com/) is great for this.
* Access to an instance of CrateDB in the cloud.
* Access to an instance of MongoDB in the cloud.

## Getting the Code

Grab a copy of the code from GitHub by cloning the repository.  Open up your terminal and change directory to wherever you store coding projects, then enter the following commands:

```bash
git clone https://github.com/simonprickett/mongodb-hotel-jobs.git
cd mongodb-hotel-jobs
```

## Getting a CrateDB Database in the Cloud

TODO

### Database Schema Setup

TODO

```sql
CREATE TABLE staff (
  id INTEGER,
  name TEXT
);
```

```sql
INSERT INTO
  staff (id, name)
VALUES
  (1, 'Simon'),
  (2, 'Alice'),
  (3, 'Michael'),
  (4, 'Stefan'),
  (5, 'Alea');
```

## Getting a MongoDB Database in the Cloud

## Editing the Project Configuration File

TODO

```bash
cp env.example .env
```

## Setting up a Python Environment

You should create and activate a Python Virtual Environment to install this project's dependencies into.  To do this, run the following commands:

```bash
python -m venv venv
. ./venv/bin/activate
```

Now install the dependencies that this project requires:

```bash
pip install -r requirements.txt
```

## Running the Python Code

### Job Creator Component

TODO

```bash
python job_creator.py
```

### Job Completer Component

TODO

```bash
python job_completer.py
```

### Some Example Queries

#### mflix Movies Example

What were the top 10 highest rated movies released in 2014, according to Rotton Tomatoes reviewers?

```sql
select
  document['title'] as title,
  document['tomatoes'] ['viewer'] ['rating'] as rotten_tomatoes_rating
from
  movies
where
  document['year'] = 2014 and document['tomatoes'] ['viewer'] ['rating'] is not null
order by
  rotten_tomatoes_rating desc
limit
  10
```

What is the average run time of comedy movies for each year 2010 onwards?

```sql
select
  document['year'] as year,
  avg(document['runtime']) as average_runtime
from
  movies
where
  document['year'] > 2009
  and document['genres'] [1] = 'Comedy'
group by
  year
order by
  year desc
```

Which films is a given actor in?

```sql
select
  document['title'] as title,
  document['year'] as year,
  document['cast'] as cast_members
from
  movies
where
  array_position(document['cast'], 'Julia Kijowska') is not null
```

#### Jobs Example

How many jobs are outstanding?

```sql
select
  count(*)
from
  jobs as backlog
where
  document['completedAt'] is null;
```

How many jobs have been completed?

```sql
select
  count(*)
from
  jobs as completed
where
  document['completedAt'] is not null;
```

Outstanding jobs by type:

```sql
select
  document['job'] as job_type,
  count(*) as backlog
from
  jobs
where
  document['completedAt'] is null
group by
  job_type
order by
  backlog desc
```

Average time to complete a job:

```sql
select
  round(avg(document['completedAt'] - document['requestedAt']) / 1000) as job_avg_time
from
  jobs 
where
  document['completedAt'] is not null
```

League table of who has completed the most jobs:

```sql
select
  s.id,
  s.name,
  count(j.document) as jobs_completed
from
  staff s join jobs j on s.id = j.document['completedBy']
where
  document['completedAt'] is not null
group by
  s.id, s.name
order by
  jobs_completed desc
```

## CrateDB Academy

Want to learn more about CrateDB?  Take our free online "CrateDB Fundamentals" course, available now at the [CrateDB Academy](https://cratedb.com/academy/fundamentals/).
