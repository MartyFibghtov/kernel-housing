from typing import Dict


def response_wrap(data: Dict = None, ok: bool = True, message: str = None) -> Dict:
    """Wrap response dict into standard api format

    Example:
    {
        result: data
        success: true
        message: Everything went fine
    }
    """

    return {'result': data, 'success': ok, 'message': message}
