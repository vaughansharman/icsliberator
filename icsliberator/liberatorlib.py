import re
from datetime import datetime
import os.path

# tags
START_TAG = "BEGIN:VTODO"
END_TAG = "END:VTODO"
CREATED_TAG = "CREATED:"
SUMMARY_TAG = "SUMMARY:"
COMPLETED_TAG = "COMPLETED:"
PERCENT_COMPLETE_TAG = "PERCENT-COMPLETE:"

# states
FIND_NEXT = "FIND_NEXT"
COLLECT = "COLLECT"

def get_existing_lists(file):
    existing_lists = set()
    if os.path.isfile(file):
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                stripped = line.strip()
                pattern = re.compile(r'@(\w*)')
                for match in re.findall(pattern, stripped):
                    existing_lists.add(match)
    return existing_lists

class TodoEntry():

    def __init__(self):
        self.createdDate = ""
        self.list = ""
        self.summary = ""
        self.completedDate = None
        self.percentComplete = ""

    def __str__(self):
        dt = self.createdDate.strftime("%Y-%m-%d")
        cleaned_list_name = self.list.replace(" ", "_")
        completed = ""
        if self.completedDate != None:
            completed = "x "
        return completed + dt + " " + self.summary + " @" + cleaned_list_name

    def __eq__(self, other):
        a = self.createdDate == other.createdDate
        b = self.list == other.list
        c = self.summary == other.summary
        d = self.completedDate == other.completedDate
        e = self.percentComplete == other.percentComplete
        return a and b and c and d and e

def handle_whole_record(record_lines):
    todo = TodoEntry()
    # todo.list = list_being_added_to
    for line_in_record in record_lines:
        if line_in_record.startswith(CREATED_TAG):
            string_date = line_in_record.split(CREATED_TAG, 1)[1].strip()
            todo.createdDate = datetime.strptime(string_date[:8], "%Y%m%d")
        elif line_in_record.startswith(SUMMARY_TAG):
            todo.summary = line_in_record.split(SUMMARY_TAG, 1)[1].strip()
        elif line_in_record.startswith(COMPLETED_TAG):
            todo.completedDate = line_in_record.split(COMPLETED_TAG, 1)[1].strip()
        elif line_in_record.startswith(PERCENT_COMPLETE_TAG):
            todo.percentComplete = line_in_record.split(PERCENT_COMPLETE_TAG, 1)[1].strip()
    return todo

def get_list_to_add_to(lists):
    list_to_add_to = ""
    listLookup = {}
    while list_to_add_to == "":
        print "Known lists are: "
        for i, item in enumerate(lists):
            listLookup[str(i+1)] = item
            print str(i+1) + ". " + item
        list = raw_input('Enter number or new list name:')
        if list in listLookup:
            return listLookup[list]
        return list

def convert(input_file, output_file):
    lists = get_existing_lists(output_file)
    state = FIND_NEXT
    to_append = []
    with open(input_file) as f:
        buffer = []
        lines = f.readlines()
        for line in lines:
            stripped = line.strip()
            if state == FIND_NEXT:
                if stripped == START_TAG:
                    state = COLLECT
            elif state == COLLECT:
                if stripped == END_TAG:
                    todo = handle_whole_record(buffer)
                    print "\nAdding list item '%s'" % todo.summary
                    list_to_add_to = get_list_to_add_to(lists)
                    todo.list = list_to_add_to
                    lists.add(list_to_add_to)
                    to_append.append(str(todo))
                    print "'%s' was added to list '%s'" % (todo.summary, todo.list)
                    buffer = []
                    state = FIND_NEXT
                else:
                    buffer.append(stripped)
    return to_append

