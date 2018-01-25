from flask_login import UserMixin
from dao.people import peopledao


class User(UserMixin):

    def build_person_dict(self, row):
        profile = {}
        profile['fname'] = row[0]
        profile['lname'] = row[1]
        profile['Phone'] = row[2]
        profile['Address'] = row[3]
        profile['City'] = row[4]
        profile['Country'] = row[5]
        profile['District'] = row[6]
        profile['Zipcode'] = row[7]
        return profile

    def __init__(self, person_id=None, id=None, password=None,
                 address_id=None, account_id=None, profile_info=None,
                 user_type=None):
        self.person_id = person_id
        self.id = id
        self.password = password
        self.address_id = address_id
        self.account_id = account_id
        self.profile_info = profile_info
        self.user_type = user_type


    def get_profile(self, pid):
        dao = peopledao()
        userlist = dao.getUserProfile(pid)
        dubylist = self.build_person_dict(userlist)
        return dubylist

    def get_user(self, us): #using pId
        dao = peopledao()
        userlist = dao.getUserKeys(us)
        if userlist:
            usr = User()
            usr.__set_user(userlist)
            return usr
        return None

    def __set_user(self, plist):
        self.person_id=plist[0]
        self.address_id=plist[1]
        self.account_id=plist[2]
        self.id=plist[3]
        self.password=plist[4]
        self.user_type=plist[5]

    def set_user(self, us):
        dao = peopledao()
        userlist = dao.getUserKeys(us)
        if userlist:
            self.__set_user(userlist)
            return True
        else:
            return False

    # @property
    # def personid(self):
    #     return self._personid
    #
    # @personid.setter
    # def personid(self, value):
    #     self._personid = value
    #
    # @property
    # def username(self):
    #     return self._username
    #
    # @username.setter
    # def username(self, value):
    #     self._username = value
    #
    # @property
    # def password(self):
    #     return self._password
    #
    # @password.setter
    # def password(self, value):
    #     self._password = value
    #
    # @property
    # def addressid(self):
    #     return self._addressid
    #
    # @addressid.setter
    # def addressid(self, value):
    #     self._addressid = value
    #
    # @property
    # def accountid(self):
    #     return self._accountid
    #
    # @accountid.setter
    # def accountid(self, value):
    #     self._accountid = value
