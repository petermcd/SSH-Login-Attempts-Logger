import requests
import config
import sqlite3


class LoginExtractor:
    def __init__(self):
        self.retrieve_login_attempts(config.DatabasePath)

    def log_attempt(self,
                    identifier: int,
                    username: str = "",
                    password: str = "",
                    host: str = "",
                    when: str = ""
                    ) -> int:
        data = '''{{
                    "TableName": "ssh-login-attempts",
                    "Item": {{
                        "id": {},
                        "username": "{}",
                        "password": "{}",
                        "host": "{}",
                        "when": "{}"
                    }}}}'''.format(identifier, username, password, host, when)
        request = requests.post(config.URL,
                                data=data,
                                headers={"x-api-key": config.API_Key}
                                )
        if request.status_code == 200:
            return True
        return False

    def retrieve_login_attempts(self, database_path: str):
        dbh = sqlite3.connect(database_path)
        select_sql = '''SELECT `id`, `username`, `password`, `host`, `when`
                 FROM logins
                 WHERE `processed` = 0;'''
        cursor = dbh.cursor()
        update_list = []
        for row in cursor.execute(select_sql):
            send = self.log_attempt(row[0], row[1], row[2], row[3], row[4])
            if send:
                update_list.append(row[0])
        update_sql = '''UPDATE logins SET `processed` = 1 WHERE `id` = ?;'''
        for update in update_list:
            cursor.execute(update_sql, [update])
        dbh.commit()
        dbh.close()


LoginExtractor()
