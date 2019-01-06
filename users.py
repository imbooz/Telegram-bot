import pickle

file_destination = r'users/ids.dat'


def file_with_ids():
	file = open(file_destination, 'rb')
	ids_list = pickle.load(file)
	file.close()
	return set(ids_list)


list_for_ids = file_with_ids()


def save_ids(user_id):
	ids_list = list_for_ids
	ids_list.update([user_id])
	file = open(file_destination, 'wb')
	pickle.dump(ids_list, file)
	file.close()


def remove_ids(user_id):
	ids_list = list_for_ids
	ids_list.remove(user_id)
	file = open(file_destination, 'wb')
	pickle.dump(ids_list, file)
	file.close()
