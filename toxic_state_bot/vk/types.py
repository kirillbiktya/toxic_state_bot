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
