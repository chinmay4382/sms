from twilio.rest import Client
account_sid = "ACbfc9d7644a2aff8838126d888976c717"#ACCOUNT DETAIL WHICH WILL BE AVAILABLE IN TWILIO DASHBOARD
auth_token = "8ebd45aa1672b5fd293xxxfe1a8cc428"#ACCOUNT DETAIL WHICH WILL BE AVAILABLE IN TWILIO DASHBOARD
client = Client(account_sid, auth_token)
client.api.account.messages.create(
	to="+917026251115",
	from_="+1831xxx0945",
	 body="this msg was sent by twilio.....for MUSK-v1")#THIS IS DESIRED MESSAGE THAT CAN BE SENT
print("message sent")
