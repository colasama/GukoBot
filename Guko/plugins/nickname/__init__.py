from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment
from nonebot.adapters.onebot.v11.message import Message
import aiosqlite


async def get_nickname(user_id): # 我震撼了，这玩意可以自动close()
    values = []
    async with aiosqlite.connect("C:/Users/Administrator/Documents/eatwhat_bot/plugins/Nickname.db") as conn:
        async with conn.execute('SELECT nickname FROM NAME WHERE user_id=? ', (user_id,)) as c:
            values = await c.fetchone()
            print(values[0])
            if values is None:
                return None
    return values[0]


async def insert(user_id,name):
    conn = await aiosqlite.connect("C:/Users/Administrator/Documents/eatwhat_bot/plugins/Nickname.db")
    c = await conn.execute('SELECT nickname FROM NAME WHERE user_id=? ',(user_id,))
    res = await c.fetchone()
    if(res != None):
        await c.execute('UPDATE name SET nickname=? WHERE user_id=?',(name,user_id))
    else:
        await c.execute('INSERT INTO name VALUES (?,?)',(user_id,name))  
    await conn.commit()
    await c.close()
    await conn.close()


@on_command('nn', only_to_me=False)
async def nn(session: CommandSession):
    nickname = session.get('nickname', prompt='想要鸽子姬怎么称呼你呢？')

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


async def get_nickname_done(qq: str,nickname: str) -> str:
    await insert(qq,nickname)
    return f'已将名字更改为{nickname}√ 真是一个好听的名字惹！'