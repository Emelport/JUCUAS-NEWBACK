# models/choices.py
from enum import Enum as PyEnum

class GenderEnum(PyEnum):
    M = 'M'
    H = 'H'
    O = 'O'
    N = 'N'

class PositionInstitution(str, PyEnum):
    ESTUDIANTE = 'Estudiante'
    MAESTRO = 'Maestro'
    DIRECTOR = 'Director'
    PERSONAL_CONFIANZA = 'Personal de confianza'
    EXTERNO = 'Externo'

class Gender(str, PyEnum):
    MUJER = 'Mujer'
    HOMBRE = 'Hombre'
    OTRO = 'Otro'

class AcademicDegree(str, PyEnum):
    LICENCIATURA = 'Licenciatura'
    MAESTRIA = 'Maestría'
    DOCTORADO = 'Doctorado'

class AreaKnowledge(str, PyEnum):
    I = 'I. Físico-Matemáticas y Ciencias de la Tierra'
    II = 'II. Biología y Química'
    III = 'III. Medicina y Ciencias de la Salud'
    IV = 'IV. Ciencias de la Conducta y la Educación'
    V = 'V. Humanidades'
    VI = 'VI. Ciencias Sociales'
    VII = 'VII. Ciencias de la Agricultura, Agropecuarias, Forestales y de Ecosistemas'
    VIII = 'VIII. Ingenierías y Desarrollo Tecnológico'
    IX = 'IX. Investigación Multidisciplinaria'

class EducationalLevel(str, PyEnum):
    PCO = 'Público en general'
    PREESC = 'Preescolar'
    PRIM = 'Primaria'
    SEC = 'Secundaria'
    MDSUP = 'Media superior'
    SUP = 'Superior'

class TypeOfPublic(str, PyEnum):
    INT = 'Interno'
    EXT = 'Externo'

class EvidenceStatus(str, PyEnum):
    SEND = 'Subido'
    DUE = 'Pendiente'
    INC = 'Incompleto'
    REJECT = 'Rechazado'
    OK = 'Aprobado'

class ActivityStatus(str, PyEnum):
    DUE = 'Pendiente'
    INC = 'Incompleto'
    REJECT = 'Rechazado'
    OK = 'Aprobado'

class UniversityRegion(str, PyEnum):
    N = 'Norte'
    CN = 'Centro-Norte'
    C = 'Centro'
    S = 'Sur'

class TypeEvidence(str, PyEnum):
    PDF = 'PDF'
    URL = 'URL'

class Modality(str, PyEnum):
    P = 'Presencial'
    V = 'Virtual'
