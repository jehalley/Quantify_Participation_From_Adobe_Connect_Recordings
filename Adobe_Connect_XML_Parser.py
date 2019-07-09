from collections import defaultdict
from bs4 import BeautifulSoup
from collections import Counter

from xml.etree import ElementTree

def get_student_roster(student_roster_csv_file_path):
    #read csv to get list of students in class store as list
    student_roster =
def get_student_ids(index_stream_xml_path,student_roster):
    '''make two separate dictionaries with the same keys (student names) one for pids and one for ids. Pids are used in
    chat transcripts and ids are used in camera, mic, and handsup tracking
    '''
    #get pID dict with Pid if student attended and zero if student did not attend
    student_placeholder =  dictionary with names from student roster as keys and zero value for pID and Id
    pIDS = make dict with name as key and pid as value from attendees
    student_pID = add student_placeholder and pIDS together

    #get id dict
    student_placeholder = dictionary with names from student roster as keys and zero value for pID and Id
    ids = make dict with name as key and pid as value from attendees
    student_id = add student_placeholder and pIDS together
def get_camera_contributions(index_stream_xml):
    #make dict of time on camera with student id as key
    camera_time = dict with id as key and time on camera as value
    replace id with student name from student_id dict

def get_microphone_contributions(index_stream_xml):
    #make dict of microphone events with student id as key
    on_mic_times = dict with id as key and times mic turned on as value
    replace id with student name from student_id dict

def get_handsup_contributions(index_stream_xml):
    # make dict of handsup events with student id as key
    handsup_events = dict with id as key and handsup events as value
    replace idmwith student name from student_id dict

def get_chat_contributions(ft_chat):
    # make dict of chat contributions with pID as key
    chat_contributions = dict with id as key and handsup events as value

def get_contribution_summary(student_ids,cam_contributions,mic_contributions,handsup_contributions, chat_contributions):
    # append all the dictionaries together


index_stream_xml_path = '/Users/JeffHalley/Adobe Connect Project/adobe connect recording files/indexstream.xml'

with open('/Users/JeffHalley/Adobe Connect Project/adobe connect recording files/indexstream.xml') as fp:
    soup = BeautifulSoup(fp,"xml")

student_name = soup.find_all('fullName')
student_id = student_name.find_all_next


name_variable = "Jeff Halley"
name_variable_before_student_id = soup.find(text= name_variable)
student_id = name_variable_before_student_id.parent.find_next_sibling("id")

def get_student_ids_and_pIDs(index_stream_xml_path):
    with open(index_stream_xml_path) as filepath:
        index_stream = BeautifulSoup(filepath,"xml")
    #this will return a result set that can be used as an index to find 
    #the record that contains id and pID for each student
    student_names_index = index_stream.find_all('fullName')
    student_names = []
    id_numbers = []
    pID_numbers = []
    for item in range(len(student_names_index)):
        #use the name index to access the actual name and add it to the list of names
        student_name = student_names_index[item].parent.fullName.text
        student_names.append(student_name)
        #use the name index to find the student id number for the student
        id_number = student_names_index[item].find_next_sibling("id").text
        id_numbers.append(id_number)
        # use the name index to find the the pID for each student and add to list
        pID_number = student_names_index[item].find_next_sibling("pID").text
        pID_numbers.append(pID_number)
    student_ids = dict(zip(student_names,id_numbers))
    student_pIDs = dict(zip(student_names,pID_numbers))
    return student_ids, student_pIDs
    #future plans: take a second argument a student roster cvs file make a dict
    #with zeroes for all students to act as a placeholder. Then use combined
    #dict from insight project. to give students with no record a zero

def get_camera_contributions(index_stream_xml_path):
    with open(index_stream_xml_path) as filepath:
        index_stream = BeautifulSoup(filepath,"xml")
    #get time when student came on camera
    camera_starts_index = index_stream.find_all(string = 'streamAdded')
    camera_start_ids = []
    camera_start_times = []
    for item in range(len(camera_starts_index)):
        #get id number of student that started their camera
        camera_start_id = camera_starts_index[item].parent.parent.streamPublisherID.text
        camera_start_ids.append(camera_start_id)
        #get time that student started their camera
        camera_start_time = camera_starts_index[item].parent.parent.startTime.text
        camera_start_times.append(camera_start_time)
    student_camera_start_times = defaultdict(set)
    for student_id, start_time in zip(camera_start_ids,camera_start_times):
        student_camera_start_times[student_id].add(start_time) 
    
    
    #get time when student turned off camera
    camera_stops_index = index_stream.find_all(string = 'streamRemoved')
    camera_stops_ids = []
    camera_stops_times = []
    for item in range(len(camera_stops_index)):
        #get id number of student that started their camera
        camera_stops_id = camera_stops_index[item].parent.parent.streamPublisherID.text
        camera_stops_ids.append(camera_stops_id)
        #get time that student started their camera
        camera_stops_time = camera_stops_index[item].parent.parent.time.text
        camera_stops_times.append(camera_stops_time)
    student_camera_stop_times = defaultdict(set)
    for student_id, stop_time in zip(camera_stops_ids,camera_stops_times):
        student_camera_stop_times[student_id].add(stop_time)
    
    #get end of class time
    end_of_class_object = index_stream.find_all(text = '__stop__')   
    end_of_class_time = end_of_class_object[len(end_of_class_object)-1].parent.parent.Number.text
    
    return student_camera_start_times, student_camera_stop_times
    
    #if students did not leave class before class stopped use end of class time
    for k in test2.keys()

 test = get_camera_contributions(index_stream_xml_path)
 
 test,test2 = get_camera_contributions(index_stream_xml_path)
 
