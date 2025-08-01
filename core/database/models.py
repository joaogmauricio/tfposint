from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
import uuid

Base = declarative_base()

def gen_id():
    return str(uuid.uuid4())

class Source(Base):
    __tablename__ = 'source'
    id = Column(String, primary_key=True, default=gen_id)
    type = Column(String)
    tool = Column(String)
    source_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    documents = relationship("Document", back_populates="source")
    phones = relationship("PhoneNumber", back_populates="source")
    emails = relationship("EmailAddress", back_populates="source")
    addresses = relationship("Address", back_populates="source")
    images = relationship("Image", back_populates="source")
    usernames = relationship("Username", back_populates="source")
    leaks = relationship("Leak", back_populates="source")
    employments = relationship("Employment", back_populates="source")

class Document(Base):
    __tablename__ = 'document'
    id = Column(String, primary_key=True, default=gen_id)
    path = Column(String)
    description = Column(Text)
    person_id = Column(String, ForeignKey('person.id'))
    source_id = Column(String, ForeignKey('source.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    person = relationship("Person", back_populates="documents")
    source = relationship("Source", back_populates="documents")

class Person(Base):
    __tablename__ = 'person'
    id = Column(String, primary_key=True, default=gen_id)
    full_name = Column(String)
    alias = Column(String)
    nationality = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    documents = relationship("Document", back_populates="person")
    phones = relationship("PhoneNumber", back_populates="person")
    emails = relationship("EmailAddress", back_populates="person")
    addresses = relationship("Address", back_populates="person")
    images = relationship("Image", back_populates="person")
    usernames = relationship("Username", back_populates="person")
    leaks = relationship("Leak", back_populates="person")
    employments = relationship("Employment", back_populates="person")
    relationships_from = relationship("Relationship", back_populates="from_person", foreign_keys="Relationship.from_person_id")
    relationships_to = relationship("Relationship", back_populates="to_person", foreign_keys="Relationship.to_person_id")

class PhoneNumber(Base):
    __tablename__ = 'phonenumber'
    id = Column(String, primary_key=True, default=gen_id)
    number = Column(String)
    person_id = Column(String, ForeignKey('person.id'))
    source_id = Column(String, ForeignKey('source.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    person = relationship("Person", back_populates="phones")
    source = relationship("Source", back_populates="phones")

class EmailAddress(Base):
    __tablename__ = 'emailaddress'
    id = Column(String, primary_key=True, default=gen_id)
    email = Column(String)
    person_id = Column(String, ForeignKey('person.id'))
    source_id = Column(String, ForeignKey('source.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    person = relationship("Person", back_populates="emails")
    source = relationship("Source", back_populates="emails")

class Address(Base):
    __tablename__ = 'address'
    id = Column(String, primary_key=True, default=gen_id)
    address = Column(String)
    person_id = Column(String, ForeignKey('person.id'))
    source_id = Column(String, ForeignKey('source.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    person = relationship("Person", back_populates="addresses")
    source = relationship("Source", back_populates="addresses")

class Image(Base):
    __tablename__ = 'image'
    id = Column(String, primary_key=True, default=gen_id)
    path = Column(String)
    person_id = Column(String, ForeignKey('person.id'))
    source_id = Column(String, ForeignKey('source.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    person = relationship("Person", back_populates="images")
    source = relationship("Source", back_populates="images")

class Relationship(Base):
    __tablename__ = 'relationship'
    id = Column(String, primary_key=True, default=gen_id)
    from_person_id = Column(String, ForeignKey('person.id'))
    to_person_id = Column(String, ForeignKey('person.id'))
    type = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    from_person = relationship("Person", back_populates="relationships_from", foreign_keys=[from_person_id])
    to_person = relationship("Person", back_populates="relationships_to", foreign_keys=[to_person_id])

class Organization(Base):
    __tablename__ = 'organization'
    id = Column(String, primary_key=True, default=gen_id)
    name = Column(String)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    employments = relationship("Employment", back_populates="organization")

class Employment(Base):
    __tablename__ = 'employment'
    id = Column(String, primary_key=True, default=gen_id)
    person_id = Column(String, ForeignKey('person.id'))
    organization_id = Column(String, ForeignKey('organization.id'))
    role = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    source_id = Column(String, ForeignKey('source.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    person = relationship("Person", back_populates="employments")
    organization = relationship("Organization", back_populates="employments")
    source = relationship("Source", back_populates="employments")

class Username(Base):
    __tablename__ = 'username'
    id = Column(String, primary_key=True, default=gen_id)
    person_id = Column(String, ForeignKey('person.id'))
    username = Column(String)
    platform = Column(String)
    source_id = Column(String, ForeignKey('source.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    person = relationship("Person", back_populates="usernames")
    source = relationship("Source", back_populates="usernames")

class Leak(Base):
    __tablename__ = 'leak'
    id = Column(String, primary_key=True, default=gen_id)
    description = Column(Text)
    link = Column(String)
    person_id = Column(String, ForeignKey('person.id'))
    source_id = Column(String, ForeignKey('source.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    person = relationship("Person", back_populates="leaks")
    source = relationship("Source", back_populates="leaks")
