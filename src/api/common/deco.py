import json
import logging
import pprint
from functools import wraps


logger = logging.getLogger("api")


def logging(message):
    """
    Request Logging
    :return: response
    """

    def wrapper(function):
        @wraps(function)
        def inner(*args, **kwargs):
            logger.info(message)
            res = function(*args, **kwargs)
            method = res.request.method
            url = res.request.url
            body = res.request.body
            status = res.status_code
            body_sep = "\n"
            log_request = f"Request method: {method}, url: {url}"
            if body is not None:
                try:
                    json_body = json.dumps(json.loads(body.decode("utf-8")), indent=4, ensure_ascii=False)
                    logger.info(log_request + f", body:{body_sep}{json_body or pprint.pformat(body)}")
                except AttributeError:
                    logger.info(log_request + f", body:{body}")
            log_response = f"Response method: {method}, url: {url}, status: {status}"
            try:
                body = res.json()
                res_text = body_sep + json.dumps(body, indent=4, ensure_ascii=False) if len(res.content) > 20 \
                    else json.dumps(body)
            except Exception:  # JSONDecodeError не ловился этот ексепшен
                res_text = res.text[:120] + "..." if len(res.text) > 120 else res.text
            logger.info(log_response + f", body: {res_text}")
            return res

        return inner

    return wrapper
