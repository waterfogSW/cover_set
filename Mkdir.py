import os

# [Item 20] Prefer Raising Exceptions to Returning None
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
# None을 반환하는 대신 에러를 명시적으로 발생시켜 에러의 위치를 파악할 수 있도록 하였습니다. 