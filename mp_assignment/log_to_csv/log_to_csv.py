
import csv
def log_to_csv(file):
	out = r"./output_data/output.csv"
	data_list =  []
	dic = {}
	with open(out, 'w') as out_file, open(file, 'r') as in_file:
		
		writer = csv.writer(out_file)
		writer.writerow(['Status', 'Message','Error', 'Time'])

		for line in in_file:
			status = line.strip().split(" ")
			
			if "200" in status and "OK" in status:
				for line in in_file:
					status = line.strip().split(" ")
					if '"Status"' in line.strip().split(":"):
						data_list.insert(0, line.strip().split(":")[-1].strip())
					elif '"Message"' in line.strip().split(":"):
						data_list.insert(1, line.strip().split(":")[-1].strip())
					elif '"Error"' in line.strip().split(":"):
						data_list.insert(2, line.strip().split(":")[-1].strip())
					elif '"Time"' in line.strip().split(":"):
						data_list.insert(3, line.strip().split("\":")[-1].strip())
			else:
				if '"Status"' in line.strip().split(":"):
					dic['status'] = line.strip().split(":")[-1].strip()
				elif '"Message"' in line.strip().split(":"):
					dic['Message'] = line.strip().split(":")[-1].strip()
				elif '"Error"' in line.strip().split(":"):
					dic['Error'] = line.strip().split(":")[-1].strip()
				elif '"Time"' in line.strip().split(":"):
					dic['Time'] = line.strip().split("\":")[-1].strip()
		if data_list:
			writer.writerow(data_list)
		elif dic:
			print(dic)

if __name__ == "__main__":
	path = r"./test_data/test.log"
	log_to_csv(path)