# Developer Notes

## Local Development

```sh
git clone https://github.com/kyleking/personal-man.git
cd personal-man
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
| File                                            |   Statements |   Missing |   Excluded | Coverage   |
|-------------------------------------------------|--------------|-----------|------------|------------|
| `personal_man/__init__.py`                      |            6 |         0 |          0 | 100.0%     |
| `personal_man/cli.py`                           |           50 |        21 |          0 | 58.0%      |
| `personal_man/controllers/__init__.py`          |            0 |         0 |          0 | 100.0%     |
| `personal_man/controllers/search_controller.py` |           21 |        10 |          0 | 52.4%      |
| `personal_man/controllers/show_controller.py`   |           21 |         9 |          0 | 57.1%      |
| `personal_man/core/__init__.py`                 |            0 |         0 |          0 | 100.0%     |
| `personal_man/core/exceptions.py`               |            4 |         0 |          0 | 100.0%     |
| `personal_man/core/version.py`                  |            8 |         8 |          0 | 0.0%       |
| `personal_man/output.py`                        |           54 |        18 |          0 | 66.7%      |
| `personal_man/search.py`                        |            6 |         1 |          0 | 83.3%      |
| `personal_man/settings.py`                      |           20 |         0 |          0 | 100.0%     |
| `personal_man/show.py`                          |           42 |        24 |          0 | 42.9%      |
| **Totals**                                      |          232 |        91 |          0 | 60.8%      |

Generated on: 2022-11-27
<!-- {cte} -->
