import argparse
import asyncio
import json

from marilyn_api.client import AsyncClient


async def main(api_root: str, headers: dict, body: dict, save_to_file: bool = False):
    aclient = AsyncClient(api_root, headers)
    data = []
    async for page in aclient.iter_statistics_detailed(body):
        if save_to_file:
            data += page["items"]
        else:
            for item in page["items"]:
                print("RECORD:", item)

    if save_to_file:
        with open(save_to_file, "w") as f:
            json.dump(data, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Downloading detailed statistics to a JSON file"
    )
    parser.add_argument("-r", "--api-root", required=True, type=str, help="Api root. Example https://app.mymarilyn.ru")
    parser.add_argument("-a", "--account", required=True, type=str, help="Account ID")
    parser.add_argument("-t", "--token", required=True, type=str, help="Token for auth")
    parser.add_argument(
        "-c", "--stats-config", required=True, type=str, help="The path to the JSON file of the body for the request"
    )
    parser.add_argument("-f", "--save-to-file", default=False, type=str, help="Save data to file")
    args = parser.parse_args()

    headers = {
        "X-API-Account": args.account,
        "X-API-Token": args.token,
    }
    with open(args.stats_config) as f:
        body = json.loads(f.read())

    asyncio.run(
        main(args.api_root, headers, body, args.save_to_file)
    )
