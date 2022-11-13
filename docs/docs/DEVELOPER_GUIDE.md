# Developer Notes

## Local Development

```sh
git clone https://github.com/kyleking/pman.git
cd pman
poetry install

# See the available tasks
poetry run doit list

# Run the default task list (lint, auto-format, test coverage, etc.)
poetry run doit --continue

# Make code changes and run specific tasks as needed:
poetry run doit run test
```

## Publishing

For testing, create an account on [TestPyPi](https://test.pypi.org/legacy/). Replace `...` with the API token generated on TestPyPi or PyPi respectively

```sh
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi ...

poetry run doit run publish_test_pypi
# If you didn't configure a token, you will need to provide your username and password to publish
```

To publish to the real PyPi

```sh
poetry config pypi-token.pypi ...
poetry run doit run publish

# For a full release, triple check the default tasks, increment the version, rebuild documentation (twice), and publish!
poetry run doit run --continue
poetry run doit run cl_bump lock document deploy_docs publish

# For pre-releases use cl_bump_pre
poetry run doit run cl_bump_pre -p rc
poetry run doit run lock document deploy_docs publish
```

## Current Status

<!-- {cts} COVERAGE -->
| File                                    |   Statements |   Missing |   Excluded | Coverage   |
|-----------------------------------------|--------------|-----------|------------|------------|
| `pman/__init__.py`                      |            6 |         0 |          0 | 100.0%     |
| `pman/cli.py`                           |           39 |        17 |          0 | 56.4%      |
| `pman/controllers/__init__.py`          |            0 |         0 |          0 | 100.0%     |
| `pman/controllers/search_controller.py` |           14 |         3 |          0 | 78.6%      |
| `pman/controllers/show_controller.py`   |           18 |         6 |          0 | 66.7%      |
| `pman/core/__init__.py`                 |            0 |         0 |          0 | 100.0%     |
| `pman/core/exceptions.py`               |            4 |         0 |          0 | 100.0%     |
| `pman/core/version.py`                  |            8 |         8 |          0 | 0.0%       |
| `pman/onboarding.py`                    |            0 |         0 |          0 | 100.0%     |
| `pman/output.py`                        |           54 |        18 |          0 | 66.7%      |
| `pman/search.py`                        |            6 |         1 |          0 | 83.3%      |
| `pman/settings.py`                      |           21 |         0 |          0 | 100.0%     |
| `pman/show.py`                          |           26 |        15 |          0 | 42.3%      |
| **Totals**                              |          196 |        68 |          0 | 65.3%      |

Generated on: 2022-11-12
<!-- {cte} -->
