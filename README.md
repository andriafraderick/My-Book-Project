📚 BookApp – Django Book Store Application

BookApp is a full-featured Django web application that allows administrators to manage books and authors, while users can browse books, add them to a cart, and proceed to checkout.

This project demonstrates CRUD operations, Django models, templates, user authentication, cart management, and Stripe checkout integration.

🚀 Features
👤 Admin Features

Add new books with:

Title
Author
Price
Quantity
Image
Description / Additional details
Update existing books
Delete books
Manage authors
Manage stock quantity

🛍️ User Features

View a list of available books

View:

Book Title
Author
Price
Quantity
Image

Add items to cart
Increase/decrease item quantity
Remove items from cart

🗂️ Project Structure

book_project/
│
├── book_app/
│   ├── models.py      # Book & Author models
│   ├── views.py       # Book list, details, and admin CRUD
│   ├── templates/
│       └── book/...
│
├── user_app/
│   ├── models.py      # Cart & CartItem models
│   ├── views.py       # Cart, checkout and user pages
│   ├── templates/
│       └── user/...
│
└── book_project/
    ├── settings.py    # Database & Stripe configuration
    ├── urls.py

🛢️ Tech Stack

Python 3
Django 5
SQLite / PostgreSQL
HTML, CSS, Bootstrap
Stripe Payment Gateway
🛒 Cart & Checkout Flow
User clicks Add to Cart

Cart stores:

Book reference
Quantity
Price

Cart page shows:

Book details
Total items
Total prUser login/registration
Search & filter booksice
Stripe checkout session created
On success → Redirect to success page
On failure → Redirect to cancel page

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/BookApp.git
cd BookApp

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run migrations
python manage.py migrate

4️⃣ Create superuser
python manage.py createsuperuser

5️⃣ Run the server
python manage.py runserver

🔑 Environment Variables

Create a .env file (DO NOT upload to GitHub):

STRIPE_SECRET_KEY=your_secret_key_here
STRIPE_PUBLISHABLE_KEY=your_public_key_here


📝 Future Improvements

Order history

Wishlist

Reviews & ratings

🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss your idea.

View total items and total price

Checkout using Stripe payment
