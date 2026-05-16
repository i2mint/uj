"""Smoke test: ensures pytest collects at least one test."""


def test_import():
    import uj  # noqa: F401
