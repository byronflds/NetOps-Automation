NetOps Automation Platform

Internal automation dashboard for network operations teams to safely manage sites, ports, and billing adjustments with role-based access and full audit logging.

Problem Statement

- Manual network operations are error-prone

- Billing moves require precision and auditability

- Existing tools lack guardrails and RBAC

Features

-Flask-based modular application factory architecture

- Role-based access control (admin vs user)

- Port provisioning and deactivation via API-backed workflows

- Billing adjustments with validation and conflict prevention

- Full CRUD operations backed by relational database

- Audit logging to application and server logs

- Secure authentication using Flask-Login

-Defensive error handling (403 / 404)

Security & Safety

- RBAC enforced at route and decorator level

- Admin-only workflows protected by custom decorators

- Client-side and server-side validation

- Audit logs for sensitive operations

Tech Stack:

Python 3.x

Flask

SQLAlchemy

Flask-Login

Jinja2

Apache (WSGI)

REST APIs (DNAC / Mist-style integrations)