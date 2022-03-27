import argparse
import asyncio
import json

from marilyn_api.client import AsyncClient


async def main(
    api_root: str, headers: dict, project_id: int, params: dict = None, save_to_file: bool = False
):
    aclient = AsyncClient(api_root, headers)
    data = []
    async for page in aclient.iter_project_placements(project_id, params=params, headers=headers):
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
    parser.add_argument("-p", "--project", required=True, type=int, help="Project ID")
    parser.add_argument(
        "-c",
        "--params-config",
        required=False,
        default=None,
        type=str,
        help="The path to the JSON file of the GET params for the request",
    )
    parser.add_argument("-f", "--save-to-file", default=False, type=str, help="Save data to file")
    args = parser.parse_args()

    headers = {
        "X-API-Account": args.account,
        "X-API-Token": args.token,
    }

    asyncio.run(main(args.api_root, headers, args.project, args.params_config, args.save_to_file))
