# MongoDB/CrateDB CDC Demonstration

## Introduction

TODO

## Prerequisites

TODO

## Getting Started

```bash
git clone https://github.com/simonprickett/mongodb-hotel-jobs.git
cd mongodb-hotel-jobs
```

```bash
python -m venv venv
. ./venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
cp env.example .env
```

* TODO set up `.env`

```bash
python job_creator.py
```

```bash
python job_completer.py
```

## CrateDB Setup

### Create and Populate staff Table

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

### Some Example Queries

#### mflix Movies Example

What were the top 10 highest rated movies released in 2014, according to Rotton Tomatoes reviewers?

```
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
