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

```sql
CREATE TABLE staff (
  id INTEGER,
  name TEXT
);
```

```sql
INSERT INTO staff (id, name) VALUES (1, 'Simon'), (2, 'Alice'), (3, 'Michael'), (4, 'Stefan'), (5, 'Alea');
```