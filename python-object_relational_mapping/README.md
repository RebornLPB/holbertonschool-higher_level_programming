# Python - Object Relational Mapping

## Description
This project connects Python to a **MySQL** database in two ways. The first half uses the low-level `MySQLdb` driver with raw SQL (including a deliberate SQL-injection demonstration and its fix). The second half uses **SQLAlchemy**, an ORM that maps tables to Python classes (`State`, `City`) so rows can be queried, inserted, updated and deleted as objects.

All scripts are written for **Python 3.8+**. Every script takes its database credentials from the command line.

## 📝 Learning Objectives
* Connect to MySQL from Python with `MySQLdb` and run queries through a cursor.
* Understand and prevent **SQL injection** by using parameterized queries (`%s`) instead of string formatting.
* Join tables in raw SQL (`cities` ↔ `states`).
* Map tables to classes with SQLAlchemy's `declarative_base`, `Column` and `ForeignKey`.
* Use an ORM `Session` to `query`, `filter`, `order_by`, `add`, `delete` and `commit`.
* Build the engine URL `mysql+mysqldb://user:password@localhost:3306/database`.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Database:** MySQL
* **Libraries:** `mysqlclient` (`MySQLdb`) and `SQLAlchemy`
* **Style Guide:** PEP 8 (check with `pycodestyle`).

```bash
pip3 install mysqlclient sqlalchemy
```

## 📁 File List & Tasks Directory

### Raw SQL with `MySQLdb`

Arguments: `<mysql username> <mysql password> <database name> [<extra argument>]`

| File | Task Title | Description |
| :--- | :--- | :--- |
| `0-select_states.py` | List states | Lists all rows of `states` in `hbtn_0e_0_usa`, sorted by `id`. |
| `0-select_states.sql` | Dataset | Creates `hbtn_0e_0_usa` with the `states` table and 5 rows. |
| `1-filter_states.py` | Filter states | Lists the states whose name starts with an uppercase `N`. |
| `2-my_filter_states.py` | Filter by name (unsafe) | Lists the states matching the name given as 4th argument, built with `str.format` — **vulnerable to SQL injection on purpose**. |
| `3-my_safe_filter_states.py` | Filter by name (safe) | Same as above, using a parameterized query (`%s`) to be injection-proof. |
| `4-cities_by_state.py` | Cities by state | Lists all cities with their state name (`JOIN`) from `hbtn_0e_4_usa`. |
| `4-cities_by_state.sql` | Dataset | Creates `hbtn_0e_4_usa` with `states` and `cities` tables and sample data. |
| `5-filter_cities.py` | Cities of a state | Prints the cities of the state given as 4th argument, comma-separated, using a parameterized query. |

### ORM with SQLAlchemy

Arguments: `<mysql username> <mysql password> <database name> [<extra argument>]`

| File | Task Title | Description |
| :--- | :--- | :--- |
| `model_state.py` | `State` model | Defines `Base` and the `State` class mapped to the `states` table (`id`, `name`). |
| `model_city.py` | `City` model | Defines the `City` class mapped to `cities` (`id`, `name`, `state_id` foreign key to `states.id`). |
| `7-model_state_fetch_all.py` | List all states | Prints every `State` as `id: name`, sorted by `id`. |
| `7-model_state_fetch_all.sql` | Dataset | Inserts the sample states used by the ORM tasks. |
| `8-model_state_fetch_first.py` | First state | Prints the first `State`, or `Nothing` if the table is empty. |
| `9-model_state_filter_a.py` | States containing "a" | Prints every `State` whose name contains the letter `a`. |
| `10-model_state_my_get.py` | Get a state by name | Prints the `id` of the `State` named after the 4th argument, or `Not found`. |
| `11-model_state_insert.py` | Add a state | Inserts the `State` "Louisiana" and prints its new `id`. |
| `12-model_state_update_id_2.py` | Update a state | Renames the `State` with `id = 2` to "New Mexico". |
| `13-model_state_delete_a.py` | Delete states containing "a" | Deletes every `State` whose name contains the letter `a`. |
| `14-model_city_fetch_by_state.py` | Cities with their state | Prints every `City` as `state name: (city id) city name`, sorted by city `id`. |
| `14-model_city_fetch_by_state.sql` | Dataset | Creates `hbtn_0e_14_usa` with `states` and `cities` tables and sample data. |

---

## 🚀 Execution & PEP 8 Testing

Load a dataset, then run a script against it:

```bash
cat 0-select_states.sql | mysql -uroot -p
./0-select_states.py root <password> hbtn_0e_0_usa
```

```bash
cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
./14-model_city_fetch_by_state.py root <password> hbtn_0e_14_usa
```

```bash
pycodestyle 0-select_states.py
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)
