class Letter:
    """
    Base class of letter
    """
    def __init__(self, email, name, from_email, subject, send_time, proxies, letter_id=None):
        self._email = email
        self._name = name
        self._from_email = from_email
        self._subject = subject
        self._send_time = send_time
        self._proxies = proxies
        self._letter = None
        self._letter_id = letter_id

    @property
    def email(self):
        """
        :return: Email address to which the letter was sent.
        """
        return self._email

    @property
    def name(self):
        """
        :return: Name of the person who sent the letter.
        """
        return self._name

    @property
    def from_email(self):
        """
        :return: Email address from which the email was sent.
        """
        return self._from_email

    @property
    def subject(self):
        """
        :return: Subject of letter.
        """
        return self._subject

    @property
    def send_time(self):
        """
        :return: Datetime when letter sent.
        """
        return self._send_time

    @property
    def letter(self):
        """
        :return: Content of letter.
        """
        return ''

    def __repr__(self):
        return f"<Letter name={self._name} from_email={self._from_email} email={self._email} subject={self._subject} send_time={self._send_time.strftime('%Y-%m-%d %H:%M:%S')}>"

    def __hash__(self):
        return hash(self._letter_id)
