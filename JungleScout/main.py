from JungleScout.Login.Login import Login
import pandas as pd

import requests

if __name__ == '__main__':

    # # Set your NordVPN credentials
    # email = "anisse9@gmail.com"
    # password = "Million.10"
    #
    # # Authenticate and get the access token
    # auth_data = {
    #     "username": email,
    #     "password": password
    # }
    #
    # auth_response = requests.post("https://api.nordvpn.com/v1/users/tokens", json=auth_data)
    #
    # if auth_response.status_code == 200:
    #     response_data = auth_response.json()
    #     access_token = response_data.get("token")
    #     if access_token:
    #         # Retrieve a list of servers
    #         servers_response = requests.get("https://api.nordvpn.com/v1/servers", headers={"Authorization": f"Bearer {access_token}"})
    #         if servers_response.status_code == 200:
    #             servers = servers_response.json()
    #
    #             # Select a random server
    #             random_server = servers["servers"][0]["hostname"]
    #
    #             # Connect to the selected server
    #             connect_data = {
    #                 "ip_address": random_server
    #             }
    #
    #             connect_response = requests.post("https://api.nordvpn.com/v1/servers/recommendations", headers={"Authorization": f"Bearer {access_token}"}, json=connect_data)
    #             connection_status = connect_response.json()
    #
    #             if connection_status.get("status") == "Online":
    #                 print("Connected to NordVPN. Your IP address has been changed.")
    #             else:
    #                 print("Failed to connect to NordVPN.")
    #         else:
    #             print("Failed to retrieve server list. Error:", servers_response.content.decode())
    #     else:
    #         print("Access token not found in the authentication response.")
    # else:
    #     print("Failed to authenticate with NordVPN. Error:", auth_response.content.decode())

    with Login() as bot:
        bot.land_first_page()