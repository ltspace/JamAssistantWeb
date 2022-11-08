import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_dir = os.path.join(BASE_DIR, 'JamAssistant', 'students', '全校学生')

template_all = os.path.join(BASE_DIR, 'JamAssistant', 'template.xml')

award_file = os.path.join(BASE_DIR, 'JamAssistant', 'JamList.csv')
json_file = os.path.join(BASE_DIR, 'JamAssistant', 'students.json')
