from App import db, login_manager


class Response(db.Model):
    __tablename__ = "responses"
    turkid = db.Column('turkid', db.String(20), unique=True, index=True, primary_key=True)
    fundtype = db.Column('fundtype', db.String(20))
    weeknumber = db.Column('weeknumber', db.Integer())
    fundpastbalance = db.Column('fundpastbalance', db.Float())
    salarypastbalance = db.Column('salarypastbalance', db.Float())
    fundhistory = db.Column('fundhistory', db.String(50))
    salaryhistory = db.Column('salaryhistory', db.String(50))
    foodhistorysalary = db.Column('foodhistorysalary', db.String(50))
    foodhistoryfund = db.Column('foodhistoryfund', db.String(50))
    timespenthistory = db.Column('timespenthistory', db.String(50))

    def __init__(self, turkid, fundtype):
        self.turkid = turkid
        self.fundtype = fundtype
        self.weeknumber = 0
        self.fundpastbalance = 100
        self.salarypastbalance = 0
        self.fundhistory = ""
        self.salaryhistory = ""
        self.foodhistoryfund = ""
        self.foodhistorysalary = ""
        self.timespenthistory = ""

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    @property
    def info(self):
        info = {}
        for key in ["fundtype", "weeknumber", "fundpastbalance", "salarypastbalance", "fundhistory",
                    "salaryhistory", "foodhistoryfund", "foodhistorysalary", "timespenthistory"]:
            info[key] = self.__dict__.get(key)
        return info

    @info.setter
    def info(self, dict):
        for key in ["weeknumber", "fundpastbalance", "salarypastbalance", "fundhistory", "salaryhistory",
                    "foodhistoryfund", "foodhistorysalary", "timespenthistory"]:
            if key in ["fundpastbalance", "salarypastbalance"]:
                setattr(self, key, float(dict[key]))
            elif key == "weeknumber":
                setattr(self, key, int(dict[key]))
            else:
                setattr(self, key, dict[key])

    def get_id(self):
        return self.turkid

    def __repr__(self):
        base = "MTurk ID = {}\n".format(self.turkid)
        for key, value in self.info.items():
            base += "{} = {}\n".format(key, value)
        return base


@login_manager.user_loader
def load_user(user_id):
    return Response.query.get(user_id)
