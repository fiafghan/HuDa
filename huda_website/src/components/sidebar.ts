export type SidebarActive =
  | 'overview'
  | 'installation'
  | 'opening'
  | 'cleaning'
  | 'transformation'
  | 'validation'
  | 'geospatial'
  | 'analysis'
  | 'automation'
  | 'interoperability'
  | 'visualization'
  | 'ml4humanitarian'
  | 'document_processing'
  | 'humanitarian_metrics'
  | 'about'
  | 'contact'

const item = (href: string, icon: string, label: string, active = false) => `
  <a href="${href}" class="flex items-center gap-2 px-3 py-2 rounded-md text-sm ${
    active ? 'bg-indigo-50 text-indigo-700' : 'text-gray-700 hover:bg-gray-100'
  }"><i data-lucide="${icon}" class="w-4 h-4"></i>${label}</a>
`

export function renderSidebar(active: SidebarActive) {
  return `
  <div class="hidden md:block fixed top-[48px] left-0 h-[calc(100vh-48px)] w-72 overflow-y-auto bg-white/80 backdrop-blur border-r border-white/60 shadow-sm p-4">
    <div class="flex items-center gap-2 mb-4">
      <i data-lucide="database" class="w-5 h-5 text-indigo-600"></i>
      <span class="text-sm font-semibold">HuDa Navigation</span>
    </div>
    <nav class="space-y-1 text-sm">
      ${item('./index.html#overview', 'home', 'Overview', active === 'overview')}
      <div class="pt-2 pb-1 text-[10px] uppercase tracking-wider text-gray-500">Pages</div>
      ${item('./about.html', 'info', 'About', active === 'about')}
      ${item('./contact.html', 'mail', 'Contact', active === 'contact')}
      <div class="pt-2 pb-1 text-[10px] uppercase tracking-wider text-gray-500">Phases</div>
      ${item('./docs_opening.html', 'folder-open', 'Opening', active === 'opening')}
      ${item('./docs_cleaning.html', 'brush', 'Cleaning', active === 'cleaning')}
      ${item('./docs_transformation.html', 'workflow', 'Transformation', active === 'transformation')}
      ${item('./docs_validation_quality.html', 'shield-check', 'Validation & Quality', active === 'validation')}
      ${item('./docs_geospatial.html', 'map', 'Geospatial', active === 'geospatial')}
      ${item('./docs_analysis.html', 'line-chart', 'Analysis', active === 'analysis')}
      ${item('./docs_automation.html', 'workflow', 'Automation', active === 'automation')}
      ${item('./docs_interoperability.html', 'share-2', 'Interoperability', active === 'interoperability')}
      ${item('./docs_visualization.html', 'bar-chart-3', 'Visualization', active === 'visualization')}
      ${item('./docs_ml4humanitarian.html', 'bot', 'ML for Humanitarian Data', active === 'ml4humanitarian')}
      ${item('./docs_document_processing.html', 'file-search', 'Document Processing', active === 'document_processing')}
      ${item('./docs_humanitarian_metrics.html', 'activity', 'Humanitarian Metrics', active === 'humanitarian_metrics')}
    </nav>
  </div>
  `
}
