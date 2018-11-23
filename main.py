from templates import parse_data
from utills.fileutill import FileUtill

answer, question, queue = parse_data.load_data()

reversed_queue = queue[::-1]

f = FileUtill()
f.write_file(reversed_queue)
print(f.read_file())
