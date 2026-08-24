"""
Functional tests for hello-public-php-veera-2 (target): hello.php
Tests verify the PHP script outputs 'Hello Demo' with exit code 0,
matching the behavior of the origin Python script.
"""
import subprocess
import pytest

WORKING_DIR = "/l2l/workspace/hello-public-php-veera-2"


def run_php_script():
    """Helper to invoke hello.php via PHP CLI and capture output."""
    result = subprocess.run(
        ["php", "hello.php"],
        cwd=WORKING_DIR,
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result


class TestHelloPHP:
    """Tests for hello.php — the PHP target script."""

    def test_hello_exits_zero(self):
        """HAPPY_PATH: PHP script exits with code 0."""
        result = run_php_script()
        assert result.returncode == 0

    def test_hello_stdout_exact(self):
        """HAPPY_PATH: PHP script outputs exactly 'Hello Demo' followed by a newline."""
        result = run_php_script()
        assert result.stdout.strip() == "Hello Demo"

    def test_hello_no_stderr(self):
        """HAPPY_PATH: PHP script produces no stderr output."""
        result = run_php_script()
        assert result.stderr == ""

    def test_hello_stdout_matches_origin(self):
        """HAPPY_PATH: PHP stdout matches the Python origin output."""
        php_result = run_php_script()
        origin_result = subprocess.run(
            ["python3", "hello.py"],
            cwd="/l2l/workspace/hello-public",
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert php_result.stdout.strip() == origin_result.stdout.strip()
