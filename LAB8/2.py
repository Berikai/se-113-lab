# Define a function extension which takes a filename f_name as a parameter, including
# its extension (e.g. “worddocument.docx”) and returns only the extension. If there are no
# extensions in the given filename, print a corresponding message.
# Hint: You can attempt to find the index of the dot character (‘.’) within the filename, and
# then access all characters after that specific index.
# Test your function by calling extension twice, once by passing "my_script.py" and
# once by passing "my_document.docx".

def extension(f_name):
    if '.' in f_name:
        return f_name.split('.')[-1]
    else:
        return f'Given name "{f_name}" is not a file name with extension.'
    
'''
# The hint way
def extension(f_name):
    if '.' in f_name:
        index = f_name.rfind('.')
        return f_name[index:]
    else:
        return f'Given name "{f_name}" is not a file name with extension.'
'''

print(extension('my_script.py'))
print(extension('my_document.docx'))