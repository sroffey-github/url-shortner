from dotenv import load_dotenv
import requests, os, json

load_dotenv() # loading env vars

# account credentials
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

print((username, password))

# get the access token
auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))

if auth_res.status_code == 200:
    # if response is OK, get the access token
    access_token = auth_res.content.decode()
    print("[!] Got access token: ", access_token + "\n")
else:
    print("[!] Cannot get access token, exiting...")
    exit()

# construct the request headers with authorization
headers = {"Authorization": f"Bearer {access_token}"}

# get the group UID associated with our account
groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
if groups_res.status_code == 200:
    # if response is OK, get the GUID
    groups_data = json.loads(groups_res.text)['groups'][0]
    guid = groups_data['guid']
else:
    print("[!] Cannot get GUID, exiting...")
    exit()

# the URL you want to shorten
print('[?] Enter the URL you want to shorten')
url = input('>>> ')
# create json variable
my_data = {
	"group_guid": guid, "long_url": url
}
# make the POST request to get shortened URL for `url`
shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", data=json.dumps(my_data), headers=headers, verify=False)
print(shorten_res.text)
if shorten_res.status_code == 200:
    # if response is OK, get the shortened URL
    link = json.loads(shorten_res.text)["link"]
    print("Shortened URL:", link)
else:
	print('[!] Error creating link')