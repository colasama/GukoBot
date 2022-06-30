from nonebot.plugin import on_keyword, PluginMetadata
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment
from pathlib import Path
import random

__plugin_meta__ = PluginMetadata(
    name='截图语录',
    description='截图说话！',
    usage='''使用 .你能想到的人名缩写 查看他们曾经说过的重要言语''',
    extra={'version': '0.0.1'}
)

RESOURCE_PATH = Path(".") / "Guko/resources/sayings"
keyword_list = ['fu', 'fufu', 'gst', 'gu', 'halfotaku', 'kira', 'motohg', 'pjsk', 'rui', 'wt', 'tls', ]
saying = on_keyword(keyword_list, priority=10)


@saying.handle()
async def _(bot: Bot, event: Event):
    # 截取命令本体
    saying_type = event.get_plaintext().strip(event.get_plaintext()[0])
    path = RESOURCE_PATH / saying_type
    file_list = path.glob(r"*")
    target = random.sample(list(file_list), k=1)[0]
    await saying.finish(MessageSegment.image(target))
