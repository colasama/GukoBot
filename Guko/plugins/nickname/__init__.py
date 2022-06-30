from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment
from nonebot.adapters.onebot.v11.message import Message
from . import db


nn = on_keyword(['nn', 'nickname'], priority=10)


@nn.handle()
async def _(bot: Bot, event: Event):
    nickname = nn.got('nickname', prompt='想要鸽子姬怎么称呼你呢？')

    nn_report = await get_nicknamedone(str(session.ctx['user_id']),nickname)
    await session.send(nn_report)


@nn.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['nickname'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('可不能没有名字喔，再想一个吧！')

    session.state[session.current_key] = stripped_arg


async def get_nickname_done(user_id: str, nickname: str) -> str:
    await db.add_nickname(user_id, nickname)
    return f'已将名字更改为{nickname}√ 真是一个好听的名字惹！'
