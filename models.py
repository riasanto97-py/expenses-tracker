class Expense:
    """ Η ΚΛΑΣΗ EXPENSE ΑΝΑΠΑΡΙΣΤΑ ΕΝΑ ΕΞΟΔΟ ΠΟΥ ΚΑΤΑΧΩΡΕΙ Ο ΧΡΗΣΤΗΣ.
    amount: ΤΟ ΠΟΣΟ ΤΟΥ ΕΞΟΔΟΥ
    category: Η ΚΑΤΗΓΟΡΙΑ (π.χ food, transport)
    description: ΣΥΝΤΟΜΗ ΠΕΡΙΓΡΑΦΗ
    date: Η ΗΜΕΡΟΜΗΝΙΑ ΤΟΥ ΕΞΟΔΟΥ
    """

    def __init__(self, amount, category, description, date):
        """ CONSTRUCTOR ΤΗΣ ΚΛΑΣΗΣ.
        ΔΗΜΙΟΥΡΓΕΙ ΕΝΑ ΝΕΟ ΑΝΤΙΚΕΙΜΕΝΟ EXPENSE ΚΑΙ ΑΠΟΘΗΚΕΥΕΙ
        ΤΑ ΔΕΔΟΜΕΝΑ ΠΟΥ ΔΙΝΕΙ Ο ΧΡΗΣΤΗΣ.
        """

        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def __repr__(self):
        """ ΚΑΘΟΡΙΖΕΙ ΠΩΣ ΘΑ ΕΜΦΑΝΙΖΕΤΑΙ ΤΟ ΑΝΤΙΚΕΙΜΕΝΟ ΟΤΑΝ ΤΟ ΚΑΝΟΥΜΕ PRINT.
        """

        return f"{self.date} | {self.category} | {self.amount} | {self.description}"
        
