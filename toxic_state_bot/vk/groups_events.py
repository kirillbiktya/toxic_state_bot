from toxic_state_bot.vk.types import JsonDeserializable, Message


class MessageNew(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, message, **kwargs):
        self.message: Message = Message.de_json(message)


class MessageEdit(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, message, **kwargs):
        self.message: Message = Message.de_json(message)


class LikeRemove(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, liker_id, **kwargs):
        self.liker_id = liker_id


class GroupLeave(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, user_id, is_self, **kwargs):
        self.user_id = user_id
        self.is_self = is_self


class GroupJoin(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, user_id, join_type, **kwargs):
        self.user_id = user_id
        self.join_type = join_type


class PollVoteNew(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, owner_id, poll_id, option_id, user_id, **kwargs):
        self.owner_id = owner_id
        self.poll_id = poll_id
        self.option_id = option_id
        self.user_id = user_id
