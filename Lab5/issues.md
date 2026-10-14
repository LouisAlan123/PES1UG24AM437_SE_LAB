# Issues found by static analysis (`supplier_orders.py`)

Line numbers refer to the original file. Ordered by severity.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Shell command injection (Bandit B605, **High**) | Security | 21 | `os.system("echo ... " + supplier)` runs through a shell; a supplier name such as `x; rm -rf ~` would execute arbitrary commands | Removed the shell call; the warehouse notification is now a plain `print`, so there is no process and no `os` import |
| SQL injection (Bandit B608, **Medium**) | Security | 11 | INSERT built with `%` string formatting from `supplier` and `item` | Parameterised query with `?` placeholders and a values tuple |
| Silent broad exception (Bandit B110 Low, Pylint W0718) | Bug / Security | 25-28 | `except Exception: pass` hides every failure while deleting orders | Catch only `sqlite3.Error` and log it with `logging.exception` |
| Global mutable state (Pylint W0603, W0621, C0103) | Design | 4-6, 10 | Module-level `conn` and `order_total` plus `global`; parameters shadow the outer `conn` | Connection created in `create_connection()` and passed explicitly; total derived from the DB with `total_quantity()` |
| Line too long / missing whitespace (Flake8 E501, E225) | Style | 5, 11, 12, 32 | Lines up to 131 characters; `order_total+=quantity` | Wrapped strings and statements, added spaces around operators |
| Unused argument (Pylint W0613) | Code quality | 16 | `markReceived(..., remarks)` never uses `remarks` | Removed the parameter and updated the caller |
| camelCase names (Pylint C0103) | Style | 9, 16, 20, 31 | `placeOrder`, `markReceived`, `notifyWarehouse`, `pendingCount` | Renamed to snake_case |
| Missing docstrings (Pylint C0114, C0116) | Documentation | 1, all functions | No module or function docstrings | Added docstrings |
| `main()` runs on import (design) | Bug | 44 | Importing the module executes the program | Added `if __name__ == "__main__":` guard |

## Results

| Tool | Before | After |
|---|---|---|
| Pylint | 2.41/10 | 10.00/10 |
| Bandit | 1 High, 1 Medium, 1 Low | 0 issues |
| Flake8 | 4 warnings | 0 warnings |

Program output is unchanged (`notifying warehouse about Acme`, then `1 540`).
