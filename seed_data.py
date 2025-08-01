from core.database.db import init_db, SessionLocal
from core.database.models import (
    Source,
    Person,
    EmailAddress,
    PhoneNumber,
    Username,
    Address,
    Document,
    Leak,
    Organization,
    Employment,
    Relationship,
)

def seed_db():
    """Populate the database with mock data for development/testing."""
    # Initialize database schema
    init_db()

    # Start a session
    session = SessionLocal()

    # Create a source record for this seeding operation
    seed_source = Source(
        type="tool",
        tool="seed-script",
        source_url="local"
    )
    session.add(seed_source)
    session.commit()

    # Mock data for 5 people
    mock_people = [
        {
            "full_name": "Alice Smith",
            "alias": "asmith",
            "nationality": "US",
            "email": "alice.smith@example.com",
            "phone": "+11234567890",
            "username": "alice_smith",
            "address": "123 Maple Street, Springfield, US",
            "document": {"path": "docs/alice_passport.pdf", "description": "Passport scan"}
        },
        {
            "full_name": "Bob Johnson",
            "alias": "bobby",
            "nationality": "UK",
            "email": "bob.johnson@example.co.uk",
            "phone": "+441234567890",
            "username": "bobj",
            "address": "456 Oak Avenue, London, UK",
            "document": {"path": "docs/bob_resume.docx", "description": "Resume"}
        },
        {
            "full_name": "Carlos Ruiz",
            "alias": "cruiz",
            "nationality": "ES",
            "email": "carlos.ruiz@example.es",
            "phone": "+341234567890",
            "username": "carlosr",
            "address": "789 Pine Road, Madrid, ES",
            "document": {"path": "docs/carlos_idcard.pdf", "description": "ID card"}
        },
        {
            "full_name": "Diana Müller",
            "alias": "dmueller",
            "nationality": "DE",
            "email": "diana.mueller@example.de",
            "phone": "+491234567890",
            "username": "diana_m",
            "address": "101 Birch Lane, Berlin, DE",
            "document": {"path": "docs/diana_contract.pdf", "description": "Employment contract"}
        },
        {
            "full_name": "Émile Dubois",
            "alias": "edubois",
            "nationality": "FR",
            "email": "emile.dubois@example.fr",
            "phone": "+331234567890",
            "username": "emiled",
            "address": "202 Cedar Boulevard, Paris, FR",
            "document": {"path": "docs/emile_driver_license.pdf", "description": "Driver license"}
        }
    ]

    # Insert persons and related records
    people_objects = []
    for entry in mock_people:
        person = Person(
            full_name=entry["full_name"],
            alias=entry["alias"],
            nationality=entry["nationality"]
        )
        session.add(person)
        session.commit()
        people_objects.append(person)

        email = EmailAddress(
            email=entry["email"],
            person_id=person.id,
            source_id=seed_source.id
        )
        phone = PhoneNumber(
            number=entry["phone"],
            person_id=person.id,
            source_id=seed_source.id
        )
        username = Username(
            username=entry["username"],
            platform="twitter",
            person_id=person.id,
            source_id=seed_source.id
        )
        address = Address(
            address=entry["address"],
            person_id=person.id,
            source_id=seed_source.id
        )
        doc_info = entry["document"]
        document = Document(
            path=doc_info["path"],
            description=doc_info["description"],
            person_id=person.id,
            source_id=seed_source.id
        )
        session.add_all([email, phone, username, address, document])
        session.commit()

    # Create organizations
    org_acme = Organization(
        name="Acme Corp",
        description="A leading widget manufacturer"
    )
    org_globex = Organization(
        name="Globex Inc",
        description="International conglomerate"
    )
    session.add_all([org_acme, org_globex])
    session.commit()

    # Employment records
    employments = [
        Employment(
            person_id=people_objects[0].id,
            organization_id=org_acme.id,
            role="Engineer",
            start_date="2020-01-15",
            end_date=None,
            source_id=seed_source.id
        ),
        Employment(
            person_id=people_objects[1].id,
            organization_id=org_globex.id,
            role="Manager",
            start_date="2018-05-01",
            end_date="2021-12-31",
            source_id=seed_source.id
        ),
        Employment(
            person_id=people_objects[2].id,
            organization_id=org_acme.id,
            role="Analyst",
            start_date="2019-07-10",
            end_date=None,
            source_id=seed_source.id
        ),
        Employment(
            person_id=people_objects[3].id,
            organization_id=org_globex.id,
            role="Consultant",
            start_date="2021-03-20",
            end_date=None,
            source_id=seed_source.id
        ),
        Employment(
            person_id=people_objects[4].id,
            organization_id=org_acme.id,
            role="Designer",
            start_date="2022-11-01",
            end_date=None,
            source_id=seed_source.id
        )
    ]
    session.add_all(employments)
    session.commit()

    # Relationships between people
    relationships = [
        Relationship(
            from_person_id=people_objects[0].id,
            to_person_id=people_objects[1].id,
            type="colleague"
        ),
        Relationship(
            from_person_id=people_objects[1].id,
            to_person_id=people_objects[2].id,
            type="friend"
        ),
        Relationship(
            from_person_id=people_objects[2].id,
            to_person_id=people_objects[3].id,
            type="sibling"
        ),
        Relationship(
            from_person_id=people_objects[3].id,
            to_person_id=people_objects[4].id,
            type="relative"
        ),
        Relationship(
            from_person_id=people_objects[4].id,
            to_person_id=people_objects[0].id,
            type="friend"
        )
    ]
    session.add_all(relationships)
    session.commit()

    # Leak records
    leaks = [
        Leak(
            description="Acme Corp data breach 2022",
            link="https://example.com/acme-breach-2022",
            person_id=people_objects[0].id,
            source_id=seed_source.id
        ),
        Leak(
            description="Globex user leak",
            link="https://example.com/globex-leak",
            person_id=people_objects[3].id,
            source_id=seed_source.id
        )
    ]
    session.add_all(leaks)
    session.commit()

    # Close session
    session.close()

    print("✅ Seeded mock data for people, contacts, user info, addresses, documents, employment, organizations, relationships, and leaks.")


if __name__ == "__main__":
    seed_db()
