class UserNotFoundException(Exception):
    """ This shouls be thrown when the user is not found in the repository."""
    pass


class UserAlreadyExistException(Exception):
    """ This shouls be thrown when the user is already exist in the repository."""
    pass


class ValuesNullException(Exception):
    """ This shouls be thrown when the user has null or empty """
    pass
