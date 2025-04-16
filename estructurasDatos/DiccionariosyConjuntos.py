persona = {
    "nombre": "Anita",
    "edad" : 29,
    "ciudad" : "Lima"
}

print("======================== impresiones =========================")
print(persona["nombre"])

persona["profesion"] = "Ingeniera Industrial"

for clave,valor in persona.items():
    print(clave," : ",valor)