"""Slug normalization helpers."""


def normalize_slug(value: str) -> str:
    """Return a lowercase, hyphen-separated slug."""
    return value.strip().lower().replace(" ", "-")
