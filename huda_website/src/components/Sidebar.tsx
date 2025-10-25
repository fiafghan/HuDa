import React from 'react'
import { Home, Info, Mail, FolderOpen, Brush, Workflow, ShieldCheck, Map, LineChart, Share2, BarChart3, Bot, FileSearch, Activity } from 'lucide-react'
import { Link, useLocation } from 'react-router-dom'

type Item = { to: string; label: string; icon: React.ReactNode; isActive?: boolean }

function NavItem({ to, label, icon, isActive }: Item) {
  const base = 'flex items-center gap-2 px-3 py-2 rounded-md text-sm'
  const active = isActive ? ' bg-indigo-50 text-indigo-700' : ' text-gray-700 hover:bg-gray-100'
  return (
    <Link to={to} className={base + active}>
      {icon}
      {label}
    </Link>
  )
}

export default function Sidebar() {
  const { pathname } = useLocation()
  const is = (p: string) => pathname === p
  return (
    <aside className="hidden md:block fixed top-[48px] left-0 h-[calc(100vh-48px)] w-72 overflow-y-auto bg-white/80 backdrop-blur border-r border-white/60 shadow-sm p-4">
      <div className="flex items-center gap-2 mb-4">
        <Home className="w-5 h-5 text-indigo-600" />
        <span className="text-sm font-semibold">HuDa Navigation</span>
      </div>
      <nav className="space-y-1 text-sm">
        <a href="/#overview" className="flex items-center gap-2 px-3 py-2 rounded-md text-sm text-gray-700 hover:bg-gray-100"><Home className="w-4 h-4" />Overview</a>
        <div className="pt-2 pb-1 text-[10px] uppercase tracking-wider text-gray-500">Pages</div>
        <NavItem to="/about" label="About" icon={<Info className="w-4 h-4" />} isActive={is('/about')} />
        <NavItem to="/contact" label="Contact" icon={<Mail className="w-4 h-4" />} isActive={is('/contact')} />
        <div className="pt-2 pb-1 text-[10px] uppercase tracking-wider text-gray-500">Phases</div>
        <NavItem to="/docs/opening" label="Opening" icon={<FolderOpen className="w-4 h-4" />} isActive={is('/docs/opening')} />
        <NavItem to="/docs/cleaning" label="Cleaning" icon={<Brush className="w-4 h-4" />} isActive={is('/docs/cleaning')} />
        <NavItem to="/docs/transformation" label="Transformation" icon={<Workflow className="w-4 h-4" />} isActive={is('/docs/transformation')} />
        <NavItem to="/docs/validation-quality" label="Validation & Quality" icon={<ShieldCheck className="w-4 h-4" />} isActive={is('/docs/validation-quality')} />
        <NavItem to="/docs/geospatial" label="Geospatial" icon={<Map className="w-4 h-4" />} isActive={is('/docs/geospatial')} />
        <NavItem to="/docs/analysis" label="Analysis" icon={<LineChart className="w-4 h-4" />} isActive={is('/docs/analysis')} />
        <NavItem to="/docs/automation" label="Automation" icon={<Workflow className="w-4 h-4" />} isActive={is('/docs/automation')} />
        <NavItem to="/docs/interoperability" label="Interoperability" icon={<Share2 className="w-4 h-4" />} isActive={is('/docs/interoperability')} />
        <NavItem to="/docs/visualization" label="Visualization" icon={<BarChart3 className="w-4 h-4" />} isActive={is('/docs/visualization')} />
        <NavItem to="/docs/ml4humanitarian" label="ML for Humanitarian Data" icon={<Bot className="w-4 h-4" />} isActive={is('/docs/ml4humanitarian')} />
        <NavItem to="/docs/document-processing" label="Document Processing" icon={<FileSearch className="w-4 h-4" />} isActive={is('/docs/document-processing')} />
        <NavItem to="/docs/humanitarian-metrics" label="Humanitarian Metrics" icon={<Activity className="w-4 h-4" />} isActive={is('/docs/humanitarian-metrics')} />
      </nav>
    </aside>
  )
}
