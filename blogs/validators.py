# -*- coding: utf-8 -*-
from rest_framework.exceptions import ValidationError
from wordplease.settings import BADWORDS


def badwords_detector(value):
    """
    valida si en value se han puesto tacos definidos en el settings.
    :param value:
    :return: Boolean
    """

    for badword in BADWORDS:
        if badword.lower() in value.lower():
            raise ValidationError(u'La palabra {0} no está permitida'.format(badword))

        # Si todo está bien devuelvo true
        return True

