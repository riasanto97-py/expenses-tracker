import sqlite3
from models import Expense

DB_NAME = "expenses.db"  # ΟΝΟΜΑ ΤΗΣ SQLITE ΒΑΣΗΣ

def create_table():
    """ΔΗΜΙΟΥΡΓΕΙ ΤΟΝ ΠΙΝΑΚΑ EXPENSES ΑΝ ΔΕΝ ΥΠΑΡΧΕΙ ΗΔΗ."""
    conn = sqlite3.connect(DB_NAME)  # ΑΝΟΙΓΜΑ ΣΥΝΔΕΣΗΣ ΜΕ ΤΗ ΒΑΣΗ
    cursor = conn.cursor()  # CURSOR: ΑΝΤΙΚΕΙΜΕΝΟ ΓΙΑ ΕΚΤΕΛΕΣΗ SQL ΕΝΤΟΛΩΝ

    # ΔΗΜΙΟΥΡΓΙΑ ΠΙΝΑΚΑ ΜΕ ΤΟΥΣ ΤΥΠΟΥΣ ΔΕΔΟΜΕΝΩΝ ΚΑΙ ΤΑ ΥΠΟΧΡΕΩΤΙΚΑ ΠΕΔΙΑ
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        date TEXT NOT NULL
    )
    """)

    conn.commit()  # ΑΠΟΘΗΚΕΥΣΗ ΑΛΛΑΓΩΝ ΣΤΗΝ ΒΑΣΗ
    conn.close()   # ΚΛΕΙΣΙΜΟ ΤΗΣ ΣΥΝΔΕΣΗΣ

def add_expense(expense: Expense):
    """ΠΡΟΣΘΗΚΗ ΝΕΟΥ ΕΞΟΔΟΥ ΣΤΗ ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ."""
    conn = sqlite3.connect(DB_NAME)  # ΑΝΟΙΓΜΑ ΣΥΝΔΕΣΗΣ ΜΕ ΤΗ ΒΑΣΗ
    cursor = conn.cursor()  # CURSOR ΓΙΑ ΕΚΤΕΛΕΣΗ SQL ΕΝΤΟΛΩΝ

    # ΕΙΣΑΓΩΓΗ ΤΩΝ ΔΕΔΟΜΕΝΩΝ ΣΤΗ ΒΑΣΗ ΜΕ PLACEHOLDERS ΓΙΑ ΠΡΟΣΤΑΣΙΑ ΑΠΟ SQL INJECTION
    cursor.execute("""
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    """, (expense.amount, expense.category, expense.description, expense.date))

    conn.commit()  # ΑΠΟΘΗΚΕΥΣΗ ΑΛΛΑΓΩΝ
    conn.close()   # ΚΛΕΙΣΙΜΟ ΤΗΣ ΣΥΝΔΕΣΗΣ

def get_expenses():
    """ΕΠΙΣΤΡΟΦΗ ΟΛΩΝ ΤΩΝ ΕΞΟΔΩΝ ΑΠΟ ΤΗ ΒΑΣΗ."""
    conn = sqlite3.connect(DB_NAME)  # ΑΝΟΙΓΜΑ ΣΥΝΔΕΣΗΣ
    cursor = conn.cursor()  # CURSOR ΓΙΑ ΕΚΤΕΛΕΣΗ SQL

    cursor.execute("SELECT * FROM expenses")  # * ΣΗΜΑΙΝΕΙ ΟΛΑ ΤΑ ΠΕΔΙΑ
    rows = cursor.fetchall()  # ΛΗΨΗ ΟΛΩΝ ΤΩΝ ΑΠΟΤΕΛΕΣΜΑΤΩΝ ΩΣ ΛΙΣΤΑ TUPLES

    conn.close()  # ΚΛΕΙΣΙΜΟ ΤΗΣ ΣΥΝΔΕΣΗΣ
    return rows  # ΕΠΙΣΤΡΟΦΗ ΤΗΣ ΛΙΣΤΑΣ ΕΞΟΔΩΝ

def delete_expense(expenses_id: int):
    """ΔΙΑΓΡΑΦΗ ΕΞΟΔΟΥ ΑΠΟ ΤΗ ΒΑΣΗ ΒΑΣΕΙ ΤΟΥ ID."""
    conn = sqlite3.connect(DB_NAME)  # ΑΝΟΙΓΜΑ ΣΥΝΔΕΣΗΣ
    cursor = conn.cursor()  # CURSOR ΓΙΑ ΕΚΤΕΛΕΣΗ SQL

    # ΔΙΑΓΡΑΦΗ ΤΟΥ ΕΞΟΔΟΥ ΜΕ ΤΟ ΣΥΓΚΕΚΡΙΜΕΝΟ ID
    cursor.execute("DELETE FROM expenses WHERE id=?", (expenses_id,))

    conn.commit()  # ΑΠΟΘΗΚΕΥΣΗ ΑΛΛΑΓΩΝ
    conn.close()   # ΚΛΕΙΣΙΜΟ ΤΗΣ ΣΥΝΔΕΣΗΣ
