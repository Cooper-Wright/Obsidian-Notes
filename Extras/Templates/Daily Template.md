<%* 
let mood = await tp.system.suggester(["Happy", "Sad", "Confused", "Tired", "Bored"], ["Happy", "Sad", "Confused", "Tired", "Bored"]) 
let why = await tp.system.prompt("Why do you feel like this?", "because")
-%>
<%* 
let item = await tp.system.suggester(["Image", "Quote"], ["Image", "Quote"])
let displayed = ""
if (item == "Quote") {
	displayed = await tp.web.daily_quote()
} else if (item == "Image" || item == null) {
	displayed = await tp.web.random_picture("500x500") 
}
-%>
<% await tp.file.move("/Daily Notes/" + tp.file.title) %>---
"Creation:": <% tp.file.creation_date() %>
Modified: <% tp.file.last_modified_date() %>
tags: <% mood %> <% item %> <% tp.file.title %>

---
# *Mood:* 
*<% mood %>, <% why %>*

# *<% item %> of the Day is:*
<% displayed %>

---

### Happened...



### Happening...



### To do...

##### University:


##### Chores:


##### Personal Life:

