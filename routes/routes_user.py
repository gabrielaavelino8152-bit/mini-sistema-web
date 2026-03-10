from flask import Blueprint, render_template, redirect, url_for, flash, session
from models.user import db, User
from forms import RegisterForm, LoginForm

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def index():
    users = User.query.all()
    return render_template('user_list.html', users=users)

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Usuario registrado con éxito', 'success')
        return redirect(url_for('user.index'))
    return render_template('register.html', form=form)

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            session['user_id'] = user.id
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('user.profile', id=user.id))
        else:
            flash('Credenciales inválidas', 'danger')
    return render_template('login.html', form=form)

@user_bp.route('/profile/<int:id>')
def profile(id):
    user = User.query.get_or_404(id)
    return render_template('profile.html', user=user)
