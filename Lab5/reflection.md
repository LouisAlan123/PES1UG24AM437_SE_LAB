# Reflection

The handout did not list the reflection questions, so these cover the usual ones.

**1. Which issues were easiest and hardest to fix?**
Flake8 style issues (line length, spacing) and renaming to snake_case were easy and mechanical. The hardest was the global `order_total` and `conn`: removing them meant changing every function signature and deciding where the total should come from (I now compute it from the database).

**2. Did the tools report any false positives?**
Not really. Bandit's B110 (try/except/pass) is Low severity but pointed at a real problem, because errors were silently lost. Pylint's docstring warnings are about convention rather than bugs, but they are still worth fixing for maintainability.

**3. How would you integrate these tools into your workflow?**
Run Flake8 and Pylint in a pre-commit hook and Bandit in CI, failing the build on any High or Medium Bandit finding or a Pylint score below a threshold such as 9.5.

**4. What did static analysis improve?**
Security: removed SQL injection and shell command injection. Reliability: errors are logged instead of swallowed, and importing the module no longer runs it. Readability: consistent naming, docstrings and formatting. The Pylint score went from 2.41 to 10.00 without changing program output.

**5. Limits of static analysis**
It cannot tell whether the program does what the business needs, for example whether `order_total` should count received orders. It also cannot find logic errors that look syntactically fine, so tests and code review are still needed.
