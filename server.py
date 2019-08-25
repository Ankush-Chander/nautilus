from bottle import route, run, static_file
import os

@route('/static/<path:path>')
def server_static(path):
	try:
		return static_file(path, root="/")
	except Exception as err:
		print(err)


# @route("/search/<search_string>")
# def search_file(search_string):
# 	search_string = search_string.lower()
# 	excludes =[]
# 	for root, dirs, files in os.walk("/home/ankush"):
# 		print(root)
# 		# print(files)


@route("/<path:path>", method="GET")
def showDirectoryContent(path="", show_hidden=False):
	t_str = "<ul>"
	try:
		top="/"+path
		for f in os.scandir(top):
			if f.name.startswith("."):
				continue
			if f.is_dir():
				dir_path = top + "/" + f.name
				t_str += "<li><a href='"+dir_path+"'>"+str(f.name)+"</li>"
			else:
				file_path = "/".join(["/static", top, f.name])
				t_str += "<li><a target='_blank' href='" + file_path + "'>" + str(f.name) + "</li>"
	except Exception as err:
		print(err)
	t_str += "</ul>"
	return t_str

run(host='localhost', port=8080)
# if __name__ == "__main__":
# 	search_file("Hello")