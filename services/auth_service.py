from database import Localsession, Base, engine, Employee
import bcrypt

# Base.metadata.drop_all(engine) # Use it to clear database in development environment
Base.metadata.create_all(engine)


def hash_password(plain_text_password):
    password_bytes = plain_text_password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=15)
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password


def verify_password(plain_text_password, hashed_password):
    password_bytes = plain_text_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)


def check_user(username: str, password: str):
    session = Localsession()
    try:
        employee = session.query(Employee).filter_by(username=username).first()
        if employee and verify_password(password, employee.password):
            return True
        else:
            return False  # Incorrect credentials
    finally:
        session.close()


def register_user(username: str, password: str):
    session = Localsession()
    try:
        if session.query(Employee).filter_by(username=username).first() is None:
            hashed_password = hash_password(password).decode('utf8')
            new_employee = Employee(username, hashed_password)
            session.add(new_employee)
            session.commit()
            return True

        else:
            return False  # Username already exists

    finally:
        session.close()
