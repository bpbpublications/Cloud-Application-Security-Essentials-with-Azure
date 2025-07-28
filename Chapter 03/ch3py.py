#
# ch3 is about public and private clouds
# the app does not know the cloud designation
# it could infer it based on some property
#
class CloudType:
    # type is a property. We initialixe to a string constant
    cloudType = "public"
    def GetCloudType() :
        return CloudType.cloudType

# print the cloud type the application runs in
ct = CloudType.GetCloudType()
print(f"application runs in {ct} cloud")