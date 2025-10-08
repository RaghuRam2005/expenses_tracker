import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from collections import defaultdict

# Get the base directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

# --- App & Database Configuration ---
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_super_secret_key_change_me'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'expenses.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Database Model Definition ---
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.Date, nullable=False)
    notes = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"Expense(id={self.id}, amount={self.amount}, category='{self.category}')"

# --- Flask Routes ---
@app.route('/')
def index():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    """Handles adding a new expense."""
    if request.method == 'POST':
        amount = request.form.get('amount')
        category = request.form.get('category')
        date_str = request.form.get('date')
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        notes = request.form.get('notes')

        new_expense = Expense(
            amount=float(amount),
            category=category,
            date_posted=date_obj,
            notes=notes
        )

        db.session.add(new_expense)
        db.session.commit()
        # This redirect correctly passes the ID to the success route
        return redirect(url_for('success', expense_id=new_expense.id))

    return render_template('add_expense.html')

@app.route('/expenses')
def view_expenses():
    """Displays all expenses and calculates totals."""
    filter_category = request.args.get('category')

    if filter_category:
        expenses = Expense.query.filter_by(category=filter_category).order_by(Expense.date_posted.desc()).all()
    else:
        expenses = Expense.query.order_by(Expense.date_posted.desc()).all()

    total_expenses = sum(expense.amount for expense in expenses)

    categories = db.session.query(Expense.category).distinct().all()
    categories = [cat[0] for cat in categories]

    return render_template(
        'expenses.html',
        expenses=expenses,
        total=total_expenses,
        categories=categories,
        current_filter=filter_category
    )

@app.route('/success/<int:expense_id>')
def success(expense_id):
    """Renders a confirmation receipt for a specific expense."""
    # This line fetches the expense from the DB using the ID
    expense = Expense.query.get_or_404(expense_id)
    # This correctly passes the 'expense' object to the template
    return render_template('success.html', expense=expense)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

