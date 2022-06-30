from Guko.database import Nickname


async def add_nickname(user_id: int, nickname: str):
    await Nickname.create(user_id=user_id, nickname=nickname)


async def update_nickname(user_id: int, nickname: str):
    await Nickname.filter(user_id=user_id).update(
        user_id=user_id, nickname=nickname
    )


async def get_nickname(user_id: int):
    return await Nickname.filter(user_id=user_id)
# class DB:
#     async def __aenter__(self):
#         return self
#
#     async def __aexit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#     async def add_sub(self, uid: int, group_id: int):
#         await BilibiliSubscription.create(uid=uid, group_id=group_id)
#
#     async def update_sub(self, uid: int, group_id: int, update_map: dict):
#         await BilibiliSubscription.filter(uid=uid, group_id=group_id).update(
#             **update_map
#         )
#
#     async def del_sub(self, query_map: dict):
#         await BilibiliSubscription.filter(**query_map).delete()
#
#     async def get_sub_list(self, query_map: dict) -> list:
#         return await BilibiliSubscription.filter(**query_map)
#
#     async def get_all_subs(self) -> list:
#         return await BilibiliSubscription.all()