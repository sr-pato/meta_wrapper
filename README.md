# meta_wrappers

Easy-to-use wrappers for Meta chat platforms

## Getting started

```sh
$ pip3 install meta_wrappers
```

In your code
```py
from meta_wrappers import Whatsapp

wpp = Whatsapp(sesh, your_whatsapp_api_id)
wpp.send_menu(
    phone_number,
    message_text,
    button_text,
    [{ "title": title, "rows": [] }],
)
```
