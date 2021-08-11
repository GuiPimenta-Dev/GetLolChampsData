import pandas as pd

from bots.facebook_bot import FacebookBot
from multi_thread_bot import MultiThreadBot

MAX_THREADS = 5

if __name__ == "__main__":
    print("Collecting items to process...")

    accounts = pd.read_excel('accounts.xlsx').values.tolist()
    items_to_process = [
        {'email': account[0], 'password': account[3], 'codes': account[4:]}
        for account in accounts
    ]

    mb = MultiThreadBot(
        max_threads=MAX_THREADS,
        bot=FacebookBot,
        items_to_process=items_to_process)

    results = mb.run()

    print(f"\nProcessed items: {str(results)}")

    success_items = sum(result['status'] == 'SUCESS' for result in results)
    print(f"\nSUCESS: {success_items} / FAILED: {len(results) - success_items}")
