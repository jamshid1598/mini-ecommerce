import os
from pathlib import Path
from dotenv import load_dotenv


"""load .env file"""
env_path = os.path.join(Path(__file__).resolve().parent.parent, '.env')
load_dotenv(env_path)


def get_allowed_hosts(hosts):
    return [s.strip() for s in hosts.split(',') if s.strip()]


secret_key = os.environ.get("SECRET_KEY", default="django-insecure-n!700@=b!^o03ty3ryvj)4(4$$2h&f3seh")
debug = os.environ.get("DEBUG", default=False)  # debug must be False in production
allowed_hosts = get_allowed_hosts(os.environ.get('ALLOWED_HOSTS', default=""))

db_name = os.environ.get("DB_NAME", default="fls.sqlite3")
db_user = os.environ.get("DB_USER", default="fls")
db_password = os.environ.get("DB_PASSWORD", default="fls_password")
db_port = os.environ.get("DB_PORT", default=5432)
db_host = os.environ.get("DB_HOST", default='db')

current_settings = os.environ.get("SETTINGS", default="proroot.settings.dev")
