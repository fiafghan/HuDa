import React from 'react'
import { Route, Routes, Navigate } from 'react-router-dom'
import Home from './pages/Home'
import About from './pages/About'
import Contact from './pages/Contact'
import Opening from './pages/docs/Opening'
import Cleaning from './pages/docs/Cleaning'
import Transformation from './pages/docs/Transformation'
import Validation from './pages/docs/Validation'
import Geospatial from './pages/docs/Geospatial'
import Analysis from './pages/docs/Analysis'
import Automation from './pages/docs/Automation'
import Interoperability from './pages/docs/Interoperability'
import Visualization from './pages/docs/Visualization'
import ML4Humanitarian from './pages/docs/ML4Humanitarian'
import DocumentProcessing from './pages/docs/DocumentProcessing'
import HumanitarianMetrics from './pages/docs/HumanitarianMetrics'

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/contact" element={<Contact />} />

      <Route path="/docs/opening" element={<Opening />} />
      <Route path="/docs/cleaning" element={<Cleaning />} />
      <Route path="/docs/transformation" element={<Transformation />} />
      <Route path="/docs/validation-quality" element={<Validation />} />
      <Route path="/docs/geospatial" element={<Geospatial />} />
      <Route path="/docs/analysis" element={<Analysis />} />
      <Route path="/docs/automation" element={<Automation />} />
      <Route path="/docs/interoperability" element={<Interoperability />} />
      <Route path="/docs/visualization" element={<Visualization />} />
      <Route path="/docs/ml4humanitarian" element={<ML4Humanitarian />} />
      <Route path="/docs/document-processing" element={<DocumentProcessing />} />
      <Route path="/docs/humanitarian-metrics" element={<HumanitarianMetrics />} />

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
