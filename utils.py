#Funcion para subir archivo de evidencia validando la extension que sea pdf, txt o imagen
def upload_evidence_file(instance, filename):
    x = filename.split('.')
    if(x.pop() not in ('pdf','jpg','txt','jpeg','png')):
        raise ValidationError('Extension de archivo invalida.')
    return f'evidence/document/{instance.activity.presenter.id}/{instance.activity.id}/{filename}'

#Funcion para subir archivo de constancia validando la extension que sea pdf
def upload_certificate_file(instance, filename):
    x = filename.split('.')
    if(x.pop() not in ('pdf')):
        raise ValidationError('Extension de archivo invalida.')
    return f'activity/document/certificate/{instance.presenter.id}/{instance.id}/{filename}'