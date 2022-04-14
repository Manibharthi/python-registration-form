import sqlite3
class database:
    def __init__(self, db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS EMPLOYEE(
            id Integer Primary Key, 
            name text, 
            age text, 
            doj text, 
            email text, 
            gender text, 
            contact text, 
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, name, age, doj, email, gender, contact, address):
        
        self.cur.execute("insert into Employee values (NULL,?, ?, ?, ?, ?, ?,?)",
                            (name, age, doj, email, gender, contact, address))
        self.con.commit()    

    

    def fetch(self):
        self.cur.execute("SELECT * FROM EMPLOYEE")
        rows=self.cur.fetchall()
        # print(rows)
        return rows

    def remove(self,id):
        self.cur.execute("delete from employee where id=?",(id,))
        self.con.commit()

    def update(self, id, name, age, doj, email, gender, contact, address):
         self.cur.execute("update Employee set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?",
                            (name, age, doj, email, gender, contact, address, id))
         self.con.commit()

             

# obj=database("Employee.db")
# obj.insert("samfg", "22", "27-02-2022", "rakumar@gmail.com", "female", "8372459354", "bridge")
# obj.fetch()
# obj.remove("12")
# obj.update("2", "sham" , "35", "12-2-2022", "mani@gmail.com","male", "4532165312", "bengal")
