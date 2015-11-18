# icsliberator

##Overview
A script / tool that allows users to migrate away from Mac Reminders to use todo.txt.

##Background
It is **way** too difficult to move between Android and IOS, this script allows you to decouple yourself from Apple and Google... Yay!

##How to use
run 

```
python runner.py
```

You will then be asked for:
 
* your existing todo.txt file, (not req'd, but it will allow you to reuse existing lists)
* The ics file to convert from

The script with then go through each item with an opportunity to add the item to an existing group or create a new group:

```
Adding list item 'HGgefbi Restaurant'
Known lists are:
1. Foo
3. Ideas
4. Funky
5. Travel
6. Enter number or new list name:
```

At the end the formatted output will be written to console, append this to your todo.txt file and you are done! Now don't go get yourself at the mercy of a close walled garden again :)