## Data-science your DMs !

Retrieve and analyse your Facebook messages, from the unstructured archive to visualisations. 

This is a work in progress.

### How to get your messages from Facebook

1. Go to "Settings"
2. Go to "Your Facebook information"
3. Choose "Download your information"
4. Leave "Date Range" on "All my data"
5. Choose "Format": "JSON"
6. "Media Quality" doesn't matter, as only text messages are extracted. You may choose "Low quality" for a faster download.
7. Select only "Messages" in "Your information".
8. Click on "Create File" and wait on the mail indicating that you can download the archive !

### What works for now :
#### The Unarchivist :
Come in two flavours...
- Command line :
  - cd into the directory of the file
  - Use python unarchivist_commandline.py [ ZIP file location ] [ location fo future CSV file ]
  - Depends on pandas, json, zipfile
- User interface :
  - cd into the directory of the file
  - Use python unarchivist_userinterface.py
  - Depends additionnaly on tkinter
  - Standalone binaries will be released in the future
