import base64


def generate_key_from_dict(data: dict):
    result = ''

    for key in data:
        result += str(key) + str(data.get(key))

    result = str(
        base64.b64encode(
            result.encode()
        )
    )

    return result
