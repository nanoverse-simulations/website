for line in open("files.txt"):
	fn = line.strip()
	print('sed -e "s/^M//" %s > ../%s' % (fn, fn))
