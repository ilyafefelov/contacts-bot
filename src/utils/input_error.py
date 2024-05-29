def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return "Contact or Note not found." + str(e)
        except ValueError as e:
            return "Invalid command usage." + str(e)
        except IndexError as e:
            return "Invalid command usage. Insufficient arguments provided. Please provide all required information." + str(e)
        except UnboundLocalError as e:
            return "Invalid command usage." + str(e)
    return inner
