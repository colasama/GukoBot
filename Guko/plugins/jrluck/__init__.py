from . import luck
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment
# import Guko.plugins.nickname.nickname as nn
from nonebot.adapters.onebot.v11.message import Message
import random

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

    await jrluck.finish(Message(f'[CQ:at,qq={event.get_user_id()}]今天的人品是{luck_number}哦~ \
                                {MessageSegment.image(luck_pic_url)}'))
