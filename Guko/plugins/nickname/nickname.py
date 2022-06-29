import random
import os
import aiosqlite
import time
import asyncio
from functools import wraps

async def search(user_id):
    values=[]
    async with aiosqlite.connect("../Nickname.db") as conn:
        async with conn.execute('SELECT * FROM NAME WHERE user_id=? ',(user_id,)) as c:
            values = await c.fetchone()
            print(values)
            await c.close()
        await conn.close()
    return values[0]

async def getNickname(user_id): # 我震撼了，这玩意可以自动close()
    values = []
    async with aiosqlite.connect("../Nickname.db") as conn:
        async with conn.execute('SELECT nickname FROM NAME WHERE user_id=? ',(user_id,)) as c:
            values = await c.fetchone()
            print(values[0])
            if(values == None):
                return None
    return values[0]

async def insert(user_id,name):
    conn = await aiosqlite.connect("../Nickname.db")
    c = await conn.execute('SELECT nickname FROM NAME WHERE user_id=? ',(user_id,))
    res = await c.fetchone()
    if(res != None):
        await c.execute('UPDATE name SET nickname=? WHERE user_id=?',(name,user_id))
    else:
        await c.execute('INSERT INTO name VALUES (?,?)',(user_id,name))  
    await conn.commit()
    await c.close()
    await conn.close()

# if __name__ =="__main__":
#     start = time.time()
#     asyncio.run(getNickname("719147538"))
    
#     # asyncio.run(insert("719112555","1111"))
#     end = time.time()
#     print(end-start)