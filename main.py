
            

import datetime
from database import create_table, add_expense, get_expenses, delete_expense
from models import Expense

# ΔΗΜΙΟΥΡΓΙΑ ΤΟΥ ΠΙΝΑΚΑ ΣΤΗ ΒΑΣΗ (ΑΝ ΔΕΝ ΥΠΑΡΧΕΙ ΗΔΗ)
create_table()

def main_menu():  # ΤΟ ΚΥΡΙΟ ΜΕΝΟΥ ΤΟΥ ΠΡΟΓΡΑΜΜΑΤΟΣ
    while True:
        print("\n---EXPENSES TRACKER---")
        print("1. ΠΡΟΣΘΗΚΗ ΝΕΟΥ ΕΞΟΔΟΥ")
        print("2. ΠΡΟΒΟΛΗ ΟΛΩΝ ΤΩΝ ΕΞΟΔΩΝ")
        print("3. ΔΙΑΓΡΑΦΗ ΕΞΟΔΟΥ")
        print("4. ΕΞΟΔΟΣ")

        choice = input("\nΕΠΙΛΕΞΤΕ ΜΙΑ ΕΝΕΡΓΕΙΑ (1-4): ")

        if choice == "1":  # ΠΡΟΣΘΗΚΗ ΝΕΟΥ ΕΞΟΔΟΥ
            while True:
                try:  # ΕΛΕΓΧΟΣ ΓΙΑ ΣΩΣΤΟ ΠΟΣΟ
                    amount_input = input("\nΠΟΣΟ ΕΞΟΔΟΥ: ").strip()
                    amount = float(amount_input.replace(',', '.'))
                    if amount <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("\nΛΑΘΟΣ ΠΟΣΟ! ΔΩΣΤΕ ΕΝΑ ΘΕΤΙΚΟ ΑΡΙΘΜΟ.")

            category = input("\nΚΑΤΗΓΟΡΙΑ (π.χ FOOD, TRANSPORT): ").strip()
            description = input("\nΠΕΡΙΓΡΑΦΗ: ").strip()

            while True:  # ΕΛΕΓΧΟΣ ΓΙΑ ΣΩΣΤΗ ΗΜΕΡΟΜΗΝΙΑ
                date = input("\nΗΜΕΡΟΜΗΝΙΑ (YYYY-MM-DD): ").strip()
                try:
                    datetime.datetime.strptime(date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("\nΛΑΘΟΣ ΜΟΡΦΗ ΗΜΕΡΟΜΗΝΙΑΣ! ΧΡΗΣΙΜΟΠΟΙΗΣΤΕ YYYY-MM-DD.")

            expense = Expense(amount, category, description, date)
            add_expense(expense)
            print("\nΤΟ ΕΞΟΔΟ ΠΡΟΣΤΕΘΗΚΕ ΜΕ ΕΠΙΤΥΧΙΑ!")

        elif choice == "2":  # ΠΡΟΒΟΛΗ ΟΛΩΝ ΤΩΝ ΕΞΟΔΩΝ
            expenses = get_expenses()
            if not expenses:
                print("\nΔΕΝ ΥΠΑΡΧΟΥΝ ΕΞΟΔΑ")
            else:
                # ΜΟΡΦΟΠΟΙΗΣΗ ΣΕ ΠΙΝΑΚΑ
                print(f"{'ID':<3} | {'ΗΜΕΡΟΜΗΝΙΑ':<12} | {'ΚΑΤΗΓΟΡΙΑ':<15} | {'ΠΟΣΟ':<8} | {'ΠΕΡΙΓΡΑΦΗ'}")
                print("-" * 65)

                for exp in expenses:
                    print(f"{exp[0]:<3} | {exp[4]:<12} | {exp[2]:<15} | {exp[1]:<8.2f} | {exp[3]}")

        elif choice == "3":  # ΔΙΑΓΡΑΦΗ ΕΞΟΔΟΥ
            expenses = get_expenses()
            if not expenses:
                print("\nΔΕΝ ΥΠΑΡΧΟΥΝ ΕΞΟΔΑ ΓΙΑ ΔΙΑΓΡΑΦΗ!")
            else:
                while True:
                    try:
                        expenses_id_input = input("\nΔΩΣΕ ΤΟ ID ΤΟΥ ΕΞΟΔΟΥ ΠΟΥ ΘΕΛΕΤΕ ΝΑ ΔΙΑΓΡΑΨΕΤΕ: ").strip()
                        expenses_id = int(expenses_id_input)
                        if expenses_id <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print("\nΛΑΘΟΣ ID! ΔΩΣΤΕ ΕΝΑ ΘΕΤΙΚΟ ΑΚΕΡΑΙΟ ΑΡΙΘΜΟ.")

                delete_expense(expenses_id)
                print("\nΤΟ ΕΞΟΔΟ ΔΙΑΓΡΑΦΗΚΕ ΜΕ ΕΠΙΤΥΧΙΑ!")

        elif choice == "4":
            print("\nΕΞΟΔΟΣ ΑΠΟ ΤΟ ΠΡΟΓΡΑΜΜΑ. ΚΑΛΗ ΣΥΝΕΧΕΙΑ!")
            break
        else:
            print("\nΛΑΘΟΣ ΕΠΙΛΟΓΗ. ΕΠΙΛΕΞΤΕ ΞΑΝΑ (1-4)")

if __name__ == "__main__":
    main_menu()
