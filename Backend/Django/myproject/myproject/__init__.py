# Bypass Django's DB version check since we are using a slightly older MariaDB with XAMPP
import django.db.backends.mysql.base

def skip_version_check(self):
    pass

django.db.backends.mysql.base.DatabaseWrapper.check_database_version_supported = skip_version_check
