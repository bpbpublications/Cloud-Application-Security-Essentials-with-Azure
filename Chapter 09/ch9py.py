#
# summary chapter
# invokes py script related to previous chapters
#
import os

class PyScript:
    # various paths
    def GetScriptPath(chapter):
        srcdir = os.path.dirname(__file__)
        srcdir1 = os.path.dirname(srcdir)
        path1 = f"{srcdir1}\\ch{chapter}py.py"
        path = f"{srcdir1}\\ch{chapter}\\ch{chapter}py.py"
        
        # debug print
        print(f"{os.getcwd()} and {path}")

        if(os.path.exists(path)) :
            return  path 
        else:
            return path1

# execute chapter script.
chapter = input("Enter chapter number:")
scrpath = PyScript.GetScriptPath(chapter)
# debug
print(f"script {scrpath}")
os.system(f"python {scrpath}")