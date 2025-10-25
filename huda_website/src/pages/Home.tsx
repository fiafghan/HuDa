import React from 'react'
import Header from '../components/Header'
import Sidebar from '../components/Sidebar'
import Footer from '../components/Footer'

export default function Home() {
  return (
    <div className="mdp min-h-screen">
      <Header />
      <div className="min-h-screen grid grid-cols-1 md:grid-cols-[280px_1fr]">
        <Sidebar />
        <main className="p-4 md:p-6">
          <section id="overview" className="mb-8">
            <h1 className="text-3xl font-bold tracking-tight mb-2">HuDa — Humanitarian Data Library</h1>
            <p className="text-gray-700">Training website and guides across the data lifecycle.</p>
          </section>
          <section id="installation" className="mb-8">
            <h2 className="text-xl font-semibold mb-2">Installation</h2>
            <p className="text-gray-700">Use the navigation to explore the docs. This React page is a first pass; detailed content from your original index can be ported section-by-section.</p>
          </section>
        </main>
      </div>
      <Footer />
    </div>
  )
}
