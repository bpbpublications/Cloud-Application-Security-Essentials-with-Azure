MIN_SELEVEL = 0
BASE_SECLEVEL = 5

class AppSecLevel:
    # define class variable 
    Seclevel = None

    # required featues 
    requiredFeatures = ["f1", "f2"]

    def __init__(self, implementedFeatures):
        # init the seclevel based on what is implemented 
        for f in AppSecLevel.requiredFeatures :
            if (f in implementedFeatures == False):
                self.Seclevel = MIN_SELEVEL
                break
            if (self.Seclevel != MIN_SELEVEL):
                self.Seclevel = BASE_SECLEVEL
        return
    
    def GetSeclevel (self):
        return self.Seclevel
    
# and the main function printing the app sec level
# implemented features must be passed in as a parameter
thisApp = AppSecLevel(["f1", "f2"])
lvl = thisApp.GetSeclevel()
print(f"application securiy level: {lvl}")