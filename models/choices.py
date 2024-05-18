cooldown = 300


# Opciones para la posición en la institución
POSITION_INSTITUTION_CHOICES = (
    ('1', 'Estudiante'),
    ('2', 'Maestro'),
    ('3', 'Director'),
    ('4', 'Personal de confianza'),
    ('5', 'Externo'),
)

#Opciones para el género
GENDER_CHOICES = (
    ('M', 'Mujer'),
    ('H', 'Hombre'),
    ('O', 'Otro'),
)

# Opciones para el grado académico
ACADEMIC_DEGREE_CHOICES = (
    ('L', 'Licenciatura'),
    ('M', 'Maestría'),
    ('D', 'Doctorado'),
)

# Opciones para el área de conocimiento
AREA_KNOWLEDGE_CHOICES = (
    ('I', 'I. Físico-Matemáticas y Ciencias de la Tierra'),
    ('II', 'II. Biología y Química'),
    ('III', 'III. Medicina y Ciencias de la Salud'),
    ('IV', 'IV. Ciencias de la Conducta y la Educación'),
    ('V', 'V. Humanidades'),
    ('VI', 'VI. Ciencias Sociales'),
    ('VII', 'VII. Ciencias de la Agricultura, Agropecuarias, Forestales y de Ecosistemas'),
    ('VIII', 'VIII. Ingenierías y Desarrollo Tecnológico'),
    ('IX', 'IX. Investigación Multidisciplinaria'),
)

# Opciones para el nivel educativo dirigido
EDUCATIONAL_LEVEL_TO_IS_DIRECTED_CHOICES = (
    ('PCO', 'Público en general'),
    ('PREESC', 'Preescolar'),
    ('PRIM', 'Primaria'),
    ('SEC', 'Secundaria'),
    ('MDSUP', 'Media superior'),
    ('SUP', 'Superior'),
)

# Opciones para el tipo de público
TYPE_OF_PUBLIC_CHOICES = (
    ('INT', 'Interno'),  # Interno: estudiantes y personal de la institución
    ('EXT', 'Externo'),  # Externo: estudiantes de otras instituciones o público en general
)

# Opciones para el estado de la evidencia
EVIDENCE_STATUS = (
    ('SEND', 'Subido'),
    ('DUE', 'Pendiente'),
    ('INC', 'Incompleto'),
    ('REJECT', 'Rechazado'),
    ('OK', 'Aprobado'),
)

# Opciones para el estado de la actividad
ACTIVITY_STATUS = (
    ('DUE', 'Pendiente'),
    ('INC', 'Incompleto'),
    ('REJECT', 'Rechazado'),
    ('OK', 'Aprobado'),
)
