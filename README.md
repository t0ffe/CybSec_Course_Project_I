# Cyber Security Course Project I

## Todo-app
#### Can the flaws outlined below be implemented in a TODO app?

1. Yes. The TODOs are saved in a db.
2. Yes. Accounts for the users.
3. Yes. Same as #2.
4. Yes. Possiibility of seeing TODOs that one has no permissions to.
5. Yes. Log logins / TODOs.
***

## 5 Flaws from OWASP

1. [**A03:2021-Injection**](https://owasp.org/Top10/A03_2021-Injection/): Introduce SQL Injection by directly concatenating user inputs into a database query. Fix it by using parameterized queries or using methods provided by Django.

2. [**A07:2021-Identification and Authentication Failures**](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/): Permits default, weak, or well-known passwords, such as "Password1" or "admin/admin". Fix it by not allowing such passwords.

3. [**A02:2021-Cryptographic Failures**](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/): Uses plain text, encrypted, or weakly hashed passwords data stores. Fix it by ensuring passwords are hashed securely.

4. [**A01:2021-Broken Access Control**](https://owasp.org/Top10/A01_2021-Broken_Access_Control/): Bypassing access control checks by modifying the URL.

5. [**A09:2021-Security Logging and Monitoring Failures**](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/): Auditable events, such as logins, failed logins, and high-value transactions, are not logged. Fix it by logging them.
