# try:
#     you do your operation here
#     ....
# except ExceptionI:
#     If there is an ExceptionI, then execute this block..
#
# except ExceptionII:
#     If there is an ExceptionII, then execute this block.
#     ..
#
# else:
#     If there is no exception then execute this block.
#
# finally:
#     this block will run no matter what..


try:
    f = open('simple.txt', 'w')
    f.write("Test write to simple text!")   # There will be error if try block is written wrong.

except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA")
else:
    print("SUCCESS!")
    f.close()

finally:
    print("Text have been written in file..")