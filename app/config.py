EURI_API_KEY = "euri-96411cfccf2b870b7c8743239a4353ceeca79beddf0a62726713756afcd19653"
try:
    # Preferred: put {"EURI_API_KEY": "..." } in .streamlit/secrets.toml
    import streamlit as st  # noqa: F401
    from streamlit import secrets
    EURI_API_KEY = secrets.get("euri-96411cfccf2b870b7c8743239a4353ceeca79beddf0a62726713756afcd19653") or ""
except Exception:
    # Fallback to hardcoded default (replace with a safe value or leave empty)
    EURI_API_KEY = "euri-96411cfccf2b870b7c8743239a4353ceeca79beddf0a62726713756afcd19653"  # ← put your key here if you aren't using secrets
