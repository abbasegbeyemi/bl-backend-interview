from task_one.solution.validators import PasswordValidator
import pytest


@pytest.mark.parametrize("password_input, error_expected",
                         [
                             ("password", 1),
                             ("L33TC0d3", None)
                         ])
def test_check_for_common_passwords(password_input, error_expected):
    """
    Test that the password does not appear in the common passwords file.
    :return:
    :rtype:
    """
    validated_password = PasswordValidator(password_input).not_common()
    assert validated_password.errors.get("not_common") == error_expected


@pytest.mark.parametrize("password_input, error_expected",
                         [
                             ("sixlen", 1),
                             ("length1Ten", None),
                             ("veryLongPasswordOver25Characters", 7),
                         ])
def test_password_within_required_length(password_input, error_expected):
    """
    Test that the password falls within the required length
    :param password_input:
    :type password_input:
    :param error_expected:
    :type error_expected:
    :return:
    :rtype:
    """
    validated_password = PasswordValidator(password_input).has_length()
    assert validated_password.errors.get("length") == error_expected


@pytest.mark.parametrize("password_input, error_expected",
                         [
                             ("aBBBcdef", 1),
                             ("fgHHHHerdf", 2),
                             ("abcdefgh", None),
                         ])
def test_password_has_no_repeated_characters(password_input, error_expected):
    """
    Test that the password has no repeated characters
    :param password_input:
    :type password_input:
    :param error_expected:
    :type error_expected:
    :return:
    :rtype:
    """
    validated_password = PasswordValidator(password_input).non_repeat()
    assert validated_password.errors.get("non_repeat") == error_expected


@pytest.mark.parametrize("password_input, error_expected",
                         [
                             ("abcdefg", 2),
                             ("a1234ghy", 1),
                             ("Abcd3fg", None),
                         ])
def test_password_is_alphanumeric(password_input, error_expected):
    """
    Test that the password is alphanumeric
    :param password_input:
    :type password_input:
    :param error_expected:
    :type error_expected:
    :return:
    :rtype:
    """
    validated_password = PasswordValidator(password_input).is_alphanumeric()
    assert validated_password.errors.get("is_alphanumeric") == error_expected


@pytest.mark.parametrize("password_input, error_expected",
                         [
                             ("password", 3),
                             ("z", 8),
                             ("aA1", 4),
                             ("1377C0d3", 0),
                         ])
def test_task_examples(password_input, error_expected):
    """
    Using the example testcases
    :param password_input:
    :type password_input:
    :param error_expected:
    :type error_expected:
    :return:
    :rtype:
    """

    validated_password = PasswordValidator(
        password_input
    ).non_repeat().not_common().has_length().is_alphanumeric()
    assert validated_password.error_report() == error_expected
