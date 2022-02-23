from battle_stocks.utils.constants import SYMBOL

class InputValidation:

    @staticmethod
    def validate_start_quit(user_input):
        validated = user_input
        while validated.upper() not in ['Y', 'N']:
            validated = input('''
Please enter (y)es to start investing or (n)o to decline\n> ''')
        return validated.upper()

    @staticmethod
    def validate_command(user_input, prompt):
        validated = user_input
        while validated.upper() not in ['B', 'S', 'Q', 'D', 'W', 'P']:
            validated = input(prompt)
        return validated.upper()

    @staticmethod
    def validate_user_name(user_input, prompt):
        validated = user_input
        while validated == '':
            validated = input(prompt)
        return validated.upper()

    @staticmethod
    def validate_company_name(user_input, prompt):
        validated = user_input
        while validated.upper() not in SYMBOL:
            validated = input(f'\n{validated.upper()} is not available.\n\n {prompt}')
        return validated.upper()

    @staticmethod
    def validate_numbers(user_input, prompt):
        validated = user_input
        while True:
            try:
                validated = float(validated)
                break
            except:
                validated = input(prompt)
        return validated
