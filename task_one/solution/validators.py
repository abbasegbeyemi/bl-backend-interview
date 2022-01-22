from __future__ import annotations
from smart_open import open
from pathlib import Path


class PasswordValidator:
    def __init__(self, password: str):
        self._password = password
        self._errors = {}

    @property
    def errors(self):
        return self._errors

    def not_common(self) -> PasswordValidator:
        """
        Check that the password is not included in the list of common passwords
        :return:
        :rtype:
        """
        common_passwords_file = Path(__file__).parents[1] / "common-passwords.txt"
        if str(self._password) in (passwd.rstrip() for passwd in open(common_passwords_file)):
            # We assume that having to change the password is a single step
            self._errors["not_common"] = 1
        return self

    def has_length(self, minimum: int = 7, maximum: int = 25) -> PasswordValidator:
        """
        Check that the password has the required length
        :param minimum:
        :type minimum:
        :param maximum:
        :type maximum:
        :return:
        :rtype:
        """
        # Number of changes is the number of characters to add or subtract
        if len(str(self._password)) < minimum:
            self._errors["length"] = minimum - len(str(self._password))
        elif len(str(self._password)) > maximum:
            self._errors["length"] = len(str(self._password)) - maximum

        return self

    def non_repeat(self):
        """
        Check that the password has no repeating characters.
        :return:
        :rtype:
        """
        repeat_flag = 0
        repeat_alert = False
        curr_char = ""
        for character in str(self._password):
            prev_char, curr_char = curr_char, character
            if prev_char == curr_char:
                if repeat_alert:
                    repeat_flag += 1
                else:
                    repeat_alert = True
            else:
                repeat_alert = False

        if repeat_flag:
            self._errors["non_repeat"] = repeat_flag
        return self

    def is_alphanumeric(self):
        """
        Check that the password is alphanumeric. At least one Uppercase, Lowercase, and digit
        :return:
        :rtype:
        """
        no_uppercase = True
        no_lowercase = True
        no_digit = True
        for character in self._password:
            # Check for numeric
            if character.isdigit():
                no_digit = False
            elif character.islower():
                no_lowercase = False
            elif character.isupper():
                no_uppercase = False

        err_count = sum([no_uppercase, no_digit, no_lowercase])
        if err_count:
            self._errors["is_alphanumeric"] = err_count
        return self

    def error_report(self):
        return sum(self.errors.values())
