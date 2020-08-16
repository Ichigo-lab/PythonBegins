from twilio.rest import Client

account_sid = "ACfe8bc4d0a593286595fe71ead55fe3f6"
auth_token = "51796ccf9ebb42935ef5a6a0750fdb02"

client = Client(account_sid, auth_token)

call = client.messages.create(
    to="...",
    from_="...",
    body="Hey Black Mamba"
)
