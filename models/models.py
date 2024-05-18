from sqlalchemy import Table,Column, Integer, String, Enum, Boolean, ForeignKey,DateTime,Date,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from models.choices import *
import secrets


Base = declarative_base() # CLASE BASE DE LA QUE HEREDARÁN LOS MODELOS

# Definición de la tabla de relación
type_activity_type_evidence = Table(
    'type_activity_type_evidence',  # Nombre de la tabla en la base de datos
    Base.metadata,  # Metadatos de la base de datos donde se define la tabla
    Column('type_activity_id', Integer, ForeignKey('type_activity.id')),  # Clave foránea a type_activity
    Column('type_evidence_id', Integer, ForeignKey('type_evidence.id'))  # Clave foránea a type_evidence
)
# MODELO DE USUARIO
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)  # Especifica una longitud, por ejemplo, 50 caracteres
    email = Column(String(150), unique=True)
    password = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))
    gender = Column(Enum('M', 'H', 'O', 'N'), default='N', nullable=True)
    phone = Column(String(10), default="Asigna uno", nullable=True)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}', phone='{self.phone}')>"

class Tokens(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    token = Column(String(6))
    created_at = Column(DateTime, default=datetime.now)
    expired = Column(Boolean, default=True)

    user = relationship("User", back_populates="tokens")

    def generate(self):
        self.token = ''.join(str(secrets.randbelow(10)) for _ in range(6))
        self.created_at = datetime.now()
        self.expired = False

    def is_expired(self, cooldown):
        now = datetime.now()
        time_difference = now - self.created_at
        return time_difference.total_seconds() >= cooldown

    def check_token(self, token):
        if not self.is_expired(cooldown):
            if self.token == token:
                return "Valido"
            else:
                return "no valido"
        else:
            return "expirado"

    def validate(self, token):
        result = {'valid': False, 'reason': 'Token '}
        reason = self.check_token(token)
        result['reason'] += reason
        result['valid'] = reason == 'Valido'
        return result

    def expire(self):
        self.expired = True

    def __repr__(self):
        return f'Token de {self.user.first_name} {self.user.last_name}: {self.token}, {self.validate(self.token)["reason"]}'

# MODELO DE UNIVERSIDADES
class University(Base):
    __tablename__ = 'university'

    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    acronym = Column(String(10))
    key_code = Column(String(10))
    type = Column(Enum('PREESC', 'PRIM', 'SEC', 'P', 'U'), nullable=True)
    region = Column(Enum('N', 'CN', 'C', 'S'), nullable=True)
    municipality = Column(String(150))
    locality = Column(String(150))
    email = Column(String(150))
    phone = Column(String(10))
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)

    def __repr__(self):
        return f"<University(name='{self.name}')>"

# MODELO DE UNIDADES ORGANIZACIONALES
class OrganizationalUnit(Base):
    __tablename__ = 'organizational_unit'

    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    acronym = Column(String(10))
    key_code = Column(String(10))
    region = Column(Enum('N', 'CN', 'C', 'S'), nullable=True)
    municipality = Column(String(150))
    locality = Column(String(150))
    email = Column(String(150))
    phone = Column(String(10))
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)

    def __repr__(self):
        return f"<OrganizationalUnit(name='{self.name}')>"
      
# MODELO DE REVISORES
class Reviewer(Base):
    __tablename__ = 'reviewer'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship("User", backref="reviewer_user")
    first_name = Column(String(50))
    last_name = Column(String(50))
    user_name = Column(String(50))
    region = Column(Enum('N', 'CN', 'C', 'S'), nullable=True)
    global_reviewer = Column(Boolean, default=False)
    origin_university_id = Column(Integer, ForeignKey('university.id'), nullable=True)
    origin_university = relationship("University", foreign_keys=[origin_university_id])
    origin_highschool_id = Column(Integer, ForeignKey('university.id'), nullable=True)
    origin_highschool = relationship("University", foreign_keys=[origin_highschool_id], backref="origin_highschool")
    origin_organizational_unit_id = Column(Integer, ForeignKey('organizational_unit.id'), nullable=True)
    origin_organizational_unit = relationship("OrganizationalUnit", foreign_keys=[origin_organizational_unit_id])
    reviewer_permission = Column(String(10))
    email = Column(String(50))
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Reviewer(first_name='{self.first_name}', last_name='{self.last_name}')>"
    
# MODELO DE REPRESENTANTES
class Representative(Base):
    __tablename__ = 'representative'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship("User", backref="representative_user")
    first_name = Column(String(50))
    last_name = Column(String(50))
    user_name = Column(String(50))
    origin_university_id = Column(Integer, ForeignKey('university.id'), nullable=True)
    origin_university = relationship("University", foreign_keys=[origin_university_id])
    origin_organizational_unit_id = Column(Integer, ForeignKey('organizational_unit.id'), nullable=True)
    origin_organizational_unit = relationship("OrganizationalUnit", foreign_keys=[origin_organizational_unit_id])
    email = Column(String(50))
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Representative(first_name='{self.first_name}', last_name='{self.last_name}')>"

# MODELO DE PRESENTADORES
class Presenter(Base):
    __tablename__ = 'presenter'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship("User", backref="presenter_user")
    first_name = Column(String(50))
    last_name = Column(String(50))
    user_name = Column(String(50))
    gender = Column(Enum('M', 'H', 'O'), nullable=True)
    curp = Column(String(18))
    email = Column(String(50))
    phone = Column(String(10))
    academic_degree = Column(String(50))
    origin_university_id = Column(Integer, ForeignKey('university.id'), nullable=True)
    origin_university = relationship("University", foreign_keys=[origin_university_id])
    origin_organizational_unit_id = Column(Integer, ForeignKey('organizational_unit.id'), nullable=True)
    origin_organizational_unit = relationship("OrganizationalUnit", foreign_keys=[origin_organizational_unit_id])
    if_belong_to_school = Column(Boolean, default=True)
    position_institution = Column(Enum('1', '2', '3', '4', '5'), default='1')
    birth_date = Column(DateTime)
    created_by_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    created_by = relationship("User", foreign_keys=[created_by_id])
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Presenter(first_name='{self.first_name}', last_name='{self.last_name}')>"

# MODELO DE FECHAS LÍMITE
class Deadline(Base):
    __tablename__ = 'deadline'

    id = Column(Integer, primary_key=True)
    name_edition = Column(String(150))
    date_edition = Column(String(4))
    date_to_upload_activities = Column(Date)
    date_to_upload_evidence = Column(Date)
    date_to_validate_evidence = Column(Date)
    date_edition_start = Column(Date)
    end_date_of_the_edition = Column(Date)
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)
    file = Column(Text)
    file_name = Column(String(150))

    def __repr__(self):
        return f"<Deadline(name_edition='{self.name_edition}', date_edition='{self.date_edition}')>"

# MODELO DE RESPONSABLE DE ACTIVIDAD
class ActivityManager(Base):
    __tablename__ = 'activity_manager'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship("User", backref="activity_manager_user")
    first_name = Column(String(50))
    last_name = Column(String(50))
    gender = Column(Enum('M', 'H', 'O'), nullable=True)
    academic_degree = Column(Enum('L', 'M', 'D'), nullable=True)
    email = Column(String(50))
    birth_date = Column(DateTime)
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)

    def __repr__(self):
        return f"<ActivityManager(first_name='{self.first_name}', last_name='{self.last_name}')>"

# MODELO DE TIPO DE EVIDENCIA
class TypeEvidence(Base):
    __tablename__ = 'type_evidence'

    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    type = Column(Enum('PDF', 'URL'))
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)
    is_optional = Column(Boolean, default=False)

    def __repr__(self):
        return f"<TypeEvidence(name='{self.name}', type='{self.type}')>"

# MODELO DE TIPO DE ACTIVIDAD
class TypeActivity(Base):
    __tablename__ = 'type_activity'

    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    title = Column(String(800))
    max_copresenter = Column(String(100))
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)
    type_evidence = relationship("TypeEvidence", secondary='type_activity_type_evidence')

    def __repr__(self):
        return f"<TypeActivity(name='{self.name}', title='{self.title}')>"

# MODELO DE ACTIVIDAD
class Activity(Base):
    __tablename__ = 'activity'

    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    description = Column(String(500))
    numbers_expected_attendees = Column(Integer)
    numbers_total_attendees = Column(Integer)
    modality = Column(Enum('V', 'P'))
    edition_id = Column(Integer, ForeignKey('deadline.id'))
    date_activity = Column(DateTime)
    educational_level_to_is_directed = Column(Enum('PCO', 'PREESC', 'PRIM', 'SEC', 'MDSUP', 'SUP'))
    type_of_public = Column(Enum('INT', 'EXT'))
    area_knowledge = Column(Enum('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'))
    presenter_id = Column(Integer, ForeignKey('presenter.id'))
    presenter = relationship("Presenter", back_populates="activity_presenter", foreign_keys=[presenter_id])
    co_presenter = relationship("Presenter", secondary='activity_co_presenter', back_populates="co_presenter_activities")
    type_id = Column(Integer, ForeignKey('type_activity.id'))
    type = relationship("TypeActivity")
    created_by_id = Column(Integer, ForeignKey('user.id'))
    created_by = relationship("User", foreign_keys=[created_by_id])
    certificate_file = Column(String(255))
    activity_status = Column(Enum('DUE', 'INC', 'REJECT', 'OK'))
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Activity(name='{self.name}', date_activity='{self.date_activity}')>"

# TABLA DE RELACIÓN PARA ACTIVIDAD Y PRESENTADOR
class ActivityCoPresenter(Base):
    __tablename__ = 'activity_co_presenter'

    activity_id = Column(Integer, ForeignKey('activity.id'), primary_key=True)
    co_presenter_id = Column(Integer, ForeignKey('presenter.id'), primary_key=True)

# MODELO DE EVIDENCIA
class Evidence(Base):
    __tablename__ = 'evidence'

    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    observation = Column(String(1500))
    evidence_file = Column(String(255))
    evidence_status = Column(Enum('SEND', 'DUE', 'INC', 'REJECT', 'OK'))
    created_by_id = Column(Integer, ForeignKey('user.id'))
    created_by = relationship("User", foreign_keys=[created_by_id])
    status_changed_by_id = Column(Integer, ForeignKey('user.id'))
    status_changed_by = relationship("User", foreign_keys=[status_changed_by_id])
    type_evidence_id = Column(Integer, ForeignKey('type_evidence.id'))
    type_evidence = relationship("TypeEvidence")
    activity_id = Column(Integer, ForeignKey('activity.id'))
    activity = relationship("Activity", back_populates="related_evidences")

    def __repr__(self):
        return f"<Evidence(name='{self.name}', evidence_status='{self.evidence_status}')>"

