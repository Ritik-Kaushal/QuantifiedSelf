from flask import after_this_request, request
from werkzeug.datastructures import ImmutableMultiDict
from flask_security.decorators import anonymous_user_required
from flask_security.proxies import _security
from flask_security.registerable import register_user
from flask_security.utils import base_render_json, suppress_form_csrf, view_commit
from flask.typing import ResponseValue
from utils.jwt_token_utils import generate_jwt_token

@anonymous_user_required
def register() -> "ResponseValue":
    """Function which handles a registration request."""

    form_class = _security.register_form

    if request.is_json:
        form_data: ImmutableMultiDict = ImmutableMultiDict(request.get_json())
        
    # Raise an exception here of request is not json
    User=None
    jwt_token=None
    form = form_class(form_data, meta=suppress_form_csrf())
    if form.validate_on_submit(): # Checks for valid form details
        after_this_request(view_commit)
        User = register_user(form)
        form.user = User
    if User is not None:
        jwt_token = generate_jwt_token(User)
    return base_render_json(form,additional={"jwt_token":jwt_token})
