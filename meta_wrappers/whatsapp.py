from requests import Session
from typing import List, Optional

from meta_wrappers.base import Wrapper
from meta_wrappers.exception import APIError
from meta_wrappers.section import Section


class WhatsappSection(Section):
    def __init__(self, title: str, rows: List[str]):
        self.title = title
        self.rows = rows

    def process(self):
        return {
            "title": self.title,
            "rows": [{
                "id": hash(row),
                "title": row,
            } for row in self.rows],
        }


class Whatsapp(Wrapper):
    def __init__(self, session: Session, id: str):
        self.session = session
        self.API = {"messages": f"https://graph.facebook.com/v15.0/{id}/messages"}
    
    def send_message(
        self,
        user: str,
        message: str,
        preview_url: Optional[bool] = False,
    ) -> str:
        payload = {
            "messaging_product": "whatsapp",
            "to": user,
            "type": "text",
            "text": {
                "body": message,
                "preview_url": preview_url,
            },
        }
        
        response = self.session.post(
            self.API["messages"],
            json=payload,
        ).json()

        if "error" in response:
            raise APIError(response["error"])

        return response["messages"][0]["id"]

    def send_menu(
        self,
        user: str,
        message: str,
        button_text: str,
        sections: List[WhatsappSection],
        header_text: Optional[str] = None,
        footer_text: Optional[str] = None,
        preview_url: Optional[bool] = False,
    ) -> str:
        payload = {
            "messaging_product": "whatsapp",
            "to": user,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "action": {
                    "button": button_text,
                    "sections": [
                        section.process() for section in sections
                    ],
                },
                "body": {
                    "text": message,
                },
            },
        }

        if header_text is not None:
            payload["interactive"]["header"] = {
                "type": "text",
                "text": header_text,
            }

        if footer_text is not None:
            payload["interactive"]["footer"] = {
                "type": "text",
                "text": footer_text,
            }

        response = self.session.post(
            self.API["messages"],
            json=payload,
        ).json()

        if "error" in response:
            raise APIError(response["error"])

        return response["messages"][0]["id"]

    def send_interactive_message(
        self,
        user: str,
        message: str,
        sections: list,
        header: Optional[str],
        footer: Optional[str],
        preview_url: Optional[bool],
    ) -> str:
        raise NotImplementedError()

    def send_file(
        self,
        user: str,
        file_url: str,
        file_type: str,
    ) -> str:
        file_types = (
            "audio",
            "document",
            "image",
            "sticker",
            "video",
        )

        if file_type not in file_types:
            file_types_list = ", ".join(file_types)
            raise Exception(
                message=f"{file_type} is not one of {file_types_list}"
            )

        payload = {
            "messaging_product": "whatsapp",
            "to": user,
            "type": file_type,
            file_type: {
                "link" : file_url,
            },
        }
        
        response = self.session.post(
            self.API["messages"],
            json=payload,
        ).json()

        # TODO: check if the download of the file from the link was
        # successful.

        if "error" in response:
            raise APIError(response["error"])

        return response["messages"][0]["id"]

    def react_to_message(
        self,
        user: str,
        message_id: str,
        emoji: str,
    ) -> None:
        payload = {
            "messaging_product": "whatsapp",
            "to": user,
            "type": "reaction",
            "reaction": {
                "message_id": message_id,
                "emoji": emoji,
            },
        }
        
        response = self.session.post(
            self.API["messages"],
            json=payload,
        ).json()

        if "error" in response:
            raise APIError(response["error"])

    def reply_to_message(
        self,
        user: str,
        message: str,
        message_id: str,
        preview_url: Optional[bool] = False,
    ) -> None:
        payload = {
            "messaging_product": "whatsapp",
            "context": {
                "message_id": message_id,
                "preview_url": preview_url,
            },
            "to": user,
            "type": "text",
            "text": {
                "body": message,
            },
        }
        
        response = self.session.post(
            self.API["messages"],
            json=payload,
        ).json()

        if "error" in response:
            raise APIError(response["error"])

    def mark_as_read(self, user: str, message_id: str) -> None:
        payload = {
            "messaging_product": "whatsapp",
            "status": "read",
            "message_id": message_id,
        }

        response = self.session.post(
            self.API["messages"],
            json=payload,
        ).json()

        if "error" in response:
            raise APIError(response["error"])
