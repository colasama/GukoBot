from . import luck
from nonebot.plugin import on_keyword, PluginMetadata
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment
# import Guko.plugins.nickname.nickname as nn
from nonebot.adapters.onebot.v11.message import Message
import random

__plugin_meta__ = PluginMetadata(
    name='今日人品',
    description='查看你今天的人品值并抽签！',
    usage='''使用 .jrluck 查看你的人品值并抽签''',
    extra={'version': '0.0.1'}
)

jrluck = on_keyword(['jrluck', 'jrrp', 'luck'], priority=10)


@jrluck.handle()
async def _(bot: Bot, event: Event):
    luck_number = luck.random_rp(event.get_user_id())
    luck_pic_url = luck.random_luck(event.get_user_id())

    # nn = await nn.getNickname(event.get_user_id())

    # if (nn != None):
    #     res = str(nn) + "今天的人品是" + str(luck_number) + "哦~"
    # else:
    #     res = str(session.ctx['sender']['nickname']) + "今天的人品是" + str(what) + "哦~"
    if event.get_event_name() == "message.private.friend":
        await jrluck.finish(Message(f'你今天的人品是{luck_number}哦~ \
                                    {MessageSegment.image(luck_pic_url)}'))
    else:
        await jrluck.finish(Message(f'[CQ:at,qq={event.get_user_id()}]今天的人品是{luck_number}哦~ \
                                            {MessageSegment.image(luck_pic_url)}'))