# FindDocumentContainingWord
This was an old file that I made when my father needed help finding a file which he only knew a single word in it.

This is now nonlocalized so it works for every computer. There are a bunch of try-except statements because of problems with permission and some files that were looked at by the program are not valid like a file made by the MacAfee program in 'Documents'. This assumes that the file is in the section of the computer called "Documents" and assumes that that exists. If a broader search range is needed, replace line 26 with path = os.path.join(os.environ['USERPROFILE']).
