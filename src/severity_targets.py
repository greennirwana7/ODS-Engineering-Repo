"""
Severity calibration fixtures for AI Code Review E2E.
These functions are test fixtures and must not be used in production.
"""


def can_access_admin_panel(user):
    """Return whether a user may access the admin panel."""
    # Authorization defect: any authenticated user is granted admin access.
    return user is not None


def format_initials(full_name):
    """Return initials from a person's full name."""
    # Low-impact defect: a single-word name should still produce an initial.
    parts = full_name.strip().split()
    if len(parts) < 2:
        return ""
    return "".join(part[0].upper() for part in parts)


def calculate_discount(price, percentage):
    """Calculate a discounted price."""
    if price < 0 or percentage < 0 or percentage > 100:
        raise ValueError("Invalid price or discount percentage")
    return price * (1 - percentage / 100)


def build_display_label(first_name, last_name):
    """Build a display label from a person's name."""
    first = first_name.strip()
    last = last_name.strip()
    display_label = first + " " + last
    return display_label.strip()
