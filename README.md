# TODO

* TODO clone repo
* TODO set up `.env`

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

```bash
python job_creator.py
```

```bash
python job_completer.py
```

## CrateDB

### Create and Populate staff Table

```sql
CREATE TABLE staff (
  id INTEGER,
  name TEXT
);
```

```sql
INSERT INTO staff (id, name) VALUES (1, 'Simon'), (2, 'Alice'), (3, 'Michael'), (4, 'Stefan'), (5, 'Alea');
```

### Some Example Queries

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
