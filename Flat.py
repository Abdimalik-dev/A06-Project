import os

files = {
    "watch-sales-app/index.html": """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Chronos Watches</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/main.jsx"></script>
  </body>
</html>""",

    "watch-sales-app/package.json": """{
  "name": "watch-sales-app",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "firebase": "^10.8.0",
    "lucide-react": "^0.344.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@types/react": "^18.3.3",
    "@types/react-dom": "^18.3.0",
    "@vitejs/plugin-react": "^4.3.1",
    "autoprefixer": "^10.4.19",
    "postcss": "^8.4.38",
    "tailwindcss": "^3.4.3",
    "vite": "^5.3.1"
  }
}""",

    "watch-sales-app/vite.config.js": """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})""",

    "watch-sales-app/tailwind.config.js": """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./*.{js,jsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}""",

    "watch-sales-app/index.css": """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer utilities {
  .scrollbar-hide::-webkit-scrollbar {
    display: none;
  }
  .scrollbar-hide {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
}""",

    "watch-sales-app/main.jsx": """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)""",

    "watch-sales-app/config.js": """import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

const defaultFirebaseConfig = {
  apiKey: "AIzaSyDummyKeyForLocalDev-ReplaceWithRealKey",
  authDomain: "your-app.firebaseapp.com",
  projectId: "your-app-id",
  storageBucket: "your-app.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abcdef"
};

const firebaseConfig = typeof __firebase_config !== 'undefined' 
  ? JSON.parse(__firebase_config) 
  : defaultFirebaseConfig;

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
export const appId = typeof __app_id !== 'undefined' ? __app_id : 'default-watch-store';""",

    "watch-sales-app/watches.js": """export const WATCH_DATA = [
  {
    id: 1,
    name: "Chronograph Master",
    brand: "LuxeTime",
    price: 1250,
    category: "Luxury",
    rating: 4.8,
    reviews: 124,
    image: "https://images.unsplash.com/photo-1524592094714-0f0654e20314?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    description: "A timeless masterpiece featuring a precise chronograph movement, sapphire crystal, and a genuine leather strap."
  },
  {
    id: 2,
    name: "Silver Prestige",
    brand: "Horology",
    price: 890,
    category: "Classic",
    rating: 4.6,
    reviews: 89,
    image: "https://images.unsplash.com/photo-1622434641406-a158123450f9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    description: "Elegant stainless steel design perfect for formal occasions. Water-resistant up to 50 meters."
  },
  {
    id: 3,
    name: "Noir Minimalist",
    brand: "Vanguard",
    price: 340,
    category: "Minimalist",
    rating: 4.9,
    reviews: 210,
    image: "https://images.unsplash.com/photo-1523170335258-f5ed11844a49?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    description: "Sleek matte black finish with a minimalist dial. For those who appreciate subtle sophistication."
  },
  {
    id: 4,
    name: "Aero Sport Edition",
    brand: "Velocity",
    price: 450,
    category: "Sports",
    rating: 4.5,
    reviews: 156,
    image: "https://images.unsplash.com/photo-1587836374828-cb4387860987?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    description: "Rugged and durable. Built for extreme conditions with a carbon fiber casing and luminous hands."
  },
  {
    id: 5,
    name: "Nexus Smartwatch",
    brand: "TechSync",
    price: 299,
    category: "Smart",
    rating: 4.7,
    reviews: 432,
    image: "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    description: "Stay connected with health tracking, notifications, and an always-on OLED display."
  },
  {
    id: 6,
    name: "Rose Gold Elegance",
    brand: "Horology",
    price: 1100,
    category: "Luxury",
    rating: 4.9,
    reviews: 76,
    image: "https://images.unsplash.com/photo-1542496658-e33a6d0d50f6?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    description: "Premium rose gold plating with a striking blue dial. A true statement piece."
  },
  {
    id: 7,
    name: "Deep Sea Diver",
    brand: "Oceanic",
    price: 780,
    category: "Sports",
    rating: 4.4,
    reviews: 92,
    image: "https://images.unsplash.com/photo-1546868871-7041f2a55e12?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    description: "Professional diving watch with 300m water resistance and a unidirectional rotating bezel."
  },
  {
    id: 8,
    name: "Vintage Aviator",
    brand: "LuxeTime",
    price: 950,
    category: "Classic",
    rating: 4.8,
    reviews: 118,
    image: "https://images.unsplash.com/photo-1614164185128-e4ec99c436d7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    description: "Inspired by classic aviation design. Features a large, easy-to-read dial and distressed leather strap."
  }
];

export const CATEGORIES = ["All", "Luxury", "Classic", "Minimalist", "Sports", "Smart"];""",

    "watch-sales-app/Navbar.jsx": """import React from 'react';
import { Search, Menu, ShoppingBag, Watch, History } from 'lucide-react';

export default function Navbar({ 
  setIsMobileMenuOpen, 
  setActiveCategory, 
  setSearchQuery, 
  searchQuery, 
  setIsOrdersModalOpen, 
  setIsCartOpen, 
  cartCount 
}) {
  return (
    <nav className="sticky top-0 z-40 w-full bg-white/85 backdrop-blur-md border-b border-zinc-200 shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center sm:hidden">
            <button 
              onClick={() => setIsMobileMenuOpen(true)}
              className="p-2 rounded-md text-zinc-600 hover:text-zinc-900 hover:bg-zinc-100"
            >
              <Menu size={24} />
            </button>
          </div>

          <div 
            className="flex-shrink-0 flex items-center cursor-pointer" 
            onClick={() => { setActiveCategory("All"); setSearchQuery(""); window.scrollTo(0,0); }}
          >
            <Watch className="h-8 w-8 text-zinc-900" />
            <span className="ml-2 text-xl font-bold tracking-tighter text-zinc-900 uppercase">Chronos</span>
          </div>

          <div className="hidden sm:flex flex-1 items-center justify-center px-8">
            <div className="relative w-full max-w-md">
              <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <Search size={18} className="text-zinc-400" />
              </div>
              <input
                type="text"
                placeholder="Search watches, brands..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="block w-full pl-10 pr-3 py-2 border border-zinc-200 rounded-full leading-5 bg-zinc-50 placeholder-zinc-400 focus:outline-none focus:bg-white focus:ring-2 focus:ring-zinc-900 focus:border-zinc-900 transition-colors sm:text-sm"
              />
            </div>
          </div>

          <div className="flex items-center space-x-2">
            <button 
              onClick={() => setIsOrdersModalOpen(true)}
              className="p-2 text-zinc-600 hover:text-zinc-900 transition-colors hidden sm:flex items-center gap-2 rounded-full hover:bg-zinc-100"
              title="Order History"
            >
              <History size={20} />
              <span className="text-sm font-medium">Orders</span>
            </button>
            <button 
              onClick={() => setIsCartOpen(true)}
              className="relative p-2 text-zinc-600 hover:text-zinc-900 hover:bg-zinc-100 rounded-full transition-colors"
            >
              <ShoppingBag size={24} />
              {cartCount > 0 && (
                <span className="absolute top-0 right-0 inline-flex items-center justify-center px-1.5 py-0.5 text-xs font-bold leading-none text-white transform translate-x-1/4 -translate-y-1/4 bg-zinc-900 rounded-full">
                  {cartCount}
                </span>
              )}
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
}""",

    "watch-sales-app/Hero.jsx": """import React from 'react';

export default function Hero({ setActiveCategory }) {
  return (
    <div className="relative bg-zinc-900 overflow-hidden">
      <div className="absolute inset-0">
        <img
          src="https://images.unsplash.com/photo-1470290449668-02ea0461bcf7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80"
          alt="Luxury Watch Background"
          className="w-full h-full object-cover opacity-40"
        />
        <div className="absolute inset-0 bg-gradient-to-r from-zinc-900 via-zinc-900/70 to-transparent"></div>
      </div>
      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 lg:py-32">
        <div className="max-w-2xl">
          <h1 className="text-4xl font-extrabold tracking-tight text-white sm:text-5xl lg:text-6xl uppercase">
            Define Your Time
          </h1>
          <p className="mt-6 text-xl text-zinc-300 max-w-3xl">
            Discover our curated collection of premium timepieces. From classic mechanical marvels to modern smartwatches, find the perfect companion for your wrist.
          </p>
          <div className="mt-10 flex gap-4">
            <button 
              onClick={() => document.getElementById('products-section').scrollIntoView({ behavior: 'smooth' })}
              className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-zinc-900 bg-white hover:bg-zinc-100 transition-colors"
            >
              Shop Collection
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}""",

    "watch-sales-app/ProductCard.jsx": """import React from 'react';
import { Star, ShoppingBag } from 'lucide-react';

export default function ProductCard({ product, setSelectedProduct, addToCart }) {
  return (
    <div className="group bg-white rounded-2xl border border-zinc-100 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col h-full">
      <div 
        className="relative aspect-[4/5] bg-zinc-100 overflow-hidden cursor-pointer"
        onClick={() => setSelectedProduct(product)}
      >
        <img 
          src={product.image} 
          alt={product.name} 
          className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-500 ease-in-out" 
          loading="lazy" 
        />
        <div className="absolute top-3 left-3 bg-white/95 backdrop-blur-sm px-2 py-1 rounded text-xs font-semibold uppercase tracking-wider text-zinc-800">
          {product.category}
        </div>
      </div>

      <div className="p-5 flex flex-col flex-grow">
        <div className="flex justify-between items-start mb-2">
          <div>
            <p className="text-sm text-zinc-500 font-medium">{product.brand}</p>
            <h3 
              className="text-lg font-bold text-zinc-900 mt-1 cursor-pointer hover:text-zinc-600 transition-colors line-clamp-1"
              onClick={() => setSelectedProduct(product)}
            >
              {product.name}
            </h3>
          </div>
          <div className="flex items-center gap-1 bg-zinc-50 px-2 py-1 rounded">
            <Star size={14} className="text-amber-500 fill-amber-500" />
            <span className="text-sm font-semibold text-zinc-700">{product.rating}</span>
          </div>
        </div>
        
        <p className="text-zinc-600 text-sm mb-4 line-clamp-2 flex-grow">{product.description}</p>

        <div className="flex items-center justify-between mt-auto pt-4 border-t border-zinc-100">
          <span className="text-xl font-bold text-zinc-900">${product.price.toLocaleString()}</span>
          <button 
            onClick={() => addToCart(product)} 
            className="bg-zinc-900 text-white px-4 py-2 rounded-xl text-sm font-semibold hover:bg-zinc-800 transition-colors flex items-center gap-1.5"
          >
            <ShoppingBag size={16} /> Add
          </button>
        </div>
      </div>
    </div>
  );
}""",

    "watch-sales-app/CartDrawer.jsx": """import React from 'react';
import { ShoppingBag, X, Plus, Minus, Trash2, CreditCard } from 'lucide-react';

export default function CartDrawer({ 
  isCartOpen, 
  setIsCartOpen, 
  cart, 
  cartCount, 
  updateQuantity, 
  removeFromCart, 
  cartTotal, 
  setIsCheckoutOpen 
}) {
  return (
    <>
      <div 
        className={`fixed inset-0 bg-black/50 backdrop-blur-sm transition-opacity z-50 ${isCartOpen ? 'opacity-100' : 'opacity-0 pointer-events-none'}`}
        onClick={() => setIsCartOpen(false)}
      />
      <div className={`fixed inset-y-0 right-0 w-full sm:w-[450px] bg-white shadow-2xl z-50 transform transition-transform duration-300 ease-in-out flex flex-col ${isCartOpen ? 'translate-x-0' : 'translate-x-full'}`}>
        <div className="px-6 py-4 border-b border-zinc-100 flex items-center justify-between bg-zinc-50">
          <h2 className="text-lg font-bold text-zinc-900 flex items-center gap-2">
            <ShoppingBag size={20} />
            Your Cart ({cartCount})
          </h2>
          <button onClick={() => setIsCartOpen(false)} className="p-2 text-zinc-400 hover:text-zinc-900 hover:bg-zinc-200 rounded-full transition-colors">
            <X size={20} />
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-6">
          {cart.length === 0 ? (
            <div className="h-full flex flex-col items-center justify-center text-zinc-500 space-y-4">
              <ShoppingBag size={48} className="text-zinc-300" />
              <p>Your cart is empty</p>
            </div>
          ) : (
            <ul className="space-y-6">
              {cart.map((item) => (
                <li key={item.id} className="flex gap-4">
                  <div className="w-20 h-20 bg-zinc-100 rounded-lg overflow-hidden flex-shrink-0 border border-zinc-200">
                    <img src={item.image} alt={item.name} className="w-full h-full object-cover" />
                  </div>
                  <div className="flex-1 flex flex-col justify-between">
                    <div>
                      <div className="flex justify-between">
                        <h3 className="font-bold text-zinc-900 line-clamp-1">{item.name}</h3>
                        <p className="font-bold text-zinc-900 ml-4">${(item.price * item.quantity).toLocaleString()}</p>
                      </div>
                      <p className="text-sm text-zinc-500">{item.brand}</p>
                    </div>
                    <div className="flex items-center justify-between mt-2">
                      <div className="flex items-center border border-zinc-200 rounded-md">
                        <button onClick={() => updateQuantity(item.id, -1)} className="p-1 text-zinc-500 hover:text-zinc-900">
                          <Minus size={14} />
                        </button>
                        <span className="w-8 text-center text-sm font-medium text-zinc-900">{item.quantity}</span>
                        <button onClick={() => updateQuantity(item.id, 1)} className="p-1 text-zinc-500 hover:text-zinc-900">
                          <Plus size={14} />
                        </button>
                      </div>
                      <button onClick={() => removeFromCart(item.id)} className="text-red-500 hover:text-red-700 p-1">
                        <Trash2 size={16} />
                      </button>
                    </div>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>

        {cart.length > 0 && (
          <div className="p-6 bg-zinc-50 border-t border-zinc-200">
            <div className="flex justify-between text-base font-medium text-zinc-900 mb-4">
              <p>Subtotal</p>
              <p>${cartTotal.toLocaleString()}</p>
            </div>
            <button 
              className="w-full bg-zinc-900 text-white px-6 py-4 rounded-xl font-bold text-lg hover:bg-zinc-800 transition-colors flex justify-center items-center gap-2"
              onClick={() => { setIsCartOpen(false); setIsCheckoutOpen(true); }}
            >
              <CreditCard size={20} /> Proceed to Checkout
            </button>
          </div>
        )}
      </div>
    </>
  );
}""",

    "watch-sales-app/CheckoutModal.jsx": """import React from 'react';
import { CreditCard, Loader2 } from 'lucide-react';

export default function CheckoutModal({ 
  isCheckoutOpen, 
  setIsCheckoutOpen, 
  isProcessingPayment, 
  handleCheckoutSubmit, 
  cartTotal 
}) {
  if (!isCheckoutOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div className="absolute inset-0 bg-black/60 backdrop-blur-sm" onClick={() => !isProcessingPayment && setIsCheckoutOpen(false)} />
      <div className="relative bg-white rounded-2xl w-full max-w-xl p-6 shadow-2xl">
        <h2 className="text-2xl font-bold text-zinc-900 mb-6 flex items-center gap-2">
          <CreditCard size={24} /> Secure Checkout
        </h2>
        <form onSubmit={handleCheckoutSubmit} className="space-y-4">
          <input type="text" required placeholder="Full Name" className="w-full px-4 py-2 rounded-lg border border-zinc-300 outline-none" />
          <input type="email" required placeholder="Email Address" className="w-full px-4 py-2 rounded-lg border border-zinc-300 outline-none" />
          <input type="text" required placeholder="Card Number" className="w-full px-4 py-2 rounded-lg border border-zinc-300 outline-none" />
          <div className="pt-4 flex items-center justify-between">
            <span className="text-xl font-bold text-zinc-900">Total: ${cartTotal.toLocaleString()}</span>
            <button 
              type="submit" 
              disabled={isProcessingPayment}
              className="bg-zinc-900 text-white px-6 py-3 rounded-xl font-bold hover:bg-zinc-800 flex items-center gap-2"
            >
              {isProcessingPayment ? <Loader2 className="animate-spin" size={20} /> : "Pay Now"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}""",

    "watch-sales-app/OrderSuccessModal.jsx": """import React from 'react';
import { CheckCircle } from 'lucide-react';

export default function OrderSuccessModal({ orderSuccess, setOrderSuccess }) {
  if (!orderSuccess) return null;
  return (
    <div className="fixed inset-0 z-[60] flex items-center justify-center p-4 bg-black/60">
      <div className="bg-white rounded-2xl w-full max-w-sm p-8 text-center shadow-2xl">
        <CheckCircle size={48} className="mx-auto text-green-600 mb-4" />
        <h2 className="text-2xl font-bold text-zinc-900 mb-2">Order Confirmed!</h2>
        <button onClick={() => setOrderSuccess(false)} className="mt-4 w-full bg-zinc-900 text-white py-3 rounded-xl font-bold">Continue</button>
      </div>
    </div>
  );
}""",

    "watch-sales-app/OrderHistoryModal.jsx": """import React from 'react';
import { History, X } from 'lucide-react';

export default function OrderHistoryModal({ isOrdersModalOpen, setIsOrdersModalOpen, pastOrders }) {
  if (!isOrdersModalOpen) return null;
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div className="absolute inset-0 bg-black/60" onClick={() => setIsOrdersModalOpen(false)} />
      <div className="relative bg-white rounded-2xl w-full max-w-2xl max-h-[80vh] overflow-y-auto p-6 shadow-2xl">
        <div className="flex justify-between items-center mb-4"><h2 className="text-xl font-bold">Order History</h2><button onClick={() => setIsOrdersModalOpen(false)}><X size={20}/></button></div>
        {pastOrders.length === 0 ? <p className="text-zinc-500">No past orders.</p> : pastOrders.map(o => <div key={o.id} className="border p-4 rounded-xl mb-3"><p>Total: ${o.total}</p></div>)}
      </div>
    </div>
  );
}""",

    "watch-sales-app/ProductModal.jsx": """import React from 'react';
import { X } from 'lucide-react';

export default function ProductModal({ selectedProduct, setSelectedProduct, addToCart }) {
  if (!selectedProduct) return null;
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div className="absolute inset-0 bg-black/60" onClick={() => setSelectedProduct(null)} />
      <div className="relative bg-white rounded-2xl w-full max-w-2xl p-6 shadow-2xl flex flex-col md:flex-row gap-6">
        <img src={selectedProduct.image} alt={selectedProduct.name} className="w-full md:w-1/2 object-cover rounded-xl" />
        <div className="flex flex-col justify-between">
          <div>
            <h2 className="text-2xl font-bold mb-2">{selectedProduct.name}</h2>
            <p className="text-xl font-bold text-zinc-900 mb-4">${selectedProduct.price}</p>
            <p className="text-zinc-600 mb-6">{selectedProduct.description}</p>
          </div>
          <button onClick={() => { addToCart(selectedProduct); setSelectedProduct(null); }} className="w-full bg-zinc-900 text-white py-3 rounded-xl font-bold">Add to Cart</button>
        </div>
      </div>
    </div>
  );
}""",

    "watch-sales-app/MobileMenu.jsx": """import React from 'react';
import { X } from 'lucide-react';
import { CATEGORIES } from './watches';

export default function MobileMenu({ isMobileMenuOpen, setIsMobileMenuOpen, setActiveCategory, activeCategory }) {
  if (!isMobileMenuOpen) return null;
  return (
    <div className="fixed inset-0 z-50 flex">
      <div className="absolute inset-0 bg-black/50" onClick={() => setIsMobileMenuOpen(false)} />
      <div className="relative w-64 bg-white h-full p-6 shadow-xl z-10 flex flex-col gap-4">
        <button onClick={() => setIsMobileMenuOpen(false)} className="self-end"><X size={20}/></button>
        {CATEGORIES.map(c => <button key={c} onClick={() => { setActiveCategory(c); setIsMobileMenuOpen(false); }} className="text-left py-2 font-medium">{c}</button>)}
      </div>
    </div>
  );
}""",

    "watch-sales-app/App.jsx": """import React, { useState, useMemo, useEffect } from 'react';
import { onAuthStateChanged, signInAnonymously } from 'firebase/auth';
import { collection, onSnapshot, addDoc } from 'firebase/firestore';
import { auth, db, appId } from './config';
import { WATCH_DATA, CATEGORIES } from './watches';
import Navbar from './Navbar';
import Hero from './Hero';
import ProductCard from './ProductCard';
import CartDrawer from './CartDrawer';
import CheckoutModal from './CheckoutModal';
import OrderSuccessModal from './OrderSuccessModal';
import OrderHistoryModal from './OrderHistoryModal';
import ProductModal from './ProductModal';
import MobileMenu from './MobileMenu';

export default function App() {
  const [cart, setCart] = useState([]);
  const [isCartOpen, setIsCartOpen] = useState(false);
  const [activeCategory, setActiveCategory] = useState("All");
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [user, setUser] = useState(null);
  const [pastOrders, setPastOrders] = useState([]);
  const [isCheckoutOpen, setIsCheckoutOpen] = useState(false);
  const [isProcessingPayment, setIsProcessingPayment] = useState(false);
  const [orderSuccess, setOrderSuccess] = useState(false);
  const [isOrdersModalOpen, setIsOrdersModalOpen] = useState(false);

  useEffect(() => {
    signInAnonymously(auth).catch(console.error);
    return onAuthStateChanged(auth, setUser);
  }, []);

  useEffect(() => {
    if (!user) return;
    return onSnapshot(collection(db, 'artifacts', appId, 'users', user.uid, 'orders'), (snapshot) => {
      setPastOrders(snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() })));
    });
  }, [user]);

  const filteredProducts = useMemo(() => {
    return WATCH_DATA.filter(watch => {
      const matchesCategory = activeCategory === "All" || watch.category === activeCategory;
      const matchesSearch = watch.name.toLowerCase().includes(searchQuery.toLowerCase()) || watch.brand.toLowerCase().includes(searchQuery.toLowerCase());
      return matchesCategory && matchesSearch;
    });
  }, [activeCategory, searchQuery]);

  const addToCart = (product) => {
    setCart(prev => {
      const exists = prev.find(item => item.id === product.id);
      if (exists) return prev.map(item => item.id === product.id ? { ...item, quantity: item.quantity + 1 } : item);
      return [...prev, { ...product, quantity: 1 }];
    });
    setIsCartOpen(true);
  };

  const updateQuantity = (id, delta) => {
    setCart(prev => prev.map(item => item.id === id ? { ...item, quantity: item.quantity + delta } : item).filter(item => item.quantity > 0));
  };

  const removeFromCart = (id) => setCart(prev => prev.filter(item => item.id !== id));
  const cartTotal = cart.reduce((total, item) => total + (item.price * item.quantity), 0);
  const cartCount = cart.reduce((count, item) => count + item.quantity, 0);

  const handleCheckoutSubmit = async (e) => {
    e.preventDefault();
    setIsProcessingPayment(true);
    setTimeout(async () => {
      if (user) {
        await addDoc(collection(db, 'artifacts', appId, 'users', user.uid, 'orders'), {
          items: cart, total: cartTotal, status: 'Completed', createdAt: Date.now()
        });
        setCart([]);
        setIsCheckoutOpen(false);
        setOrderSuccess(true);
      }
      setIsProcessingPayment(false);
    }, 1500);
  };

  return (
    <div className="min-h-screen bg-white font-sans text-zinc-900">
      <Navbar {...{ setIsMobileMenuOpen, setActiveCategory, setSearchQuery, searchQuery, setIsOrdersModalOpen, setIsCartOpen, cartCount }} />
      <Hero setActiveCategory={setActiveCategory} />
      <main className="max-w-7xl mx-auto px-4 py-12" id="products-section">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {filteredProducts.map(product => <ProductCard key={product.id} product={product} setSelectedProduct={setSelectedProduct} addToCart={addToCart} />)}
        </div>
      </main>
      <CartDrawer {...{ isCartOpen, setIsCartOpen, cart, cartCount, updateQuantity, removeFromCart, cartTotal, setIsCheckoutOpen }} />
      <CheckoutModal {...{ isCheckoutOpen, setIsCheckoutOpen, isProcessingPayment, handleCheckoutSubmit, cartTotal }} />
      <OrderSuccessModal {...{ orderSuccess, setOrderSuccess }} />
      <OrderHistoryModal {...{ isOrdersModalOpen, setIsOrdersModalOpen, pastOrders }} />
      <MobileMenu {...{ isMobileMenuOpen, setIsMobileMenuOpen, setActiveCategory, activeCategory }} />
      <ProductModal {...{ selectedProduct, setSelectedProduct, addToCart }} />
    </div>
  );
}"""
}

for path, content in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Successfully generated all files in a single flat 'watch-sales-app' folder!")
