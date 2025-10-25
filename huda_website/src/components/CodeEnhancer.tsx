import React, { useEffect } from 'react'

export default function CodeEnhancer() {
  useEffect(() => {
    try {
      const w = window as any
      if (w.hljs && typeof w.hljs.highlightAll === 'function') {
        w.hljs.highlightAll()
      }
    } catch {}

    const pres = Array.from(document.querySelectorAll('pre')) as HTMLElement[]
    pres.forEach((pre) => {
      if (pre.getAttribute('data-copy-attached') === '1') return
      pre.classList.add('relative')
      const codeEl = pre.querySelector('code') as HTMLElement | null
      if (!codeEl) return

      const btn = document.createElement('button')
      btn.type = 'button'
      btn.textContent = 'Copy'
      btn.className = 'copy-btn absolute top-2 right-2 text-xs px-2 py-1 rounded bg-gray-700 text-white hover:bg-gray-800 active:bg-gray-900'
      btn.addEventListener('click', () => {
        const text = codeEl.innerText
        navigator.clipboard.writeText(text).then(() => {
          const old = btn.textContent
          btn.textContent = 'Copied!'
          setTimeout(() => (btn.textContent = old || 'Copy'), 1200)
        })
      })
      pre.appendChild(btn)
      pre.setAttribute('data-copy-attached', '1')
    })
  })
  return null
}
