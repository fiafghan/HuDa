import React from 'react'
import Header from '../components/Header'
import Sidebar from '../components/Sidebar'
import Footer from '../components/Footer'

export default function About() {
  return (
    <div className="mdp min-h-screen">
      <Header />
      <Sidebar />
      <div className="md:pl-72">
        <main className="max-w-5xl mx-auto p-6 md:p-10">
          <header className="mb-8">
            <h1 className="text-3xl font-bold tracking-tight">About HuDa</h1>
            <p className="text-gray-600 mt-2">Humanitarian Data Library — simple, practical guides for real-world data work.</p>
          </header>

          <section className="grid md:grid-cols-3 gap-6 mb-12">
            <div className="p-6 rounded-xl bg-white shadow-sm">
              <div className="flex items-center gap-2 mb-2 text-mdp"><i className="w-5 h-5" />
                <span className="font-semibold">Our Mission</span>
              </div>
              <p className="text-gray-700">Make data tasks easier for humanitarian teams with clear examples, plain language, and copyable code.</p>
            </div>
            <div className="p-6 rounded-xl bg-white shadow-sm">
              <div className="flex items-center gap-2 mb-2 text-mdp"><i className="w-5 h-5" />
                <span className="font-semibold">Who We Serve</span>
              </div>
              <p className="text-gray-700">Field analysts, IM officers, and decision-makers who need quick, reliable data guidance.</p>
            </div>
            <div className="p-6 rounded-xl bg-white shadow-sm">
              <div className="flex items-center gap-2 mb-2 text-mdp"><i className="w-5 h-5" />
                <span className="font-semibold">Our Values</span>
              </div>
              <p className="text-gray-700">Clarity. Practicality. Reliability. Built with care for high-stakes contexts.</p>
            </div>
          </section>

          <section className="mb-12">
            <h2 className="text-xl font-semibold mb-3">The Team</h2>
            <div className="grid md:grid-cols-2 gap-6">
              <div className="p-6 rounded-xl bg-white shadow-sm">
                <div className="flex items-center gap-3 mb-2">
                  <div className="w-10 h-10 rounded-full bg-mdp flex items-center justify-center text-white font-semibold">H</div>
                  <div>
                    <div className="font-medium">HuDa Maintainers</div>
                    <div className="text-sm text-gray-600">Data & Engineering</div>
                  </div>
                </div>
                <p className="text-gray-700 text-sm">We maintain the library, keep examples up-to-date, and respond to community feedback.</p>
              </div>
              <div className="p-6 rounded-xl bg-white shadow-sm">
                <div className="flex items-center gap-3 mb-2">
                  <div className="w-10 h-10 rounded-full bg-mdp flex items-center justify-center text-white font-semibold">C</div>
                  <div>
                    <div className="font-medium">Contributors</div>
                    <div className="text-sm text-gray-600">Community</div>
                  </div>
                </div>
                <p className="text-gray-700 text-sm">Field practitioners and analysts sharing real-world tips and examples.</p>
              </div>
            </div>
          </section>

          <section className="mb-16">
            <h2 className="text-xl font-semibold mb-3">Contact</h2>
            <p className="text-gray-700">Have feedback or ideas? Visit the <a className="underline" href="/contact">Contact</a> page. We read every message.</p>
          </section>
        </main>
        <Footer />
      </div>
    </div>
  )
}
