# Practice Questions

"""
# Chapter 9 Questions

1. What is a relative path relative to?
- the current working directory

2. What does an absolute path start with?
- the root folder, if Windows C:\, if Mac/Linux /

3. What does Path('C:/Users') / 'Al' evaluate to on Windows?
- 'C:/Users/A1'
- On Windows, it evaluates to WindowsPath('C:/Users/Al'). On other operating systems, it evaluates to a different kind of Path object but with the same path.

4. What does 'C:/Users' / 'Al' evaluate to on Windows?
- Error, can't combine strings with /

5. What do the os.getcwd() and os.chdir() functions do?
- os.getcwd() returns absolute path of current working directory
- os.chdir() changes the current working directory

6. What are the . and .. folders?
- . is current folder
- .. is parent folder

7. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?
- dir name = 'C:\bacon\eggs'
- base name = spam.txt

8. What are the three “mode” arguments that can be passed to the open() function?
- read, write, append

9. What happens if an existing file is opened in write mode?
- the contents of the file are overwritten by the new input
* An existing file opened in write mode is erased and completely overwritten.

10. What is the difference between the read() and readlines() methods?
- The read() method returns the file’s entire contents as a single string value. The readlines() method returns a list of strings, where each string is a line from the file’s contents

11. What data structure does a shelf value resemble?
- A shelf value resembles a dictionary value; it has keys and values, along with keys() and values() methods that work similarly to the dictionary methods of the same names.

"""