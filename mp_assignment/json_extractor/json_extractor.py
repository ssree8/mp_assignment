import json
import os
import copy

def read_json(path):
	obj = None
	files=os.listdir(path)
	for file in files:
		fl_path = os.path.join(path, file)
		with open(fl_path, "r") as f:
			obj=json.load(f)
		return obj, file

def creat_json(obj, path, file):
	nw_path =  os.path.join(path, file)
	
	with open(nw_path, "w") as outfile:
		data = json.dumps(obj)
		outfile.write(data)

def json_extract(obj, key):
	"""Recursively fetch values from nested JSON."""
	arr = []
	obj_copy=None
	def extract(obj, arr, key):
		"""Recursively search for values of key in JSON tree."""
		obj_copy = copy.copy(obj)
		if isinstance(obj, dict):
			for k, v in obj_copy.items():
				if isinstance(v, (dict, list)):
					extract(v, arr, key)
				elif k == key:
					del obj[key]
		elif isinstance(obj_copy, list):
			for item in obj_copy:
				extract(item, arr, key)
		return obj_copy

	new_obj = extract(obj, arr, key)
	return new_obj
	

if __name__ == "__main__":
	out = r"./output_data"
	path = r'./test_data'
	obj, file = read_json(path)
	txt = "text"
	new_onj = json_extract(obj, txt)
	creat_json(new_onj, out, file)