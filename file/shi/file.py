fd = open("html.html","a+")
fds = open("shi.html","a+")
for line in fd:
    fds.write(line)

fd.close()
fds.close()
