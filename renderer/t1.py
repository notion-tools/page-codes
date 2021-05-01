from config import config
from notion.client import NotionClient
from notion import block

client = NotionClient(token_v2=config["token_v2"])


root_page = client.get_block('https://www.notion.so/hnhs/The-title-has-now-changed-and-has-live-updated-in-the-browser-aa6ab8278725460a9523d96f89a717ff')
root_page.children.add_new(block.CodeBlock, caption="1123", title="123")
print(root_page.type)
print(root_page.children)


