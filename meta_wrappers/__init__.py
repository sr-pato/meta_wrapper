from typing import Mapping

from meta_wrappers.base import Wrapper
from meta_wrappers.section import Section # noqa: F401
from meta_wrappers.whatsapp import Whatsapp, WhatsappSection # noqa: F401


wrappers: Mapping[str, Wrapper] = {
    "whatsapp": Whatsapp,
}
