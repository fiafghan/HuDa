import React from 'react'
import Header from '../components/Header'
import Sidebar from '../components/Sidebar'
import Footer from '../components/Footer'

export default function DocsLayout({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="mdp min-h-screen">
      <Header />
      <Sidebar />
      <div className="md:pl-72">
        <main className="max-w-7xl mx-auto px-4 md:px-6 py-8">
          <h1 className="text-3xl font-bold tracking-tight mb-4">{title}</h1>
          {children}
        </main>
        <Footer />
      </div>
    </div>
  )
}
