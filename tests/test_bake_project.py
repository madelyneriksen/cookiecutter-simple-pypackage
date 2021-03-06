from contextlib import contextmanager

import os
import subprocess


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def test_project_tree(cookies):
    result = cookies.bake(extra_context={'module_name': 'testproject'})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'testproject'


def test_run_flake8(cookies):
    result = cookies.bake(extra_context={'module_name': 'codestylecompat'})
    with inside_dir(str(result.project)):
        assert subprocess.check_call(['pycodestyle', 'codestylecompat/']) == 0


def test_run_pylint(cookies):
    result = cookies.bake(extra_context={'module_name': 'pylintcompat'})
    with inside_dir(str(result.project)):
        assert subprocess.check_call(['pylint', 'pylintcompat']) == 0
