
class AppAddress:

    # the app address.
    # the app can live in any cloud or blockchain. The address contains the information.
    # 
    apploc = "someplace" 

    def GetAppAddress():
        return AppAddress.apploc

# print the app address
print(f"app is installed at {AppAddress.GetAppAddress()}")