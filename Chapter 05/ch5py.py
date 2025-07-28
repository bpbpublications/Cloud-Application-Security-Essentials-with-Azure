#
# compute, storage and networking services are provided by the cloud
# 
class CloudServices:
    # cloud services
    servicenames = "compute, storage and networking"
    def GetCloudServiceNames():
        return CloudServices.servicenames
    
# print the cloud service names
csn = CloudServices.GetCloudServiceNames()
print(f"the cloud offers {csn} services")