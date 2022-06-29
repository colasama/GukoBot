import pytest
from nonebug import App

from tests.utils import make_fake_message, make_fake_event


@pytest.mark.asyncio
async def test_plugin_jrluck(app: App):
    from Guko.plugins.jrluck import jrluck

    Message = make_fake_message()

    async with app.test_matcher(jrluck) as ctx:
        bot = ctx.create_bot()

        msg = Message("/jrluck")
        event = make_fake_event(_message=msg)()

        ctx.receive_event(bot, event)
        ctx.should_call_send(event, "tests", False)
        ctx.should_finished()
