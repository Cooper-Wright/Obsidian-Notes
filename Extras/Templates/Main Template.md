---
"Creation:": <% tp.file.creation_date("dddd Do MMMM YYYY HH:mm:ss") %>
Modified: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
---
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
<% await tp.file.move("/To Be Sorted/" + tp.file.title) %>
# *Tags*
#<% mood %> #<% item %> #<% tp.file.title %>

# *Mood:* 
*<% mood %>, <% why %>*

# *<% item %> of the Day is:*
<% displayed %>

