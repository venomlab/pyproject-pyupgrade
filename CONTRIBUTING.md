# Contributing

## If you found a bug and want to report it

[Create a new issue](https://github.com/venomlab/pyproject-pyupgrade/issues/new)
and specify detailed information about environment you run `pyproject-pyupgrade`:

- Python version
- OS family/version
- How `pyproject-pyupgrade` is installed (pip/pipx/poetry/...)
- How you run `pyproject-pyupgrade`
- `pyproject.toml`, full if possible (it could be an issue related to TOML parser)
- Steps to reproduce the issue

(Optional) Provide a Pull Request that fixes the issue - it would be extra appreciated.
Don't forget to run pre-commit hooks and all the tests (once they're available).
Look for the [feature/bugfix request guide](#if-you-want-to-provide-a-feature-or-fix-a-bug) for details

## If you want to request a new feature

[Create a new issue](https://github.com/venomlab/pyproject-pyupgrade/issues/new)
and specify detailed information about what feature do you want:

- Describe what the problem do you have that this feature would solve
- Provide example usages (in configuration or via CLI) of your feature

(Optional, but highly recommended) Provide a Pull Request that implements the feature - your request may be added way faster.
Don't forget to run pre-commit hooks and all the tests (if there are any).
Look for the [feature/bugfix request guide](#if-you-want-to-provide-a-feature-or-fix-a-bug) for details

## If you want to provide a feature or fix a bug

[Fork a repository](https://github.com/venomlab/pyproject-pyupgrade/fork)
create a branch with the following format `<request-type>/<short-branch-description>`
where `<request-type>` could be `bug` or `feature`,
and `<short-branch-description>` could be, for example `add-pyupgrade-ini-configuration-support`

Make code changes in your own fork. Does not matter how many commits you have or what are commit messages,
it anyway will be squashed before merge.

Requrements:

- All pre-commit hooks _must_ pass
- All tests _must_ pass (if there are any :smile:)

[Create a Pull Request](https://github.com/venomlab/pyproject-pyupgrade/compare)
fill it with information about your changes:

- What does your Pull Request do
- What problem you solved
- (if it is a bug fix) It is a good time to link the Pull Request to an Issue
