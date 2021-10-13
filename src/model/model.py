from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import os
import ast


class DefaultTools:
    
    path = os.path.dirname(os.path.abspath(__file__))   
    db_path = os.path.join(path, 'database.db')
    engine = create_engine(f'sqlite:///{db_path}?check_same_thread=False', echo=True)
    engine_session = sessionmaker(engine)
    session_handle = engine_session()
    base = declarative_base(bind=engine)


class Account(DefaultTools.base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    ronin_address = Column(String(32))
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

class Scholar(DefaultTools.base):
    __tablename__ = 'scholars'

    name = Column(String(32), primary_key=True)
    email = Column(String(32))
    daily_goal = Column(Integer)
    account_id = Column(Integer, ForeignKey('accounts.id'), primary_key=True)
    last_time_checked = Column(String(16))
    daily_profit = Column(Integer)
    daily_profit_cached = Column(Integer)
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
    def set_account_id(cls, session, name_input: str, account_id: int):
        session.query(cls).filter(cls.name.like(f'%{name_input}%')).update({cls.account_id: account_id})
        
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
    
    
if __name__ == '__main__':
    DefaultTools.base.metadata.create_all(DefaultTools.engine)
    
# TODO:
# criar um metodo para atualizar daily profit
# importante também deixar salvo quando foi a ultima consulta, ou usar o localtime \
# com base nesses dados podemos resetar o daily profit e popular os ganhos mensais do scholar ate o momento,
# pensar em fazer uma db para registrar os ganhos diarios
