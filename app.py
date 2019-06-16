from notion.client import NotionClient
from apps import ACTIVATED_APPS
from token import fetch_token

def main():
    try:
        token = fetch_token()
    except Exception as e:
        print(f'Unable to get Notion credentials: {str(e)}')
        return

    notion = NotionClient(token_v2=token)

    for app in ACTIVATED_APPS:
        app.run(notion)

    print('Job Done')

if __name__ == '__main__':
    main()

