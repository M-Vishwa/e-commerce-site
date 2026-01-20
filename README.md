# E-Commerce Site 🛒

A modern, fully responsive e-commerce platform designed to provide a seamless shopping experience. This project features a robust product management system, user authentication, and a sleek user interface.

## 🚀 Features

- **User Authentication:** Secure login and registration (JWT/Firebase).
- **Product Browsing:** Filter products by category, price, and ratings.
- **Shopping Cart:** Add, remove, and update item quantities in real-time.
- **User Profile:** Manage personal info and track order history.
- **Admin Dashboard:** (Optional) Add, edit, or delete products and manage orders.
- **Responsive Design:** Optimized for mobile, tablet, and desktop views.

## 🛠️ Tech Stack

**Frontend:**
- React.js / Vite
- Redux (State Management)
- Tailwind CSS / Bootstrap (Styling)

**Backend:**
- Node.js & Express.js
- MongoDB (Database)
- JWT (Authentication)

**Deployment:**
- Frontend: Vercel / Netlify
- Backend: Render / Heroku

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/M-Vishwa/e-commerce-site.git](https://github.com/M-Vishwa/e-commerce-site.git)
   cd e-commerce-site
   
      cd backend
   npm install
   
   cd ../frontend
   npm install
   
   MONGO_URI=your_mongodb_connection_string
   JWT_SECRET=your_secret_key
   PORT=5000
   
   # From root or backend folder
      npm run dev
