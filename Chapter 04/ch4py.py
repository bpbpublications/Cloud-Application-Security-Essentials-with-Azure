#
# application identity
#
class AppIdentity:
    # for illustration define some appid
    appId = 1234
    def GetAppIdentity():
        return AppIdentity.appId
    

# print the app id of this app
appid = AppIdentity.GetAppIdentity()
print(f"this appid is {appid}")