from enum import Enum

class PositionInstitution(str, Enum):
    ESTUDIANTE = 'Estudiante'
    MAESTRO = 'Maestro'
    DIRECTOR = 'Director'
    PERSONAL_CONFIANZA = 'Personal de confianza'
    EXTERNO = 'Externo'

class Gender(str, Enum):
    MUJER = 'Mujer'
    HOMBRE = 'Hombre'
    OTRO = 'Otro'

class AcademicDegree(str, Enum):
    LICENCIATURA = 'Licenciatura'
    MAESTRIA = 'Maestría'
    DOCTORADO = 'Doctorado'

class AreaKnowledge(str, Enum):
    I = 'I. Físico-Matemáticas y Ciencias de la Tierra'
    II = 'II. Biología y Química'
    III = 'III. Medicina y Ciencias de la Salud'
    IV = 'IV. Ciencias de la Conducta y la Educación'
    V = 'V. Humanidades'
    VI = 'VI. Ciencias Sociales'
    VII = 'VII. Ciencias de la Agricultura, Agropecuarias, Forestales y de Ecosistemas'
    VIII = 'VIII. Ingenierías y Desarrollo Tecnológico'
    IX = 'IX. Investigación Multidisciplinaria'

class EducationalLevel(str, Enum):
    PCO = 'Público en general'
    PREESC = 'Preescolar'
    PRIM = 'Primaria'
    SEC = 'Secundaria'
    MDSUP = 'Media superior'
    SUP = 'Superior'

class TypeOfPublic(str, Enum):
    INT = 'Interno'
    EXT = 'Externo'

class EvidenceStatus(str, Enum):
    SEND = 'Subido'
    DUE = 'Pendiente'
    INC = 'Incompleto'
    REJECT = 'Rechazado'
    OK = 'Aprobado'

class ActivityStatus(str, Enum):
    DUE = 'Pendiente'
    INC = 'Incompleto'
    REJECT = 'Rechazado'
    OK = 'Aprobado'

class UniversityRegion(str, Enum):
    N = 'Norte'
    CN = 'Centro-Norte'
    C = 'Centro'
    S = 'Sur'

class TypeEvidence(str, Enum):
    PDF = 'PDF'
    URL = 'URL'

class Modality(str, Enum):
    P = 'Presencial'
    V = 'Virtual'