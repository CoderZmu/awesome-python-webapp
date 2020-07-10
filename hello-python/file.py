
import os
def searchFile(path, file):
  for sub in os.listdir(path):
    sub_path = os.path.join(path, sub)
    if (os.path.isfile(sub_path)) and file in sub:
      print(sub_path)
    elif (os.path.isdir(sub_path)):
      searchFile(sub_path, file)


if __name__ == '__main__':
  searchFile('/Users/lishiming/Desktop/react/test', 'js')
