from django.conf import settings


def split_number(number):
    """Parse number card string"""
    number = str(number)
    spl = [number[i:i + 4] for i in range(0, len(number), 4)]
    return "{0}-{1}-{2}-{3}".format(*spl)


def check_attempts(card):
    """Count attempts and check MAX_ATTEMPTS limit"""
    if card.attempts < settings.MAX_ATTEMPTS:
        return {"success": True}
    card.is_active = False
    card.save()
    return {"success": False, "message": ('Your account has been locked '
                                          'out because of too many '
                                          'failed login attempts.')}


def check_is_active(card):
    if card.is_active:
        return {"success": True}
    return {"success": False, "message": 'Card is locked'}


def check_existence(card):
    if card:
        return {"success": True}
    return {"success": False, "message": "The card does not exist"}


def check_auth(card, auth):
    if auth:
        return {"success": True}

    card.attempts += 1
    response = check_attempts(card)
    if not response['success']:
        return response
    card.save()

    return {"success": False,
            "message": 'Invalid PIN. Left {0} attempts'.format(
                settings.MAX_ATTEMPTS - card.attempts)}
