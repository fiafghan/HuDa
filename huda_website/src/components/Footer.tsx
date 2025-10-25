import React from 'react'
import { Info, Mail } from 'lucide-react'
import { Link } from 'react-router-dom'

export default function Footer() {
  const year = new Date().getFullYear()
  return (
    <footer className="border-t border-white/60 bg-white/70 backdrop-blur supports-[backdrop-filter]:bg-white/60">
      <div className="max-w-7xl mx-auto px-4 md:px-6 py-6 flex flex-col md:flex-row items-center justify-between gap-4">
        <div className="text-sm text-gray-600">© <span>{year}</span> HuDa. Built for humanitarian analysts.</div>
        <div className="flex items-center gap-4 text-gray-600">
          <Link to="/about" className="inline-flex items-center gap-1 hover:text-gray-900"><Info className="w-4 h-4" />About</Link>
          <Link to="/contact" className="inline-flex items-center gap-1 hover:text-gray-900"><Mail className="w-4 h-4" />Contact</Link>
        </div>
      </div>
    </footer>
  )
}
