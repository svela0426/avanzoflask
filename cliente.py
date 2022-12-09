
class Cliente:
    def __init__(self, name, apellido,empresa,contrasena,deuda):
        self.name = name
        self.apellido = apellido
        self.contrasena = contrasena
        self.empresa = empresa
        self.deuda=deuda


    def toDBCollection(self):
        return{
            'name': self.name,
            'apellido': self.apellido,
            'contrasena': self.contrasena,
            'empresa': self.empresa,
            'deuda': self.deuda,

        }