
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base

ENGINE = create_engine('sqlite:///data_base.db3', echo=False)

BASE = declarative_base()


class Category(BASE):
    __tablename__ = 'categories'
    category_name  = Column(String, primary_key=True, nullable=False)
    category_description = Column(String, nullable=False)

    def __init__(self, category_name, category_description):
        self.category_name = category_name
        self.category_description = category_description


class Unit(BASE):
    __tablename__ = 'units'
    unit  = Column(String, primary_key=True, nullable=False)

    def __init__(self, unit):
        self.unit = unit


class Position(BASE):
    __tablename__ = 'positions'
    position  = Column(String, primary_key=True, nullable=False)

    def __init__(self, position):
        self.position = position


class Good(BASE):
    __tablename__ = 'Goods'
    good_id = Column(Integer, primary_key=True, nullable=False)
    good_name = Column(String)
    good_unit = Column(String, ForeignKey('units.unit'))
    good_cat = Column(String, ForeignKey('categories.category_name'))

    def __init__(self, good_id, good_name, good_unit, good_cat):
        self.good_id = good_id
        self.good_name = good_name
        self.good_unit = good_unit
        self.good_cat = good_cat


class Employe(BASE):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    employee_fio = Column(String)
    employee_position = Column(String, ForeignKey('positions.position'))

    def __init__(self, employee_id, employee_fio, employee_position):
        self.employee_id = employee_id
        self.employee_fio = employee_fio
        self.employee_position = employee_position


class Vendor(BASE):
    __tablename__ = 'Vendors'
    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column(String)
    vendor_ownerchipform = Column(String)
    vendor_address = Column(String)
    vendor_phone = Column(String)
    vendor_email = Column(String)

    def __init__(self, vendor_id, vendor_name, vendor_ownerchipform, vendor_address, vendor_phone, vendor_email):
        self.vendor_id = vendor_id
        self.vendor_name = vendor_name
        self.vendor_ownerchipform = vendor_ownerchipform
        self.vendor_address = vendor_address
        self.vendor_phone = vendor_phone
        self.vendor_email = vendor_email


BASE.metadata.create_all(ENGINE)
