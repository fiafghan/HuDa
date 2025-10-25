import React from 'react'
import { Home, Download, Info, Mail, Database } from 'lucide-react'
import { Link, useLocation } from 'react-router-dom'

export default function Header() {
  const { pathname } = useLocation()
  const isActive = (to: string) => pathname === to

  return (
    <div className="w-full bg-gradient-to-r from-indigo-600 via-sky-600 to-emerald-600 text-white">
      <div className="max-w-7xl mx-auto px-4 md:px-6">
        <div className="flex items-center justify-between py-3">
          <div className="flex items-center gap-2">
            <Database className="w-5 h-5" />
            <span className="font-semibold tracking-tight">HuDa — Humanitarian Data Library</span>
          </div>
          <nav className="hidden md:flex items-center gap-4 text-sm opacity-90">
            <a href="/#overview" className={`inline-flex items-center gap-1 hover:opacity-100 ${isActive('/') ? 'opacity-100' : ''}`}>
              <Home className="w-4 h-4" />Overview
            </a>
            <a href="/#installation" className={`inline-flex items-center gap-1 hover:opacity-100 ${isActive('/') ? 'opacity-100' : ''}`}>
              <Download className="w-4 h-4" />Install
            </a>
            <Link to="/about" className={`inline-flex items-center gap-1 hover:opacity-100 ${isActive('/about') ? 'opacity-100' : ''}`}>
              <Info className="w-4 h-4" />About Us
            </Link>
            <Link to="/contact" className={`inline-flex items-center gap-1 hover:opacity-100 ${isActive('/contact') ? 'opacity-100' : ''}`}>
              <Mail className="w-4 h-4" />Contact Us
            </Link>
          </nav>
        </div>
      </div>
    </div>
  )
}
