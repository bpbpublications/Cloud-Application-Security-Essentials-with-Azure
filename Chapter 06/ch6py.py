#
# application identity samples
#
class IdentityContext:
    # identity 
    id = 1234
    def GetId() :
        return IdentityContext.id

class AuthzCompute:
    # default authz
    authzDefault = 123
    # compute authorization 
    def Authz(id, res):
        # given an identity and a resource 
        # compute the effective authz
        return AuthzCompute.authzDefault
    
# 
# this identity is...
# 
thisid = IdentityContext.GetId()

# and is authorized to ...
rights = AuthzCompute.Authz(thisid, "someresource")
# print the authorization 
print(f"identity {thisid} has rights {rights} to someresource")
