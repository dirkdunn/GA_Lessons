# Opening and reading a file.
filename = raw_input('Could I get a filename please? > ')

while filename != 'exit':
    try:
        txt = open(filename)
        print txt.read()
    except IOError:
        print 'Woops! looks like we couldn\'t find that one.'

    filename = raw_input('Could I get a filename please? > ')
