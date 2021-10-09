import json

from toxic_state_bot.vk.util import is_dict, is_string


# region etrnnoir's code, that I have copypasted
class JsonDeserializable:
    @classmethod
    def de_json(cls, json_string):
        """
        Returns an instance of this class from the given json dict or string.
        This function must be overridden by subclasses.
        :return: an instance of this class created from the given json dict or string.
        """
        raise NotImplementedError

    @staticmethod
    def check_json(json_type, dict_copy=True):
        """
        Checks whether json_type is a dict or a string. If it is already a dict, it is returned as-is.
        If it is not, it is converted to a dict by means of json.loads(json_type)
        :param json_type: input json or parsed dict
        :param dict_copy: if dict is passed and it is changed outside - should be True!
        :return: Dictionary parsed from json or original dict
        """
        if is_dict(json_type):
            return json_type.copy() if dict_copy else json_type
        elif is_string(json_type):
            return json.loads(json_type)
        else:
            raise ValueError("json_type should be a json dict or string.")


# endregion


class VKUpdate(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(obj['type'], obj['object'], obj['group_id'], obj.get(['event_id']))

    def __init__(self, u_type, u_object, group_id, event_id=None):
        self.u_type = u_type
        try:
            self.u_object = group_events[self.u_type].de_json(u_object)
        except KeyError:
            print('no such update type')
            pass
        self.group_id = group_id
        self.event_id = event_id


class Message(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, m_id, date, peer_id, from_id, text, **kwargs):
        self.m_id: int = m_id
        self.date: int = date
        self.peer_id: int = peer_id
        self.from_id: int = from_id
        self.text: str = text


class ClientInfo:
    pass


class WallPost(JsonDeserializable):
    @classmethod
    def de_json(cls, json_string):
        if json_string is None:
            return None
        obj = cls.check_json(json_string, dict_copy=False)
        return cls(**obj)

    def __init__(self, p_id, owner_id, **kwargs):
        self.p_id: int = p_id
        self.owner_id: int = owner_id


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


group_events = {'like_remove': LikeRemove, 'group_leave': GroupLeave, 'group_join': GroupJoin, 'poll_vote_new': PollVoteNew, 'message_new': MessageNew, 'message_edit': MessageEdit}