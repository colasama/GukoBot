from pathlib import Path
from tortoise import Tortoise

from Guko.utils.log import log

# Forked from https://github.com/Kyomotoi/ATRI
# 临时的实现，寻求更好的方式！欢迎pr


DB_DIR = Path(".") / "data" / "sql"
DB_DIR.mkdir(parents=True, exist_ok=True)


async def run():
    import database.models

    await Tortoise.init(
        db_url=f"sqlite://{DB_DIR}/db.sqlite3",
        modules={"models": [locals()["models"]]},
    )
    await Tortoise.generate_schemas()


async def init_database():
    log.info("正在初始化数据库...")
    await run()
    log.success("数据库初始化完成")


async def close_database_connection():
    log.info("正在关闭数据库连接...")
    await Tortoise.close_connections()
    log.info("数据库成功关闭")
