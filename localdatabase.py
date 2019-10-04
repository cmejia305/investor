import psycopg2
userName = ""
password = ""
try:
    conn = psycopg2.connect(
        database="invest",
        user="postgres",
        password="6108",
        host="127.0.0.1",
        port="5432"
    )

    def retrieveAllUserInfo(user, passW):
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM auth WHERE username='{user}' AND pass='{passW}'")
        rows = cursor.fetchall()
        if(rows):
            for row in rows:
                role = row[2]
            if(role == "administrator"):
                print(f"{user}, you have been authenticated. You're an admnistrator")
            else:
                print(f"{user}, you have been authenticated. You're a user")
        else:
            print("User does not exist")
        cursor.close()
    userNameInput = input("Enter your username >> ")
    passwordInput = input("Enter your password >> ")
    retrieveAllUserInfo(userNameInput, passwordInput)
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data frm your database", error)
