import requests


class VK:
	API_URL = 'https://api.vk.com/method/'

	def __init__(self, token, version='5.199'):
		self.token = token
		self.version = version

	def _call(self, method, **params):
		params['access_token'] = self.token
		params['v'] = self.version

		r = requests.post(self.API_URL + method, params=params)
		data = r.json()

		if 'error' in data:
			raise Exception(data['error'])

		return data['response']

	# USERS
	def users_get(self, user_ids=None, fields=None):
		return self._call('users.get', user_ids=user_ids, fields=fields)

	def users_search(self, q, count=20):
		return self._call('users.search', q=q, count=count)

	# FRIENDS
	def friends_get(self, user_id=None):
		return self._call('friends.get', user_id=user_id)

	# GROUPS
	def groups_get(self, user_id=None):
		return self._call('groups.get', user_id=user_id)

	def groups_get_members(self, group_id, count=1000, offset=0):
		return self._call('groups.getMembers', group_id=group_id, count=count, offset=offset)

	# MESSAGES
	def messages_send(self, user_id, message=None, attachment=None, random_id=0):
		return self._call('messages.send', user_id=user_id, message=message, attachment=attachment, random_id=random_id)	

	def messages_get_history(self, user_id, count=20):
		return self._call('messages.getHistory', user_id=user_id, count=count)

	# WALL
	def wall_post(self, owner_id, message):
		return self._call('wall.post', owner_id=owner_id, message=message)

	def wall_get(self, owner_id, count=10):
		return self._call('wall.get', owner_id=owner_id, count=count)