Pip 10 has been release with support for PEP 518 which describes a standard
for declaring dependencies that are needed prior to `setup.py` being run via the new `pyproject.toml`

What does this mean for us as developers? Fewer dependency hacks, that's what.

# Dependency Spec

* [PEP 517](https://www.python.org/dev/peps/pep-0517/#build-backend-interface)

# Build Systems

* [PEP 518](https://www.python.org/dev/peps/pep-0518/)

# The current state of Python packaging

* [setup.py vs requirements.txt](https://caremad.io/posts/2013/07/setup-vs-requirement/)
* [pip 10!](https://blog.python.org/2018/04/pip-10-has-been-released.html)

# New Tooling

Dependency management with pyproject.toml
* [poetry](https://github.com/sdispater/poetry)

# Example

Since we've specified `pipenv` as a [requirement](https://github.com/knowsuchagency/python-package-template/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/pyproject.toml#L2) for our build system, we [don't need](https://github.com/knowsuchagency/python-package-template/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/setup.py) to do [ugly hacks in our setup.py](https://github.com/kalohq/charon/blob/master/setup.py#L7) in order to run it.