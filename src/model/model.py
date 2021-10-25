from requests.sessions import session
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import os
import ast


class DefaultTools:
    
    path = os.path.dirname(os.path.abspath(__file__))   
    db_path = os.path.join(path, 'database.db')
    engine = create_engine(f'sqlite:///{db_path}?check_same_thread=False', echo=False)
    engine_session = sessionmaker(engine)
    session_handle = engine_session()
    base = declarative_base(bind=engine)      


class Account(DefaultTools.base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    ronin_address = Column(String(42))
    data = Column(String(500))
    scholar = relationship('Scholar', backref='account')

    def __repr__(self):
        return f'Ronin: {self.ronin_address}, data: {self.data}, scholar: {self.scholar}'

    @classmethod
    def find_by_address(cls, session, ronin_address: str):
        return session.query(cls).filter(cls.ronin_address == ronin_address).first()

    @classmethod
    def find_by_id(cls, session, id_input: str):
        return session.query(cls).filter(cls.id == id_input).first()

    @classmethod
    def get_axies_amount(cls, session) -> int:
        q = session.query(cls).all()
        
        amount_axies = 0
        
        for acc in q:
            data_dict = ast.literal_eval(acc.data)
            
            amount_axies += len(data_dict)
            
        return amount_axies

    @classmethod
    def get_axie_image(cls, session, lista_id: list) -> list:
        images = []

        for id in lista_id:
            obj = session.query(cls).filter(cls.id == id).first()
            data = ast.literal_eval(obj.data)

            images.append(data['0']['image'])

        return images


class Scholar(DefaultTools.base):
    __tablename__ = 'scholars'

    name = Column(String(32), primary_key=True)
    email = Column(String(32))
    mmr = Column(Integer)
    rank = Column(Integer)
    total_acc_slp = Column(Integer)
    total_average_slp = Column(Integer)
    daily_goal = Column(Integer)
    account_id = Column(Integer, ForeignKey('accounts.id'), primary_key=True)
    last_time_checked = Column(String(16))
    daily_profit = Column(Integer)
    actual_month_profit = Column(Integer)
    last_month_profit = Column(Integer)
    next_to_last_month_profit = Column(Integer)

    def __repr__(self):
        return f'Name: {self.name}, email: {self.email}, daily_goal: {self.daily_goal}, ' \
               f'account: {self.account.ronin_address}'

    @classmethod
    def find_by_name(cls, session, name_input: str):
        return session.query(cls).filter(cls.name.like(f'%{name_input}%')).first()

    @classmethod
    def find_by_rank(cls, session, rank_input: list) -> list:
        q = []
        
        for rank in rank_input:
            q.append(session.query(cls).filter_by(rank=rank).first())

        return q
    
    @classmethod
    def set_account_id(cls, session, name_input: str, account_id: int):
        session.query(cls).filter(cls.name.like(f'%{name_input}%')).update({cls.account_id: account_id}, synchronize_session=False)
        session.commit()
               
    @classmethod
    def set_daily_profit(cls, session, value, name_input=None, ronin=None):
        
        if name_input != None:
            session.query(cls).filter(cls.name.like(f'%{name_input}%')).update({cls.daily_profit: value}, synchronize_session=False)
        else:
            r = session.query(Account).filter(Account.ronin_address.like(f'%{ronin}%')).first()
            session.query(cls).filter(cls.account_id == r.id).update({cls.daily_profit: value}, synchronize_session=False)
        session.commit()
    
    @classmethod
    def set_month_changed(cls, session):
        scholars_list = cls.get_all_scholars(session)
         
        for i in range(0, cls.get_scholar_amount(session)):
            actual_month_value = scholars_list[i].actual_month_profit
            last_month_value = scholars_list[i].last_month_profit
            
            session.query(cls).filter(cls.name.like(f'%{scholars_list[i].name}%')).update({cls.next_to_last_month_profit: last_month_value}, synchronize_session=False)
            session.query(cls).filter(cls.name.like(f'%{scholars_list[i].name}%')).update({cls.last_month_profit: actual_month_value}, synchronize_session=False)
            session.query(cls).filter(cls.name.like(f'%{scholars_list[i].name}%')).update({cls.actual_month_profit: 0}, synchronize_session=False)
            session.commit()
   
    @classmethod 
    def update_month_profit(cls, session, name_input: str, value: int):
        scholar = cls.find_by_name(session, name_input)
        
        value_update = value + scholar.actual_month_profit
        
        session.query(cls).filter(cls.name.like(f'%{name_input}%')).update({cls.actual_month_profit: value_update},  synchronize_session=False)
        session.commit()
    
    @classmethod
    def update_rank(cls, session, name_input: str, value: int):        
        value_update = value
        
        session.query(cls).filter(cls.name.like(f'%{name_input}%')).update({cls.rank: value_update},  synchronize_session=False)
        session.commit()
    
    @classmethod
    def update_mmr(cls, session, name_input: str, value: int):        
        value_update = value
        
        session.query(cls).filter(cls.name.like(f'%{name_input}%')).update({cls.mmr: value_update},  synchronize_session=False)
        session.commit()

    @classmethod
    def update_total_slp_acc(cls, session, name_input: str, value: int):        
        value_update = value
        
        session.query(cls).filter(cls.name.like(f'%{name_input}%')).update({cls.total_acc_slp: value_update},  synchronize_session=False)
        session.commit()

    @classmethod
    def update_average_slp(cls, session, name_input: str, value: int):        
        value_update = value
        
        session.query(cls).filter(cls.name.like(f'%{name_input}%')).update({cls.total_average_slp: value_update},  synchronize_session=False)
        session.commit()
                    
    @classmethod
    def update_time_checked(cls, session, value: str):
        
        q = session.query(cls.last_time_checked).all()
        
        session.query(cls).update({cls.last_time_checked: value}, synchronize_session=False)
        session.commit()
    
    @classmethod
    def get_ronin_address(cls, session, name_input: str) -> list:
        scholar = cls.find_by_name(session, name_input)
        
        ronin_address = scholar.account.ronin_address

        return ronin_address
    
    @classmethod
    def get_all_scholars(cls, session) -> list:
        
        q = session.query(cls).all()        
        
        return q
        
    @classmethod
    def get_scholar_amount(cls, session) -> int:
        q = session.query(cls).all()
        
        amount_scholar = len(q)
            
        return amount_scholar

    @classmethod
    def get_daily_goal_and_profit(cls, session) -> int:
        goal = [tpl[0] for tpl in session.query(cls.daily_goal).all()]
        profit = [tpl[0] for tpl in session.query(cls.daily_profit).all()]
        
        total_goal = sum(goal)
        total_profit = sum(profit) 
            
        return total_goal, total_profit
    
    @classmethod
    def get_months_values(cls, session) -> int:
        actual = [tpl[0] for tpl in session.query(cls.actual_month_profit).all()]
        last = [tpl[0] for tpl in session.query(cls.last_month_profit).all()]
        next_last = [tpl[0] for tpl in session.query(cls.next_to_last_month_profit).all()]
        
        total_actual = sum(actual)
        total_last = sum(last)
        total_next_last = sum(next_last)
        
        return total_actual, total_last, total_next_last
    
    @classmethod
    def get_dict_last_time_checked(cls, session) -> dict:
        
        dict_return = {'name': [tpl[0] for tpl in session.query(cls.name).all()],
                       'last_time': []}
        
        for k, v in dict_return.items():
            if k == 'name':
                for item in v:
                    append_list = [dict_return['last_time'].append(tpl[0]) for tpl in session.query(cls.last_time_checked).filter(cls.name == item).all()]
        
        return dict_return
    
    @classmethod
    def get_dict_daily_profit(cls, session) -> dict:
        dict_return = { 'name': [tpl[0] for tpl in session.query(cls.name).all()],
                       'daily_profit': []}
        
        for k, v in dict_return.items():
            if k == 'name':
                for item in v:
                    append_list = [dict_return['daily_profit'].append(tpl[0]) for tpl in session.query(cls.daily_profit).filter(cls.name == item).all()]
        
        return dict_return
    
    @classmethod
    def get_dict_acc_ronin(cls, session) -> dict:
    
        dict_return = { 'name': [tpl[0] for tpl in session.query(cls.name).all()],
                       'acc_ronin': []}
        
        for k, v in dict_return.items():
            if k == 'name':
                for item in v:
                    obj = cls.find_by_name(session, item)
                    r = session.query(Account).filter(Account.id.like(f'%{obj.account_id}%')).first()
                    dict_return['acc_ronin'].append(r.ronin_address)
        
        return dict_return



if __name__ == '__main__':
    DefaultTools.base.metadata.create_all(DefaultTools.engine)
