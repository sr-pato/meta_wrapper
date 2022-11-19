from abc import ABC, abstractmethod
from requests import Session
from typing import List, Optional

from meta_wrappers.section import Section


class Wrapper(ABC):
    """
    Base class for platform wrappers.
    """

    @abstractmethod
    def __init__(self, session: Session, id: str):
        """
        Initialize the wrapper from an existing session and an ID.
        """
        pass

    @abstractmethod
    def send_message(
        self,
        user: str,
        message: str,
        preview_url: Optional[bool],
    ) -> str:
        """
        Sends a message to an user and returns the message ID.
        Optionally adds a URL preview (if there is any) to the
        message.
        """
        pass

    @abstractmethod
    def send_menu(
        self,
        user: str,
        message: str,
        button_text: str,
        sections: List[Section],
        header: Optional[str],
        footer: Optional[str],
        preview_url: Optional[bool],
    ) -> str:
        """
        Sends a interactive message with a button and sections to an
        user and returns the message ID.
        It may have a header text and/or a footer text.
        Optionally adds a URL preview (if there is any) to the
        message.
        """
        pass

    @abstractmethod
    def send_interactive_message(
        self,
        user: str,
        message: str,
        sections: list,
        header: Optional[str],
        footer: Optional[str],
        preview_url: Optional[bool],
    ) -> str:
        """
        Sends a interactive message with a button and sections to an
        user and returns the message ID.
        It may have a header text and/or a footer text.
        Optionally adds a URL preview (if there is any) to the
        message.
        """
        pass

    @abstractmethod
    def send_file(
        self,
        user: str,
        file_url: str,
        file_type: str,
    ) -> str:
        """
        Sends a file to an user given its URL and type and returns
        the message ID.
        `file_type` should be "audio", "document", "image", "sticker"
        or "video".
        """
        pass

    @abstractmethod
    def reply_to_message(
        self,
        user: str,
        message: str,
        message_id: str,
    ) -> None:
        """
        Replies to a message with another message.
        """
        pass

    @abstractmethod
    def react_to_message(
        self,
        user: str,
        message_id: str,
        emoji: str,
    ) -> None:
        """
        Reacts to a message given with an Unicode emoji.
        """
        pass

    @abstractmethod
    def mark_as_read(self, user: str, message_id: str) -> None:
        """
        Marks a message as read.
        """
        pass
