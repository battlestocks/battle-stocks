class InputValidation:
    @staticmethod
    def start_or_quit(user_input):
        validated = user_input
        while validated.upper() not in ['Y', 'N']:
            validated = input('''
Please enter (y)es to start investing or (n)o to decline> ''')
        return validated.upper()
