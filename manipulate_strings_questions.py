# Manipulating Strings Practice Questions and Answers

"""
1. What are escape characters?
- Escape characters allow you to use certain symbols like apostrophes or quotes inside a string
without causing an error
2. What do the \n and \t escape characters represent?
- The \n is for a newline and the \t is for a horizontal tab
3. How can you put a \ backslash character in a string?
- To include a backslash in a string you should use a \\
4. The string value &quot;Howl&#39;s Moving Castle&quot; is a valid string. Why isn’t it a problem that the single quote
character in the word Howl&#39;s isn’t escaped?
- Because the string is surrounded by double quotes. The alternate form would not work (single
on outside and single used in string)
5. If you don’t want to put \n in your string, how can you write a string with newlines in it?
- Print separate statements due to the default of the end parameter in print being a newline
Print(‘Hi’)
Print(‘Bye’)
Print(&#39;Hi\nBye’)
6. What do the following expressions evaluate to?
 &#39;Hello, world!&#39;[1] = ‘e’
 &#39;Hello, world!&#39;[0:5] = ‘Hello’
 &#39;Hello, world!&#39;[:5] = ‘Hello’
 &#39;Hello, world!&#39;[3:] = ‘lo, world!’
7. What do the following expressions evaluate to?
 &#39;Hello&#39;.upper() = ‘HELLO’
 &#39;Hello&#39;.upper().isupper() = True
 &#39;Hello&#39;.upper().lower() = ‘hello’
8. What do the following expressions evaluate to?
 &#39;Remember, remember, the fifth of November.&#39;.split() - [&#39;Remember,&#39;, &#39;remember,&#39;, &#39;the&#39;, &#39;fifth&#39;,
&#39;of&#39;, &#39;November.&#39;]

 &#39;-&#39;.join(&#39;There can be only one.&#39;.split()) - There-can-be-only-one.
9. What string methods can you use to right-justify, left-justify, and center a string?
- rjust(), ljust(), center()
10. How can you trim whitespace characters from the beginning or end of a string?
- rstrip(), lstrip(), strip()
"""