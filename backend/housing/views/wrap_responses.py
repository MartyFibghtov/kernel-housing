from typing import Dict


def response__wrap(data: Dict = None, ok: bool = True, message: str = None, error_code: int =200) -> Dict:
    """Wrap response dict into standard api format

    Example:
    {
        result: data
        success: true
        message: Everything went fine
    }
    """

    if not ok:
        return

    return {'result': data, 'success': ok, 'message': message}
