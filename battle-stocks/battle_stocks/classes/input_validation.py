class InputValidation:
    @staticmethod
    def validate_start_quit(user_input):
        validated = user_input
        while validated.upper() not in ['Y', 'N']:
            validated = input('''
Please enter (y)es to start investing or (n)o to decline\n> ''')
        return validated.upper()

    @staticmethod
    def validate_buy_sell_quit(user_input):
        validated = user_input
        while validated.upper() not in ['B', 'S', 'Q']:
            validated = input('''
Now that you are intersted, you can either buy or sell stocks!

To buy stocks please enter: (b)uy
To sell stocks please enter: (s)ell
To quit please enter: (q)uit

> ''')
        return validated.upper()
