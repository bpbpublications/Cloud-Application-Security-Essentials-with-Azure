#
# illustrating encryption of data at rest
# for encrypting data in transit, use tls (https)
#

# the data service
class SomeService:
    # to start, the key is empty
    key = None
    data = [key]

    def StoreData(dataTostore):
        # data is  stored in the list where first element is the dek
        SomeService.data.append(DataCrypt.Encrypt(SomeService.data[0], dataTostore))

        # returning length of the list which is also the index of the added data
        return len(SomeService.data)

    def GetData(dataindex):
        return DataCrypt.Decrypt(SomeService. data[0], SomeService.data[dataindex])

class DataCrypt:
    def Encrypt(key, data):
        # if the key is empty, generate it
        return data
    def Decrypt(key, data):
        return data
# 
# the app
#
ind = SomeService.StoreData("123")
print(f"data len is {ind}")
d = SomeService.GetData(ind-1)
print(f"stored data is {d}")