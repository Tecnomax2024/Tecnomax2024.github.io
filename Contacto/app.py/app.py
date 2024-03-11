from flask import Flask, render_template, flash, redirect, url_for
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'Tecnomaxcmgmail.com'
app.config['MAIL_PASSWORD'] = 'Nallelyg1989'
app.config['MAIL_DEFAULT_SENDER'] = 'Tecnomaxcm@gmail.com'

mail = Mail(app)

class ContactForm(FlaskForm):
    nombre = StringField('Nombre')
    correo = StringField('Correo Electrónico')
    mensaje = TextAreaField('Mensaje')
    enviar = SubmitField('Enviar')

@app.route('/', methods=['GET', 'POST'])
def contacto():
    form = ContactForm()

    if form.validate_on_submit():
        enviar_correo(form.nombre.data, form.correo.data, form.mensaje.data)
        flash('Mensaje enviado con éxito', 'success')
        return redirect(url_for('Contacto'))

    return render_template("Contacto.html", form=form)

def enviar_correo(nombre, correo, mensaje):
    subject = 'Nuevo mensaje de contacto'
    body = f'Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}'

    message = Message(subject, recipients=['Tecnomaxmc@gmail.com'])
    message.body = body

    try:
        mail.send(message)
    except Exception as e:
        print(f'Error al enviar el correo: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)