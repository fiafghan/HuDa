import React from 'react'
import Header from '../components/Header'
import Sidebar from '../components/Sidebar'
import Footer from '../components/Footer'

export default function Contact() {
  return (
    <div className="mdp min-h-screen">
      <Header />
      <Sidebar />
      <div className="md:pl-72">
        <main className="max-w-5xl mx-auto p-6 md:p-10">
          <header className="mb-8">
            <h1 className="text-3xl font-bold tracking-tight">Contact Us</h1>
            <p className="text-gray-600 mt-2">Questions, suggestions, or feedback? Send us a note — we’d love to hear from you.</p>
          </header>

          <div className="grid md:grid-cols-3 gap-6 mb-12">
            <div className="p-6 rounded-xl bg-white shadow-sm">
              <div className="flex items-center gap-2 mb-2 text-mdp"><span className="font-semibold">Email</span></div>
              <p className="text-gray-700 text-sm">support@huda.example</p>
            </div>
            <div className="p-6 rounded-xl bg-white shadow-sm">
              <div className="flex items-center gap-2 mb-2 text-mdp"><span className="font-semibold">GitHub</span></div>
              <p className="text-gray-700 text-sm"><a className="underline" href="#">github.com/huda</a></p>
            </div>
            <div className="p-6 rounded-xl bg-white shadow-sm">
              <div className="flex items-center gap-2 mb-2 text-mdp"><span className="font-semibold">Community</span></div>
              <p className="text-gray-700 text-sm"><a className="underline" href="#">Join our community chat</a></p>
            </div>
          </div>

          <section className="grid gap-6 md:grid-cols-2">
            <form className="p-6 rounded-xl bg-white shadow-sm space-y-4" onSubmit={(e)=>{e.preventDefault(); (e.currentTarget as HTMLFormElement).reset(); alert('Thanks! We received your message.')}}>
              <div>
                <label className="text-sm text-gray-700" htmlFor="name">Name</label>
                <input id="name" name="name" className="mt-1 w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400" placeholder="Your full name" />
              </div>
              <div>
                <label className="text-sm text-gray-700" htmlFor="email">Email</label>
                <input id="email" name="email" type="email" className="mt-1 w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400" placeholder="you@example.com" />
              </div>
              <div>
                <label className="text-sm text-gray-700" htmlFor="message">Message</label>
                <textarea id="message" name="message" rows={5} className="mt-1 w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400" placeholder="How can we help?"></textarea>
              </div>
              <button className="btn-mdp-primary inline-flex items-center gap-2">Send Message</button>
            </form>

            <div className="p-6 rounded-xl bg-white shadow-sm">
              <h2 className="text-xl font-semibold mb-2">Support Hours</h2>
              <p className="text-gray-700 text-sm">Monday–Friday, 9:00–17:00 (UTC)</p>
              <h2 className="text-xl font-semibold mt-6 mb-2">Response Time</h2>
              <p className="text-gray-700 text-sm">We aim to respond within 2 business days.</p>
            </div>
          </section>
        </main>
        <Footer />
      </div>
    </div>
  )
}
