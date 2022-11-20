class Global:
    code = {
        "a001": {"debit": ["Inventory"], "credit": ["Cash"]},
        "a002": {"debit": ["Inventory"], "credit": ["Accounts Payable"]},
        "a003": {"debit": ["Inventory"], "credit": ["Notes Payable"]},
        "b001": {"debit": ["Cash"], "credit": ["Inventory"]},
        "b002": {"debit": ["Accounts Payable"], "credit": ["Inventory"]},
        "b003": {"debit": ["Notes Payable"], "credit": ["Inventory"]},
        "c001": {"debit": ["Cash"], "credit": ["Sales Revenue"]},
        "c002": {"debit": ["Accounts Receivable"], "credit": ["Sales Revenue"]},
        "c003": {"debit": ["Notes Receivable"], "credit": ["Sales Revenue"]},
        "c004": {"debit": ["Cost of Goods Sold"], "credit": ["Inventory"]},
        "d001": {"debit": ["Inventory"], "credit": ["Cash"]},
        "d002": {"debit": ["Inventory"], "credit": ["Accounts Receivable"]},
        "d003": {"debit": ["Inventory"], "credit": ["Notes Receivable"]},
        "d004": {"debit": ["Inventory"], "credit": ["Cost of Goods Sold"]},
        "e001": {"debit": ["Inventory(adj.)"], "credit": ["Inventory"]},
        "e002": {"debit": ["Inventory"], "credit": ["Inventory(adj.)"]},
    }
