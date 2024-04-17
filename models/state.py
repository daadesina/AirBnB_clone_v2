#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Getter attribute"""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
