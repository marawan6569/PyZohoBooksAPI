from pyzohoapi import ZohoInventory, ZohoBooks


api = ZohoInventory("774525475", "com",
                    client_id="1000.GD6CJ7MWC8AWC6CZI1ZL474UYURQXS",
                    client_secret="ab74c6e5565fd99fdee9e40b364cd960941c4529da",
                    refresh_token="1000.b2b7578e7a9d2ea5710cc224c638e39e.8cd3fb716ac5ef887eed25275f4a990b"
                    )


contact = api.Contact(email="marawa6569@gmail.com").First()
contact.first_name = "Changed"
contact.Update()
