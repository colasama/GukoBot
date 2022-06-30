from nonebot.plugin import on_keyword, PluginMetadata
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment
from nonebot.adapters.onebot.v11.message import Message
import random
from . import meal

__plugin_meta__ = PluginMetadata(
    name='今天吃什么',
    description='今天吃什么捏',
    usage='''使用 .eatwhat 获取不正经的饭饭
             使用 .eat 获取正儿八经的饭饭
             使用 .eats 获取百航校内食堂の推荐
             食物添加修改功能正在重构中''',
    extra={'version': '0.0.1'}
)

eatwhat = on_keyword(['eat', 'eatwhat', 'eats'], priority=10)


@eatwhat.handle()
async def _(bot: Bot, event: Event):
    # 截取命令本体
    meal_type = event.get_plaintext().strip(event.get_plaintext()[0])
    what_to_eat = meal.get_random_meal(meal_type)
    await eatwhat.finish(f'今天去吃{what_to_eat}吧！')
