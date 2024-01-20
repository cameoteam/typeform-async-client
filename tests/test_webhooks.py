# third-party imports
import pytest

# locale imports
from atypeform.schemas.webhooks import CreateRequestBodyModel
from atypeform.schemas.webhooks import CreateResponseBodyModel
from atypeform.schemas.webhooks import GetResponseBodyModel
from atypeform.settings import ApiRouter
from atypeform.webhooks import Webhooks


class TestWebhooks:

    _router = ApiRouter()
    _router.__head__ = "https://api.typeform.com"

    # webhook
    form_id = "Xc3tLQwC"
    tag = "child"

    async def test_get_list(self, client):
        webhooks = Webhooks(client, self._router)
        response = await webhooks.get(self.form_id)
        print(response)
        assert False
        assert isinstance(response, GetResponseBodyModel)

    async def test_create(self, client):
        webhooks = Webhooks(client, self._router)
        response = await webhooks.create(
            self.form_id,
            "child",
            {
                "enabled": True,
                "url": "https://7c71-185-211-158-168.ngrok-free.app/webhook/Xc3tLQwC",
            }
        )
        assert isinstance(response, CreateResponseBodyModel)

    @pytest.mark.skip
    async def test_delete(self, client):
        if not self.form_id:
            return

        webhooks = Webhooks(client, self._router)
        response = await webhooks.delete(self.form_id, self.tag)
        assert response.status == 204
