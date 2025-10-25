export type ActivePage = 'home' | 'about' | 'contact' | 'docs'

export function renderHeader(active: ActivePage = 'home') {
  const link = (href: string, icon: string, label: string, isActive = false) => `
    <a href="${href}" class="inline-flex items-center gap-1 ${isActive ? 'opacity-100' : 'opacity-90 hover:opacity-100'}"><i data-lucide="${icon}" class="w-4 h-4"></i>${label}</a>
  `

  return `
  <div class="w-full bg-gradient-to-r from-indigo-600 via-sky-600 to-emerald-600 text-white">
    <div class="max-w-7xl mx-auto px-4 md:px-6">
      <div class="flex items-center justify-between py-3">
        <div class="flex items-center gap-2">
          <i data-lucide="database" class="w-5 h-5"></i>
          <span class="font-semibold tracking-tight">HuDa — Humanitarian Data Library</span>
        </div>
        <div class="hidden md:flex items-center gap-4 text-sm">
          ${link('./index.html#overview','home','Overview', active==='home')}
          ${link('./index.html#installation','download','Install', active==='home')}
          ${link('./about.html','info','About Us', active==='about')}
          ${link('./contact.html','mail','Contact Us', active==='contact')}
        </div>
      </div>
    </div>
  </div>`
}
