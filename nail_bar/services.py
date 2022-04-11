# move the services dictionary here

# to then make a dynamic list we could use for a drop down on a form:
# look through the dictionary using enumerate, this gives the index number for each entry which we can use as the
# back-end descriptor, get it to return the name of each service e.g. French Manicure etc
# save this as a separate list and then use this to populate the drop down using SelectField

# also clean stuff up - have a seperate routes file, and an app file, we don't have __init__.py file as isn't currently
# a package and we also don't have app.py, we have nail_bar_app