export function renderFooter() {
  const year = new Date().getFullYear()
  return `
  <footer class="border-t border-white/60 bg-white/70 backdrop-blur supports-[backdrop-filter]:bg-white/60">
    <div class="max-w-7xl mx-auto px-4 md:px-6 py-6 flex flex-col md:flex-row items-center justify-between gap-4">
      <div class="text-sm text-gray-600">© <span>${year}</span> HuDa. Built for humanitarian analysts.</div>
      <div class="flex items-center gap-4 text-gray-600">
        <a href="./about.html" class="inline-flex items-center gap-1 hover:text-gray-900"><i data-lucide="info" class="w-4 h-4"></i>About</a>
        <a href="./contact.html" class="inline-flex items-center gap-1 hover:text-gray-900"><i data-lucide="mail" class="w-4 h-4"></i>Contact</a>
      </div>
    </div>
  </footer>`
}
